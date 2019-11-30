from time import sleep, gmtime, strftime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request 
import datetime
import re
import os


while(1):
	init_t = strftime("%Y%m%d-%H%M%S", gmtime())
	print('Initiated at ' + init_t + ' ....')

	#Ruta del driver
	path = "./"
	driver = webdriver.Chrome(path+'chromedriver')

	#Pagina de login
	init_url = 'https://www.instagram.com/accounts/login/'
	driver.get(init_url)

	sleep(5)
	#Cuenta y claves a introducir
	insta_ID = 'by.cerrato'
	insta_PW = '123er56ty7' #usuario de pruebas

	#Rellenamos los campos con el usuario y contraseña
	element_id = driver.find_element_by_name("username")
	element_password = driver.find_element_by_name("password")
	element_id.send_keys(insta_ID)
	element_password.send_keys(insta_PW)
	element_password.submit(); sleep(5)


	#Scrapping
	threshold_nLike = 0 # Importa unicamente imagenes con más de este número
	keys = ['Madrid'] #Hashtags para scrappear

	count_total = 100 # Cuenta fotos
	count_included = 100 
	nLikes_total = [] #Cuenta likes


	for keyIdx in range(len(keys)):
	    
	    # (1) Entra al hashtag
	    key_url='https://www.instagram.com/explore/tags/'+keys[keyIdx]+'/'
	    driver.get(key_url); sleep(5)
	    
	    # Carga página
	    elem = driver.find_element_by_tag_name("body") 
	    no_of_pagedowns = 1
	    while no_of_pagedowns:
	        elem.send_keys(Keys.PAGE_DOWN)
	        sleep(3)
	        no_of_pagedowns-=1
	    
	    possible_posts = driver.execute_script(
	            "return window._sharedData.entry_data."
	            "TagPage[0].graphql.hashtag.edge_hashtag_to_media")['edges']
	    nPost = len(possible_posts)
	    print('Key #'+ str(keyIdx)+keys[keyIdx]+' nPost:'+str(nPost) )
	    count_total = count_total + nPost
	    
	    print(nPost)
	    # (2) Info de las fotos
	    count_local = 0
	    for postIdx in range(nPost): 
	        postInfo = str( possible_posts[postIdx] )
	        nLike = postInfo.split("edge_media_preview_like': {'count': ")[1].split("}")[0]
	        nComment = postInfo.split("edge_media_to_comment': {'count': ")[1].split("}")[0]
	        userID = postInfo.split("owner': {'id': '")[1].split("'}")[0]
	        postTimeStr = postInfo.split("'taken_at_timestamp': ")[1].split(", 'thumbnail_resources'")[0]
	        

	        postTimeInt = int(postTimeStr)
	        timestamp = datetime.datetime.fromtimestamp(postTimeInt)
	        postTimestamp = timestamp.strftime('%Y%m%d-%H%M%S')

	        summary = "_UID_"+userID +"_postTime_"+postTimestamp+"_nLik_"+nLike
	        
	        nLikes_total.append(int(nLike))
	        
	        # (3) Likes y nombre de la foto a guardar
	        if int( nLike ) > threshold_nLike:
	            count_local = count_local + 1
	            
	            if count_local < 100: imageN = '000'+ str(count_local)
	            elif count_local < 1000: imageN= '00'+str(count_local)
	            else: imageN = str(count_local)
	    
	            fname = 'download_images/'+keys[keyIdx] + imageN + summary+ '.jpg'
	            imgURL = postInfo.split("'thumbnail_src': '")[1].split("'")[0]
	            urllib.request.urlretrieve(imgURL, path+fname)
	            
	    count_included = count_included + count_local

	driver.close()

	# Copiamos los archivos al cluster
	cpCluster = 'scp ./download_images/* acerrato@35.242.236.241:./images/'
	os.system(cpCluster)

	#Historificamos en Local
	mvLocal = 'mv ./download_images/*.jpg ../03_almacenamiento/hist'
	os.system(mvLocal)

	sleep(600)

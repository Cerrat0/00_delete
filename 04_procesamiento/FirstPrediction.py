from imageai.Prediction import ImagePrediction
import re
import os
import requests
import string
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
image = args.echo

execution_path = './'
prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath( execution_path + "resnet50_weights_tf_dim_ordering_tf_kernels.h5")
prediction.loadModel()

predictions,percentage_probabilities = prediction.predictImage(image, result_count=1)

x = predictions,percentage_probabilities

a = str(x)

b = a.replace('(', '')

c = b.replace('[', '')                    

d = c.replace("'", "")

e = d.replace(']', '')

f = e.replace(')', '')

name = str(image)

extractID = re.search('UID_(.+?)_postTime_', name)
if extractID:
    UID = extractID.group(1)

extractTime = re.search('_postTime_(.+?)_nLik_', name)
if extractTime:
    postTime = extractTime.group(1)
 	
extractLike = re.search('_nLik_(.+?).jpg', name)
if extractLike:
    n_Like = extractLike.group(1)

with open(execution_path +'results.csv', 'a') as file:
	file.write(UID + ',' + postTime + ',' + n_Like + ',' +  f +  '\n')

imageProcessed = image.replace(".jpg", "")
imageProcessed = imageProcessed.replace('../../03_almacenamiento/hist/','')


os.rename(image, './hist_PROCESSED/'+imageProcessed+".png")

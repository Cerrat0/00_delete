Para el reconocimiento de imagenes finalmente se ha optado por la herramienta ImageAI

Para instalar esta librería se debe hacer desde...

https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.2/imageai-2.0.2-py3-none-any.whl

Al ser una librería externa y no tener permisos ha sido inviable pasarselo a pyspark

Se ha intentado instalar en todos los nodos pero tampoco ha sido viable, 
tampoco pasandoselo a spark como argumento --py-files (ruta del zip)

finalmente se ha ejecutado en local, proximos pasos sería conseguir usar la librería desde pyspark

El modelo pre-entrenado se puede descargar desde:
https://github.com/fchollet/deep-learning-models/releases/download/v0.2/resnet50_weights_tf_dim_ordering_tf_kernels.h5

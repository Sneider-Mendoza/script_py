import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt

datos, metadatos = tfds.load('fashion_mnist', as_supervised=True, with_info=True)



datos_entrenamiento, datos_pruebas = datos['train'], datos['test']

nombres_clases = metadatos.features['label'].names
print(nombres_clases)

# Normalizar los datos (pasar de 0-255 a 0-1)
def normalizar(imagenes,etiquetas):
    imagenes=tf.cast(imagenes, tf.float32)
    imagenes /= 255 # Aqui lo pasa de 0-255 a 0-1
    return imagenes, etiquetas

#normalizar los datos de entrenamiento y pruebas con la funcion que hicimos
datos_entrenamiento = datos_entrenamiento.map(normalizar)
datos_pruebas = datos_pruebas.map(normalizar)

# Agregar a cache (usar memoria en lugar de disco, entrenamiento mas rapido)
datos_entrenamiento = datos_entrenamiento.cache()
datos_pruebas = datos_pruebas.cache()

#mostrar una imagen de los datos de prueba, de momento se mostrara la primera

for imagen, etiqueta in datos_entrenamiento.take(1):
    break
imagen = imagen.numpy().reshape((28, 28)) # redimensionar, cosas de tensores

# Dibujar 
plt.figure()
plt.imshow(imagen, cmap=plt.cm.binary)
plt.grid(False)
plt.show()
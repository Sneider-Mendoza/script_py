import requests
import mysql.connector
import pandas as pd

# Establecer detalles de la conexión
conexion = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)

# Crear objeto cursor para interactuar con la base de datos
cursor = conexion.cursor()

# Ejecutar consulta SQL
cursor.execute("SELECT id,name,latitude,longitude FROM pds where city_id is null")

# Recuperar los resultados de la consulta
resultados_pds = cursor.fetchall()
cursor.close()
conexion.close()

# # Crear objeto cursor para interactuar con la base de datos
# cursor2 = conexion.cursor()

# # Ejecutar consulta SQL
# cursor2.execute("SELECT id,name FROM cities")

# # Recuperar los resultados de la consulta
# resultados_cities = cursor2.fetchall()

lis_dic = []
for tupla in resultados_pds:
    id = tupla[0]
    dic = {'id': tupla[0], 'nombre': tupla[1], 'lat': tupla[2], 'long': tupla[3],}
    lis_dic.append(dic)
    
lis_ciudades_encontradas_cordenadas = []  
for i in range(len(lis_dic)):
    lat = lis_dic[i]['lat']
    long = lis_dic[i]['long']
    name = lis_dic[i]['nombre']
    id = lis_dic[i]['id']

    # Define la clave de API y la URL base de OpenCage
    API_KEY = "5b6332b55a9248f0b07d1f3428405718"
    BASE_URL = "https://api.opencagedata.com/geocode/v1/json"

    ubicacion = {'q': f'{lat}, {long}', 'key': API_KEY}

    # Hace una solicitud a la API de OpenCage con las coordenadas dadas
    response = requests.get(BASE_URL, params=ubicacion)
    
    # Analiza la respuesta JSON y muestra la información de la ciudad y el estado
    if response.status_code == 200:
        data = response.json()['results'][0]['components']
    
        ciudad = data.get('county') or data.get('city') or data.get('town')
        estado = data.get('state') or data.get('region')
    
    else:
        print("Error al hacer la solicitud a la API.")
            
    ciu_dep = {'Ciudad': ciudad, 'Departamaneto': estado }
    lis_ciudades_encontradas_cordenadas.append(ciu_dep)
    
union = []

for i in range(len(lis_dic)):
    dic_union = {}
    for key in lis_dic[i]:
        dic_union[key] = lis_dic[i][key]
    for key in lis_ciudades_encontradas_cordenadas[i]:
        dic_union[key] = lis_ciudades_encontradas_cordenadas[i][key]
    union.append(dic_union) 
    

df = pd.DataFrame(union)

# Exportar a un archivo Excel
df.to_excel('C:/Users/SneiderMendoza/Downloads/pds_que_no_tenian_ciudad.xlsx', index=False, engine='openpyxl')

    



# # Crear un conjunto de ciudades a partir del array de diccionarios
# ciudades_dicc = set(d["Ciudad"].upper() for d in Lis_ciudades_encontradas_cordenadas)

# # Crear una lista con los IDs de las ciudades que aparecen en ambos arrays
# ids = [t[0] for t in resultados_cities if t[1].upper() in ciudades_dicc]

   
   
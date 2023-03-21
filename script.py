import requests
import mysql.connector

# Establecer detalles de la conexión
conexion = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="enr"
)
# Crear objeto cursor para interactuar con la base de datos
cursor = conexion.cursor()

# Ejecutar consulta SQL
cursor.execute("SELECT latitude,longitude FROM pds where city_id is null")

# Recuperar los resultados de la consulta
resultados = cursor.fetchall()
# Creamos variabeles para que guarden los resultados de la consulta

# Imprimir los resultados
# for tupla in resultados:
    # lat, log = tupla
    # print(lat, log)

# Define la clave de API y la URL base de OpenCage
API_KEY = "5b6332b55a9248f0b07d1f3428405718"
BASE_URL = "https://api.opencagedata.com/geocode/v1/json"

ubicacion = {'q': f'{8.4926499583569}, {-73.639900415467}', 'key': API_KEY}


# Hace una solicitud a la API de OpenCage con las coordenadas dadas
response = requests.get(BASE_URL, params=ubicacion)

# Analiza la respuesta JSON y muestra la información de la ciudad y el estado
if response.status_code == 200:
    data = response.json()['results'][0]['components']
    print(data)
    if 'county' in data and 'state' in data:
        ciudad = data['county']
        estado = data['state']
        
    elif 'city' in data and 'state' in data:
        ciudad = data['city']
        estado = data['state']
        
    elif 'town' in data and 'state' in data:
        ciudad = data['town']
        estado = data['state']
        
    elif 'town' in data and 'region' in data:
        ciudad = data['town']
        estado = data['region']
        
    elif 'county' in data and 'region' in data:
        ciudad = data['county']
        estado = data['region']
        
        
    print(f"Ciudad => {ciudad} -- Departamento => {estado}.")
else:
    print("Error al hacer la solicitud a la API.")

    

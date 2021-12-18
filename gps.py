import requests
import urllib

api_url = "http://open.mapquestapi.com/directions/v2/route?"
key = MAPQUEST_KEY



while True:
    origin = input("Ingresa la Ciudad de origen: ")
    if origin == 'q':
        break

    destination = input("Ingresa el Destino: ")
    if destination == 'q':
        break

    url = api_url + urllib.parse.urlencode({"key":key, "from":origin, "to":destination})
    json_data = requests.get(url).json()
    status_code = json_data['info']['statuscode']
    if status_code == 0:
        distance = json_data["route"]["distance"]*1.609
        travel_time = json_data["route"]["formattedTime"]
        fuel_used = json_data["route"]["fuelUsed"]*3.78
        print("-----------------------------------------------------------------")
        print(f"Información del viaje de {origin.capitalize()} a {destination.capitalize()}")
        print(f'Distancia {distance} Kilometros ')
        print(f'Duración del viaje {travel_time}')
        print(f'Promedio de uso de combustible {fuel_used} litros')
        print("-----------------------------------------------------------------")
        print("Indicaciones de viaje")

        for each in json_data['route']['legs'][0]['maneuvers']:
            distance_remaigning = distance - each['distance'] * 1.61
            print(each["narrative"] + "(" + str("{:.2f}".format(distance_remaigning)) + "Km faltantes")
            distance= distance_remaigning
    else:
        print("Ubicación desconocida")


    






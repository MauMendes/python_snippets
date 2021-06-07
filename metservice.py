import requests
import re
import json

DEFAULT_BASE = 'http://metservice.com/publicData'

TOWN_SLUG_REGEX = re.compile(r'\/([\w-]+)$')

def _get_data(endpoint: str, base: str):
    try:
        resp = requests.get(base + endpoint)
        print(base+endpoint)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError:
        # TODO: error handling?
        return None

def _city_data(city: str, endpoint: str, base: str):
    return _get_data(endpoint.format(city), base)

def get_cities_list(base = DEFAULT_BASE):
    resp = _get_data("/webdata/towns-cities", base)
    search = resp["layout"]["search"]
    towns = {}
    for island in search:
        for region in island["items"]:
            for town in region["children"]:
                town_url = town["url"]


                towns[town["label"]] = TOWN_SLUG_REGEX.search(town_url).group(1)
    return towns

def getLocalForecast(city: str, base: str = DEFAULT_BASE):
    return _get_data(f'/localForecast{city}', base)

def getSunProtectionAlert(city: str, base: str = DEFAULT_BASE):
    return _get_data(f'/sunProtectionAlert{city}', base)

def getOneMinObs(city: str, base: str = DEFAULT_BASE):
    return _get_data(f'/oneMinObs_{city}', base)

def getHourlyObsAndForecast(city: str, base: str = DEFAULT_BASE):
    return _get_data(f'/hourlyObsAndForecast_{city}', base)

def getLocalObs(city: str, base: str = DEFAULT_BASE):
    return _get_data(f'/localObs_{city}', base)

def getTides(city: str, base: str = DEFAULT_BASE):
    return _get_data(f'/tides_{city}', base)

def getWarnings(city: str, base: str = DEFAULT_BASE):
    return _get_data(f'/warningsForRegion3_urban.{city}', base)

def getRises(city: str, base: str = DEFAULT_BASE):
    return _get_data(f'/riseSet_{city}', base)

def getPollen(city: str, base: str = DEFAULT_BASE):
    return _get_data(f'/pollen_town_{city}', base)

def getDaily(city: str, base: str = DEFAULT_BASE):
    return _get_data(f'/climateDataDailyTown_{city}_32', base)



def getTemperature(city:str):
  
  temp = 0.0
  
  try:
    link = 'http://metservice.com/publicData/webdata/towns-cities/locations/' + city
    resp = requests.get(link)
    #print(link)
    resp.raise_for_status()

    webdata_str = json.dumps(resp.json(), indent=4)
    webdata_json = json.loads(webdata_str)
    #with open('output.txt', 'w') as file:  # Use file to refer to the file object
    #  file.write(webdata_str)

    #print(webdata_str)
    #weather_general = webdata_json["layout"]["primary"]["slots"]["left-major"]["modules"][0]
    try:
      weather_obs = webdata_json["layout"]["primary"]["slots"]["left-major"]["modules"][0]["observations"]
    except KeyError:
      return temp

    temp = float(weather_obs["temperature"]["current"])
  except:
    return temp
  return temp 

cities = get_cities_list(base=DEFAULT_BASE)

#print(cities)
#print(len(cities))
#print(type(cities))

for key in cities.keys(): 
  temp = getTemperature(cities[key])
  print( key, ":", str(temp), "C" )

str_cities = json.dumps(cities, indent=4)
#print(str_cities)


#data = _get_data('https://www.metservice.com/towns-cities/locations/christchurch', str = DEFAULT_BASE)
#print(data)

try:
    link = 'http://metservice.com/publicData/webdata/towns-cities/locations/dargaville'
    resp = requests.get(link)
    print(link)
    resp.raise_for_status()

    webdata_str = json.dumps(resp.json(), indent=4)
    webdata_json = json.loads(webdata_str)
    with open('output.txt', 'w') as file:  # Use file to refer to the file object
      file.write(webdata_str)

    #print(webdata_str)
    weather_general = webdata_json["layout"]["primary"]["slots"]["left-major"]["modules"][0]
    weather_obs = webdata_json["layout"]["primary"]["slots"]["left-major"]["modules"][0]["observations"]
    #data = json.dumps(weather_obs, indent=4)
    #print(data)


    print("#### WEATHER CONDITIONS ####")
    print("Location: ", weather_general["source"])
    #print(weather_general)
    if "asAt" in weather_general:
      print("Time: ", weather_general["asAt"])
    print("Current Temperature: ",weather_obs["temperature"]["current"], "C")
    print("Current Humidity: ",weather_obs["rain"]["relativeHumidity"], "%")
    print("Current Pressure: ",weather_obs["pressure"]["atSeaLevel"], "hPa")
    print("Current Wind: ",weather_obs["wind"]["averageSpeed"], "km/h : ", weather_obs["wind"]["direction"]," - ", weather_obs["wind"]["strength"])

    print("Clothing Layers: ",weather_obs["clothing"]["layers"])
    

except requests.HTTPError:
    # TODO: error handling?
    print('None')


#for city in cities:
#if city == "Christchurch":
#  print(city)

#print(_city_data("Christchurch Central", "/webdata/towns-cities", DEFAULT_BASE))
#print(getDaily("Christhcurch Central", DEFAULT_BASE))
#print(getLocalForecast("Christhcurch Central", DEFAULT_BASE))
  
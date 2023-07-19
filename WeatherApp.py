import requests
import json

try:
    city = input("Enter the Name of the City: ")

    url = f"http://api.weatherapi.com/v1/current.json?key=8c169b5978144328ae522024231707&q={city}"

    r = requests.get(url)
    #print(r.text)

    wdic = json.loads(r.text)
    print(f"The current temp. of {city} city is",wdic["current"]["temp_c"],"celsius" )
except:
    print("Enter correct City name ")

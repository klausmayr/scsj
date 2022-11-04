import requests
import json
import geojson

start = 'https://api.mapbox.com/isochrone/v1/mapbox/driving/'
end = '?contours_minutes=5&contours_colors=6706ce&polygons=true&access_token=pk.eyJ1Ijoia2xhdXNtYXlyIiwiYSI6ImNsM20xZWFxejAwNmkza29mcHptN243aTYifQ.lfLe-OcdZ89adHFcD7r9tQ'

with open('galveston_2022_polling_places.geojson') as f:
    gj = geojson.load(f)

for i in gj['features']:
    ft = i['geometry']['coordinates']
    name = i['properties']['POLL PLACE']
    name = name.replace(" ", "_")
    file = name + ".geojson"
    coords = str(ft)
    coords = coords.replace(" ", "")
    coords = coords.replace("[", "")
    coords = coords.replace("]", "")
    url = start + coords + end
    response = requests.get(url)
    print("Saving " + file + "...")
    with open(file, 'w') as f:
        r = response.json()
        f.write(json.dumps(r))

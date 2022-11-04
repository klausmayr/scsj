import requests
import json
import geojson

API_KEY = [YOUR_API_KEY]
geoFile = [YOUR_FILE_PATH]
export_file_property = [GEOJSON_PROPERTY_FOR_EXPORT_FILE_NAME]

start = 'https://api.mapbox.com/isochrone/v1/mapbox/driving/'
end = '?contours_minutes=10&contours_colors=6706ce&polygons=true&access_token=' + API_KEY

with open(geoFile) as f:
    gj = geojson.load(f)

for i in gj['features']:
    ft = i['geometry']['coordinates']
    name = i['properties'][export_file_property]
    name = name.replace(" ", "_")
    file = "2020_" + name + ".geojson"
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

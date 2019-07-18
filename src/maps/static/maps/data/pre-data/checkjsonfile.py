import json
import csv
import pandas as pd
path = 'src/mysite/maps/static/maps/data/'

f = open(path + 'GDP-circle.geojson', 'r')
json_dict = json.load(f)
print(json_dict)
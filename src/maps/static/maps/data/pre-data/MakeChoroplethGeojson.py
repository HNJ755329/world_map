import json
import csv
import pandas as pd
path = 'src/mysite/maps/static/maps/data/'

f = open(path + 'countries.geojson', 'r')
json_dict = json.load(f)
df = pd.read_csv(path + 'imf-dm-export-20190530-Population-reshape.csv')
df = df.set_index(['ISO_A3'])

#print(json_dict)
for i, country in enumerate(json_dict["features"]):
        #country["type"] = "Feature"
        ADMIN = country["properties"]["ADMIN"]
        ISO_A3 = country["properties"]["ISO_A3"]
        try:
                #country["properties"]["ADMIN"] = df.loc[ISO_A3,"ADMIN"]
                for year, x in df.loc[ISO_A3].items():
                        if year.isnumeric():
                                country["properties"]["Population" + year] = x
        except:
                pass

output = open(path + 'Population-Choropleth.geojson', 'w')
json.dump(json_dict, output)

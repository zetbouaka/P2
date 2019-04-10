from pyproj import Transformer, transform
import csv

def function(tf, lat, lon, alt):
    x, y, z = tf.transform(lat, lon, alt)
    return x, y, z

transformer =  Transformer.from_proj(4326, 5186)

f = open('input.csv', 'r', encoding='utf-8')
out = open('output.csv', 'w', encoding='utf-8', newline='')

wr = csv.writer(out)
rdr = csv.reader(f)

for line in rdr:
    name=line[0]
    lon=line[1]
    lat=line[2]
    alt=line[3]
    result = function(transformer, lon, lat, alt)
    wr.writerow([name, result[0], result[1], result[2]])
    #print(function(transformer, lon, lat, alt))

f.close()

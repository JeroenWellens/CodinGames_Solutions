import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = '3,879483'
lat = '43,608177'
n = int('3')
#key,street,city,phone,lon,lat
def1 = '1;Maison de la Prevention Sante;6 rue Maguelone 340000 Montpellier;;3,87952263361082;43,6071285339217'
def2 = '2;Hotel de Ville;1 place Georges Freche 34267 Montpellier;;3,89652239197876;43,5987299452849'
def3 = '3;Zoo de Lunaret;50 avenue Agropolis 34090 Mtp;;3,87388031141133;43,6395872778854'

defibs_raw = [def1,def2,def3]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

#change ',' for '.'
def comma_to_point(number):
    new = ''
    for n in number:
        if(n != ','):
            new += n
        else:
            new += '.'
    return new

lon = comma_to_point(lon)
lat = comma_to_point(lat)
for f in defibs_raw:
        f = comma_to_point(f)
  
#code here

# split the defib_raw info
defibs = {}

for d in defibs_raw:
    fib = d.split(sep=';')
    coord = (float(fib[-2]),float(fib[-1]))
    coord
    #key,street,city,phone,lon,lat
    defibs.update({int(fib[0]):{'place':fib[1],'address':fib[2],'phone':fib[3],'loc':coord}})

# using the provided formulas
def distance(p1,p2):
    
    x = (p2[0]-p1[0])*math.cos((p1[1]+p2[1])/2)
    y = (p2[1]-p1[1])
    
    d = np.sqrt(x**2 + y**2) * 6371
    
    return d

me = (float(lon),float(lat))
dist = np.inf
index = -1
# finding the closest point
for f in defibs:
    dis = distance(me,defibs[f]['loc'])
    if(dis<dist):
        dist=dis
        index = f
    

# answer is 'Maison de la Prevention Sante'
print(defibs[index]['place'])




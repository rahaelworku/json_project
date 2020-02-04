import json

in_file = open('eq_data_30_day_m1.json', 'r')
out_file = open('readable_eq_data.json', 'w')

eq_data = json.load(in_file)

print(type(eq_data))

#dumps to output file
json.dump(eq_data,out_file,indent=4)

#features is alist of dictionaries 
list_of_eqs = eq_data['features']

#check to see what type of object we have 
print(type(list_of_eqs))

#check to see the number of eqs
print(len(list_of_eqs))

mags, lons, lats, hover_texts= [],[],[],[]

#get magnitude of earthquakes 
for eq in list_of_eqs:
    mag=eq['properties']['mag']
    mags.append(mag)

print(mags[:10])

for eq in list_of_eqs:
    mag = eq['properties']['mag']
    lon = eq['geometry']['coordinates'][0]
    lat= eq['geometry']['coordinates'][1]
    hover_text=eq['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(hover_text)

print(mags[:10])


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline 

#data=[Scattergeo(lon=lons,lat=lats)]

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text':hover_texts,
    'marker':{
        #list comprehension (the size becomes larger)
        'size':[5*mag for mag in mags],
        'color':mags,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Magnitude'}
     },
}]

my_layout = Layout(title="global_earthquakes.html")

fig= {'data':data, 'layout':my_layout}

offline.plot(fig,filename='global_earthquakes.html')
offline.plot(fig,filename='global_earthquakes.html')




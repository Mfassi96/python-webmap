import folium, pandas
datos=pandas.read_csv("Volcanoes.csv")
recorte=datos.loc[:,["NAME","STATUS","ELEV","LAT","LON"]]
# Creando listas de los distintos datos para inserta
lista_lat=list(recorte['LAT'])
lista_lon=list(recorte['LON'])
lista_names=list(recorte['NAME'])
lista_elev=list(recorte['ELEV'])
lista_status=list(recorte['STATUS'])

# funcion para dar color dinamico a los marcadores
def get_elev(el):
    if el <1000:
        return "green"
    elif 1000<=el<3000:
        return "orange"
    else:
        return "red"

# Crear el mapa con una ubicación válida (latitud y longitud) y atribución para el tile
map1 = folium.Map(
    location=[38.241574, -111.868111]
)

fg=folium.FeatureGroup("mymap")

# Agregar un marcador
for lt,ln,nm,st,el in zip(lista_lat, lista_lon,lista_names, lista_status, lista_elev):
        fg.add_child(folium.CircleMarker(location=[lt, ln],
                                     radius=6,
                                     popup=nm + "\n" + st + "\n Altura:" + str(el),
                                     color='grey',
                                     fill_color=get_elev(el),
                                     fill=True,
                                     fill_opacity=0.7))
        
fg.add_child(folium.GeoJson(data=open('world.json','r',encoding='UTF-8-sig').read()))

map1.add_child(fg)
# Guardar el mapa en un archivo HTML
map1.save("map1.html")

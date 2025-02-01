import folium, pandas
datos=pandas.read_csv("Volcanoes.csv")
recorte=datos.loc[:,["LAT","LON"]]
lista_lat=list(recorte['LAT'])
lista_lon=list(recorte['LON'])

# Crear el mapa con una ubicación válida (latitud y longitud) y atribución para el tile
map1 = folium.Map(
    location=[45.0, -73.0]
)

fg=folium.FeatureGroup("mymap")

# Agregar un marcador
for lt, ln in zip(lista_lat, lista_lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="Nuevo marcador", icon=folium.Icon(color="red")))

map1.add_child(fg)
# Guardar el mapa en un archivo HTML
map1.save("map1.html")

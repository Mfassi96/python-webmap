import folium

# Crear el mapa con una ubicación válida (latitud y longitud) y atribución para el tile
map1 = folium.Map(
    location=[45.0, -73.0]
)

fg=folium.FeatureGroup("mymap")

# Agregar un marcador
fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Nuevo marcador", icon=folium.Icon(color="red")))

map1.add_child(fg)
# Guardar el mapa en un archivo HTML
map1.save("map1.html")

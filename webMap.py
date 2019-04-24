import folium

map = folium.Map(location=[38.58,-9989],zoom_start=6,tiles="Mapbox bright")

map.save("webMap.html")
import folium
import geocoder

ip = geocoder.ip('me')
map = folium.Map(location=ip.latlng)
map.add_child(folium.Marker(location=ip.latlng,popup="Marker",icon=folium.Icon(color='blue')))
map.save("webMap.html")
import folium
import geocoder

ip = geocoder.ip('me')
map = folium.Map(location=ip.latlng)
featureGroup = folium.FeatureGroup(name="Web Map")
featureGroup.add_child(folium.Marker(location=ip.latlng,popup="Marker",icon=folium.Icon(color='blue')))
map.add_child(featureGroup)
map.save("webMap.html")


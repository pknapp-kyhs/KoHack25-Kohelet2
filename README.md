# Kohelet2

pip install folium 
import folium

my_map = folium.Map(location=[latitude, longitude], zoom_start=12)

folium.Marker([51.5074, -0.1278], popup="London").add_to(my_map)


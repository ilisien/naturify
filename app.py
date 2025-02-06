import folium

import folium.map
import panel as pn

pn.extension(design="bootstrap",theme="dark")

m = folium.Map(location=[52.51,13.39],zoom_start=12)

latitude = pn.widgets.FloatSlider(
    value=0,start=-180,end=180,step=1, name="map latitude"
)

longitude = pn.widgets.FloatSlider(
    value=0, start=-90, end=90, step=1, name="map longitude"
)

zoom_slider = pn.widgets.FloatSlider(
    value=12, start=5, end=20, name="zoom slider"
)

def create_map(lat,lon,zoom_start):
    return folium.Map(location=[lat,lon],zoom_start=zoom_start)

map_display = pn.bind(create_map, lat=latitude, lon=longitude, zoom_start=zoom_slider)

pn.Column(
    pn.pane.PNG("https://picsum.photos/200/300"),
    pn.pane.plot.Folium(map_display,height=400),
    latitude,
    longitude,
    zoom_slider,
).servable()
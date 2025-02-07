#
# we want to do the following:
# - deliver "flash cards" to the user to identify
# - flash cards need to be:
#    - approximately random
#    - skewed towards observations with more votes
#    - properly spaced by species to make studying useful
# - in a study list, the program should choose a few species to start
# off with, and then as the user progresses it should decide new species
# to show.
# - need to have some sort of "memory" function -- perhaps a login thing?
# - should also be able to study by other things:
#    - (native/invasive) in (place)
#    - just in a place
#    - under a certain phylum
#    - "wildflowers" or "trees" -- non-phylogenic distinctions
#    - custom list
# - needs to also show the place, studied and non-studied flashcards like
# quizlet style, and the expanded taxa (or at least the family) of them
# also needs the common name of everything to be all nice to brodie and
# stuff
#
#
#

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
    pn.pane.PNG("https://picsum.photos/300/100",sizing_mode='stretch_width'),
    pn.pane.plot.Folium(map_display,sizing_mode='stretch_width',height=200),
    latitude,
    longitude,
    zoom_slider,
).servable()
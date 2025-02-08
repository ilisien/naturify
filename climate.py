import rasterio, os
import numpy as np

import matplotlib.pyplot as plt
from rasterio.plot import show

from download_climate_data import download_climate_data

# see https://www.nature.com/articles/sdata2018214
KOPPEN_CLASSES = {
    1: "Af - Tropical Rainforest",
    2: "Am - Tropical Monsoon",
    3: "Aw - Tropical Savanna",
    4: "BWh - Hot Desert",
    5: "BWk - Cold Desert",
    6: "BSh - Hot Steppe",
    7: "BSk - Cold Steppe",
    8: "Csa - Hot-summer Mediterranean",
    9: "Csb - Warm-summer Mediterranean",
    10: "Csc - Cold-summer Mediterranean",
    11: "Cfa - Humid Subtropical",
    12: "Cfb - Marine West Coast",
    13: "Cfc - Subpolar Oceanic",
    14: "Dsa - Hot-summer Continental",
    15: "Dsb - Warm-summer Continental",
    16: "Dsc - Cold-summer Continental",
    17: "Dsd - Continental Subarctic",
    18: "Dfa - Humid Continental",
    19: "Dfb - Warm-summer Humid Continental",
    20: "Dfc - Subarctic",
    21: "Dfd - Extreme Subarctic",
    22: "ET - Tundra",
    23: "EF - Ice Cap"
}

climate_data_path = "climate_data/koppen_geiger_0p1.tif"

def get_koppen_climate(lat,lon):
    if not os.path.exists(climate_data_path):
        download_climate_data()

    with rasterio.open(climate_data_path) as dataset:
        row,col = dataset.index(lon,lat)
        climate_value = dataset.read(1)[row,col]
        print(climate_value)

        return KOPPEN_CLASSES.get(climate_value, "Unknown Climate Zone")

def debug_data():
    with rasterio.open(climate_data_path) as dataset:
        data = dataset.read(1)
        unique_values = np.unique(data)
        print(unique_values)
        fig, ax = plt.subplots(figsize=(10, 6))
        show(dataset, ax=ax, cmap="jet")
        ax.set_title("Köppen-Geiger Climate Classification")
        plt.show()
    

if __name__ == "__main__":
    #lat, lon = 45.0, -93.0
    #koppen_climate = get_koppen_climate(lat, lon)
    #print(koppen_climate)
    debug_data()
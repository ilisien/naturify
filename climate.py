import rasterio, os
import numpy as np
import matplotlib.pyplot as plt
from rasterio.plot import show
import pandas as pd

from download_climate_data import download_climate_data

climate_data_tif_path = "climate_data/koppen_geiger_0p1.tif"
koppen_table = "climate_data/koppen_table.csv"

KOPPEN_CLASSES = pd.read_csv(koppen_table).set_index("Class")

def get_koppen_major(number):
    try:
        return KOPPEN_CLASSES.loc[number,"Major"]
    except:
        return -1

def get_koppen_climate(lat,lon):
    if not os.path.exists(climate_data_tif_path):
        download_climate_data()

    with rasterio.open(climate_data_tif_path) as dataset:
        row,col = dataset.index(lon,lat)
        climate_value = dataset.read(1)[row,col]
        return get_koppen_major(climate_value), climate_value

def debug_data():
    with rasterio.open(climate_data_tif_path) as dataset:
        data = dataset.read(1)
        unique_values = np.unique(data)
        print(unique_values)
        fig, ax = plt.subplots(figsize=(10, 6))
        show(dataset, ax=ax, cmap="jet")
        ax.set_title("Köppen-Geiger Climate Classification")
        plt.show()
    

if __name__ == "__main__":
    lat, lon = 45.0, -93.0
    koppen_climate = get_koppen_climate(lat, lon)
    print(koppen_climate)
    #debug_data()
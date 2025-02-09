import rasterio, os
import numpy as np
import matplotlib.pyplot as plt
from rasterio.plot import show
import pandas as pd

from utilities import download_climate_data

climate_data_tif_path = "climate_data/koppen_geiger_0p1.tif"
koppen_table = "climate_data/koppen_table.csv"

KOPPEN_CLASSES = pd.read_csv(koppen_table).set_index("Class")

# guesses based on major designations -- this can definitely be better
DECIDUOUS_DESIGNATIONS = {
    1: {
        1: "growth",
        2: "growth",
        3: "growth",
        4: "growth",
        5: "growth",
        6: "growth",
        7: "growth",
        8: "growth",
        9: "growth",
        10: "growth",
        11: "growth",
        12: "growth",
    },
    2: {
        1: "growth",
        2: "growth",
        3: "growth",
        4: "growth",
        5: "growth",
        6: "growth",
        7: "growth",
        8: "growth",
        9: "growth",
        10: "growth",
        11: "growth",
        12: "growth",
    },
    3: {
        1: "bare",
        2: "flowery",
        3: "flowery",
        4: "growth",
        5: "growth",
        6: "mature",
        7: "mature",
        8: "mature",
        9: "mature",
        10: "autumn",
        11: "autumn",
        12: "bare",
    },
    4: {
        1: "bare",
        2: "flowery",
        3: "flowery",
        4: "flowery",
        5: "growth",
        6: "growth",
        7: "mature",
        8: "mature",
        9: "autumn",
        10: "autumn",
        11: "autumn",
        12: "bare",
    },
    5: {
        1: "bare",
        2: "bare",
        3: "bare",
        4: "bare",
        5: "bare",
        6: "flowery",
        7: "mature",
        8: "mature",
        9: "autumn",
        10: "autumn",
        11: "bare",
        12: "bare",
    }
}

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
        return get_koppen_major(climate_value)
    
def get_deciduous_designation(lat,lon,month):
    return DECIDUOUS_DESIGNATIONS[get_koppen_climate(lat,lon)][month]

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
    lat, lon = 31.416640670364572, -89.9857476516928
    koppen_climate = get_koppen_climate(lat, lon)
    print(koppen_climate)
    debug_data()
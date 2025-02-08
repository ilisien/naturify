import rasterio
import numpy as np

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
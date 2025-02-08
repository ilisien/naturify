import pyinaturalist as inat
from dataclasses import dataclass
from box import Box
from datetime import datetime
import random

SPECIES_LISTS = {
    "CTOP": "species_lists/commontreesofpa2011.txt",
}

def species_list(title):
    with open(SPECIES_LISTS[title], "r") as file:
        lines = [line.strip().lower() for line in file]
    return lines
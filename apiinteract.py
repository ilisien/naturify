import pyinaturalist as inat
from box import Box

SPECIES_LISTS = {
    "CTS OF PA": "species_lists/commontreesofpa2011.txt",
}



#print(len(Box(inat.get_observations(user_id='ilisien',taxon_name="tufted titmouse",d1="2025-01-01")).results[0].identifications))
import pyinaturalist as inat
from dataclasses import dataclass
from box import Box
import datetime

SPECIES_LISTS = {
    "CTS OF PA": "species_lists/commontreesofpa2011.txt",
}

class ObservationStack:
    def __init__(self,raw_api_result):
        self.boxed_raw = Box(raw_api_result)
        self.observations = [INatObservation(result) for result in self.boxed_raw.results]

class INatObservation:
    def __init__(self,boxed_result):
        self.boxed_raw = boxed_result

        # user data on this object
        self.times_reviewed = 0
        self.last_reviewed = None # would normally be a datetime object

        # object data
        self.user = self.boxed_raw.user
        self.grade = self.boxed_raw.quality_grade
        self.geoprivacy = self.boxed_raw.taxon_geoprivacy
        self.uuid = self.boxed_raw.uuid
        self.species_guess = self.boxed_raw.species_guess

        self.place_guess = self.boxed_raw.place_guess
        self.identifications = self.boxed_raw.identifications
        self.project_observations = self.boxed_raw.project_observations
        self.photos = self.boxed_raw.photos
        self.user = self.boxed_raw.user

        self.geoprivacy = self.boxed_raw.geoprivacy
        self.location = self.boxed_raw.location

        self.taxon = self.boxed_raw.taxon

        self.num_identification_agreements = self.boxed_raw.num_identification_agreements
        self.num_identification_disagreements = self.boxed_raw.num_identification_disagreements

        

# "grab_species_list" should obtain a list of api objects that conform to the 
# parsed observation object standard set out by the above class 

print(Box(inat.get_observations(user_id='ilisien',taxon_name="fulvifomes robiniae")).results[0].community_taxon_id)
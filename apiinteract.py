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
        self.author = self.get_author_title()
        #self.grade = self.boxed_raw.quality_grade (shouldn't ever be needed; need to be filtering for this in the api calls)
        self.uuid = self.boxed_raw.uuid
        self.sci_name = self.boxed_raw.taxon.name.lower()
        self.common_name = self.boxed_raw.taxon.preferred_common_name.lower()

        self.place = self.boxed_raw.place_guess.lower()
        self.location = self.boxed_raw.location

        self.identifications = self.boxed_raw.identifications
        self.project_observations = self.boxed_raw.project_observations
        self.photos = self.boxed_raw.photos
        self.user = self.boxed_raw.user

        self.geoprivacy = self.boxed_raw.geoprivacy
        

        self.taxon = self.boxed_raw.taxon

        self.num_identification_agreements = self.boxed_raw.num_identification_agreements
        self.num_identification_disagreements = self.boxed_raw.num_identification_disagreements
    
    def get_author_title(self):
        user = self.boxed_raw.user
        return f"{user.name} ({user.login})"
    
    def debug(self):
        print(f"author: {self.author}")
        print(f"uuid: {self.uuid}")
        print(f"sci_name: {self.sci_name}")
        print(f"common_name: {self.common_name}")
        print(f"place: {self.place}")
        print(f"location: {self.location}")

        

# "grab_species_list" should obtain a list of api objects that conform to the 
# parsed observation object standard set out by the above class 

if __name__ == "__main__":
    fungus = INatObservation(Box(inat.get_observations(user_id='ilisien',taxon_name="fulvifomes robiniae")).results[0])
    fungus.debug()
import pyinaturalist as inat
from dataclasses import dataclass
from box import Box
import datetime

SPECIES_LISTS = {
    "CTS OF PA": "species_lists/commontreesofpa2011.txt",
}

class Photo:
    def __init__(self,boxed_photo_object):
        self.boxed_raw = boxed_photo_object
        
        self.id = self.boxed_raw.id
        self.license = self.boxed_raw.license_code
        self.attribution = self.boxed_raw.attribution
        self.square_url, self.thumb_url, self.original_url = self.get_photo_urls()

    def __repr__(self):
        return f"photo {self.id} | license: {self.license} | url: {self.square_url}"

    def get_photo_urls(self):
        square = self.boxed_raw.url
        thumb = square.replace("square","thumb")
        original = square.replace("square","original")
        return square, thumb, original


class Observation:
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
        self.date = self.boxed_raw.observed_on # (datetime object)

        self.identification_count = 2 + self.boxed_raw.num_identification_agreements + self.boxed_raw.num_identification_disagreements
        self.photos = [Photo(photo) for photo in self.boxed_raw.photos]

    def __repr__(self):
        return f"{self.sci_name} by {self.author}"
    
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
        print(f"date: {self.date}")
        print(f"identification_count: {self.identification_count}")
        print(f"photos: {self.photos}")

class ObservationStack:
    def __init__(self,raw_api_result):
        self.observations = [Observation(result) for result in Box(raw_api_result).results]

    def __repr__(self):
        return f"stack: {self.observations}"
    
    def add_new_result(self,new_api_result):
        self.observations.extend([Observation(result) for result in Box(new_api_result).results])

# "grab_species_list" should obtain a list of api objects that conform to the 
# parsed observation object standard set out by the above class 

if __name__ == "__main__":
    fungus = Observation(Box(inat.get_observations(user_id='ilisien',taxon_name="fulvifomes robiniae")).results[0])
    fungus.debug()
    #result = inat.get_observations(user_id='ilisien')
    #stack = ObservationStack(result)
    #result2 = inat.get_observations(user_id='brodiebard')
    #stack.add_new_result(result2)
    #print(stack)

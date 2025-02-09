import pyinaturalist as inat
from dataclasses import dataclass
from box import Box
from datetime import datetime
import random
from climate import get_deciduous_designation

def find_duplicates(list):
    seen = {}
    duplicates_indices = []
    
    for i, item in enumerate(list):
        if item in seen:
            duplicates_indices.append(i)
        else:
            seen[item] = True
    
    return duplicates_indices

class Photo:
    def __init__(self,boxed_photo_object):
        self.boxed_raw = boxed_photo_object
        
        self.id = self.boxed_raw.id
        self.license = self.boxed_raw.license_code
        self.attribution = self.boxed_raw.attribution
        sq, th, og = self.get_photo_urls()
        self.urls = Box({
            "square": sq,
            "thumb": th,
            "original": og
        })
        
    def __repr__(self):
        return f"photo {self.id} | license: {self.license} | url: {self.square_url}"

    def get_photo_urls(self):
        square = self.boxed_raw.url
        thumb = square.replace("square","thumb")
        original = square.replace("square","original")
        return square, thumb, original
    
    def to_dict(self):
        return self.boxed_raw.to_dict(),
    
    @classmethod
    def from_dict(cls,raw_dict):
        return cls(raw_dict)

class Observation:
    def __init__(self,boxed_result, times_reviewed = 0, last_reviewed = None):
        self.boxed_raw = boxed_result

        # user data on this object
        self.times_reviewed = times_reviewed
        self.last_reviewed = last_reviewed # would normally be a datetime object

        # object data
        self.author = self.get_author_title()
        #self.grade = self.boxed_raw.quality_grade (shouldn't ever be needed; need to be filtering for this in the api calls)
        self.uuid = self.boxed_raw.uuid
        self.sci_name = self.boxed_raw.taxon.name.lower()
        self.common_name = self.boxed_raw.taxon.preferred_common_name.lower()

        self.place = self.boxed_raw.place_guess.lower()
        self.location = self.boxed_raw.location
        self.date = self.boxed_raw.observed_on # (datetime object)
        self.season_estimate = get_deciduous_designation(self.location[0],self.location[1],self.date.month) 

        self.id_count = 2 + self.boxed_raw.num_identification_agreements + self.boxed_raw.num_identification_disagreements
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
        print(f"season_estimate: {self.season_estimate}")
        print(f"id_count: {self.id_count}")
        print(f"photos: {self.photos}")
    
    def summary(self):
        return Box({
            "sci_name": self.sci_name,
            "id_count": self.id_count,
            "year": self.date.year,
            "times_reviewed": self.times_reviewed,
            "last_reviewed": self.last_reviewed,
        })
    
    def update_reviews(self):
        self.times_reviewed += 1
        self.last_reviewed = datetime.now()
    
    def to_dict(self):
        return {
            "raw": self.boxed_raw.to_dict(),
            "times_reviewed": self.times_reviewed,
            "last_reviewed": self.last_reviewed.isoformat() if self.last_reviewed is None else None
        }
    
    @classmethod
    def from_dict(cls,dict):
        return cls(
            boxed_result=dict["raw"],
            times_reviewed=dict["times_reviewed"],
            last_reviewed=datetime.fromisoformat(dict["last_reviewed"]) if dict["last_reviewed"] is not None else None
        )

class ObservationStack:
    def __init__(self,raw_api_result=None,dictlist=None):
        if raw_api_result is None:
            if dictlist is None:
                self.observations = None
            else:
                self.observations = [Observation.from_dict(d) for d in dictlist]
        else:
            self.observations = [Observation(result) for result in Box(raw_api_result).results]
            self.remove_duplicates()

    def __repr__(self):
        return f"stack: {self.observations}"
    
    def add_new_result(self,new_api_result):
        self.observations.extend([Observation(result) for result in Box(new_api_result).results])
        self.remove_duplicates()
    
    def remove_duplicates(self):
        uuid_list = [o.uuid for o in self.observations]
        duplicates = sorted(find_duplicates(uuid_list),reverse=True)
        if duplicates:
            for i in duplicates:
                del self.observations[i]

    #def deliver_observation(self,desired_species=None):
    #    if desired_species is None:
    #        # just pick a totally random observation
    #        scores = [o.id_count for o in self.observations]
    #        return random.choices(self.observations,weights=scores,k=1)[0]
    
    def all_observations(self):
        return self.observations
    
    def to_dict(self):
        return {
            "observations": [o.to_dict() for o in self.observations] if self.observations else None
        }
    
    @classmethod
    def from_dict(cls, raw_dict):
        return cls(
            dictlist=raw_dict["observations"]
        )

# "grab_species_list" should obtain a list of api objects that conform to the 
# parsed observation object standard set out by the above class 

if __name__ == "__main__":
    #fungus = Observation(Box(inat.get_observations(user_id='ilisien',taxon_name="fulvifomes robiniae")).results[0])
    #fungus.debug()
    
    #result = inat.get_observations(user_id='ilisien')
    #stack = ObservationStack(result)
    #result2 = inat.get_observations(user_id='brodiebard')
    #stack.add_new_result(result2)
    #print(stack)
    #print("")
    #print("")
    #print("")
    #for _ in range(0,100):
    #    print(stack.deliver_observation())

    result = inat.get_observations(user_id='ilisien',quality_grade="research")
    stack = ObservationStack(result)
    for observation in stack.all_observations():
        print(f"{observation.season_estimate} : {observation.date.month}")

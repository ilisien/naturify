from simple_spaced_repetition import Card
from datetime import timedelta as td
from icecream import ic

from observations import ObservationStack

class OrganismCard(Card):
    def __init__(self,taxon,deciduous_state,observation_stack=None, **kwargs):
        super().__init__(kwargs)
        self.taxon = taxon
        self.deciduous_state = deciduous_state
        self.observation_stack = observation_stack if observation_stack else ObservationStack()

    def __repr__(self):
        return f"OrganismCard for {self.taxon}"

    def to_dict(self):
        return {
            "taxon": self.taxon,
            "deciduous_state": self.deciduous_state,
            "status": self.status,
            "step": self.step,
            "interval": self.interval.total_seconds() if self.interval else None,
            "ease": self.ease,
            "observation_stack": self.observation_stack.to_dict(),
        }

    @classmethod
    def from_dict(cls, orgcard_dict):
        return cls(
            taxon = orgcard_dict["taxon"],
            deciduous_state = orgcard_dict["deciduous_state"],
            status = orgcard_dict["status"],
            step = orgcard_dict["step"],
            interval = td(seconds=orgcard_dict["interval"]) if orgcard_dict["interval"] else None,
            ease = orgcard_dict["ease"],
            observation_stack = ObservationStack.from_dict(orgcard_dict["observation_stack"]),
        )

if __name__ == "__main__":
    bladdernut_card = OrganismCard("staphylea trifolia","bare")
    ic(bladdernut_card)
    bladdernut_dict = bladdernut_card.to_dict()
    ic(bladdernut_dict)
    coffeetree_dict = bladdernut_dict
    coffeetree_dict["taxon"] = "gymnocladus dioicus"
    ic(coffeetree_dict)
    coffeetree_card = OrganismCard.from_dict(coffeetree_dict)
    ic(coffeetree_card)

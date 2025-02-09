from simple_spaced_repetition import Card

class OrganismCard(Card):
    def __init__(self,taxon,deciduous_state):
        super().__init__()
        self.taxon = taxon
        self.deciduous_state = deciduous_state

if __name__ == "__main__":
    pass
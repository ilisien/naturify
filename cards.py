from simple_spaced_repetition import Card

class OrganismCard(Card):
    def __init__(self,taxon,time_of_year):
        super().__init__()
        self.taxon = taxon
        self.time_of_year = time_of_year


if __name__ == "__main__":
    pass
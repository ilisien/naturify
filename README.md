# naturify

a webapp in panel to pull photos from inaturalist to act as an infinite flashcard bank for learning to identify plants



we want to do the following:
- deliver "flash cards" to the user to identify
  - flash cards need to be:
    - approximately random
    - skewed towards observations with more votes
    - properly spaced by species to make studying useful
  - in a study list, the program should choose a few species to start off with, and then as the user progresses it should decide new species to show.
  - need to have some sort of "memory" function -- perhaps a login thing?
  - should also be able to study by other things:
    - (native/invasive) in (place)
    - just in a place
    - under a certain phylum
    - "wildflowers" or "trees" -- non-phylogenic distinctions
    - custom list
    - by some common trees of pa book or whatever
  - needs to also show the place, studied and non-studied flashcards like quizlet style, and the expanded taxa (or at least the family) of them also needs the common name of everything to be all nice to brodie and stuff


because cards and observations are sort of different, they need to be essentially separate

knowing a species is what we're testing, through different images held in the observations

so there can be a base "observation stack" which contains observations that will be referenced by cards, and then there should be a "card stack" of different cards (species, time of year, etc.) which reference observations and pull from the observation stack.

perhaps observation stacks should be held by cards? so a list of potential observations to be used is gotten?
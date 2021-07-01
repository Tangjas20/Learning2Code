from pokecenter import PokeCenter
from pokemon import Pokemon

def test_6_pokemon():
    pallet_town_center = PokeCenter()
    
    pikachu = Pokemon("Pikachu", 100, 50, 20)
    assert pallet_town_center.add_pokemon(pikachu) == True, "Should add Pikachu!"
    assert pallet_town_center.add_pokemon(pikachu) == False, "Pikachu already is in the pokebed! Should not add him/her again."
    # Add your tests to make sure no more than 6 pokemon are added!

def test_has_pokemon():
    pallet_town_center = PokeCenter()
    # Add your own tests to test has_pokemon()

def test_heal():
    pallet_town_center = PokeCenter()
    # Add your own tests to test heal()

test_6_pokemon()
test_has_pokemon()
test_heal()

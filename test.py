"""Only for testing"""

from utils.table import Seat, Table
from utils.openspace import Openspace

def test_openspace():
    openspace = Openspace(num_tables=3, seats_per_tables=4)
    
    names = ["Stef", "Oscar", "Edoardo", "Kevin", "Maxime", "Jean", "Hussain", "Nina", "Elsa", "Nicole"]

    seated_names = openspace.setup_openspace(names)
    print("\nFinal state:")
    print(openspace)
    print("Seated Names:", seated_names)

    return seated_names

seated_names = test_openspace()





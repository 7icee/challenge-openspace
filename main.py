import pandas as pd
import random

from utils.table import Seat, Table
from utils.openspace import Openspace
from utils.file_utils import Retrieve_names, Create_excel

''''''
file_path = r'C:\Users\hp\Imad\challenge-openspace\List_of_names.xlsx'

def test_openspace():
    """"""
    openspace = Openspace(num_tables=6, seats_per_tables=4)
    
    names = Retrieve_names(file_path)

    seated_names = openspace.setup_openspace(names)
    print(openspace)    

    return seated_names

seated_people: list = test_openspace()

Create_excel(seated_people)





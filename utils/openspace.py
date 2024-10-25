import random

from .table import Seat, Table
from .file_utils import Create_excel

class Openspace:
    def __init__(self, num_tables: int, seats_per_tables: int):
        """Defines an openspace"""
        
        self.num_tables = num_tables
        self.seats_per_tables = seats_per_tables
        self.tables_openspace: list = [Table(seats_per_tables) for _ in range(num_tables)]

    def setup_openspace(self, names: list) -> list:
        """Allows to randomise a list a 24 names and set up the openspace with class Seat and Table"""

        if len(names) <= 24:
            random.shuffle(names)
        else:
            names = names[:24]
            random.shuffle(names)

        seated_names = []
        for name in names:
            seated = False
            for table in self.tables_openspace:
                if table.set_occupant_table(name):
                    seated_names.append(name)
                    seated = True
                    break
            
            #if not seated:
                #print(f"{name} could not be seated.")
        
        return seated_names
        
    def __str__(self) -> str :
        """Returns a clean summary of the final openspace arrangement"""

        result = []
        
        for i, table in enumerate(self.tables_openspace, 1):
            result.append(f"Table {i}: {table}")
        return "\n".join(result)

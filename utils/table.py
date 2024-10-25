class Seat:
    def __init__(self, occupant: str = "", free: bool = True):
        """Defines a seat"""

        self.free: bool = free
        self.occupant: str = occupant

    def set_occupant_seat(self, name: str) -> None:
        """Allows to set a occupant to a seat"""

        if self.free == True:
            self.occupant = name
            self.free = False
        
        #else:
            #print(f'This seat is already occupied by {self.occupant}')

    def __str__(self) -> str:
        """Returns free if the seat is free or the name of the occupant if the seat is not free"""

        if self.free:
            return 'Free'
        else:
            return f'by {self.occupant}'





class Table:
    def __init__(self,free_seats: int):
        """Defines a table"""

        self.free_seats: int = free_seats
        self.seats: list = [Seat() for _ in range(free_seats)]
    
    def check_free_seats(self) -> int:
        """Retruns the number of free seats"""

        return sum(seat.free for seat in self.seats)
    
    def set_occupant_table(self, name: str) -> None:
        """Allows to set on occupant on a seat of a table"""

        for seat in self.seats:
            if seat.free:
                seat.set_occupant_seat(name)
                self.free_seats -= 1
                return True
        #print(f"There is no free seat at this table for {name}")
        return False
    
    def __str__(self) -> str:
        """Returns the status of a table with the number of free seats and the names off the occupants"""

        table_occupants = ", ".join(str(seat) for seat in self.seats)
        return f'This table has {self.free_seats} free seats . This table is occupied {table_occupants}.'



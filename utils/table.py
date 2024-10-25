class Seat:
    def __init__(self, occupant: str = "", free: bool = True):
        """"""

        self.free: bool = free
        self.occupant: str = occupant

    def set_occupant_seat(self, name: str) -> None:
        """"""

        if self.free == True:
            self.occupant = name
            self.free = False
        
        else:
            print(f'This seat is already occupied by {self.occupant}')

    def __str__(self) -> str:
        """"""

        if self.free:
            return 'Free'
        else:
            return f'by {self.occupant}'





class Table:
    def __init__(self,free_seats: int):
        """"""

        self.free_seats: int = free_seats
        self.seats: list = [Seat() for _ in range(free_seats)]
    
    def check_free_seats(self) -> int:
        """"""

        return sum(seat.free for seat in self.seats)
    
    def set_occupant_table(self, name: str) -> None:
        """"""

        for seat in self.seats:
            if seat.free:
                seat.set_occupant_seat(name)
                self.free_seats -= 1
                print(f"{name} has been seated")
                return True
        print(f"There is no free seat at this table for {name}")
        return False
    
    def __str__(self) -> str:
        """"""

        table_occupants = ", ".join(str(seat) for seat in self.seats)
        return f'This table has {self.free_seats} free seats . This table is occupied by {table_occupants}.'



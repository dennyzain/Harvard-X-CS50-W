class Flight():
    def __init__(self,capacity):
        self.capacity=capacity
        self.passengers=[]
    
    def add_passenger(self,name):
        if self.open_seats():
            self.passengers.append(name)
            return True
        else:
            return False

    def open_seats(self):
        return self.capacity - len(self.passengers)

seats = Flight(4)

people= ['harry','ron', 'hermione', 'draco','dumbledore']


for person in people:
    if seats.open_seats():
        seats.add_passenger(person)
        print(seats.passengers)
        print(f'Added {person} of Flight seats')
    else:
        print(f'No available seat for {person}')


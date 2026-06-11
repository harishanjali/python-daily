class Movie:
    def __init__(self,movie,price,no_of_tickets):
        self.movie = movie
        self.price = price
        self.no_of_tickets = no_of_tickets

    def get_price(self):
        return self.price*self.no_of_tickets
    

obj = Movie('pushpa',200,5)
print('total amount: ',obj.get_price())

class CricketPlayer:
    def __init__(self,name,runs,matches):
        self.name = name
        self.runs = runs
        self.matches = matches

    def get_average(self):
        return self.runs//self.matches
    
obj = CricketPlayer('virat',13000,250)
print('player average',obj.get_average())

class Mobile:
    def __init__(self,name,percentage):
        self.name = name
        self.percentage = percentage

    def check_percentage(self):
        if self.percentage<=15:
            return 'Low Battery'
        else:
            return 'Sufficient Battery'
        
obj = Mobile('Infinix',15)
print(obj.check_percentage())

class HotelRoom:
    rooms = []
    for i in range(101,111):
        obj = {
            'status':False,
            'number':i
        }
        rooms.append(obj)

    def __init__(self,room_no):
        self.room_no = room_no

    def book_room(self):
        res = HotelRoom.update_rooms(self.room_no)
        if res==True:
            return 'BOOKED'
        else:
            return 'ALREADY BOOKED'
    
    @classmethod
    def update_rooms(cls,no):
        # print(cls.rooms)
        for room in cls.rooms:
            if room['number']==no:
                status = room['status']
                if status==False:
                    room['status'] = True
                    return True
                else:
                    room['status'] = False
                    return False


obj = HotelRoom(103)
print(obj.book_room())

obj = HotelRoom(103)
print(obj.book_room())



class ElectricityBill:
    def __init__(self,name,units):
        self.name = name
        self.units = units
        self.amount = 0
    def bill(self):
        if self.units<=100:
            self.amount = self.units*5
        elif self.units>100 and self.units<=300:
            self.amount = self.units*7
        else:
            self.amount = self.units*10
        return self.amount
    
obj = ElectricityBill('ramesh',250)
print('bill is',obj.bill())
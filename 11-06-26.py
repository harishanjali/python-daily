class PasswordManager:
    def __init__(self,password):
        self.password = password

    def strength(self):
        if len(self.password)>7:
            return 'Strong'
        else:
            return 'Not Strong'
        

obj = PasswordManager('pytho12345')

print('password manager: ',obj.strength())

class Battery:
    def __init__(self,percentage):
        self.percentage = percentage

    def status(self):
        if self.percentage<50:
            return 'Low Battery'
        elif self.percentage>50 and self.percentage<80:
            return 'Medium charge'
        else:
            return 'Full Charge'
        
obj = Battery(40)
print('battery status: ',obj.status())

class TrafficSignal:
    def __init__(self,color):
        self.color = color
    def signal_result(self):
        if self.color == 'red':
            return 'stop'
        elif self.color == 'orange':
            return 'stop and proceed'
        elif self.color == 'green':
            return 'go'
        
obj = TrafficSignal('red')
print('traffic: ',obj.signal_result())

class WaterTank:
    def __init__(self,level):
        self.level = level
        self.total = 3000

    def check_status(self):
        if (self.total//self.level)*100==0:
            return 'empty'
        elif (self.total//self.level)*100<50:
            return 'less than half but not empty'
        elif (self.total//self.level)*100>=50 and (self.total//self.level)*100<100:
            return 'Half FUll'
        else:
            return 'Full'
        
obj = WaterTank(3000)
print('water level: ',obj.check_status())

class Elevator:
    current_floor = 0
    elevator_direction = 'moving down'
    @classmethod
    def change_floor(cls,floor):
        if floor<0 or floor>10:
            return 'Enter proper floor no, between 0 to 10'
        if floor==cls.current_floor:
            return 'You are on same Floor'
        if floor>cls.current_floor:
            # print('test')
            cls.elevator_direction = 'Moving Up^^^^'
        else:
            cls.elevator_direction = 'Moving Down'
        
        cls.current_floor = floor
        return (floor,cls.elevator_direction)
    
# obj = Elevator()
print('Elevator')
print(Elevator.change_floor(4))
print(Elevator.change_floor(0))
print(Elevator.change_floor(5))
print(Elevator.change_floor(8))
print(Elevator.change_floor(3))
print(Elevator.change_floor(3))

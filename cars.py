
#Defines the 4 cars with uniques stats

class Car:
    def __init__(self, name, speed, turn_left, turn_right,distance):
        self.name = name
        self.speed = speed
        self.turn_left = turn_left
        self.turn_right = turn_right
        self.distance = distance
        
car1 = Car("SpeedDemon", 9,6,6,7)
car2 = Car("Lefty", 6,9,7,7)
car3 = Car("Righty", 6,7,9,6)
car4 = Car("Balanced", 7,7,7,7)
from abc import ABC, abstractmethod

class Ship(ABC):
    def __init__(self, name, displacement, speed):
        self.name = name
        self.displacement = displacement
        self.speed = speed
    @abstractmethod
    def __str__(self):
        pass
    
class Frigate(Ship):
    def __init__(self, name, displacement, speed, armament):
        super().__init__(name, displacement, speed)
        self.armament = armament
       
    def __str__(self):
        return self.name
    
    def get_armament(self):
        return self.armament

class Destroyer(Ship):
    def __init__(self, name, displacement, speed, gun_caliber):
        super().__init__(name, displacement, speed)
        self.gun_caliber = gun_caliber
        
    def __str__(self):
        return self.name
    
    def get_gun_caliber(self):
        return self.gun_caliber
    
class Cruiser(Ship):
    def __init__(self, name, displacement, speed, missile_system):
        super().__init__(name, displacement, speed)
        self.missile_system = missile_system
        
    def __str__(self):
        return self.name
    
    def get_missile_system(self):
        return self.missile_system
    
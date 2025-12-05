class Pasport :
    def __init__(self, name, surname, birth_date, passport_number):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.passport_number = passport_number
        
    def __str__(self):
        return f"Passport(Name: {self.name}, Surname: {self.surname}, Birth Date: {self.birth_date}, Passport Number: {self.passport_number})"    
    def add_info(self, name, surname, birth_date, passport_number):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.passport_number = passport_number
    def change_info(self, name=None, surname=None, birth_date=None, passport_number=None):
        if name:
            self.name = name
        if surname:
            self.surname = surname
        if birth_date:
            self.birth_date = birth_date
        if passport_number:
            self.passport_number = passport_number
        
class ForeignPasport(Pasport): 
    def __init__ (self, name , surname, birthdate, passport_number, visa, foreign_passport_number):
        super().__init__(name, surname, birthdate, passport_number)
        self.visa = visa
        self.foreign_passport_number = foreign_passport_number
        
    def add_visa(self, visa):
        self.visa.append(visa)
        
    def remove_visa(self, visa):
        if visa in self.visa:
            self.visa.remove(visa)

    def add_foreign_passport_number(self, foreign_passport_number):
        self.foreign_passport_number = foreign_passport_number
            
    def __str__(self):
        return f"ForeignPassport(Name: {self.name}, Surname: {self.surname}, Birth Date: {self.birth_date}, Passport Number: {self.passport_number}, Visa: {self.visa}, Foreign Passport Number: {self.foreign_passport_number})"
    
class TemperatureConverter:
    conversions = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        TemperatureConverter.conversions += 1
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        TemperatureConverter.conversions += 1
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def get_conversions():
        return TemperatureConverter.conversions    
   
import logging
import argparse



class InvalidNameError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return f'Invalid name: {self.value}. Name should be a non-empty string.'


class InvalidAgeError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return f'Invalid age: {self.value}. Age should be a positive integer.'


class InvalidIdError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return f'Invalid id: {self.value}. Id should be a 6-digit positive integer between 100000 and 999999.'


class Person:

    def __init__(self, surname, name, father_name, age):
        if surname != '' and isinstance(surname, str):
            self.surname = surname
        else:
            raise InvalidNameError(surname)

        if name != '' and isinstance(name, str):
            self.name = name
        else:
            raise InvalidNameError(name)

        if father_name != '' and isinstance(father_name, str):
            self.father_name = father_name
        else:
            raise InvalidNameError(father_name)

        if age > 0 and isinstance(age, int):
            self.age = age
        else:
            raise InvalidAgeError(age)

    def birthday(self):
        logging.info(f'Происходит увеличение возраста на 1: с {self.age} на {self.age + 1}')
        self.age += 1


    def get_age(self):
        return self.age


class Employee(Person):

    def __init__(cls, surname, name, father_name, age, ID):
        super().__init__(surname, name, father_name, age)
        if 99999 < ID < 1000000 and isinstance(ID, int):
            cls.ID = ID
        else:
            raise InvalidIdError(ID)

    def get_level(cls):
        return sum([i for i in (cls.ID % 7)])




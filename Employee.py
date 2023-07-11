from enum import Enum


class Awards(Enum):
    #Перечисление с премиями и баллами
    international = 2


class Employee(object):
    name = ""
    score = 0
    grade = 1
    awards = []
    def __init__(self, name, awards, score):
        self.name = name
        self.score = score
        self.awards = self.set_awards(awards)

    def set_awards(self, args):
        """Инициализирует премии из входящего массива премий"""
        for item in args:
            self.awards.append(item)
        return self.awards




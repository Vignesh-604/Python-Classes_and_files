class Animals:                                                 # This is the class for Object Functions.
    def __init__(self, pet, rating, fren,):
        self.pet = pet
        self.rating = rating
        self.fren = fren

    def rate(self):                                            # Function for the class.
        if self.rating >= 8:
            return "Super Cool"
        else:
            return "Not Cool"

class Animals_2:                                               # Class for Object Functions.py.
    def __init__(self, wild, food, animal):
        self.wild = wild
        self.fuf = food
        self.ani = animal

class Quiz:                                                    # Class for Multiple Choice Questions.py
    def __init__(self, quiz, ans):
        self.quiz = quiz
        self.ans = ans

class Farm:                                                    # Class for Inheritence.py.
    def cat(self):
        print("Cat is cool.")

    def dog(self):
        print("Dog is calm.")

    def mon(self):
        print("Monkey is crazy.")

    def ber(self):
        print("Bear is furry.")

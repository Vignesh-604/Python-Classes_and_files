from Class import Farm

class Barn(Farm):

    def ber(self):                             # Inheritence value of this function will update the value set in class.
        print("Bear is wild.")
                                               # This is excecuted in Inherty.py
    def fox(self):
        print("Fox is smart.")

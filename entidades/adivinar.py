import random

class Adivinar:
    def __init__(self, numero):
        self.numero = numero

    def adivinar_proceso(self):
        if random.randint(1, 10) == self.numero:
         print("Adivine el numero que ingresaste")
        else:
            print("No adivine lol que mal, sera para la proxima")

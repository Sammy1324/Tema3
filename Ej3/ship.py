class Ship:
    def __init__(self, name, length, crew, passengers):
        self.name = name
        self.length = length
        self.crew = crew
        self.passengers = passengers
    def __str__(self):
        return f"Nave {self.name} con longitud de {self.length}m, {self.crew} tripulantes, y {self.passengers} pasajeros"
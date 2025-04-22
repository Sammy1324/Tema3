from ship import Ship

class Launcher:

    def create_ships(self):
        ships = [
            Ship("GX 3000", 300, 4, 30),
            Ship("Bismarck", 100, 2, 10),
            Ship("Cometa Veloz", 200, 3, 20),
            Ship("Titan del Cosmos", 400, 5, 40),
            Ship("GX 2000", 50, 1, 5),
            Ship("Titan del Espacio", 150, 2, 15),
            Ship("GX 4000", 500, 5, 50)
        ]
        return ships

    def organise(self):
        ships = self.create_ships()

        ships_by_name = []
        length = []
        ships_by_length = []

        for ship in ships:
            ships_by_name.append(ship.name)
            length.append(ship)

        ships_by_name.sort(key=lambda x: len(x))
        length.sort(key=lambda x: x.length)
        length.reverse()

        for ship in length:
            ships_by_length.append(ship.name)

        print(f"Naves por nombre: {ships_by_name}\n\n. Naves por longitud: {ships_by_length}.\n")

    def show_CometaNdTitan(self):
        ships = self.create_ships()
        print("Naves Cometa Veloz y Titan del Cosmos:")
        for ship in ships:
            if ship.name == "Cometa Veloz" or ship.name == "Titan del Cosmos":
                print(f"{ship}.\n")

    def most_passengers(self):
        ships = self.create_ships()
        ships.sort(key=lambda x: x.passengers, reverse=True)
        print("Las 5 naves con más pasajeros son:")
        for i in range(5):
            print(f"{i+1}. {ships[i].name}.\n")
    
    def most_crew(self):
        ships = self.create_ships()
        max_crew = max(ships, key=lambda x: x.crew)
        print(f"La nave con más tripulantes es: {max_crew.name} con {max_crew.crew} tripulantes.\n")

    def show_GX(self):
        ships = self.create_ships()
        print("Naves que empiezan con GX:")
        for ship in ships:
            if ship.name.startswith("GX"):
                print(f"{ship}.\n")
            
    def show_oversix_passengers(self):
        ships = self.create_ships()
        print("Naves con más de 6 pasajeros:")
        for ship in ships:
            if ship.passengers > 6:
                print(f"{ship}.\n")

    def show_by_length(self):
        ships = self.create_ships()
        ships.sort(key=lambda x: x.length)
        print("Naves más pequeña y más grande:")
        print(f"Más pequeña: {ships[0].name} con {ships[0].length}m de longitud.")
        print(f"Más grande: {ships[-1].name} con {ships[-1].length}m de longitud.\n")
        

    def main(self):
        self.organise()
        self.show_CometaNdTitan()
        self.most_passengers()
        self.most_crew()
        self.show_GX()
        self.show_oversix_passengers()
        self.show_by_length()
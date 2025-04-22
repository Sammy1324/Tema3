class Launcher:
    def create_stone(self, size):
        stones = []
        for i in range(1, size + 1):  # Crear piedras de 1 a size
            stones.append(i)
        return stones

    def move_stone(self, size, source, target, auxiliary):
        moves = []  # Lista para almacenar los movimientos

        def pyramid(n, source, target, auxiliary):
            if n == 1:
                # Mover una piedra del origen al destino
                moves.append((source, target))
            else:
                # Mover n-1 piedras al auxiliar
                pyramid(n - 1, source, auxiliary, target)
                # Mover la piedra más grande al destino
                moves.append((source, target))
                # Mover las n-1 piedras del auxiliar al destino
                pyramid(n - 1, auxiliary, target, source)

        pyramid(size, "source", "target", "auxiliary")  # Usar nombres de pilas como cadenas
        return moves

    def main(self, size):
        return self.move_stone(size, "source", "target", "auxiliary")
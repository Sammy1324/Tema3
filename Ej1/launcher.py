from stone import Stone

class Launcher:
    def create_stone(self, size):
        stones = []
        for i in range(1, size):
            stone = Stone(i)
            stones.append(stone.size)
            stones.sort()
        return stones
        
    def move_stone(self, size, source, target, auxiliary):
        l = self.create_stone(size)
        for i in l:
            source.append(i)
        while True:
            if len(source) == 0:
                    print(f"Destino: {target}")
                    break    
            if size % 2 == 0:
                auxiliary.append(source[0])
                source.pop(0)
            else:
                target.append(source[0])
                source.pop(0)

    def main(self):
        self.move_stone(75, [], [], [])
import pygame
from launcher import Launcher
import sys

class App:
    def __init__(self, size):
        pygame.init()
        self.size = size
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Visualización de Pirámide de Piedras")
        self.clock = pygame.time.Clock()

        # Colores
        self.bg_color = (30, 30, 30)
        self.pillar_colors = [(100, 0, 100), (0, 100, 200), (0, 200, 100)]
        self.text_color = (255, 255, 255)

        # Generar colores únicos para las piedras
        self.stone_colors = [
            (255 - i * 20, 100 + i * 10, 150 + i * 5) for i in range(size)
        ]

        # Fuente para el texto
        self.font = pygame.font.Font(None, 36)

        # Posiciones de las pilas
        self.pillar_positions = [200, 400, 600]
        self.pillar_width = 10
        self.pillar_height = 300

        # Inicializar las pilas
        self.source = list(range(size, 0, -1))  # De mayor a menor
        self.target = []
        self.auxiliary = []
        self.moves = []

        # Lanzador
        self.launcher = Launcher()
        self.moves = self.launcher.main(size)

        # Índice del movimiento actual
        self.current_move_index = 0
        self.move_count = 0

    def draw_pillars(self):
        """Dibuja las pilas en la pantalla."""
        for i, x in enumerate(self.pillar_positions):
            pygame.draw.rect(
                self.screen,
                self.pillar_colors[i],
                (x - self.pillar_width // 2, self.screen_height - self.pillar_height, self.pillar_width, self.pillar_height),
            )

    def draw_titles(self):
        """Dibuja los títulos de las pilas."""
        titles = ["Principal", "Destino", "Auxiliar"]
        for i, title in enumerate(titles):
            text = self.font.render(title, True, self.text_color)
            text_rect = text.get_rect(center=(self.pillar_positions[i], self.screen_height - self.pillar_height - 20))
            self.screen.blit(text, text_rect)

    def draw_stones(self):
        """Dibuja las piedras en las pilas."""
        piles = [self.source, self.target, self.auxiliary]
        for i, pile in enumerate(piles):
            x = self.pillar_positions[i]
            y = self.screen_height
            for stone in pile:
                width = stone * 20
                height = 20
                y -= height
                pygame.draw.rect(
                    self.screen,
                    self.stone_colors[stone - 1],  # Usar un color único para cada piedra
                    (x - width // 2, y, width, height),
                )

    def draw_move_counter(self):
        """Dibuja el contador de movimientos en la pantalla."""
        text = self.font.render(f"Movimientos: {self.move_count}", True, self.text_color)
        self.screen.blit(text, (10, 10))

    def animate_step(self):
        """Realiza un único paso de la animación."""
        if self.current_move_index < len(self.moves):
            move = self.moves[self.current_move_index]
            from_pile = getattr(self, move[0])
            to_pile = getattr(self, move[1])

            if from_pile:
                stone = from_pile.pop()
                to_pile.append(stone)

            self.current_move_index += 1
            self.move_count += 1

    def run(self):
        """Ejecuta la simulación."""
        running = True

        print("Iniciando la simulación... Por favor revisa tu barra de tareas para ver la animación.")

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(self.bg_color)
            self.draw_pillars()
            self.draw_titles()
            self.draw_stones()
            self.draw_move_counter()

            self.animate_step()

            pygame.display.flip()
            self.clock.tick(2)

        pygame.quit()
        sys.exit()
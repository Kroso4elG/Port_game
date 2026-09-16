import pygame

class Ship:

    def __init__(self):
        self.x = 300
        self.y = 250
        self.width = 180
        self.height = 45
        self.containers = 20
        self.state = "moored"

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            (80, 80, 80),
            (self.x, self.y, self.width, self.height)
        )
        
    def unload(self):
        if self.containers > 0:
            self.containers -= 1
            
            if self.containers == 0:
                self.state = "finished"
        
    

pygame.init()

font = pygame.font.Font(None, 30)

WIDTH = 900
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Port Game 0.1")

clock = pygame.time.Clock()

# -------------------------
# НАСТРОЙКИ СУДНА
# -------------------------

ship_exists = False
ship = Ship()


# -------------------------
# ИГРОВОЙ ЦИКЛ
# -------------------------

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if not ship_exists:
                ship = Ship()
                ship_exists = True
                
            else:
                ship.unload()
                
                if ship.state == "finished":
                    ship_exists = False
                
        
    # -------------------------
    # КАРТА
    # -------------------------

    # ВОДА
    screen.fill((40, 130, 180))

    # БЕТОННАЯ ТЕРРИТОРИЯ
    pygame.draw.rect(
        screen,
        (150, 150, 150),
        (0, 350, 900, 250)
    )

    # ПРИЧАЛ
    pygame.draw.rect(
        screen,
        (100, 100, 100),
        (250, 300, 300, 70)
    )

    # СКЛАД
    pygame.draw.rect(
        screen,
        (120, 120, 120),
        (600, 400, 220, 130)
    )

    # ГРУЗОВИКИ
    pygame.draw.rect(
        screen,
        (200, 200, 200),
        (300, 430, 60, 30)
    )

    pygame.draw.rect(
        screen,
        (200, 200, 200),
        (400, 430, 60, 30)
    )


    # -------------------------
    # ГЛАВНЫЙ ЦИКЛ, ОТРИСОВКА СУДНА
    # -------------------------

    if ship_exists:
        ship.draw(screen)
        
        text = font.render(
            "Контейнеры: " + str(ship.containers),
            True,
            (255, 255, 255)
        )
        screen.blit(text, (300, 210))
        
    if ship.state == "finished":
        text = font.render(
            "Разгрузка завершена!",
            True,
            (255, 255, 255)
        )
        screen.blit(text, (300, 240))
        
    pygame.display.flip()

    clock.tick(60)


pygame.quit()

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

# -------------------------
# НАСТРОЙКИ ЭКРАНА
# -------------------------

# Реальный экран телефона
display = pygame.display.set_mode(
    (0, 0),
    pygame.FULLSCREEN
)

display_width, display_height = display.get_size()

# Логическое разрешение игры
WIDTH = 600
HEIGHT = int(WIDTH * display_height / display_width)

# Поверхность, на которой работает сама игра
screen = pygame.Surface((WIDTH, HEIGHT))

# Коэффициенты перевода координат касания
scale_x = WIDTH / display_width
scale_y = HEIGHT / display_height

pygame.display.set_caption("Port Game 0.0.1")

clock = pygame.time.Clock()

# -------------------------
# НАСТРОЙКИ СУДНА
# -------------------------

ship_exists = False
ship = Ship()

# -------------------------
# НАСТРОЙКИ ВВОДА
# -------------------------

touch_x = 0
touch_y = 0

# -------------------------
# ИГРОВОЙ ЦИКЛ
# -------------------------

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # -------------------------
        # ОБРАБОТКА ВВОДА
        # -------------------------

        if event.type == pygame.MOUSEBUTTONDOWN:

            # Перевод координат телефона в координаты игры
            touch_x = int(event.pos[0] * scale_x)
            touch_y = int(event.pos[1] * scale_y)
            
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
    #ГЛАВНЫЙ ЦИКЛ, ОТРИСОВКА СУДНА
    # -------------------------

    if ship_exists:
        ship.draw(screen)
        
        text = font.render(
        "Контейнеры: " + str(ship.containers),        True,
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

    # -------------------------
    # ОТЛАДКА КООРДИНАТ
    # -------------------------

    text = font.render(
        "Касание: " + str(touch_x) + ", " + str(touch_y),
        True,
        (255, 255, 255)
    )
    screen.blit(text, (20, 20))
        
# Масштабируем игровую поверхность на настоящий экран
    scaled_screen = pygame.transform.scale(
        screen,
        (display_width, display_height)
)

    display.blit(scaled_screen, (0, 0))

    pygame.display.flip()

    clock.tick(60)


pygame.quit()
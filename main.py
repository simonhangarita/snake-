import pygame
import random
from tkinter import *
from tkinter import messagebox


class Cuerpo:

    def __init__(self, window):
        self.x = 60
        self.y = 60
        self.window = window
        self.dir = 3  # 0 right, 1 left, 2 down, 3 up

    def draw(self):
        pygame.draw.rect(self.window, 
(255, 255, 255),
                         (self.x, self.y, 10, 10))

    def draw_head(self):
        pygame.draw.rect(self.window, (127, 127, 127),
                         (self.x, self.y, 10, 10))

    def movement(self):
        if self.dir == 0:
            self.x += 10
        elif self.dir == 1:
            self.x -= 10
        elif self.dir == 2:
            self.y += 10
        elif self.dir == 3:
            self.y -= 10


class food:

    def __init__(self, window):
        self.x = random.randrange(12) * 10
        self.y = random.randrange(12) * 10
        self.window = window

    ###3
    def draw(self):
        pygame.draw.rect(self.window, (255, 0, 0), (self.x, self.y, 10, 10))

    def relocate(self):
        flag = False
        while True:
            self.x = random.randrange(12) * 10
            self.y = random.randrange(12) * 10
            for posi in range(len(snake)):
                if snake[posi].x == self.x and snake[posi].y == self.y:
                    flag = True
                    break
            if not flag:
                break


def redraw(window):
    window.fill((0, 0, 0))
    if manz == -1:
      comida.draw()
    snake[0].draw_head()
    for i in range(1, len(snake)):
        snake[i].draw()


def snake_ubicacion():
    if (len(snake)) > 1:
        for i in range(len(snake) - 1):
            snake[len(snake) - i - 1].x = snake[len(snake) - i - 2].x
            snake[len(snake) - i - 1].y = snake[len(snake) - i - 2].y


def Colision():
    hit = False
    if (len(snake)) > 1:
        for i in range(len(snake) - 1):
            if snake[0].x == snake[i + 1].x and snake[0].y == snake[i + 1].y:
                hit = True
    return hit


def main():
    global comida, snake , manz
    movs = 0
    manz = -1
    window = pygame.display.set_mode((130, 130))
    window.fill((0, 0, 0))
    pygame.display.set_caption("Snake")
    snake = [Cuerpo(window), Cuerpo(window), Cuerpo(window)]
    snake[0].draw()
    comida = food(window)
    redraw(window)
    run = True
    velocidad = 200
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:  ###4
                if event.key == pygame.K_DOWN:
                    if snake[0].dir != 3:
                        snake[0].dir = 2
                if event.key == pygame.K_LEFT:
                    if snake[0].dir != 0:
                        snake[0].dir = 1
                if event.key == pygame.K_RIGHT:
                    if snake[0].dir != 1:
                        snake[0].dir = 0
                if event.key == pygame.K_UP:
                    if snake[0].dir != 2:
                        snake[0].dir = 3
        snake_ubicacion()
        snake[0].movement()
        movs +=1
        if movs == manz:
          comida.relocate()
          manz = -1
        redraw(window)
        pygame.display.update()
        pygame.time.delay(velocidad)
        ###2
        if snake[0].x >= 130:
            Tk().wm_withdraw()
            messagebox.showinfo(title="Perdiste",
                                message=f"Llegaste a una longitud de {len(snake)}")
            break
        elif snake[0].x < 0:
            Tk().wm_withdraw()
            messagebox.showinfo(title="Perdiste",
                                message=f"Llegaste a una longitud de {len(snake)}")
            break

        if snake[0].y >= 130:
            Tk().wm_withdraw()
            messagebox.showinfo(title="Perdiste",
                                message=f"Llegaste a una longitud de {len(snake)}")
            break
        elif snake[0].y < 0:
            Tk().wm_withdraw()
            messagebox.showinfo(title="Perdiste",
                                message=f"Llegaste a una longitud de {len(snake)}")
            break

        if Colision():
            Tk().wm_withdraw()
            messagebox.showinfo(title="Perdiste",
                                message=f"Llegaste a una longitud de {len(snake)}")
            break

        if snake[0].x == comida.x and snake[0].y == comida.y:
            ####1
            #if velocidad > 35:
            #    velocidad -= 5
            manz = random.randint(1,10)
            movs = 0
            #comida.relocate()
            snake.append(Cuerpo(window))
            snake_ubicacion()


main()
pygame.quit()
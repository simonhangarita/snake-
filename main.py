import pygame
import random
from tkinter import *
from tkinter import messagebox
import time

class Cuerpo:

    """
    Esta clase corresponde al cuerpo de la serpiente.
    """
  
    def __init__(self, window):
        # La serpiente inicia en la posicion indicada en el enunciado
        self.x = 60
        self.y = 60
        self.window = window
        self.dir = 3  # inicia moviendose hacia arriba


      
    def draw(self):
        """Esta funcion permite dibujar el cuerpo de la serpiente."""

        # El metodo pygame.draw.rect() recibe como parametros una
        # ventana, un color RGB y un tamano.
        pygame.draw.rect(self.window, 
                        (255, 255, 255),
                        (self.x, self.y, 10, 10)
                        )
      
    
    def draw_head(self):
      """Dibuja la cabeza de la serpiente, la cual tiene un color
      diferente al resto del cuerpo."""
      
      pygame.draw.rect(self.window, 
                         (127, 127, 127),
                         (self.x, self.y, 10, 10)
                        )
      
    
    def movement(self):
        """Permite dirigir el movimiento de la serpiente,
      segun el comando utilizado por el jugador.
      0 es derecha, 1 izquierda, 2 abajo y 3 arriba."""
      
        if self.dir == 0:
            self.x += 10
        elif self.dir == 1:
            self.x -= 10
        elif self.dir == 2:
            self.y += 10
        elif self.dir == 3:
            self.y -= 10


class Alimento:
    """Esta clase tendra los metodos asociados a la aparicion
    de alimento durante el juego."""

  
    def __init__(self, window):
        #ubicamos a la manzana inicialmente en la posicion indicada en el ununciado
        self.x = 100
        self.y = 30
        self.window = window


    def draw(self):
        """Esta funcion permite dibujar la manzana, con una tonalidad
      roja y el tamano del rectangulo."""
        pygame.draw.rect(self.window,
                         (255, 0, 0),
                         (self.x, self.y, 10, 10)
                        )
      
  
    def relocate(self):
        """Esta funcion tiene la logica para la reaparicion aleatoria
      de la manzana."""
        flag = False
      
        #Con este ciclo verificamos que la posicion en que aparezca la manzana no coincida con la posicion actual de la serpiente 
        while True:
            self.x = random.randrange(12) * 10
            self.y = random.randrange(12) * 10
            for posi in range(len(snake)):##O(n)
                # Se revisa que ningun elemento del cuerpo de la
                # serpiente, tenga las mismas coordenadas de la potencial
              # nueva manzana.
                if snake[posi].x == self.x and snake[posi].y == self.y:##O(1)
                    flag = True
                    break
            if not flag:
                break

#esta funcion nos sirve para dibujar nuevamente toda la ventana principal, la manzana(en caso de que la aleatoriedad permita generarla en este turno) y toda la serpiente con su cola
def redraw(window):
    """Esta funcion se encarga de dibujar nuevamente toda la ventana
    principal, con todas las actualizaciones que hayan ocurrido en
    un movimiento: el cambio de posicion de la manzana (si aplica)
    y todos los elementos de la serpiente."""
  
    window.fill((0, 0, 0))
    if apple == -1:
      comida.draw()

    # La cabeza de la serpiente tiene un metodo diferente, al ser
    # de otro color.
    snake[0].draw_head()
  
    for i in range(1, len(snake)):#O(n)
        snake[i].draw() #O(1)?
#con esta funcion buscamos que cada una de las partes de la serpiente a partir de la cola hasta la cabeza, se ubiquen donde estaba la parte siguiente a la hora de realizar un movimiento (lo cual permite que todo el cuerpo siga el movimiento de la cabeza).
def snake_ubication():
    """Con esta funcion, cada una de las partes de la serpiente
    desde la cola hasta la cabeza se ubican donde estaba la parte
    siguiente a la hora de realizar un movimiento (lo cual permite
    que todo el cuerpo siga el movimiento de la cabeza)."""
    if (len(snake)) > 1:
        for i in range(len(snake) - 1):#O(n)
            snake[len(snake) - i - 1].x = snake[len(snake) - i - 2].x #O(1)
            snake[len(snake) - i - 1].y = snake[len(snake) - i - 2].y#O(1)

#esta funcion nos permite parar el programa cuando ocurre que la cabeza de la serpiente choca con otra parte del cuerpo. Es decir, la cabeza de la serpiente coincide en su posicion con alguna otra parte del cuerpo de la serpiente
def colision():
    """Esta funcion se encarga de detener el programa cuando la cabeza
    de la serpiente colisiona con alguna parte de su cuerpo, es decir,
    si su nueva posicion coincide con alguna otra posicion de su cuerpo."""
  
    hit = False
    if (len(snake)) > 1:
        for i in range(len(snake) - 1):#O(n)
            if snake[0].x == snake[i + 1].x and snake[0].y == snake[i + 1].y:#O(1)
                hit = True
    return hit


def main():
    # Se definen las siguientes variables como globales
    # para que puedan ser accedidas desde el Scope de las demas
    # funciones o clases
    global comida, snake , apple

  
    movs = 0 # con esta variable controlamos el numero de movimientos hasta que la manzana aparezca
    apple = -1 # esta variable nos sirve para manejar la aleatoriedad de la aparicion de la manzana

    # Se configura la ventana del juego, tamaño y color de fondo:
    window = pygame.display.set_mode((130, 130))
    window.fill((0, 0, 0))
    pygame.display.set_caption("Snake")

  
    # El cuerpo inicialmente tendria 3 partes(incluyendo la cabeza)
    snake = [Cuerpo(window), Cuerpo(window), Cuerpo(window)]
    snake[0].draw()
    comida = Alimento(window)
    redraw(window)
    run = True
    velocidad = 1# Variable para controlar la velocidad del programa
    #Con velocidad en 0.5 se ve bien.

  
    while run:
      
      # En este ciclo controlamos los eventos que ocurran por parte del jugador
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:  
              
              #los condicionales siguientes permiten cambiar la direccion de la serpiente con los comandos ingresados por el jugador, si el comando es valido
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
                      
        # Actualizamos las posiciones del cuerpo (todavia no la cabeza) de la serpiente:
        snake_ubication()
      
        # La cabeza se mueve segun el comando ingresado por el
        # usuario
        snake[0].movement()
        movs +=1
      
      #con este condicional creamos la manzana cuando los movimientos de la serpiente igualan a los movimientos aleatorios hasta que la manzana aparezca
        if movs == apple:
          comida.relocate()
          apple = -1
        redraw(window)
        pygame.display.update()
      ##con esta funcion controlamos la velocidad
        # pygame.time.delay(velocidad) está ralentizando al parecer, probemos co time.sleep
        time.sleep(velocidad)
      #los siguientes condicionales nos sirven para acabar el juego cuando la serpiente choca con una pared
        if snake[0].x >= 130:
            Tk().wm_withdraw()
            messagebox.showinfo(title="Perdiste",
                                message=f"Has chocado con un borde.\nLlegaste a una longitud de {len(snake)}")
            break
        elif snake[0].x < 0:
            Tk().wm_withdraw()
            messagebox.showinfo(title="Perdiste",
                                message=f"Has chocado con un borde.\nLlegaste a una longitud de {len(snake)}")
            break

        if snake[0].y >= 130:
            Tk().wm_withdraw()
            messagebox.showinfo(title="Perdiste",
                                message=f"Has chocado con un borde.\nLlegaste a una longitud de {len(snake)}")
            break
        elif snake[0].y < 0:
            Tk().wm_withdraw()
            messagebox.showinfo(title="Perdiste",
                                message=f"Has chocado con un borde.\nLlegaste a una longitud de {len(snake)}")
            break
        #con este condicional controlamos el final del juego en caso de que la serpiente choque con su cuerpo
        if colision():
            Tk().wm_withdraw()
            messagebox.showinfo(title="Perdiste",
                                message=f"Chocaste con tu propio cuerpo. \nLlegaste a una longitud de {len(snake)}.")
            break
          
        #en este condicional verificamos si la serpiente se come la manzana, lo cual ocurre si la cabeza de la serpiente coincide en la posicion con la manzana
        if snake[0].x == comida.x and snake[0].y == comida.y:
            ####1
            #if velocidad > 35:
            #    velocidad -= 5
            #generamos un numero random de movimientos entre 1 y 10 hasta que aparezca nuevamente la manzana
            apple = random.randint(1,10)
          #actualizamos los movimientos de la serpiente a cero para que coincida con el numero de movimientos que debe recibe la variable anterior hasta que aparezca la manzana
            movs = 0
            #comida.relocate()
            snake.append(Cuerpo(window))
            #snake_ubication()
            redraw(window)

root = Tk()
root.withdraw()
messagebox.showinfo("¿Estas listo?",
 """Bienvenido al juego Snake.
 Deberas alcanzar las manzanas que iran apareciendo en el tablero.
 Ten cuidado de no chocar con tu cuerpo ni con los bordes.
 Para moverte, usa las flechas del teclado.""")

main()
pygame.quit()

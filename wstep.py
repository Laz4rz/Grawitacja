import pygame
from time import sleep
from class_vector import Vector


colors = {
    'blue': (135,206,235),
    'black': (0,0,0)
}

class Planet:
    def __init__(self, pos, vel, mass, radius, color=colors['blue']):
        self.pos = pos
        self.vel = vel
        self.mass = mass
        self.radius = radius
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, self.color, self.pos.grid_cords, self.radius)

    #zaokroglam bo pygame musi miec calkowite
    #pozwala na korzystanie z pos_grid bez pisania pos_grid() tylko jak atrybut pos_grid
    #po napisaniu klasy Vector to jest zbedne w sumie bo tamta sie zajmuje zaokraglaniem
    # @property
    # def pos_grid(self):
    #     return (round(self.pos[0]),round(self.pos[1]))

    def update(self, dt):
        #to mozna skomentować bo dodane wektory
        # new_pos = (
        #     self.pos[0] + self.vel[0] * dt,
        #     self.pos[1] + self.vel[1] * dt
        # )
        new_pos = self.pos + self.vel * dt
        self.pos = new_pos

pygame.init()

win_size = (820, 820)
win = pygame.display.set_mode(win_size)

p1 = Planet(
    pos = Vector(410.222, 410.123123),
    vel = Vector(10,10),
    mass = 1,
    radius = 15
)


#
while True:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             exit()
#         if event.type == pygame.MOUSEBUTTONUP:
#             pygame.draw.circle(win, colors['blue'], pygame.mouse.get_pos(), 20)
#         print(event)
     win.fill(colors['black'])
     p1.update(0.01)
     p1.draw(win)
     pygame.display.update()

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices=((1,1,1),
          (1,-1,1),
          (-1,-1,1),
          (1,-1,1),
          (1,-1,1),
          (1,-1,1),
          (1,-1,1),)

def sq():
    glBegin(GL_LINES)
    for e in edge:
        for vertex in e:
            glVertex3iv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display=(500,500)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL|RESIZABLE)

    gluPerspective(40, display[0]/display[1], 1, 10)
    glTranslatef(0.0, 0.0, -5)
    glRotatef(45, 1, 0, 0)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1, 1, 2, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        sq()
        pygame.display.flip()
        pygame.time.wait(10)

main()
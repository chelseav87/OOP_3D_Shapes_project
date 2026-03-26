import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices=((0,0,1),(1,1,-1),(1,-1,-1),(-1,-1,-1),(-1, 1, -1))
faces=((1,2,3,4), # base
       (0,1,2), # right side
       (0,2,3), # front side
       (0,3,4), # left side
       (0,4,1)) # back side

# draw pyramid
def sq():
    glColor3f(1,1,1)

    glBegin(GL_QUADS)
    glNormal3f(0,0,-1)
    for vertex in faces[0]:
        glVertex3iv(vertices[vertex])
    glEnd()

    glBegin(GL_TRIANGLES)
    glNormal3f(0,1,1)
    for vertex in faces[1]:
        glVertex3iv(vertices[vertex])
    glEnd()

    glBegin(GL_TRIANGLES)
    glNormal3f(1, 0, 1)
    for vertex in faces[2]:
        glVertex3iv(vertices[vertex])
    glEnd()

    glBegin(GL_TRIANGLES)
    glNormal3f(0, -1, 1)
    for vertex in faces[3]:
        glVertex3iv(vertices[vertex])
    glEnd()

    glBegin(GL_TRIANGLES)
    glNormal3f(-1, 0, 1)
    for vertex in faces[4]:
        glVertex3iv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display=(500,500)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL|RESIZABLE)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_NORMALIZE)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glLightfv(GL_LIGHT0, GL_POSITION, (1,1,1,1))

    gluPerspective(50, display[0]/display[1], 1, 10)
    glTranslatef(0.0, 0.0, -5)
    glRotatef(270, 1, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1, 1, 1, 100)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        sq()
        pygame.display.flip()
        pygame.time.wait(30)

main()
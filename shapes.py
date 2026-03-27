import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

class Shapes3D:
    def __init__(self, shape_type, colour, location):
        self.__shape_type = shape_type
        self.__shape_colour = colour
        self.__shape_location = location

    def volume(self):
        return None

    def surface_area(self):
        return None

    def draw(self):
        return None

    def getType(self):
        return self.__shape_type

class SquarePyramid(Shapes3D):
    def __init__(self, colour, location, base_length, height):
        super().__init__("Square-based Pyramid", colour, location)
        self.__base_length = base_length
        self.__height = height

    def volume(self):
        return 1/3 * self.__base_length ** 2 * self.__height

    def surface_area(self):
        return self.__base_length ** 2 + 2 * self.__base_length * (self.__base_length ** 2 / 4 + self.__height ** 2) ** 0.5

    def draw(self):
        vertices = [(0, 0, self.__height),
                    (self.__base_length, self.__base_length, -self.__height),
                    (self.__base_length, -self.__base_length, -self.__height),
                    (-self.__base_length, -self.__base_length, -self.__height),
                    (-self.__base_length, self.__base_length, -self.__height)]
        faces = [(1, 2, 3, 4),  # base
                 (0, 1, 2),  # right side
                 (0, 2, 3),  # front side
                 (0, 3, 4),  # left side
                 (0, 4, 1)]  # back side

        def draw_pyramid():
            glColor3f(1, 1, 1)

            glBegin(GL_QUADS)
            glNormal3f(0, 0, -1)
            for vertex in faces[0]:
                glVertex3fv(vertices[vertex])
            glEnd()

            glBegin(GL_TRIANGLES)
            glNormal3f(0, 1, 1)
            for vertex in faces[1]:
                glVertex3fv(vertices[vertex])
            glEnd()

            glBegin(GL_TRIANGLES)
            glNormal3f(1, 0, 1)
            for vertex in faces[2]:
                glVertex3fv(vertices[vertex])
            glEnd()

            glBegin(GL_TRIANGLES)
            glNormal3f(0, -1, 1)
            for vertex in faces[3]:
                glVertex3fv(vertices[vertex])
            glEnd()

            glBegin(GL_TRIANGLES)
            glNormal3f(-1, 0, 1)
            for vertex in faces[4]:
                glVertex3fv(vertices[vertex])
            glEnd()

        def visual():
            pygame.init()
            display = (500, 500)
            pygame.display.set_mode(display, DOUBLEBUF | OPENGL | RESIZABLE)

            glEnable(GL_DEPTH_TEST)
            glEnable(GL_LIGHTING)
            glEnable(GL_LIGHT0)
            glEnable(GL_COLOR_MATERIAL)
            glEnable(GL_NORMALIZE)
            glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
            glLightfv(GL_LIGHT0, GL_POSITION, (1, 1, 1, 1))

            gluPerspective(55, display[0] / display[1], 1, 10)
            glTranslatef(0.0, 0.0, -4)
            glRotatef(270, 1, 0, 0)

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                glRotatef(1, 1, 1, 100)
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                draw_pyramid()
                pygame.display.flip()
                pygame.time.wait(30)
        visual()

class Icosahedron(Shapes3D):
    def __init__(self, colour, location, side_length):
        super().__init__("Icosahedron", colour, location)
        self.__side_length = side_length

    def volume(self):
        return (5 * (3 + 5 ** 0.5))/12 * self.__side_length ** 3

    def surface_area(self):
        return 5 * 3 ** 0.5 * self.__side_length ** 2

    def draw(self):
        phi = (1 + 5 ** 0.5) / 2
        vertices = [(phi, 0, -1), (phi, 0, 1), (-phi, 0, -1), (-phi, 0, 1),
                    (-1, phi, 0), (1, phi, 0), (-1, -phi, 0), (1, -phi, 0),
                    (0, -1, phi), (0, 1, phi), (0, -1, -phi), (0, 1, -phi)]
        faces = [(0, 11, 5), (0, 5, 1), (0, 1, 7), (0, 7, 10), (0, 10, 11),
                 (1, 5, 9), (5, 11, 4), (11, 10, 2), (10, 7, 6), (7, 1, 8),
                 (3, 9, 4), (3, 4, 2), (3, 2, 6), (3, 6, 8), (3, 8, 9),
                 (4, 9, 5), (2, 4, 11), (6, 2, 10), (8, 6, 7), (9, 8, 1)]

        def draw_icosahedron():
            glColor3f(1, 1, 1)
            glBegin(GL_TRIANGLES)
            for face in faces:
                v1 = np.array(vertices[face[0]])
                v2 = np.array(vertices[face[1]])
                v3 = np.array(vertices[face[2]])
                normal = np.cross(v2 - v1, v3 - v1)
                normal = normal / np.linalg.norm(normal)
                glNormal3fv(normal)
                for vertex in face:
                    glVertex3fv(vertices[vertex])
            glEnd()

        def visual():
            pygame.init()
            display = (500, 500)
            pygame.display.set_mode(display, DOUBLEBUF | OPENGL | RESIZABLE)

            glEnable(GL_DEPTH_TEST)
            glEnable(GL_LIGHTING)
            glEnable(GL_LIGHT0)
            glEnable(GL_COLOR_MATERIAL)
            glEnable(GL_NORMALIZE)
            glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
            glLightfv(GL_LIGHT0, GL_POSITION, (1, 1, 0, 1))

            gluPerspective(50, display[0] / display[1], 1, 10)
            glTranslatef(0.0, 0.0, -5)
            glRotatef(120, 1, 0, 0)
            glScalef(self.__side_length, self.__side_length, self.__side_length)

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                glRotatef(1, 1, 1, 100)
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                draw_icosahedron()
                pygame.display.flip()
                pygame.time.wait(30)

        visual()
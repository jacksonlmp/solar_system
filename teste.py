import sys

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def Desenha():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 0.0, 0.0)

    glBegin(GL_QUADS)
    glVertex2i(50,150)
    glVertex2i(50,50)
    glColor3f(0.0,0.0,1.0)
    glVertex2i(150,50)
    glVertex2i(150,150)
    glEnd()

    glBegin(GL_POINTS)
    glColor3f(1.0,0.0,0.0)
    glVertex2i(200,50)
    glVertex2i(100,130)
    glVertex2i(150,130)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.0,1.0,0.0)
    glVertex2i(0,0)
    glVertex2i(200,200)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex2i(100,100)
    glVertex2i(100,200)
    glVertex2i(200,200)
    glVertex2i(200,100)
    glEnd()

    glFlush()

def Inicializa():
    glClearColor(0.0,0.0,0.0, 1.0)

def AlteraTamanhoJanela(w, h):
    if (h == 0):
        h = 1

    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    if (w <= h):
        gluOrtho2D(0.0, 250.0, 0.0, 250.0*h/w)
    else:
        gluOrtho2D(0.0, 250.0*w/h, 0.0, 250.0)

if __name__ == "__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400,350)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Quadrado")
    glutDisplayFunc(Desenha)
    glutReshapeFunc(AlteraTamanhoJanela)
    Inicializa()
    glutMainLoop()
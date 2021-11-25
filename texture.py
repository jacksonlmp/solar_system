import numpy

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image

global texture_index, tex0, tex1, tex2, tex3, tex4, tex5, tex6, tex7, tex8, tex9, tex10, tex11


#load images
def load_images():
    global tex0, tex1, tex2, tex3, tex4, tex5, tex6, tex7, tex8, tex9, tex10, tex11
    tex0 = read_texture('./textures/sun.jpg')
    tex1 = read_texture('./textures/mercury.jpg')
    tex2 = read_texture('./textures/venus.jpg')
    tex3 = read_texture('./textures/earth.jpg')
    tex4 = read_texture('./textures/moon.jpg')
    tex5 = read_texture('./textures/mars.jpg')
    tex6 = read_texture('./textures/jupiter.jpg')
    tex7 = read_texture('./textures/saturn.jpg')
    tex8 = read_texture('./textures/saturnRing.jpg') #sem referencia
    tex9 = read_texture('./textures/uranus.jpg')
    tex10 = read_texture('./textures/uranusRing.jpg') #sem referencia
    tex11 = read_texture('./textures/neptune.jpg')
    return tex0, tex1, tex2, tex3, tex4, tex5, tex6, tex7, tex8, tex9, tex10, tex11

def read_texture(filename):
    img = Image.open(filename)
    img_data = numpy.array(list(img.getdata()), numpy.int8)
    textID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textID)
    # glPixelStorei(GL_UNPACK_ALIGNMENT, texture_index)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
    return textID

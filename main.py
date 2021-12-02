import sys
import math

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from texture import load_images

# Variaveis globais
global angulo, fAspect, rotX, rotY, rotZ, obsX, obsY, obsZ, solAtivo
global rotX_ini, rotY_ini, obsX_ini, obsY_ini, obsZ_ini, x_ini, y_ini, botao
global tex0, tex1, tex2, tex3, tex4, tex5, tex6, tex7, tex8, tex9, tex10, tex11

solAtivo = 1
orbita = 1
eixoX, eixoY, eixoZ = 0, 0, 0

# Constantes utilizadas na interacao com o mouse
SENS_ROT = 5.0
SENS_OBS = 10.0
SENS_TRANSL = 10.0


def Desenha_planeta(textura, pos_y, pos_x, escala, diametro, raio):
  t = glutGet(GLUT_ELAPSED_TIME) / 1000.0
  a = t*2

  glPushMatrix()
  glRasterPos2f(0,-pos_y)
  # glutBitmapString(GLUT_BITMAP_9_BY_15, planeta)
  glTranslated(0, -pos_y, 0)
  # Movimento de Translação
  glTranslatef((pos_x * math.cos(2.0 * 3.14 * a*raio / 100)),(pos_y +pos_y * math.sin(2.0 * 3.14 * a*raio/ 100)), 0)
  obj = gluNewQuadric()
  gluQuadricTexture(obj, GL_TRUE)
  glEnable(GL_TEXTURE_2D)
  glBindTexture(GL_TEXTURE_2D, textura)
  glScalef(escala,escala, escala)
  glRotated(a * 20, 0, 0, 1)
  gluSphere(obj, diametro, 25, 25)
  glDisable(GL_TEXTURE_2D)
  glPopMatrix()

def Desenha_planetas_com_Satelites_e_Aneis(textura_planeta, textura_satelite, textura_aneis, pos_y, pos_x, escala, diametro1, diametro2, raio, raio_lua):

  t = glutGet(GLUT_ELAPSED_TIME) / 1000.0
  a = t * 2

  glPushMatrix()
  glRasterPos2f(0,-pos_y)
  # glutBitmapString(GLUT_BITMAP_9_BY_15, planeta)
  glTranslated(0, -pos_y, 0)
  # Movimento de Translacao
  glTranslatef((pos_x * math.cos(2.0 * 3.14 * a*raio / 100)),(pos_y +pos_y * math.sin(2.0 * 3.14 * a*raio/ 100)), 0)
  obj = gluNewQuadric()
  gluQuadricTexture(obj, GL_TRUE)
  glEnable(GL_TEXTURE_2D)
  glBindTexture(GL_TEXTURE_2D,textura_planeta)
  glScalef(escala,escala,escala)
  glRotated(a*20, 0, 0, 1)
  gluSphere(obj,diametro1,25,25)
  glScalef(escala,escala,escala)
  # Desenha o anel
  glEnable(GL_TEXTURE_2D)
  glBindTexture(GL_TEXTURE_2D, textura_aneis)
  desenhaAnel(pos_x/80,pos_y/80)

  # Satelite
  # Translacao da Lua
  glTranslatef(pos_x/20*(math.cos(2.0 * 3.14 * a*raio_lua / 100)),(pos_y/20*math.sin(2.0 * 3.14 * a*raio_lua / 100)), 0)
  glBindTexture(GL_TEXTURE_2D,textura_satelite)
  glScalef(escala,escala,escala)
  glRotated(a * 5, 1, 0, 1)
  gluSphere(obj,diametro2,50,50)
  glDisable(GL_TEXTURE_2D)

  glPopMatrix()

def desenha_planetas_com_Satelites(textura_planeta, textura_satelite, pos_y, pos_x, escala, diametro1, diametro2, raio, raio_lua):
  t = glutGet(GLUT_ELAPSED_TIME) / 1000.0
  a = t*2

  glPushMatrix()
  glRasterPos2f(0,-pos_y)
  # glutBitmapString(GLUT_BITMAP_9_BY_15, planeta)
  glTranslated(0, -pos_y, 0)
  # Movimento de Translacao
  glTranslatef((pos_x * math.cos(2.0 * 3.14 * a*raio / 100)),(pos_y +pos_y * math.sin(2.0 * 3.14 * a*raio/ 100)), 0)
  obj = gluNewQuadric()
  gluQuadricTexture(obj,GL_TRUE)
  glEnable(GL_TEXTURE_2D)
  glBindTexture(GL_TEXTURE_2D,textura_planeta)
  glScalef(escala,escala,escala)
  glRotated(a*20, 0, 0, 1)
  gluSphere(obj,diametro1,25,25)

  # Satelite
  # Translacao da Lua
  glTranslatef(pos_x/10*(math.cos(2.0 * 3.14 * a*raio_lua / 100)),(pos_y/10*math.sin(2.0 * 3.14 * a*raio_lua / 100)), 0)

  glBindTexture(GL_TEXTURE_2D,textura_satelite)
  glScalef(escala,escala,escala)
  glRotated(a*5, 1, 0, 1)
  gluSphere(obj,diametro2,50,50)
  glDisable(GL_TEXTURE_2D)

  glPopMatrix()

def desenhaAnel(eixoX, eixoY):
  glPushMatrix()
  glBegin(GL_LINE_LOOP)
  for i in range(360):
    rad = i*3.14/180
    glVertex2f(math.cos(rad)*eixoX,math.sin(rad)*eixoY)
  glEnd()
  glPopMatrix()

def Desenha():
  glDrawBuffer(GL_BACK)
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  # desenha todos os objetos na tela
  Sistema_Solar()
  glutSwapBuffers()

# Desenha o sistema solar e as orbitas dos planetas
def Sistema_Solar():
  global tex1, tex2

  t = glutGet(GLUT_ELAPSED_TIME) / 1000.0
  a = t
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

  # SOL
  if(solAtivo==1):
    # GLfloat
    light_ambient = [eixoX,eixoY,eixoZ,1.0]
    light_diffuse = [eixoX,eixoY,eixoZ,1.0]
    light_specular = [eixoX, eixoY, eixoZ, 1.0]
    light_position= [1.0, 0.0, 0.0, 1.0]
    
    # configura alguns parametros do modelo de iluminacao: MATERIAL
    mat_ambient    = [0.7, 0.7, 0.7, 1.0 ]
    mat_diffuse    = [0.8, 0.8, 0.8, 1.0 ]
    mat_specular   = [ 1.0, 1.0, 1.0, 1.0 ]
    high_shininess = [ 100.0 ]

    glShadeModel (GL_SMOOTH)

    # Propriedades da fonte de luz
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE)

    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)

    glPushMatrix()
    glRasterPos2f(0,1.5)
    # glutBitmapString(GLUT_BITMAP_9_BY_15, "Sol")
    qobj = gluNewQuadric()
    gluQuadricTexture(qobj, GL_TRUE)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D,tex0)
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, high_shininess)
    glRotated(a*7, 0, 0, 1)
    glScalef(3,3,3)
    gluSphere(qobj,1,25,25)
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)
  else:
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)

   # MERCURIO - Diametro: 4.879,4 km
  Desenha_planeta(tex1, 7, 7, 2,0.48,3.7)

  # VENUS - Diametro: 12.103,6 km
  Desenha_planeta(tex2, 17, 17, 1.2, 1.21 ,2.5)

  # TERRA E LUA - Diametro Terra: 12.756,2 km
  desenha_planetas_com_Satelites(tex3, tex4, 27, 27, 1.2,1.27,0.5,1.9,0.2)

  # MARTE - Diametro: 6.792,4 km
  desenha_planetas_com_Satelites(tex5, tex4, 41, 41, 1.2,0.68,0.5,1.9,1)

  # JUPITER       */ #Diametro: 142.984 km
  Desenha_planetas_com_Satelites_e_Aneis(tex6, tex4, tex8, 80, 80, 1.5,1.43,0.25,1.9,1)

  # SATURNO     */ #Diametro: 120.536 km
  Desenha_planetas_com_Satelites_e_Aneis(tex7, tex4, tex8, 97, 97, 1.5,1.2,0.25,1.5,1)

  # URANO   */ #Diametro: 51.118 km
  Desenha_planetas_com_Satelites_e_Aneis(tex8, tex4, tex10, 107, 107, 1.5,0.51,0.25,1.2,1.3)

  # NETUNO   */  #Diametro: 49.528 km
  Desenha_planetas_com_Satelites_e_Aneis(tex11, tex4, tex10, 127, 127, 1.5,0.495,0.20,1,1)

  # PLUTAO */  #Diametro: 2.377 km
  desenha_planetas_com_Satelites(tex4, tex4, 140, 140,-0.35,2.3,3,0.8,0.6)

  glRasterPos2f(0,-51)
  # glutBitmapString(GLUT_BITMAP_9_BY_15, "Cinturao de Asteroides")
  # desenhaAsteroide(10,10)

def Desenha_Orbita(pos_y, pos_x):
  glPushMatrix()
  glTranslated(0, -pos_y, 0)
  glBegin(GL_LINE_LOOP)
  for i in range(100): # Desenha a linha da orbita, a variavel i vai juntando cada linha em uma circunferencia
    glVertex2f(
      pos_x * math.cos(2.0 * 3.14 * i / 100),
      pos_y + pos_y * math.sin(2.0 * 3.14 * i / 100)
    )

  glEnd()
  glPopMatrix()

def mostraOrbitas():

  # MERCURIO - Diametro: 4.879,4 km
  Desenha_Orbita(7,7)

  # VENUS - Diametro: 12.103,6 km
  Desenha_Orbita(17,17)

  # TERRA - Diametro: 12.756,2 km
  Desenha_Orbita(27,27)

  # MARTE -Diametro: 6.792,4 km
  Desenha_Orbita(41,41)

  # JUPITER - Diametro: 142.984 km
  Desenha_Orbita(80,80)

  # SATURNO - Diametro: 120.536 km
  Desenha_Orbita(97,97)

  # URANO -Diametro: 51.118 km
  Desenha_Orbita(107,107)

  # NETUNO - Diametro: 49.528 km
  Desenha_Orbita(127,127)

  # PLUTAO - Diametro: 2.377 km
  # Desenha_Orbita(140,140)

def Sistema_Solar_com_orbitas():
  glDrawBuffer(GL_BACK)
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  # desenha todos os objetos na tela
  Sistema_Solar()
  mostraOrbitas()
  glutSwapBuffers()

def atualiza():
  glutPostRedisplay()

def Inicializa ():
  global angulo, rotX, rotY, rotZ, obsX, obsY, obsZ
  global tex0, tex1, tex2, tex3, tex4, tex5, tex6, tex7, tex8, tex9, tex10, tex11

  # Inicializa a variavel que especifica o angulo da projecao
  # perspectiva
  angulo = 10
  # Inicializa as variaveis usadas para alterar a posicao do
  # observador virtual
  rotX = 0
  rotY = 0
  rotZ = 0
  obsX = obsY = 0
  obsZ = 150

  # loadTexture() #Inicializa as texturas
  tex0, tex1, tex2, tex3, tex4, tex5, tex6, tex7, tex8, tex9, tex10, tex11 = load_images()

  # #Inicializa obj
  # inicializaObj()

  glEnable(GL_CULL_FACE)
  glCullFace(GL_BACK)

  glEnable(GL_LIGHTING)
  glEnable(GL_LIGHT0)
  glEnable(GL_DEPTH_TEST)

def PosicionaObservador():
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()

  glTranslatef(-obsX*0.5,-obsY*0.5,-obsZ*0.5)
  glRotatef(rotX,1,0,0)
  glRotatef(rotY,0,1,0)
  glRotatef(rotZ,0,0,1)

def EspecificaParametrosVisualizacao():
  global angulo
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluPerspective(angulo,fAspect,0.5,2000)
  PosicionaObservador()

def Redimensiona(w, h):
  global fAspect
  # Para previnir uma divisao por zero
  if ( h == 0 ):
    h = 1

  glViewport(0, 0, w, h)
  # Calcula a correção de aspecto
  fAspect = w/h

  EspecificaParametrosVisualizacao()

def SpecialKeyboard(tecla, eixoX, eixoY):
  global angulo, rotX, rotY
  
  if tecla == GLUT_KEY_RIGHT:
    glRotatef(rotX, 1, 0, 0)
    rotX += 1

  elif tecla == GLUT_KEY_LEFT:
    glRotatef(rotY, 0, 1, 0)
    rotY += 1

  elif tecla == GLUT_KEY_DOWN:
    if(angulo<=150):
      angulo +=5 # diminui zoom

  elif tecla == GLUT_KEY_UP:
    if(angulo>=10):
      angulo -=5 # aumenta zoom
  EspecificaParametrosVisualizacao()
  glutPostRedisplay()

def teclado(tecla, eixoX, eixoY):
  global solAtivo, orbita, obsZ

  if tecla == chr(27): # Esc para sair
    sys.exit()

  elif tecla == b'l' or tecla == b'L': # Remove o Sol e toda a luz do sistema
    solAtivo = not solAtivo
    glutDisplayFunc(Sistema_Solar_com_orbitas)

  elif tecla == b'c' or tecla == b'C': # Centraliza no Sol - visao superior do sistema
    obsZ = 50

  elif tecla == b'o' or tecla == b'O': # Mostra ou remove as orbitas
    orbita = not orbita

    if(orbita==True):
      glutDisplayFunc(Sistema_Solar_com_orbitas)
    else:
      # Mostra o sistema solar sem as orbitas
      glutDisplayFunc(Desenha)

  glLoadIdentity()
  gluLookAt(obsX,obsY,obsZ, 0,0,0, 0,1,0)
  glutPostRedisplay()

def GerenciaMouse(button, state, eixoX, eixoY):
  global obsX, obsY, obsZ, rotX, rotY, obsX_ini, obsY_ini, obsZ_ini, rotX_ini, rotY_ini, x_ini, y_ini, botao

  if (state==GLUT_DOWN):
    # Salva os parametros atuais
    x_ini = eixoX
    y_ini = eixoY
    obsX_ini = obsX
    obsY_ini = obsY
    obsZ_ini = obsZ
    rotX_ini = rotX
    rotY_ini = rotY
    botao = button
  else:
    botao = -1

def GerenciaMovimento(eixoX, eixoY):
  global x_ini, y_ini, rotX, rotY, obsX, obsY, obsZ

  # Botao esquerdo do mouse
  if(botao==GLUT_LEFT_BUTTON):
    # Calcula diferenças
    deltax = x_ini - eixoX
    deltay = y_ini - eixoY
    # E modifica angulos
    rotY = rotY_ini - deltax/SENS_ROT
    rotX = rotX_ini - deltay/SENS_ROT

  # Botao direito do mouse
  elif(botao==GLUT_RIGHT_BUTTON):
    deltax = x_ini - eixoX
    deltay = y_ini - eixoY
    # Calcula diferença
    deltaz = deltax - deltay
    # E modifica distancia do observador
    obsZ = obsZ_ini + deltaz/SENS_OBS

  PosicionaObservador()
  glutPostRedisplay()

def main():
  glutInit(sys.argv)
  glutInitContextVersion(1,1) 
  glutInitContextProfile(GLUT_COMPATIBILITY_PROFILE)

  glutInitDisplayMode(GLUT_RGB| GLUT_DOUBLE | GLUT_DEPTH)
  glutInitWindowSize(1800,1200)
  glutInitWindowPosition(100,100)
  glutCreateWindow("Sistema Solar")

  # imprimeInstrucoes() <-> Metodo comentado

  glutDisplayFunc(Sistema_Solar_com_orbitas)

  glutReshapeFunc(Redimensiona)

  glutSpecialFunc(SpecialKeyboard)
  glutKeyboardFunc(teclado)
  glutMouseFunc(GerenciaMouse)
  glutMotionFunc(GerenciaMovimento)

  Inicializa()

  glutIdleFunc(atualiza) 
  glutMainLoop() 
  return 0

main()
from OpenGL.GL import *
from glew_wish import *
import glfw
import random

def main():
    #Inicia glfw
    if not glfw.init():
        return 

    #Crea la ventana
    #Independientemente del SO que usemos
    window = glfw.create_window(800,600,"Mi ventana", None, None)

    #configuramos OpenGl
    glfw.window_hint(glfw.SAMPLES,4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
        #Establecemos el contexto
    glfw.make_context_current(window)

     #Activamos las funciones modernas de OpenGL
    glweExperimental = True 

    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return 

    #Obtenemos versiones de OpenGl y Shader
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):

        R = random.random()
        B = random.random()
        A = random.random()
        
        #Estableceregion  del dibujo
        glViewport(0,0,800,600)
        #Establece color de borrado
        glClearColor(R,B,0.5,A)
        #Borra el ocntenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #dibujar

        #Preguntar si hubo entradas de perifericos(teclado, mouse, gamepad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #termina los procesos que inicio glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()


    
        
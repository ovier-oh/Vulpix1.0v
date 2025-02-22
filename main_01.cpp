#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <iostream>

int main() {
    // Inicializar GLFW
    if (!glfwInit()) {
        std::cerr << "Error al inicializar GLFW" << std::endl;
        return -1;
    }

    // Crear una ventana OpenGL
    GLFWwindow* ventana = glfwCreateWindow(800, 600, "Mi primera ventana OpenGL", nullptr, nullptr);
    if (!ventana) {
        std::cerr << "Error al crear la ventana" << std::endl;
        glfwTerminate();
        return -1;
    }

    // Hacer el contexto actual
    glfwMakeContextCurrent(ventana);

    // Inicializar GLEW
    glewExperimental = GL_TRUE;
    if (glewInit() != GLEW_OK) {
        std::cerr << "Error al inicializar GLEW" << std::endl;
        return -1;
    }

    // Bucle principal
    while (!glfwWindowShouldClose(ventana)) {
        glClear(GL_COLOR_BUFFER_BIT); // Limpiar el buffer de color

        glfwSwapBuffers(ventana); // Intercambiar buffers
        glfwPollEvents();         // Manejar eventos
    }

    // Limpiar recursos y cerrar
    glfwDestroyWindow(ventana);
    glfwTerminate();
    return 0;
}


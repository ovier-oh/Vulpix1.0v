#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <iostream> 

// Codigo fuente del Vertex Shader 
const char* vertexShaderSource = R"(
    #version 330 core 
    layout (location = 0) in vec3 aPos; 
    void main(){
      gl_Position = vec4(aPos, 1.0);
    }
)";

// Codigo fuente del Fragment Shader 
const char* fragmentShaderSource = R"(
      #version 330 core
      out vec4 FragColor;
      void main(){
        FragColor = vec4(1.0, 0.5, 0.2, 1.0) // Color naranja 
      }
    )";

int main(){
    // 1. Inicializar GLFW
    if (!glfwInit()) {
        std::cerr << "Error al inicializar GLFW" << std::endl;
        return -1;
    }

    // 2. Crear la ventana
    GLFWwindow* window = glfwCreateWindow(800, 600, "Triángulo OpenGL", nullptr, nullptr);
    if (!window) {
        std::cerr << "Error al crear la ventana GLFW" << std::endl;
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(window);

    // 3. Inicializar GLEW
    glewExperimental = GL_TRUE;
    if (glewInit() != GLEW_OK) {
        std::cerr << "Error al inicializar GLEW" << std::endl;
        return -1;
    }

    // 4. Definir los vértices del triángulo
    float vertices[] = {
        -0.5f, -0.5f, 0.0f, // Abajo izquierda
         0.5f, -0.5f, 0.0f, // Abajo derecha
         0.0f,  0.5f, 0.0f  // Arriba centro
    };

    // 5. Crear VBO y VAO
    GLuint VBO, VAO;
    glGenVertexArrays(1, &VAO);
    glGenBuffers(1, &VBO);

    glBindVertexArray(VAO);

    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);

    // 6. Crear y compilar shaders
    GLuint vertexShader = glCreateShader(GL_VERTEX_SHADER);
    glShaderSource(vertexShader, 1, &vertexShaderSource, nullptr);
    glCompileShader(vertexShader);

    GLuint fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
    glShaderSource(fragmentShader, 1, &fragmentShaderSource, nullptr);
    glCompileShader(fragmentShader);

    GLuint shaderProgram = glCreateProgram();
    glAttachShader(shaderProgram, vertexShader);
    glAttachShader(shaderProgram, fragmentShader);
    glLinkProgram(shaderProgram);

    glDeleteShader(vertexShader);
    glDeleteShader(fragmentShader);

    // 7. Loop de renderizado
    while (!glfwWindowShouldClose(window)) {
        glClear(GL_COLOR_BUFFER_BIT);

        glUseProgram(shaderProgram);
        glBindVertexArray(VAO);
        glDrawArrays(GL_TRIANGLES, 0, 3);

        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    // 8. Limpieza
    glDeleteVertexArrays(1, &VAO);
    glDeleteBuffers(1, &VBO);
    glDeleteProgram(shaderProgram);

    glfwDestroyWindow(window);
    glfwTerminate();
    return 0;
}

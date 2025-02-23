## Módulo 2: Fundamentos de OpenGL en C+++ 

Ahora que tenemos OpenGL instalado y funcionando en Windows, Linux y macOS, pasemos a los fundamentos: **dibujar un triangulo** con OpenGL.

### 2.1 ¿Cómo se dibujan gráficos en OpenGL?

OpenGL trabaja con primitivas graficas, que son formas básicas como:

- **Puntos** (GL_POINTS)
- **Lineas** (GL_LINES)
- **Triangulo** (GL_TRIANGLES)

La mayoria de los objetos en 3D se construyen combinando triangulos, por eso **nuestro primer paso es dibujar un triangulo**.

### 2.2 Dibujar un Triangulo en OpenGL 

**Explicacion** 

Para dibujar un triangulo en OpenGL, seguimos estos pasos: 

1. Definir los vertices del triangulo (en un array) 
2. Crear un Vertex Buffer Object (VBO) para almacenar los vertices en la GPU. 
3. Crear un Vertex Array Object (VAO) para manejar la configuracion de los datos. 
4. Escribir shaders (programas en la GPU) para renderizar el triangulo. 
5. Dibujar el triangulo en el loop principal. 

### 2.3 Codigo en C++ (DIbujar un Triangulo) 

Guarda esto como main_triangule.cpp 

```
#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <iostream> 

// codigo fuente del Vertex Shader 
const char* vertexShaderSource = R"(
    #version 300 core 
    layout (location = 0) in vec3 aPos; 
    void main(){
        gl_Position = vec4(aPos, 1.0);
    }
)";

// codigo fuente del Fragment Shader 
const char* fragmentShaderSource = R"(
    #veriosn 330 core 
    out vec4 FragColor; 
    void main(){
        FragColor = vec4(1.0, 0.5, 0.2, 1.0); // Color naranja
    }
)";

int main(){
    // Inicializar GLFW 
    if(!glfwInit()){
        std::cerr << "Error al inicializar GLFW" << std::endl;
        return -1;
    }
    
    // Crear la ventana 
    GLFWwindow* window = glfwCreateWindow(800, 600, ·Triangulo OpenGl", nullptr, nullptr");
    if(!window){
        std::cerr << "Error al crear la ventana GLFW" << std::endl;
        glfwTerminate();
        return -1;
    }
    glfwMakeContexxtCurrent(window);
    
    // Inicializar GLEW 
    glewExperimental = GL_TRUE;
    if(glewInit() != GLEW_OK){
        std::cerr << "Error al iniicializar GLEW" << std::endl;
        return -1;
    }
        
    // Definir los vertices del triangulo 
    float vertices[] = {
        -0.5f, -0.5f, 0.0f;
        0.5f, -0.5f, 0.0f;
        0.0f, 0.5f, 0.0f;
    };
    
    // Crear BBO Y VAO 
    GLuint VBO, VAO;
    glGenVertexArrays(1, &VAO);
    glGenBuffers(1, &VBO);
    
    glBindVertexArray(VAO);

    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
    
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
    glEnableVertexAttibArray(0);

    // Crear y compilar shaders
    GLuinit vertexShader = glCreateShader(GL_VERTEX_SHADER);
    glShaderSource(vertexShader, 1, &vertexShaderSource, nullptr);
    glCompileShader(vertexShader);

    GLuinit fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
    glShaderSource(fragmentShader, 1, &fragmentShaderSource, nullptr);
    glCompileShader(fragmentShader);

    GLuinit shaderProgram = glCreateProgram();
    glAttachShader(shaderProgram, vertexShader);
    glAttachShader(shaderProgram, fragmentShader);
    glLinkProgram(shaderProgram);

    glDalateShader(vertexShader);
    glDeleteShader(fragmentShader);
    
    // Loop de renderizado 
    while(!glfwWindowShouldClose(window)){
        glClear(GL_COLOR_BUFFER_BIT);

        glUseProgram(shaderProgram);
        glBindVertexArray(VAO);
        glDraArrays(GL_TRIANGLES, 0, 3);

        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    // Limpieza 
    glDeleteVertexArrays(2, &VAO);
    glDeteleBuffers(1, &VBO);
    glDeleteProgram(shaderProgram);

    glDestroyWindow(window);
    glfwTerminate();
    return 0;
}
```

### 2.4 Explicación del Código

- Vertex Shader: Recibe posiciones de los vértices y las convierte en coordenadas de pantalla.
- Fragment Shader: Establece el color del triángulo (naranja en este caso).
- VBO (Vertex Buffer Object): Almacena los datos del triángulo en la GPU.
- VAO (Vertex Array Object): Administra cómo los datos se leen en la GPU.
- Shaders: Se compilan y enlazan para renderizar los gráficos.
- Bucle de Renderizado:

    - glClear(GL_COLOR_BUFFER_BIT): Limpia la pantalla.
    - glUseProgram(shaderProgram): Activa el programa de shaders.
    - glDrawArrays(GL_TRIANGLES, 0, 3): Dibuja el triángulo.
    - glfwSwapBuffers(window): Muestra el resultado en pantalla.

### 2.5 Compilar en Windows, Linux y macOS

- Linux (Ubuntu, Arch, Fedora)
bash
```
g++ main.cpp -o opengl_triangle -lGL -lGLEW -lglfw
./opengl_triangle
```
- Windows (MinGW)
powershell
```
g++ main.cpp -o opengl_triangle.exe -lopengl32 -lglfw3 -lglew32
opengl_triangle.exe
```
- macOS
bash
```
g++ main.cpp -o opengl_triangle -framework OpenGL -lglfw -lglew
./opengl_triangle
```
#### 2.6 Resultado esperado

Al ejecutar el código, verás un triángulo naranja en la pantalla. 🟧🔺

- **Tareas del Módulo 2**
    - Compilar y ejecutar el código en tu sistema
    - Modificar el color del triángulo en el fragment shader
    - Intentar cambiar la posición de los vértices para formar otras figuras



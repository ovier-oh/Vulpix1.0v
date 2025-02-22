## Modúlo 1: Introducción a OpenGl 

### 1.1 ¿Qué es OpenGL?

**OpenGL** (Open Graphics Library) es una API (Interfaz de Programación de Aplicaciones) que permite a los programa renderizar graficos en 2D y 3D. Fue desarrollada por  **Silicon Graphics Inc. (SGI)** y es ampliamente utilizada en videojuegos, simulaciones cientificas y graficos industriales. 

-  **Características de OpenGL**
    - Independiente de la plataformaa (Windows, Linux, macOS). 
    - Basada en una API de estado. 
    - Renderizado en tiempo real con acaleracion por hardware. 
    - Ampliamente soportada por las tarjetas gráficas modernas. 

**Comparación con otras  tecnologías:**       


| Tecnología        | Plataforma          | Propósito                         |
| :---------------- | :-----------------: | ---------------------------------:|
| OpenGL            |  Multiplataforma    | Gráficos 2D y3D                   |
| DirectX           |  Windows            | Gráficos y Multimedia             |
| Vulkan            |  Multiplataforma    | Bajo nivell, optimizacion externa |

### 1.2 Instalación de OpenGL

### 1.2.1 Instalacion Windows 

En windows, necesitamos instalar 

- **GLFW** (para ventanas y entradas)
- **GLEW** (para extensiones OpenGL)
- **MinGW o MSVC** (compiladores)

**Paso 1:** Instalar Mingw-w64

    - Descarga e instala Mingw-w64 desde https://www.mingw-w64.org/.

Verifica la instalación:

powershell
```
gcc --version
```
**Paso 2:** Descargar Bibliotecas

    - Descargar GLFW: https://www.glfw.org/download.html
    - Descargar GLEW: http://glew.sourceforge.net/
    - Descomprime y copia los archivos `.lib` en `C:\Mingw-w64\lib\` y los `.h` en `C:\Mingw-w64\include\`.

**Paso 3:** Compilar y probar

Compila un archivo OpenGL en Windows:

powershell
```
g++ main.cpp -o opengl_app -lopengl32 -lglfw3 -lglew32
opengl_app.exe
```

Prueba OpenGL en Windows con:

powershell
```
glxinfo | findstr "OpenGL renderer"
```
### 1.2.2 Instalacion macOS

En macOS, OpenGL ya viene instalado, pero necesitamos GLFW y GLEW.

**Paso 1:** Instalar Homebrew

Si no tienes Homebrew, instálalo con:

bash
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Paso 2:** Instalar OpenGL, GLFW y GLEW
```
brew install glew glfw
```
Verificar OpenGL en macOS:

bash
```
glxinfo | grep "OpenGL renderer"
```

### 1.2.3 Instalacion Linux 

#### Linux (arch, Ubuntu, Fedora)

En Linux, OpenGl generalmente se instala junto con los controladores de la GPU. 

**ArchLinux**
```
sudo pacman -S mesa vulkan-raedon glew glfw
```

Para verificar la instalación:
```
glxinfo | grep "OpenGL renderer"
```

**Ubuntu/Debian**
```
sudo apt update
sudo apt install mesa-utils libglew-dev libglfw3 libglfw3-dev
```
para verificar OpenGl: 
```
glxinfo | grep "OpenGL renderer"
```

**Fedora**
```
sudo dnf install mesa-dri-drivers glew glfw 
```
Prueba OpenGl en Linux con: 
```
glxgears
```








## 1.3 Tu primer programa en OpenGL 

Vamos a crear un programa básico en C que abre una ventana y muestra un color de fondo. 

#### Código

en tu editor de texto o IDE crear un archivo `main.cpp`

```
// Incluimos librerias necesarias
#include <GL/glew.h>        // GLEW: carga de extenciones de OpenGL
#include <GLFW/glfw3.h>     // GLFW: Manejo de ventanas y entradas (teclado, mouse)
#include <iostream>         // Libreria estandar de C++ para entrada/salida 

int main(){
    // Inicializar GLFW (Biblioteca para crear ventanas y manejar eventos)
    if(!glfwInit()){
        std::cerr << "Error al iniciar GLFW" << std::endl;  // Mensaje de error si GLFW no se inicializa
        return -1; // Salimos con codigo de error 
    }

    // Crear una ventana OpenGL 
    /*
   GLFWwindow * glfwCreateWindow	(	int 	width,
                                        int 	height,
                                        const char * 	title,
                                        GLFWmonitor * 	monitor,
                                        GLFWwindow * 	share 
                                    )	 
    */
    GLDWwindow* ventana = glfwCreateWindow(800, 600, "Mi primera ventana OpenGL", nullptr, nullptr);
    
    // Comprobamos si la ventana se creo correctamente 
    if(!ventana){
        std::cerr << "Error al crear la ventana" << std::endl;
        glfTerminate(); // Cierra GLFW si la ventana no se pudo crear 
        return -1;
    }

    // Bucle princial: mantiene la ventana abierta hasta que el usuario la cierre 
    while(!glfwWindowShouldClose(ventana)){
        // Limpiar el buffer de color de la pantalla (fondo negro por defecto)
        glClear(GL_COLOR_BUFFER_BIT);

        // Intercambiar buffers de la ventana (doble buffer para evitar parpadeos) 
        glfwSwapBuffers(ventana);
        
        // manejar eventos (teclado, mouse, etc.)
        glfwPollEvents();
    }
    
    // Limpiar recursos y cerrar la ventana 
    glfwDestroyWindow(ventana);
    glfwTerminate(); // Finaliza GLFW y libera recursos 

    return 0; // Salida exitosa 
}
```

### 1.4 Compilacion y ejecucion  

**1 Linux (Arch, Ubuntu, Fedora)**

OpenGL ya está instalado en la mayoría de las distribuciones de Linux, solo necesitamos las bibliotecas GLFW y GLEW.

bash 
```
g++ main.cpp -o opengl_app -lGL -lGLEW -lglfw
./opengl_app
```
**2 Windows (MinGW, MSVC)**
- MinGW
powershell
```
g++ main.cpp -o opengl_app.exe -lopengl32 -lglfw3 -lglew32
opengl_app.exe
```
- Si usas MSVC (Visual Studio), abre PowerShell y usa:

PowerShell
```
cl main.cpp /Fe:opengl_app.exe /link opengl32.lib glfw3.lib glew32.lib
opengl_app.exe
```
**3 macOS**
En terminal 
bash
```
g++ main.cpp -o opengl_app -framework OpenGL -lglfw -lglew
./opengl_app
```


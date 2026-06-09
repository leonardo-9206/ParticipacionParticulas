# Simulación de Partículas y Energía Cinética

Este proyecto es una simulación física en Python que resuelve un sistema de partículas en un cubo tridimensional, calculando su centro de masa y distribuciones de energía cinética. 

El programa asigna aleatoriamente posiciones $(x,y,z)$ y velocidades $(v_x, v_y, v_z)$ a un conjunto de partículas idénticas y analiza sus propiedades.

## ¿Qué hace el código?
1. **Posiciones y Velocidades**: Genera posiciones aleatorias en un cubo de 1.0 m de lado y velocidades entre -10 y 10 m/s para cada partícula.
2. **Cálculos Físicos**:
   - **Centro de masa**: Ubicación promedio de todas las partículas.
   - **Energía Cinética Traslacional**: La energía debida al movimiento del centro de masa.
   - **Energía Cinética Interna (Rotacional)**: La energía debida al movimiento relativo de las partículas respecto a su centro de masa.
   - **Energía Cinética Total**: La suma de la energía traslacional y la interna.
3. **Análisis Estadístico**: Repite la simulación miles de veces para calcular qué fracción de la energía se vuelve "interna" al sistema en promedio, y genera un histograma comparativo (`histograma_energias.png`).

---

## Requisitos Previos (Instalación)
Para poder ejecutar este proyecto, necesitas tener instalado **Python** en tu computadora.

1. Descarga Python desde la página oficial: [python.org/downloads](https://www.python.org/downloads/).
2. Abre el instalador y **es vital** que marques la casilla que dice **"Add python.exe to PATH"** (Agregar python.exe al PATH) que se encuentra hasta abajo en la primera ventana del instalador.
3. Termina la instalación.

---

## ¿Cómo ejecutar (compilar) el código?

Al estar escrito en Python, no requiere compilación previa. Se ejecuta directamente a través de un intérprete.

1. Abre tu terminal (Consola de comandos, PowerShell, o la terminal integrada de Visual Studio Code).
2. Asegúrate de estar en la carpeta donde se encuentra el archivo `simulacion_particulas.py`.
3. Instala las librerías matemáticas requeridas ejecutando el siguiente comando:
   ```bash
   pip install numpy matplotlib
   ```
4. Una vez instaladas las dependencias, corre el programa con:
   ```bash
   python simulacion_particulas.py
   ```
*(Nota: Si te aparece un error indicando que `python` no se reconoce, intenta usar `py simulacion_particulas.py`)*

---

## ¿Cómo cambiar el número de partículas?
El código está diseñado para ser completamente escalable. Para cambiar la cantidad de partículas simuladas:

1. Abre el archivo `simulacion_particulas.py` en cualquier editor de texto o en Visual Studio Code.
2. Localiza la línea 36 dentro de la función `main()` que dice:
   ```python
   N = 100
   ```
3. Cambia ese número al valor que desees (por ejemplo, `N = 500` o `N = 1000`).
4. Guarda el archivo (`Ctrl + S`).
5. Vuelve a ejecutar el código desde la terminal. El programa automáticamente adaptará la masa, las matrices de posiciones y las gráficas al nuevo número de partículas.

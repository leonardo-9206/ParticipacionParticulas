import numpy as np
import matplotlib.pyplot as plt

def simular_particulas(num_particulas=100, masa_g=10.0, lado_cubo_m=1.0, v_min=-10.0, v_max=10.0):
    """
    Simula un sistema de partículas y calcula sus propiedades energéticas y centro de masa.
    """
    # Convertir masa a kg (SI)
    masa_kg = masa_g / 1000.0
    masa_total = num_particulas * masa_kg

    # Generar posiciones aleatorias (x, y, z) entre 0 y lado_cubo_m
    posiciones = np.random.uniform(0, lado_cubo_m, (num_particulas, 3))
    
    # Generar velocidades aleatorias (vx, vy, vz) entre v_min y v_max
    velocidades = np.random.uniform(v_min, v_max, (num_particulas, 3))

    # 1. Centro de masa (R_cm)
    # Como todas las partículas tienen la misma masa, es simplemente el promedio de las posiciones
    centro_de_masa = np.mean(posiciones, axis=0)

    # 2. Velocidad del centro de masa (V_cm)
    velocidad_cm = np.mean(velocidades, axis=0)

    # 3. Energía cinética traslacional del centro de masa (K_trans)
    # K_trans = 1/2 * Masa_total * |V_cm|^2
    v_cm_cuadrado = np.sum(velocidad_cm**2)
    k_trans_cm = 0.5 * masa_total * v_cm_cuadrado

    # 4. Energía cinética total del sistema (K_total)
    # K_total = suma( 1/2 * m_i * |v_i|^2 )
    v_cuadrados = np.sum(velocidades**2, axis=1)
    k_total = np.sum(0.5 * masa_kg * v_cuadrados)

    # 5. Energía cinética interna (K_int) (El libro le llama rotacional alrededor del centro)
    # K_int = K_total - K_trans_cm  (por el teorema de König)
    # De forma equivalente, es la energía medida respecto al centro de masa
    velocidades_relativas = velocidades - velocidad_cm
    v_rel_cuadrados = np.sum(velocidades_relativas**2, axis=1)
    k_interna = np.sum(0.5 * masa_kg * v_rel_cuadrados)

    return centro_de_masa, k_trans_cm, k_interna, k_total

def main():
    # Parámetros del problema
    N = 100
    
    print(f"--- Simulación inicial para {N} partículas ---")
    cm, k_trans, k_int, k_tot = simular_particulas(num_particulas=N)
    
    print(f"Ubicación del centro de masa (x, y, z): ({cm[0]:.4f}, {cm[1]:.4f}, {cm[2]:.4f}) m")
    print(f"Energía cinética traslacional del CM:    {k_trans:.4f} J")
    print(f"Energía cinética interna (alrededor CM): {k_int:.4f} J")
    print(f"Energía cinética total del sistema:      {k_tot:.4f} J")
    print(f"Relación comprobada (K_trans + K_int = K_tot): {k_trans + k_int:.4f} J == {k_tot:.4f} J\n")

    # Parte b: Repetir el proceso para generar estadísticas e histogramas
    num_simulaciones = 1000
    print(f"--- Ejecutando {num_simulaciones} simulaciones para obtener promedios y graficar ---")
    
    k_trans_lista = []
    k_int_lista = []
    k_tot_lista = []

    for _ in range(num_simulaciones):
        _, k_trans, k_int, k_tot = simular_particulas(num_particulas=N)
        k_trans_lista.append(k_trans)
        k_int_lista.append(k_int)
        k_tot_lista.append(k_tot)

    fraccion_interna_promedio = np.mean(k_int_lista) / np.mean(k_tot_lista)
    print(f"En promedio, la fracción de la energía que es interna es: {fraccion_interna_promedio:.2%}")
    print("La inmensa mayoría de la energía se encuentra en forma de energía interna debido a que el movimiento aleatorio de las partículas hace que la velocidad neta del centro de masa sea cercana a cero.\n")

    # (Se eliminó la generación del histograma por petición)

if __name__ == "__main__":
    main()

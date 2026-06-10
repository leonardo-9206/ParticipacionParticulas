import numpy as np

N = 100
masa_g = 10.0
lado_cubo = 1.0

vmin = -10.0
vmax = 10.0

masa_kg = masa_g / 1000.0
masa_total = N * masa_kg

posiciones = np.random.uniform(0, lado_cubo, (N, 3))
velocidades = np.random.uniform(vmin, vmax, (N, 3))

centro_de_masa = np.mean(posiciones, axis=0)
velocidad_cm = np.mean(velocidades, axis=0)

v_cm_cuadrado = np.sum(velocidad_cm**2)
k_trans = 0.5 * masa_total * v_cm_cuadrado

v_cuadrados = np.sum(velocidades**2, axis=1)
k_tot = np.sum(0.5 * masa_kg * v_cuadrados)

velocidades_relativas = velocidades - velocidad_cm
v_rel_cuadrados = np.sum(velocidades_relativas**2, axis=1)
k_int = np.sum(0.5 * masa_kg * v_rel_cuadrados)

print(f"Particulas: {N}")
print(f"Rango de velocidades: {vmin} a {vmax} m/s\n")

print(f"Centro de masa (x, y, z): ({centro_de_masa[0]:.4f}, {centro_de_masa[1]:.4f}, {centro_de_masa[2]:.4f}) m")
print(f"Energia traslacional: {k_trans:.4f} J")
print(f"Energia interna: {k_int:.4f} J")
print(f"Energia total: {k_tot:.4f} J")
print(f"Comprobacion: {k_trans + k_int:.4f} J == {k_tot:.4f} J\n")

num_sim = 1000
k_tot_lista = []
k_int_lista = []

for _ in range(num_sim):
    v_temp = np.random.uniform(vmin, vmax, (N, 3))
    v_cm_temp = np.mean(v_temp, axis=0)
    
    v_cuad_temp = np.sum(v_temp**2, axis=1)
    k_tot_temp = np.sum(0.5 * masa_kg * v_cuad_temp)
    
    v_rel_temp = v_temp - v_cm_temp
    v_rel_cuad_temp = np.sum(v_rel_temp**2, axis=1)
    k_int_temp = np.sum(0.5 * masa_kg * v_rel_cuad_temp)
    
    k_tot_lista.append(k_tot_temp)
    k_int_lista.append(k_int_temp)

fraccion = np.mean(k_int_lista) / np.mean(k_tot_lista)
print(f"Fraccion de energia interna promedio: {fraccion:.4f}")

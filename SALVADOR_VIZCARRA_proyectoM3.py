import numpy as np
import matplotlib.pyplot as plt
import random

def galton_desde_caminata(N_pelotas, N_pasos, prob):
    posiciones_finales = []

    for _ in range(N_pelotas):
        pos = 0
        for _ in range(N_pasos):
            if random.random() >= prob:
                pos += 1
            else:
                pos -= 1
        posiciones_finales.append(pos)
     
    plt.hist(posiciones_finales, bins=range(min(posiciones_finales), max(posiciones_finales)+2), edgecolor='black')
    plt.xlabel('Posición final')
    plt.ylabel('Número de pelotas')
    plt.title(f'Máquina de Galton simulada con {N_pelotas} pelotas')
    plt.grid(True)
    plt.show()

galton_desde_caminata(N_pelotas=3000, N_pasos=20, prob=0.5)
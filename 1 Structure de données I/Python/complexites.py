#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

nb = 100
liste_n = np.linspace(1, nb, nb)
liste_1 = np.ones(nb)
liste_carre = liste_n**2
liste_log = np.log2(liste_n)
liste_nlog = np.log2(liste_n)*liste_n

plt.figure(figsize = (8, 8))
plt.plot(liste_n, liste_1, label='0(1)')
plt.plot(liste_n, liste_n, label='0(n)')
plt.plot(liste_n, liste_log, label='0(log(n))')
plt.plot(liste_n, liste_nlog, label='0(nlog(n))')
plt.plot(liste_n, liste_carre, label='0(n²)')
axes = plt.gca()
axes.set_xlim(0, nb) 
axes.set_ylim(0, nb) 
plt.xlabel('taille du tableau')
plt.ylabel("ordre de grandeur du nombre d'opérations")
plt.legend()


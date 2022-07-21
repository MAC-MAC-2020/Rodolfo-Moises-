from cProfile import label
from cmath import nan
from pickle import NONE
from re import X
from tkinter import font
from turtle import distance
from unittest import result
import misfunciones as rodo
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
import seaborn as sns

trayectorias = rodo.cargararchivo('trajectories_TODAS.txt', delimiter='\t')
trayectorias = np.asarray(trayectorias)
trayectorias = trayectorias[:,0:2]

distancia_eucl = np.zeros(len(trayectorias)-1, dtype=np.float32)

for i in range(0,len(trayectorias)-1):
    distancia_eucl[i] = np.linalg.norm(trayectorias[i]-trayectorias[i+1])

velocidad_nan = distancia_eucl/0.05

donde_datos = [velocidad_nan>-1][0]
donde_datos = np.insert(donde_datos,len(donde_datos),0)
donde_datos = np.insert(donde_datos,0,1)

ind_datos = np.where(donde_datos==1)[0] # igual a 1 limite inferior ligual a 0 limite superior
derivada_ind_datos = np.diff(ind_datos)
idxs_inf = np.where(derivada_ind_datos!=1)[0]

lims = ind_datos[idxs_inf]
quitar_indices = np.where((np.diff(lims)<150))
lims = np.delete(lims,[quitar_indices])
lims = np.insert(lims,len(lims),len(velocidad_nan))

lim_sup = 0
velocidades = np.zeros([len(lims)-1,len(velocidad_nan)]) # Una matriz tan garande como el numero de ensayos  (despues se recorta)
for i in range(0,len(lims)):
    lim_sup = lim_sup+1
    if i<len(lims)-1:
        vel_n = velocidad_nan[lims[i]:lims[lim_sup]]
        vel_n = vel_n[~np.isnan(vel_n)]
        velocidades[i,0:len(vel_n)] = vel_n

velocidad_promedio = np.nanmean(velocidades,axis=0, dtype=np.float32)
velocidad_std = np.std(velocidades,axis=0, dtype=np.float32)

#-----------------------------------------------------------------------------------------------------------------PLOT

x = np.arange(0,200)
plt.figure(figsize=(10,7))
plt.plot(x,velocidad_promedio[0:200],c = 'k', lw = 0.88, label = 'Velocidad')
plt.fill_between(x, velocidad_promedio[0:200] - velocidad_std[0:200], velocidad_promedio[0:200] + velocidad_std[0:200], color='k', alpha=0.1)
plt.title('Velocidad promedio por sesión', fontsize = 12, fontweight = 'bold')
plt.xlabel('Tiempo', fontsize = 10, fontweight = 'normal')
plt.ylabel('Velocidad', fontsize = 10, fontweight = 'normal')
plt.legend(loc = 'best', frameon= False)
plt.show()




# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 12:06:48 2017

@author: Roberto J. Marin
"""

import pandas as pd
import numpy as np
import os
from subprocess import Popen, PIPE
import fileinput
import sys
from pandas import ExcelWriter

media = "media" + ".txt"
varianza = "varianza" + ".txt"
desv_estandar = "desv_estandar" + ".txt"
asimetria = "asimetria" + ".txt"
curtosis = "curtosis" + ".txt"
confiabilidad = "confiabilidad" + ".txt"

# Se leen los valores de las variables
df_di = pd.read_excel("variables.xlsx", converters={'c1':str, 'phi1':str, 'uws1':str, 'D01':str, 'Ks1':str, 'Ths1':str,
'Thr1':str, 'Alp1':str, 'c2':str, 'phi2':str, 'uws2':str, 'D02':str, 'Ks2':str, 'Ths2':str, 'Thr2':str, 'Alp2':str,
'c3':str, 'phi3':str, 'uws3':str, 'D03':str, 'Ks3':str, 'Ths3':str, 'Thr3':str, 'Alp3':str, 'c4':str, 'phi4':str,
'uws4':str, 'D04':str, 'Ks4':str, 'Ths4':str, 'Thr4':str, 'Alp4':str, 'c5':str, 'phi5':str, 'uws5':str, 'D05':str,
'Ks5':str, 'Ths5':str, 'Thr5':str, 'Alp5':str})
                                                    
c1 = df_di["c1"].astype(str).values
phi1 = df_di["phi1"].astype(str).values
uws1 = df_di["uws1"].astype(str).values
D01 = df_di["D01"].astype(str).values
Ks1 = df_di["Ks1"].astype(str).values
Ths1 = df_di["Ths1"].astype(str).values
Thr1 = df_di["Thr1"].astype(str).values
Alp1 = df_di["Alp1"].astype(str).values

c2 = df_di["c2"].astype(str).values
phi2 = df_di["phi2"].astype(str).values
uws2 = df_di["uws2"].astype(str).values
D02 = df_di["D02"].astype(str).values
Ks2 = df_di["Ks2"].astype(str).values
Ths2 = df_di["Ths2"].astype(str).values
Thr2 = df_di["Thr2"].astype(str).values
Alp2 = df_di["Alp2"].astype(str).values

c3 = df_di["c3"].astype(str).values
phi3 = df_di["phi3"].astype(str).values
uws3 = df_di["uws3"].astype(str).values
D03 = df_di["D03"].astype(str).values
Ks3 = df_di["Ks3"].astype(str).values
Ths3 = df_di["Ths3"].astype(str).values
Thr3 = df_di["Thr3"].astype(str).values
Alp3 = df_di["Alp3"].astype(str).values

c4 = df_di["c4"].astype(str).values
phi4 = df_di["phi4"].astype(str).values
uws4 = df_di["uws4"].astype(str).values
D04 = df_di["D04"].astype(str).values
Ks4 = df_di["Ks4"].astype(str).values
Ths4 = df_di["Ths4"].astype(str).values
Thr4 = df_di["Thr4"].astype(str).values
Alp4 = df_di["Alp4"].astype(str).values

c5 = df_di["c5"].astype(str).values
phi5 = df_di["phi5"].astype(str).values
uws5 = df_di["uws5"].astype(str).values
D05 = df_di["D05"].astype(str).values
Ks5 = df_di["Ks5"].astype(str).values
Ths5 = df_di["Ths5"].astype(str).values
Thr5 = df_di["Thr5"].astype(str).values
Alp5 = df_di["Alp5"].astype(str).values

def reemplazar(file, searchexp, replaceexp):
    for linea in fileinput.input(file, inplace=True):
        if searchexp in linea:
            linea = linea.replace(searchexp, replaceexp)
        sys.stdout.write(linea)

def menores_uno(_df, n):
    valores = []
    cont = 0
    for c in range(n):
        valores.extend(_df[c].values)
    for j in valores:
        if j < 1.0 and not (np.isnan(j)):
            cont += 1
    return cont


datos = {'a. Total': ["Total (-)"], 'b. FS min': ["FSmin"], 'c. FS prom': ["FSmean"],
         'd. Failing area': ["Failing area"], 'e. Error_r max': ["Er_max"], 'f. Error_r prom': ["Er_prom"],
         'g. Error_r desv': ["Er_desv"], 'h. v1': ["v1"], 'h. v2': ["v2"], 'h. v3': ["v3"], 'h. v4': ["v4"],
         'h. v5': ["v5"], 'h. v6': ["v6"], 'h. v7': ["v7"], 'h. v8': ["v8"],
         'r. c1': [], 's. phi1': [], 't. uws1': [], 'u. D01': [], 'v. Ks1': [], 'w. Ths1': [], 'x. Thr1': [],
         'y. Alp1': [], 
         'r. c2': [], 's. phi2': [], 't. uws2': [], 'u. D02': [], 'v. Ks2': [], 'w. Ths2': [], 'x. Thr2': [],
         'y. Alp2': [],
         'r. c3': [], 's. phi3': [], 't. uws3': [], 'u. D03': [], 'v. Ks3': [], 'w. Ths3': [], 'x. Thr3': [],
         'y. Alp3': [],
         'r. c4': [], 's. phi4': [], 't. uws4': [], 'u. D04': [], 'v. Ks4': [], 'w. Ths4': [], 'x. Thr4': [],
         'y. Alp4': [],
         'r. c5': [], 's. phi5': [], 't. uws5': [], 'u. D05': [], 'v. Ks5': [], 'w. Ths5': [], 'x. Thr5': [],
         'y. Alp5': []}


fail = []
max_e = 0
prom_e = 0
desv_e = 0
contador = 0

for i in range(len(c1) - 1):
    
    contador += 1

    reemplazar("tr_in.txt", c1[i], c1[i + 1])
    reemplazar("tr_in.txt", phi1[i], phi1[i + 1])
    reemplazar("tr_in.txt", uws1[i], uws1[i + 1])
    reemplazar("tr_in.txt", D01[i], D01[i + 1])
    reemplazar("tr_in.txt", Ks1[i], Ks1[i + 1])
    reemplazar("tr_in.txt", Ths1[i], Ths1[i + 1])
    reemplazar("tr_in.txt", Thr1[i], Thr1[i + 1])
    reemplazar("tr_in.txt", Alp1[i], Alp1[i + 1])
    reemplazar("tr_in.txt", c2[i], c2[i + 1])
    reemplazar("tr_in.txt", phi2[i], phi2[i + 1])
    reemplazar("tr_in.txt", uws2[i], uws2[i + 1])
    reemplazar("tr_in.txt", D02[i], D02[i + 1])
    reemplazar("tr_in.txt", Ks2[i], Ks2[i + 1])
    reemplazar("tr_in.txt", Ths2[i], Ths2[i + 1])
    reemplazar("tr_in.txt", Thr2[i], Thr2[i + 1])
    reemplazar("tr_in.txt", Alp2[i], Alp2[i + 1])
    reemplazar("tr_in.txt", c3[i], c3[i + 1])
    reemplazar("tr_in.txt", phi3[i], phi3[i + 1])
    reemplazar("tr_in.txt", uws3[i], uws3[i + 1])
    reemplazar("tr_in.txt", D03[i], D03[i + 1])
    reemplazar("tr_in.txt", Ks3[i], Ks3[i + 1])
    reemplazar("tr_in.txt", Ths3[i], Ths3[i + 1])
    reemplazar("tr_in.txt", Thr3[i], Thr3[i + 1])
    reemplazar("tr_in.txt", Alp3[i], Alp3[i + 1])
    reemplazar("tr_in.txt", c4[i], c4[i + 1])
    reemplazar("tr_in.txt", phi4[i], phi4[i + 1])
    reemplazar("tr_in.txt", uws4[i], uws4[i + 1])
    reemplazar("tr_in.txt", D04[i], D04[i + 1])
    reemplazar("tr_in.txt", Ks4[i], Ks4[i + 1])
    reemplazar("tr_in.txt", Ths4[i], Ths4[i + 1])
    reemplazar("tr_in.txt", Thr4[i], Thr4[i + 1])
    reemplazar("tr_in.txt", Alp4[i], Alp4[i + 1])
    reemplazar("tr_in.txt", c5[i], c5[i + 1])
    reemplazar("tr_in.txt", phi5[i], phi5[i + 1])
    reemplazar("tr_in.txt", uws5[i], uws5[i + 1])
    reemplazar("tr_in.txt", D05[i], D05[i + 1])
    reemplazar("tr_in.txt", Ks5[i], Ks5[i + 1])
    reemplazar("tr_in.txt", Ths5[i], Ths5[i + 1])
    reemplazar("tr_in.txt", Thr5[i], Thr5[i + 1])
    reemplazar("tr_in.txt", Alp5[i], Alp5[i + 1])

    os.system(".\TRIGRS.exe")

    if __name__ == '__main__':
        # leer número de columnas
        df_ = pd.read_table("TRfs_min_env_2.txt")
        numero_columnas = df_.columns
        ncols = int(numero_columnas[0].split()[1])
        df = pd.read_table("TRfs_min_env_2.txt", sep=' ', names=range(ncols))
        df = df.drop(df.index[[0, 1, 2, 3, 4, 5]])
        # pasar las columnas de str a float
        for j in range(ncols):
            df[j] = df[j].astype(float)
        df = df.replace(-9999, np.nan)
        FS = df
        v1 = FS[80][27]
        v2 = FS[90][35]
        v3 = FS[100][423]
        v4 = FS[500][400]
        v5 = FS[500][408]
        v6 = FS[500][420]
        v7 = FS[500][500]
        v8 = FS[500][600]

        if i == 0:
            FS_sum = FS

        if i>0:
            FS_sum = np.add(FS_sum, FS)

        FS_prom = np.divide(FS_sum, i + 1)
        Dif_var = np.power(np.subtract(FS, FS_prom), 2)
        Dif_asim = np.power(np.subtract(FS, FS_prom), 3)
        Dif_curt = np.power(np.subtract(FS, FS_prom), 4)
        if i == 0:
            Difv_sum = Dif_var
            Difa_sum = Dif_asim
            Difc_sum = Dif_curt
        if i > 0:
            Difv_sum =  np.add(Difv_sum, Dif_var) #Sumatoria de s^2-Varianza
            var = np.multiply(1/i, Difv_sum)
            desv = np.power(var, 0.5)
            betha = np.divide(np.subtract(FS_prom,1),desv)
        if i > 1:
            asim_sum = np.add(Difa_sum, Dif_asim) #Sumatoria de g1-Asimetría
            asim = np.multiply(np.divide((i + 1)/(i * (i - 1)), np.power(desv,3)), asim_sum)
        if i > 2:
            curt_sum = np.add(Difc_sum, Dif_curt) #Sumatoria de g2-Curtosis
            term1 = np.multiply(np.divide((i + 1) * (i + 2)/(i * (i - 1) * (i - 2)), np.power(desv,4)), curt_sum)
            term2 = 3 * (i^2) / ((i - 1) * (i - 2))
            curt = np.subtract(term1, term2)

            FS_prom = FS_prom.replace(np.nan, -9999)
            var = var.replace(np.nan, -9999)
            desv = desv.replace(np.nan, -9999)
            asim = asim.replace(np.nan, -9999)
            curt = curt.replace(np.nan, -9999)
            betha = betha.replace(np.nan, -9999)

            FS_prom.to_csv(media, header=None, index=None, sep=' ')
            var.to_csv(varianza, header=None, index=None, sep=' ')
            desv.to_csv(desv_estandar, header=None, index=None, sep=' ')
            asim.to_csv(asimetria, header=None, index=None, sep=' ')
            curt.to_csv(curtosis, header=None, index=None, sep=' ')
            betha.to_csv(confiabilidad, header=None, index=None, sep=' ')
            
        df2 = df * 0  # Se crea un dataframe con valores de 0
        elem = []

        for k in range(ncols):
            elem.extend(df[k].values)
            if contador == 1:
                fail.extend(df2[k].values)

        k = 0
        for j in elem:
            if j < 1.0 and not (np.isnan(j)):
                fail[k] += 1
            k += 1

        df3 = pd.DataFrame(np.array(fail).reshape(len(df.columns), len(df.index)))
        # Convierte lista en dataframe (filas y columnas)

        df3 = df3.transpose()  # Transpone el dataframe para tener la matriz ordenada correctamente

        if i > 0:
            pf_p = pf #Probabilidad de falla en iteración anterior
        pf = np.divide(df3,i + 1)

        if i > 0:
            error_r = np.abs(np.divide(np.subtract(pf, pf_p), pf))
            max_e = max(error_r.max())
            sum_e = np.sum(error_r.sum())
            total_e = sum(error_r.count())
            prom_e = sum_e / total_e
            desv_e = error_r.stack().std()

        pf = pf.replace(np.nan, -9999) #Probabilidad de falla

        writer = ExcelWriter('prob_falla.xlsx')
        df3.to_excel(writer, 'Sheet1')
        writer.save()
        pf.to_csv(r'prob_falla.txt', header=None, index=None, sep=' ')

        minimo = min(df.min())
        suma = np.sum(df.sum())
        # uso la función de menores que uno
        menores = menores_uno(df, ncols)
        total = sum(df.count())
        promedio = suma / total
        # celdas que fallan porcentaje de area que falla
        failing = menores / total

        datos['r. c1'] = c1
        datos['s. phi1'] = phi1
        datos['t. uws1'] = uws1
        datos['u. D01'] = D01
        datos['v. Ks1'] = Ks1
        datos['w. Ths1'] = Ths1
        datos['x. Thr1'] = Thr1
        datos['y. Alp1'] = Alp1
        datos['r. c2'] = c2
        datos['s. phi2'] = phi2
        datos['t. uws2'] = uws2
        datos['u. D02'] = D02
        datos['v. Ks2'] = Ks2
        datos['w. Ths2'] = Ths2
        datos['x. Thr2'] = Thr2
        datos['y. Alp2'] = Alp2
        datos['r. c3'] = c3
        datos['s. phi3'] = phi3
        datos['t. uws3'] = uws3
        datos['u. D03'] = D03
        datos['v. Ks3'] = Ks3
        datos['w. Ths3'] = Ths3
        datos['x. Thr3'] = Thr3
        datos['y. Alp3'] = Alp3
        datos['r. c4'] = c4
        datos['s. phi4'] = phi4
        datos['t. uws4'] = uws4
        datos['u. D04'] = D04
        datos['v. Ks4'] = Ks4
        datos['w. Ths4'] = Ths4
        datos['x. Thr4'] = Thr4
        datos['y. Alp4'] = Alp4
        datos['r. c5'] = c5
        datos['s. phi5'] = phi5
        datos['t. uws5'] = uws5
        datos['u. D05'] = D05
        datos['v. Ks5'] = Ks5
        datos['w. Ths5'] = Ths5
        datos['x. Thr5'] = Thr5
        datos['y. Alp5'] = Alp5
        datos['a. Total'].append(total)
        datos['b. FS min'].append(minimo)
        datos['c. FS prom'].append(promedio)
        datos['d. Failing area'].append(failing)
        datos['e. Error_r max'].append(max_e)
        datos['f. Error_r prom'].append(prom_e)
        datos['g. Error_r desv'].append(desv_e)
        datos['h. v1'].append(v1)
        datos['h. v2'].append(v2)
        datos['h. v3'].append(v3)
        datos['h. v4'].append(v4)
        datos['h. v5'].append(v5)
        datos['h. v6'].append(v6)
        datos['h. v7'].append(v7)
        datos['h. v8'].append(v8)
        print("---")



df = pd.DataFrame(fail)
writer = ExcelWriter('List_failresults.xlsx')
df.to_excel(writer, 'Sheet1')
writer.save()

df = pd.DataFrame(datos)
print(df)
writer = ExcelWriter('Resultsall.xlsx')
df.to_excel(writer, 'Sheet1')
writer.save()

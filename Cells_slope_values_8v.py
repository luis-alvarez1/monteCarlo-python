# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 12:06:48 2017

@author: Wolf
"""

import pandas as pd
import numpy as np
import os
from subprocess import Popen, PIPE
import fileinput
import sys
from pandas import ExcelWriter



if __name__ == '__main__':
    # leer número de columnas
    df_ = pd.read_table("zones.txt")
    numero_columnas = df_.columns
    ncols = int(numero_columnas[0].split()[1])
    df = pd.read_table("zones.txt", sep=' ', names=range(ncols))
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
print(v1, v2, v3, v4, v5, v6, v7, v8)

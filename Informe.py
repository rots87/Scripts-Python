#!/usr/bin/env python3
# -*- coding: latin-1 -*-
# @Author: Nestor Cañas
# @Create At: 22/10/2018
# @Version: 1.0
# @Last Modifier: Nestor Cañas

import csv
import os
import sys
user = []
ffolder = []
sfolder = []
tfolder = []
with open('C:/Users/SOPORTE-T/Desktop/informe.csv', encoding="utf8") as csvfile:
    report = csv.reader(csvfile, delimiter=',')
    for row in report:
        array = row[0].split('/')
        try:
            user.append(array[0])
        except Exception as e:
            user.append('')
        try:
            ffolder.append(array[1])
        except Exception as e:
            ffolder.append('')
        try:
            sfolder.append(array[2])
        except Exception as e:
            sfolder.append('')
        try:
            tfolder.append(array[3])
        except Exception as e:
            tfolder.append('')

with open('C:/Users/SOPORTE-T/Desktop/limpio.csv', mode='w') as limpio_file:
    limpio_file = csv.writer(limpio_file, delimiter=',')
    x = len(user)
    y = 0
    while y < x:
        limpio_file.writerow([user[y], ffolder[y], sfolder[y], tfolder[y]])
        y = y+1

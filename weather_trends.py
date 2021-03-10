#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:26:51 2021

@author: bronsky
"""

import pandas as pd
import matplotlib.pyplot as plt

df_phx = pd.read_csv('/Users/bronsky/Documents/phx_avg_temp.csv', encoding='utf-8')
df_globe = pd.read_csv('/Users/bronsky/Documents/world_avg_temp.csv', encoding='utf-8')


df_phx['avg_temp'] = df_phx['avg_temp'].rolling(10).mean()
df_globe['avg_temp'] = df_globe['avg_temp'].rolling(10).mean()


fig, ax = plt.subplots()
fig.autofmt_xdate()

plt.plot(df_phx['year'], df_phx['avg_temp'])
plt.plot(df_globe['year'], df_globe['avg_temp'])

# tick font sizes
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# title and labels
plt.title('10 Year Moving Average Temperatures', fontsize=20)
plt.legend(labels =['Phoenix', 'Globe'], fontsize=14)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Temp', fontsize=16)
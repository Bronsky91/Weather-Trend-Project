#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:26:51 2021

@author: bronsky
"""

import pandas as pd
import matplotlib.pyplot as plt

# Raw Data from tables
df_phx = pd.read_csv('/Users/bronsky/Documents/phx_avg_temp.csv', encoding='utf-8')
df_globe = pd.read_csv('/Users/bronsky/Documents/world_avg_temp.csv', encoding='utf-8')

# First and Last Ten Temps
phx_first_ten = df_phx.head(10)
globe_first_ten = df_globe.head(10)
phx_last_ten = df_phx.tail(10)
globe_last_ten = df_globe.tail(10)


print('First 10 year avg Phx: ' + str(phx_first_ten['avg_temp'].mean()))
print('First 10 year avg Global: ' + str(globe_first_ten['avg_temp'].mean()))
print('Last 10 year avg Phx: ' + str(phx_last_ten['avg_temp'].mean()))
print('Last 10 year avg Global: ' + str(globe_last_ten['avg_temp'].mean()))

# Total avgs and the difference
total_phx_avg = df_phx['avg_temp'].mean()
total_global_avg = df_globe['avg_temp'].mean()
total_difference = total_phx_avg - total_global_avg

print('Overall Average Temp of Phx: ' + str(total_phx_avg))
print('Overall Average Temp of Global: ' + str(df_globe['avg_temp'].mean()))
print('Overall Difference in Average Temp of Both: ' + str(total_difference))

fig, ax = plt.subplots()
fig.autofmt_xdate()

phx_rolling_avg = df_phx['avg_temp'].rolling(10).mean()
globe_rolling_avg = df_globe['avg_temp'].rolling(10).mean()

# Last Forty Years of Rolling Average data
phx_last_forty_difference = phx_rolling_avg[178] - phx_rolling_avg[138]
globe_last_forty_difference = globe_rolling_avg[178] - globe_rolling_avg[138]

print('Last 40 year rolling avg increase for Phx: ' + str(phx_last_forty_difference))
print('Last 40 year rolling avg global increase: ' + str(globe_last_forty_difference))

plt.plot(df_phx['year'], phx_rolling_avg)
plt.plot(df_globe['year'], globe_rolling_avg)

# tick font sizes
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid()

# title and labels
plt.title('10 Year Moving Average Temperatures', fontsize=20)
plt.legend(labels =['Phoenix', 'Globe'], fontsize=14)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Temp in Celsius', fontsize=16)
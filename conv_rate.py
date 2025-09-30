conv_rate = 0.6214
print('KPH\tMPH')
print('-------------')
for KPH in range(60,131,10):
    MPH = KPH * conv_rate
    print(KPH,'\t', format(MPH, '.2f'))
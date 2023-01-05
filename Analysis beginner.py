import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ไฟล์ข้อมูลของเรา.csv')
//แสดงข้อมูลทั้งหมด//
print(df.head(จำนวนข้อมูล))
print()

//ดูข้อมูลโดยรวมของ 1 คอลัมน์//
descrip = df.Deaths.describe()
print()
print(descrip)

//แสดงข้อมูลแบบละเอียดทั้งหมด//
grp = df.groupby('ชื่อคอลัมน์')
for name,group in grp:
    print(name)
    print(group)
    print('\n')
    
//แสดงกราฟ//
หากอยากได้กราฟ แท่ง
df['ชื่อคอลัมน์'].head(10).plot.bar('เทส')

หากอยากได้กราฟ จุด
Recovered = df.Recovered
Active = df.Active
plt.scatter(Recovered,Active)
plt.show()

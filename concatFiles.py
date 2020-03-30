import pandas as pd
import os
import glob

path = r'C:\Users\lucas.zarza\Desktop\planilhas_BBCE'

filenames = glob.glob(path + "/*.xlsx")
print(filenames)

df=pd.DataFrame()

for file in filenames:
    info = pd.read_excel(file)
    df = df.append(info)

print(df)

writer = pd.ExcelWriter(r'C:\Users\lucas.zarza\Desktop\MasterFile_PrecosBBCE.xlsx')
df.to_excel(writer)
writer.save()

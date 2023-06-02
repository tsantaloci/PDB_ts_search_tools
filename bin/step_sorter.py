import numpy as np
import pandas as pd






class Step(object):
    def __init__(self,name,step,value):
        self.name = name
        self.step = step
        self.value = value

file = 'f1585-small-test.csv'
values = []
with open(file,'r') as fp:
    data = fp.readlines()
    for line in data:
        line = line.strip().split(',')
        print(line)
        values.append(Step(line[0],line[3],line[2]))
step1 = []
step2 = []
step3 = []
step4 = []

for c in values:
    if c.step == 'I':
        step1.append(c)
    if c.step == 'II':
        step2.append(c)
    if c.step == 'III':
        step3.append(c)
    if c.step == 'IV':
        step4.append(c)

df_1 = {'Name':[],
      'Values':[],
      'Step':[]}


"""
makes a duplicate path list for step 1
"""
new_1 = []
step1_new = []
dup_1 = []
for i in step1:
    if i.name not in new_1:
        new_1.append(i.name)
        step1_new.append(i)
    else:
        dup_1.append(i)
"""
makes a duplicate energy list for step 1 NEXT STEP TODO LIST
"""



"""
creating data frame for step 1
"""

for x in step1_new:
    df_1['Name'].append(x.name)
    df_1['Values'].append(x.value)
    df_1['Step'].append(x.step)
df_1 = pd.DataFrame(df_1)
df_1 = df_1.sort_values(by='Values')



"""
makes a duplicate path list for step 2
"""
new_1 = []
step2_new = []
dup_1 = []
for i in step2:
    if i.name not in new_1:
        new_1.append(i.name)
        step2_new.append(i)
    else:
        dup_1.append(i)


"""
creating data frame for step 2
"""

    

df_2 = {'Name':[],
      'Values':[],
      'Step':[]}

for x in step2_new:
    df_2['Name'].append(x.name)
    df_2['Values'].append(x.value)
    df_2['Step'].append(x.step)
df_2 = pd.DataFrame(df_2)
df_2 = df_2.sort_values(by='Values')

"""
makes a duplicate path list for step 3
"""
new_1 = []
step3_new = []
dup_1 = []
for i in step3:
    if i.name not in new_1:
        new_1.append(i.name)
        step3_new.append(i)
    else:
        dup_1.append(i)

"""
creating data frame for step 3
"""

df_3 = {'Name':[],
      'Values':[],
      'Step':[]}

for x in step3_new:
    df_3['Name'].append(x.name)
    df_3['Values'].append(x.value)
    df_3['Step'].append(x.step)
df_3 = pd.DataFrame(df_3)
df_3 = df_3.sort_values(by='Values')

"""
makes a duplicate path list for step 4
"""
new_1 = []
step4_new = []
dup_1 = []
for i in step3:
    if i.name not in new_1:
        new_1.append(i.name)
        step4_new.append(i)
    else:
        dup_1.append(i)

"""
creating data frame for step 4
"""

df_4 = {'Name':[],
      'Values':[],
      'Step':[]}

for x in step4_new:
    df_4['Name'].append(x.name)
    df_4['Values'].append(x.value)
    df_4['Step'].append(x.step)
df_4 = pd.DataFrame(df_3)
df_4 = df_4.sort_values(by='Values')

df = df_1.append(df_2).append(df_3).append(df_4)

print(df.to_csv('test.csv',index=False))
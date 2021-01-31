
import csv

contents=[]

with open('st.txt','r', newline='') as f:
    f = csv.reader(f,delimiter=',')
    for i in f:
        contents.append(i)

for i in contents:
    print(i)
    
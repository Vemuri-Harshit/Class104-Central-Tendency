import csv;

with open('data_2.csv', newline='') as data:
    reader = csv.reader(data);
    filedata = list(reader);

filedata.pop(0);


height_of_all = []

for i in range(len(filedata)):

    height = filedata[i][1]
    height_of_all.append(float(height));

height_of_all.sort();

n = len(height_of_all);

if len(height_of_all) % 2 == 0:
    n1 = float(height_of_all[n // 2])
    n2 = float(height_of_all[n // 2 - 1])
    median = (n1 + n2) / 2
    
else:
    median = float(height_of_all[n // 2])

print(median);
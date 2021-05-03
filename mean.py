import csv;

with open('data_2.csv', newline='') as data:
    reader = csv.reader(data);
    filedata = list(reader);

filedata.pop(0);


height_of_all = []

for i in range(len(filedata)):

    height = filedata[i][1]
    height_of_all.append(float(height));

l = len(height_of_all);
total = 0;

for i in height_of_all:
    total = total + i;

mean = total / l;

print(mean);
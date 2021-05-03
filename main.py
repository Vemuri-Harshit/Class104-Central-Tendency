import csv;
from collections import Counter;

# with open('data.csv', newline='') as data:
#     reader = csv.reader(data);
#     filedata = list(reader);
#     print(reader);
#     print(filedata);    

newdata = 'harshit';
data = Counter(newdata);
newlist = data.items();
value = data.values();



print(data);
print(newlist);
print(value);
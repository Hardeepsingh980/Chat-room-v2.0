from csv import DictReader

f = open('log_details.csv', 'r')
r = DictReader(f)
l_c = []
for row in r:
            l1 = []
            l1.append(row['name'])
            l1.append(row['username'])
            l1.append(row['password'])
            l_c.append(l1)


print(f.read(100))

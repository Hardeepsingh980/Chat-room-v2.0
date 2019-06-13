from csv import DictReader



def change():
    f = open('resources/log_details.csv','w')
    temp = open('resources/temp.txt','r')

    data = temp.read(1000)
    data = data.split('@')
    for i in data:
        print(i)
        f.write(i)
        f.write('\n')

    temp.close()

    f.close()


#change()






    

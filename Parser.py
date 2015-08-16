__author__ = 'root'
import csv

# input_file = csv.DictReader(open())
# x = 0;
# for row in input_file:
#     print row
#     x+=1
#     if(x==6):
#         break
with open('bone density example.csv', 'rb') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    reader = csv.reader(csvfile, dialect)
    l_reader = list(reader)
    new_list = list()
    for row in l_reader:
        if not (row[0] == 'Patient Name' or str(row).__contains__('Page')):
            new_list.append(row)

for row in new_list:
    if row[0] == '' and new_list[new_list.index(row) - 1][0] == '' and new_list[new_list.index(row) - 2][0] != '':
        
        print "/*****************USER*****************/ \n"
        print "Name: " + str(new_list[new_list.index(row) - 2][0]).upper()
        print "Gender: " + str(new_list[new_list.index(row) - 2][2]).upper()
        print "DOB: " + str(new_list[new_list.index(row) - 2][3]).upper()
        print "Language: " + str(new_list[new_list.index(row) - 2][4]).upper()
        print "Account Number: " + str(new_list[new_list.index(row) - 2][5]).upper()
        print "Race: " + str(new_list[new_list.index(row) - 2][6]).upper()
        print "Ethnicity: " + str(new_list[new_list.index(row) - 2][7]).upper()
        print "Phone Number: " + str(new_list[new_list.index(row) - 2][8]).upper()
        print "Reminder Method: " + str(new_list[new_list.index(row) - 2][14])
        if str(new_list[new_list.index(row) - 2][10]) == '':
            print "Email: N/A"
        else:
            print "Email: " + str(new_list[new_list.index(row) - 2][10]).lower()
        if str(new_list[new_list.index(row) - 2][12]).__contains__("returned") or str(
                new_list[new_list.index(row) - 2][12]).__contains__("RTN"):
            print "Adress: " + str(new_list[new_list.index(row) - 1][12]).upper() + " " + str(
                row[12]).upper() + " " + str(new_list[new_list.index(row) - 2][13]).upper() + " " + str(
                new_list[new_list.index(row) - 1][13]).upper() + " " + str(row[13]).upper()
        else:
            print "Adress: " + str(new_list[new_list.index(row) - 2][12]).upper() + " " + str(
                new_list[new_list.index(row) - 1][12]).upper() + " " + str(row[12]).upper() + " " + str(
                new_list[new_list.index(row) - 2][13]).upper() + " " + str(
                new_list[new_list.index(row) - 1][13]).upper() + " " + str(row[13]).upper()
        print "/*****************END USER*****************/ \n"

    elif row[0] != '' and new_list[new_list.index(row) - 1][0] == '' and new_list[new_list.index(row) - 2][0] != '':

        print "/*****************USER*****************/ \n"
        print "Name: " + str(new_list[new_list.index(row) - 2][0]).upper()
        print "Gender: " + str(new_list[new_list.index(row) - 2][2]).upper()
        print "DOB: " + str(new_list[new_list.index(row) - 2][3]).upper()
        print "Language: " + str(new_list[new_list.index(row) - 2][4]).upper()
        print "Account Number: " + str(new_list[new_list.index(row) - 2][5]).upper()
        print "Race: " + str(new_list[new_list.index(row) - 2][6]).upper()
        print "Ethnicity: " + str(new_list[new_list.index(row) - 2][7]).upper()
        print "Phone Number: " + str(new_list[new_list.index(row) - 2][8]).upper()
        print "Reminder Method: " + str(new_list[new_list.index(row) - 2][14])
        if str(new_list[new_list.index(row) - 2][10]) == '':
            print "Email: N/A"
        else:
            print "Email: " + str(new_list[new_list.index(row) - 2][10]).lower()

        print "Adress: " + str(new_list[new_list.index(row) - 2][12]).upper() + " " + str(
            new_list[new_list.index(row) - 1][12]).upper() + " " + str(
            new_list[new_list.index(row) - 2][13]).upper() + " " + str(new_list[new_list.index(row) - 1][13]).upper()
        print "/*****************END USER*****************/ \n"

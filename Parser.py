"""parses the file and displayes each individual record"""
__author__ = 'root'
import csv

with open('bone density example.csv', 'rb') as csvfile:
    DIALECT = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    READER = csv.reader(csvfile, DIALECT)
    LIST_READER = list(READER)
    NEW_LIST = list()
    for row in LIST_READER:
        if not (row[0] == 'Patient Name' or str(row).__contains__('Page')):
            NEW_LIST.append(row)


def display_details(current_row, new_list):
    """displays the details except for address"""
    print "/*****************USER*****************/ \n"
    print "Name: " + \
          str(new_list[new_list.index(current_row) - 2][0]).upper()
    print "Gender: " \
          + str(new_list[new_list.index(current_row) - 2][2]).upper()
    print "DOB: " + \
          str(new_list[new_list.index(current_row) - 2][3]).upper()
    print "Language: " + \
          str(new_list[new_list.index(current_row) - 2][4]).upper()
    print "Account Number: " + \
          str(new_list[new_list.index(current_row) - 2][5]).upper()
    print "Race: " + \
          str(new_list[new_list.index(current_row) - 2][6]).upper()
    print "Ethnicity: " + \
          str(new_list[new_list.index(current_row) - 2][7]).upper()
    print "Phone Number: " + \
          str(new_list[new_list.index(current_row) - 2][8]).upper()
    print "Reminder Method: " + \
          str(new_list[new_list.index(current_row) - 2][14])

    if str(NEW_LIST[NEW_LIST.index(current_row) - 2][10]) == '':
        print "Email: N/A"
    else:
        print "Email: " \
              "" + str(NEW_LIST[NEW_LIST.index(current_row) - 2][10]).lower()


for row in NEW_LIST:
    if row[0] == '' and NEW_LIST[NEW_LIST.index(row) - 1][0] == '' \
            and NEW_LIST[NEW_LIST.index(row) - 2][0] != '':

        display_details(row, NEW_LIST)

        if str(NEW_LIST[NEW_LIST.index(row) - 2][12]).__contains__("returned") \
                or str(NEW_LIST[NEW_LIST.index(row) - 2][12]).__contains__("RTN"):
            print "Adress: " + str(NEW_LIST[NEW_LIST.index(row) - 1][12]).upper() + " " + str(
                row[12]).upper() + " " + str(NEW_LIST[NEW_LIST.index(row) - 2][13]).upper() + " " + str(
                NEW_LIST[NEW_LIST.index(row) - 1][13]).upper() + " " + str(row[13]).upper()
        else:
            print "Adress: " + str(NEW_LIST[NEW_LIST.index(row) - 2][12]).upper() + " " + str(
                NEW_LIST[NEW_LIST.index(row) - 1][12]).upper() + " " + str(row[12]).upper() + " " + str(
                NEW_LIST[NEW_LIST.index(row) - 2][13]).upper() + " " + str(
                NEW_LIST[NEW_LIST.index(row) - 1][13]).upper() + " " + str(row[13]).upper()
        print "/*****************END USER*****************/ \n"

    elif row[0] != '' and NEW_LIST[NEW_LIST.index(row) - 1][0] == '' \
            and NEW_LIST[NEW_LIST.index(row) - 2][0] != '':

        display_details(row, NEW_LIST)

        print "Adress: " + str(NEW_LIST[NEW_LIST.index(row) - 2][12]).upper() + " " + str(
            NEW_LIST[NEW_LIST.index(row) - 1][12]).upper() + " " + str(
            NEW_LIST[NEW_LIST.index(row) - 2][13]).upper() + " " + \
              str(NEW_LIST[NEW_LIST.index(row) - 1][13]).upper()
        print "/*****************END USER*****************/ \n"

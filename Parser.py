"""parses the file and displays each individual record"""
__author__ = 'root'
import csv


def remove_title_info(list_reader):
    for title_row in list_reader:
        if str(title_row).__contains__('Patient Name'):
            end_title = list_reader.index(title_row)
            return end_title


def remove_extra_titles(list_to_clean, new_list, end_title, sorted_headings):
    # list_to_remove = new_list[:end_title]
    # title_dict = {}
    # for title in list_to_remove:
    #     if any(title):
    #         for word in title:
    #             if any(word):
    #                 dict = {word: title.index(word)}
    #                 title_dict.update(dict)
    # for row in list_to_clean:
    #     for key in title_dict:
    #         if any(str(row[title_dict[key]])):
    #             if str(row[title_dict[key]]).__contains__(key):
    #                 row[title_dict[key]] = ''
    for rows in list_to_clean:
        count = 0
        if any(rows):
            for items in rows:
                if any(items):
                    count += 1
        if count < 5 and not(bool(rows[headings_dict[sorted_headings[9]]] == '') != bool(rows[headings_dict[sorted_headings[9]] + 1] == '')):
            list_to_clean[list_to_clean.index(rows)] = ['','','','','','','','','','','','','','','']


with open('bone density example.csv', 'rb') as csvfile:
    DIALECT = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    READER = csv.reader(csvfile, DIALECT)
    LIST_READER = list(READER)
    NEW_LIST = list()
    headers = list()
    headings_dict = {}
    end_title_info = remove_title_info(LIST_READER)

    for row in LIST_READER:
        if str(row).__contains__('Patient Name'):
            headers = row
        elif not str(row).__contains__('Page'):
            NEW_LIST.append(row)

    for heading in headers:
        if any(heading):
            dict = {heading: headers.index(heading)}
            headings_dict.update(dict)
    # print headings_dict
    sorted_headings = sorted(headings_dict, key=headings_dict.__getitem__)
    # print sorted_headings
    remove_extra_titles(NEW_LIST, LIST_READER, end_title_info, sorted_headings)
    # for rows in NEW_LIST:
    #     print rows


def display_details(current_row, new_list):
    """displays the details except for address"""
    row_2_above = new_list.index(current_row) - 2
    print "/*****************USER*****************/ \n"
    print "Name: " + \
          str(new_list[row_2_above][headings_dict[sorted_headings[0]]]).upper()
    print "Gender: " + \
          str(new_list[row_2_above][headings_dict[sorted_headings[1]]]).upper()
    print "DOB: " + \
          str(new_list[row_2_above][headings_dict[sorted_headings[2]]]).upper()
    print "Language: " + \
          str(new_list[row_2_above][headings_dict[sorted_headings[3]]]).upper()
    print "Account Number: " + \
          str(new_list[row_2_above][headings_dict[sorted_headings[4]]]).upper()
    print "Race: " + \
          str(new_list[row_2_above][headings_dict[sorted_headings[5]]]).upper()
    print "Ethnicity: " + \
          str(new_list[row_2_above][headings_dict[sorted_headings[6]]]).upper()
    print "Phone Number: " + \
          str(new_list[row_2_above][headings_dict[sorted_headings[7]]]).upper()
    print "Reminder Method: " + \
          str(new_list[row_2_above][headings_dict[sorted_headings[10]]])

    if str(NEW_LIST[row_2_above][headings_dict[sorted_headings[8]]]) == '':
        print "Email: N/A"
    else:
        print "Email: " \
              "" + str(NEW_LIST[row_2_above][headings_dict[sorted_headings[8]]]).lower()


for row in NEW_LIST:
    if any(row):
        row_2_above_2 = NEW_LIST.index(row) - 2
        row_1_above = NEW_LIST.index(row) - 1
        if row[headings_dict[sorted_headings[0]]] == '' and NEW_LIST[row_1_above][headings_dict[sorted_headings[0]]] == '' \
                and NEW_LIST[row_2_above_2][headings_dict[sorted_headings[0]]] != '':

            display_details(row, NEW_LIST)

            if str(NEW_LIST[row_2_above_2][headings_dict[sorted_headings[9]]]).__contains__("returned") \
                    or str(NEW_LIST[row_2_above_2][headings_dict[sorted_headings[9]]]) \
                            .__contains__("RTN"):

                print "Address: " + \
                      str(NEW_LIST[row_1_above][headings_dict[sorted_headings[9]]]).upper() \
                      + " " + str(row[headings_dict[sorted_headings[9]]]).upper()
            else:

                print "Address: " \
                      + str(NEW_LIST[row_2_above_2][headings_dict[sorted_headings[9]]]).upper() \
                      + " " + str(NEW_LIST[row_1_above][headings_dict[sorted_headings[9]]]).upper() \
                      + " " + str(row[headings_dict[sorted_headings[9]]]).upper()
                print "/*****************END USER*****************/ \n"

        elif row[headings_dict[sorted_headings[0]]] != '' and NEW_LIST[row_1_above][headings_dict[sorted_headings[0]]] == '' \
                and NEW_LIST[row_2_above_2][headings_dict[sorted_headings[0]]] != '':

            display_details(row, NEW_LIST)

            print "Address: " + str(NEW_LIST[row_2_above_2][headings_dict[sorted_headings[9]]]).upper() \
                  + " " + str(NEW_LIST[row_1_above][headings_dict[sorted_headings[9]]]).upper() \
                  + " " + str(NEW_LIST[row_2_above_2][headings_dict[sorted_headings[9]] + 1]).upper() \
                  + " " + str(NEW_LIST[row_1_above][headings_dict[sorted_headings[9]] + 1]).upper()
            print "/*****************END USER*****************/ \n"

import pandas as pd
from random import randint


# lists of data


first_names = [
    "Tom",
    "Susan",
    "Zack",
    "Stephan",
    "Louis",
    "Billy",
    "Linda",
    "Raul",
    "Robert",
    "Paul",
    "Xavier",
    "Taylor",
    "Jonny",
    "Johnathan",
    "Patrick",
    "Moira",
    "Timothy",
    "Javier",
    "156331.1",
    "Tulip",
    "45",
    "Bryce",
    "Donna",
    "Randy",
    "Duane"]


last_names = [
    "Johnson",
    "Armstrong",
    "Jackson",
    "Arnold",
    "Davis",
    "Watson",
    "Garfield",
    "Stoneking",
    "Davidson",
    "Grande",
    "1365122",
    "1",
    "Surandon",
    "Johnathan",
    "Vaughan",
    "Brenner",
    "987",
    ".6",
    "Poppy.1",
    "Winn",
    "Nicholson",
    "Warner",
    "Brown",
    "Blue",
    "Johnson"]


zip_code = [
    "32654",
    "96536-1987",
    "456",
    "36965953",
    "96584",
    "963852",
    "xc",
    "95632",
    "36412365",
    "45986-4212",
    "13654785",
    "96458",
    "78459",
    "98745845458454",
    "33333",
    "x",
    "96864",
    "12365-4584",
    "99545",
    "98641",
    "964",
    "1.2",
    "98521",
    "32654",
    "12546"]


phone = [
    "965-698-4596",
    "8954621365",
    "85963545",
    "6985",
    "tys",
    "985-986-4685",
    "897-695-4512",
    "8975462136",
    "986-654-2136",
    "9658741532",
    "965-415-35215",
    "968-745-5432",
    "458.65.6954",
    "451.652.1253",
    "695-458-4512",
    "3264125041",
    "969-854-7845",
    "652-451-3625",
    "3201203252",
    "32362",
    "659410253",
    "985475130",
    "9658654121",
    "3261451201",
    "965-745-4851"]

# prameters for customer list
customer_list = []


for i in range(len(first_names)):
    customer_list.append({"First Name": first_names[i],
                          "Last Name": last_names[i],
                          "Zip Code": zip_code[i],
                          "Phone": phone[i]})


# checking to see if first and name is string of letters
def check_first_name(first_names):
    result = ''
    for first_name in first_names:
        if not first_name.isalpha():
            result += ""
        else:
            result += first_name
    return result


def check_last_name(last_names):
    result = ''
    for last_name in last_names:
        if not last_name.isalpha():
            result += ""
        else:
            result += last_name
    return result


# check to see if Zip is in right format and is int
def check_zip(zip_code):
    while "-" in zip_code:
        zip_code = zip_code.replace("-", "")
    if not zip_code.isdigit():
        return ""
    if len(zip_code)==5:
        return zip_code
    else:
        if len(zip_code)!=9:
            return ""
        else:
            zipc=''
            for i in range(len(zip_code)):
                if i==5:
                    zip+="-"
                    zipc+=zip_code[i]
                return zipc


# checks phone to see if in right format and is integer
def check_phone(phone):
    while "-" in phone:
        phone = phone.replace("-", "")
    if len(phone)!=10:
        return ""
    elif not phone.isdecimal():
        return ""
    else:
        fphone=''
    for i in range(10):
        if i in [3,6]:
            fphone+="-"
        fphone+=phone[i]

    return fphone

customer_list.append({"First Name": first_names[i],
                      "Last Name": last_names[i],
                      "Zip Code": zip_code[i],
                      "Phone": phone[i]})


def display(customer):
    first_name = customer['First Name']
    last_name = customer['Last Name']
    Zip = customer['Zip Code']
    ph = customer['Phone']
    return "{:>30}".format(check_first_name(first_name))+"{:>30}".format(check_last_name(last_name)) + "{:>30}".format(check_zip(Zip)) + "{:>30}".format(check_phone(ph))


print("{:>30}{:>30}{:>30}{:>30}".format(
    "First name", "Last name", "Zip code", "Phone number"))
customers = list(map(display, customer_list))
for customer in customers:
    print(customer)
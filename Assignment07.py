# ------------------------------------------------- #
# Title: Pickles and Exceptions
# Description: An example of using pickling and try/except statements
# ChangeLog: (Who, When, What)
# <CAllen>,<5.31.2023>,Created Script
# ------------------------------------------------- #

import pickle


# Data -------------------------------------------- #
strFileName = 'AppData.pkl'
lstCustomer = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    file = open(file_name, 'wb')
    pickle.dump(lstCustomer, file)
    file.close()
    return print("Saved!")

def read_data_from_file(file_name):
    objfile = open(file_name, 'rb')
    objFiledata = pickle.load(objfile)
    objfile.close()
    print(objFiledata)
    return objFiledata

# Presentation ------------------------------------ #
try:
    oldfiledata = read_data_from_file(strFileName)
    lstCustomer.append(oldfiledata)
except:
    print('No AppData.pkl found, continue making list.')

Id = float(input('Enter your ID number: '))
name = input('Enter you Name: ')
Id_name = [Id, name]
lstCustomer.append(Id_name)
save_data_to_file(file_name=strFileName, list_of_data=lstCustomer)
read_data_from_file(file_name=strFileName)

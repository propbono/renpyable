# renpyable.py - Simple python programm to reneame TIF files 
# (generated from Trueflow RIP) for better sort ability.
# Author: propbono
# E-mail: propbono@gmail.com
#

import os
import operator

import config

#get current version of programm
version = config.VERSION

# get directory where TIF files is located (from config.py file)
working_directory = config.TIF_DIRECTORY

# list of all files in this directory
file_list = os.listdir(working_directory)

# global variable for checking while loop
answer = 0

# temporary create method 
def create_test_files(number, directory):
    for i in range(1, number + 1):
        name1 = "Test_file_n" + str(i) + "_FRONT.txt"
        name2 = "Test_file_n" + str(i) + "_FRONT_K.txt"
        name3 = "Test_file_n" + str(i) + "_BACK.txt"
        name4 = "Test_file_n" + str(i) + "_BACK_K.txt"
        file1 = open(directory + name1, 'a')
        file1.close()
        file2 = open(directory + name2, 'a')
        file2.close()
        file3 = open(directory + name3, 'a')
        file3.close()
        file4 = open(directory + name4, 'a')
        file4.close()


# temporary delete method - run time: 0.274
def delete_test_files(directory):
    files = os.listdir(directory)
    for f in files:
        if (operator.contains(f, "Test_file")):
            os.remove(directory + f)


#########################################################
#	Function for repair file numbering					#
#		i.e. 01 in exchange for 1						#
#														#
#		file_list	- the list of files to repair		#
#		digits		- how many digits will have new		#
#					  number: 2 - 01, 3 - 001, etc.		#
#														#
#########################################################
def correct_numbers_for(file_list, digits):
    for digit in range(1, int(digits) + 1):
        print("\n############################################################")
        print("#	Changing numbers - LOOP NO. ", digit, "			   #")
        print("############################################################\n\n")
        file_list = os.listdir(working_directory)
        for f in file_list:
            print("	File: ", f)
            print("	----------------------------------------------------")
            replace_number_for_string(f, "FRONT", digit)
            replace_number_for_string(f, "FRONT_K", digit)
            replace_number_for_string(f, "BACK", digit)
            replace_number_for_string(f, "BACK_K", digit)
            print("	----------------------------------------------------\n")
    file_list = os.listdir(working_directory)


#############################################################
#	Helper function which change old name for new name		#
#	with proper number.										#	
#															#
#		name	-	file name from file_list list			#
#		string	-	a string which are helping to locate	#
#					number in the file name					#
#		digits	-	a number of digits in new number		#
#															#
#############################################################
def replace_number_for_string(name, string, digits):
    if operator.contains(name, "A" + string):
        string = "A" + string
        print("		Change: No\n")

    if name.endswith(string, 0, len(name) - 4):
        begin = -4 - len(string) - 1 - digits
        end = -4 - len(string) - 1
        if (not name[begin:end].isdigit()):
            new_name = name[:begin + 1] + "0" + name[end - digits + 1:]
            print("		Change: Yes")
            print("		New Name: ", new_name, "\n")
            os.rename(working_directory + name, working_directory + new_name)
        else:
            print("		Change: No")


#########################################################################
#	Function which correct TIFF files name:								#
#		This function search for file which ends with "FRONT" or 		#
#		"FRONT_K" string and put before this string letter "A"			#
#																		#
#			file_list	-	lit of file to repair						#
#																		#
#########################################################################
def correct_names_for(file_list):
    file_list = os.listdir(working_directory)
    print("\n############################################################")
    print("#	Changing names - FRONT => AFRONT 		   #")
    print("############################################################\n\n")
    for f in file_list:
        print("	File: ", f)
        print("	----------------------------------------------------")
        if operator.contains(f, "AFRONT") or operator.contains(f, "BACK"):  # run time: 1 - 0.314, 2 - 0.115
            print("		Change: No\n")
            continue
        else:
            if f.endswith("FRONT", 0, len(f) - 4):
                new_name = f[:-9] + "A" + f[-9:]
                os.rename(working_directory + f, working_directory + new_name)
                print("		Change: Yes")
                print("		New Name: ", new_name, "\n")
            elif f.endswith("FRONT_K", 0, len(f) - 4):
                new_name = f[:-11] + "A" + f[-11:]
                os.rename(working_directory + f, working_directory + new_name)
                print("		Change: Yes")
                print("		New Name: ", new_name, "\n")
        print("	----------------------------------------------------\n")
    file_list = os.listdir(working_directory)


while answer < 6:
    print("TIFF name changer v.", version)
    print("This programm let you change name of TIF files generated by Trueflow.\nChoose what do you want to do:\n")
    print("1. Numbers correction i.e. 1 = 1, 2 = 02, 3 = 003 etc.")
    print("2. Name correction FRONT = AFRONT")
    print("3. Chain points 1, 2 ")
    print("4. Generate test files")
    print("5. Delete test files")
    print("6. Exit program.")
    answer = int(input("Choose : "))

    if answer == 1:
        digits = input("How many digits will have new number?: ")
        correct_numbers_for(file_list, digits)
    elif answer == 2:
        correct_names_for(file_list)
    elif answer == 3:
        digits = input("How many digits will have new number?: ")
        correct_numbers_for(file_list, digits)
        correct_names_for(file_list)
    elif answer == 4:
        create_test_files(20, working_directory)
    elif answer == 5:
        delete_test_files(working_directory)
		

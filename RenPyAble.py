#!usr/bin/python
import os
import cProfile

# get current directory (directory where renpyable.py is located) 
current_directory = os.getcwd()
# list of all files in this directory
file_list = os.listdir(current_directory)
# global variable for checking while loop
answer = 0

def create_test_files(number):
	for i in range(1,number):
		name1 = "Test_file_no"+str(i)+"_FRONT.txt"
		name2 = "Test_file_no"+str(i)+"_FRONT_K.txt"
		name3 = "Test_file_no"+str(i)+"_BACK.txt"
		name4 = "Test_file_no"+str(i)+"_BACK_K.txt"
		file1 = open(name1,'a')
		file1.close()
		file2 = open(name2,'a')
		file2.close()
		file3 = open(name3,'a')
		file3.close()
		file4 = open(name4,'a')
		file4.close()
		
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
	file_list = os.listdir(current_directory)
	for f in file_list:
			replace_number_for_string(f, "FRONT", digits)
			replace_number_for_string(f, "FRONT_K", digits)
			replace_number_for_string(f, "BACK", digits)
			replace_number_for_string(f, "BACK_K" ,digits)
	file_list = os.listdir(current_directory)	

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
	if name.endswith(string, 0, len(name)-4):
		begin = -4 - len(string) - 1 - digits
		end = -4 - len(string) - 1
		print("File name: ", name)
		print("String: ", string)
		print("Begin: ", begin)
		print("End: ", end)
		print("Name[begin:end]: ", name[begin:end])
		print("isdigit(): " , name[begin:end].isdigit())
		if(not name[begin:end].isdigit()):
			new_name = name[:begin + 1]+"0"+name[end-digits+1:]
			print("New Name: ", new_name,"\n")
			os.rename(name,new_name)

#########################################################################
#	Function which correct TIFF files name:								#
#		This function search for file which ends with "FRONT" or 		#
#		"FRONT_K" string and put before this string letter "A"			#
#																		#
#			file_list	-	lit of file to repair						#
#																		#
#########################################################################
def correct_names_for(file_list):
	file_list = os.listdir(current_directory)
	for f in file_list:
		if f.endswith("FRONT",0, len(f)-4):
			new_name = f[:-9]+"A"+f[-9:]
			os.rename(f,new_name)
		elif f.endswith("FRONT_K",0,len(f)-4):
			new_name = f[:-11]+"A"+f[-11:]
			os.rename(f,new_name)	
	file_list = os.listdir(current_directory)

		

while (int(answer) < 6):
	print("Program do korekty nazwy plików.\nWybierz co chcesz zrobić:\n")
	print("1. Korekta numerów 1 = 01, 2 = 02 itd.")
	print("2. Korekta numerów 01 = 001, 10 = 010, itd.")
	print("3. Korekta nazwy FRONT = AFRONT")
	print("4. Punkty 1, 2, 3 razem")
	print("5. Wygeneruj pliki testowe")
	print("6. Wyjście z programu.")
	answer = input("Wybieram :")
	
	if int(answer) == 1:
		correct_numbers_for(file_list, 2)
	elif int(answer) == 2:
		correct_numbers_for(file_list, 3)
	elif int(answer) == 3:
		correct_names_for(file_list)
	elif int(answer) == 4:
		correct_numbers_for(file_list, 2)
		correct_numbers_for(file_list, 3)
		correct_names_for(file_list)
	elif int(answer) == 5:
		create_test_files(200)
		

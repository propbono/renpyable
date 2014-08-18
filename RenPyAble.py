#!usr/bin/python
import os
import cProfile

# Pobieranie ścieżki dostępu
current_directory = os.getcwd()
answer = 0
file_list = os.listdir(current_directory)

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
		
#######################################################
#	Funkcja poprawiająca numerowanie plików:		  #
#		np. 01 zamiast 1                              #
#		file_list	- lista plików na której          #
#					  dokonuje się korekta            #
#		number		- ile cyfr ma miec liczba         #
#					  2 to 01, 3 to 001 itd.          #
#######################################################
def correct_numbers_for(file_list, number):
	file_list = os.listdir(current_directory)
	for f in file_list:
			replace_number_for_string(f, "FRONT", number)
			replace_number_for_string(f, "FRONT_K", number)
			replace_number_for_string(f, "BACK", number)
			replace_number_for_string(f, "BACK_K" ,number)
	file_list = os.listdir(current_directory)	

###########################################################
#	Funkcja pomocnicza zamieniajca nazwę na prawidłową    #
#		name	-	nazwa pliku z listy file_list         #
#		string	-	ciąg znaków pomagający określić       #
#					gdzie znajdyje się numer              #
#		number	-	liczba cyfr jaką ma mieć numer        #
###########################################################
def replace_number_for_string(name, string, number):	
	if name.endswith(string, 0, len(name)-4):
		begin = -4 - len(string) - 1 - number
		end = -4 - len(string) - 1
		print("File name: ", name)
		print("String: ", string)
		print("Begin: ", begin)
		print("End: ", end)
		print("Name[begin:end]: ", name[begin:end])
		print("isdigit(): " , name[begin:end].isdigit())
		if(not name[begin:end].isdigit()):
			new_name = name[:begin + 1]+"0"+name[end-number+1:]
			print("New Name: ", new_name,"\n")
			os.rename(name,new_name)

#######################################################################
#	Funkcja poprawiająca nazwę pliku tak aby poprawnie się sortowały  #
#		file_list	-	lista plików które mają być poprawione        #
#######################################################################
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

def aggregateFunctions():
		correct_numbers_for(file_list, 2)
		correct_numbers_for(file_list, 3)
		correct_names_for(file_list)

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
		cProfile.run('aggregateFunctions()')
	elif int(answer) == 5:
		cProfile.run('create_test_files(200)')
		

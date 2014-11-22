# renpyable.py - Simple python programme to rename TIF files
# (generated from Trueflow RIP) for better sort ability.
__author__ = 'propbono'
# E-mail: propbono@gmail.com
#

import os
import operator
import datetime
import re

from config import RealConfig
from config import FakeConfig
from tester import Tester
from rename import Rename


class Renpyable:
    def __init__(self, config):
        """
            Initialization method
            creates and assign necessary values from configuration file.
            tif_directory - directory where tiff files are stored
            doa_directory - whole disk with customers jobs where *Doa.pdf files are stored
            ppf_directory - directory where cip3 (ppf) files are stored
            pdf_to_ppf_directory - directory where pdf files used to create ppf files are stored
            version - variable responsible for keeping version program
        """
        self.version = config.VERSION
        self.tif_directory = config.TIF_DIRECTORY
        self.doa_directory = config.DOA_DIRECTORY
        self.ppf_directory = config.PPF_DIRECTORY
        self.pdf_to_ppf_directory = config.PDF_ARCHIVE_DIRECTORY
        self.directories = {self.tif_directory, self.doa_directory,
                            self.ppf_directory, self.pdf_to_ppf_directory}

    def create_test_files(self, number):
        """
            Temporary create method for testing purposes
            Creates necessary files to test other functions
            Without messing up real files
        """
        for directory in self.directories:
            Tester.create_test_files(directory, number)

    def delete_test_files(self):
        """
            Temporary delete method.
            Deletes all temporarily created test files
            Opposite to create_test_files method
        """
        for directory in self.directories:
            Tester.delete_test_files(directory)

    def correct_tiff_filenames(self, digits):
        """
            Function lit every file in folder TIF_DIRECTORY from config file
            and of every file execute dunction Rename.correct_filename(name,digits)
            which changes name acordingly: upcase to smallcase,  word front to afront,
            numbering convention from 1, 2, 3 to 001, 002, 003 if digits = 3

            :param digits:
        """
        file_list = os.listdir(self.tif_directory)
        file_renamed_count = 0
        file_in_list_count = len(file_list)
        for name in file_list:
            new_name =  Rename.correct_filename(name, digits)
            if name.__ne__(new_name):
                os.rename(self.tif_directory + name, self.tif_directory + new_name)
                file_renamed_count += 1
        print("Files in folder: " + str(file_in_list_count) + "\nFiles changed: " +
               str(file_renamed_count))

    def delete_unused_doa_files(self):
        pass

    # tif_file_list = os.listdir(directory)
    # for f in tif_file_list:
    # print()

    def delete_old_ppf_files(self):
        ppf_file_list = os.listdir(self.ppf_directory)
        for f in ppf_file_list:
            modification_date = self.get_modification_time(
                self.ppf_directory + f)

            try:
                today_date = datetime.date.today()
                delete_threshold_date = datetime.date(today_date.year,
                                                     today_date.month - 1,
                                                     today_date.day)
            except:
                delete_threshold_date = today_date

            if (modification_date <= delete_threshold_date):
                print('{0:20} ==> {1} ==> {2} ==> {3}'.format(f,
                                                              modification_date,
                                                              delete_threshold_date,
                                                              "deleted!"))
                os.remove(self.ppf_directory + f)

    def delete_old_pdf_to_ppf_files(self):
        pdf_to_ppf_file_list = os.listdir(self.pdf_to_ppf_directory)
        for f in pdf_to_ppf_file_list:
            print(f)

    def get_modification_time(self, filename):
        time = os.path.getmtime(filename)
        return datetime.date.fromtimestamp(time)

    # delete this - after refactoring with Rename class
    def correct_pdf_filenames(self, digits):
        """
            Implement listening option, and hotfloders
            You copy files to hotfolder i.e. pdf_in
            The are processed there and after finished they are copied to pdf_out

            Corrects pdf chunk files from clients,
            and preparing them for binding. <-- bad word
            i.e. 1_time.pdf, 20_movies.pdf
            will change to: 001_time.pdf and 020_movies.pdf
        """
        for name in pdf_file_list:
            if name.endswith('pdf') or name.endswith("PDF"):
                number = re.search(r'\d+', name).group()
                new_name = name.replace(number, number.zfill(3))
                os.rename(name, new_name)


if __name__ == "__main__":
    # global variable for checking while loop
    answer = 0
    # change to RealConfig() for production
    renpyable = Renpyable(FakeConfig())

    while answer < 7:
        print()
        print("TIFF name changer v.", renpyable.version)
        print("This programme let you change name of TIF files generated by "
             "Trueflow.\nChoose what do you want to do:\n")
        print("1. Correct File names i.e. 1 = 1, 2 = 02, 3 = 003 | "
              "AFRONT instead FRONT etc.")
        print("2. Delete unused *DoA.pdf files")
        print("3. Delete > 2 month-old *.ppf files")
        print("4. Delete > 2 month-old *.pdf to *.ppf files")
        print("5. Generate test files")
        print("6. Delete test files")
        print("7. Exit program.")
        answer = int(input("Choose : "))

        if answer == 1:
            digits = input("How many digits will have new number?: ")
            renpyable.correct_tiff_filenames(int(digits))
        elif answer == 2:
            renpyable.delete_unused_doa_files()
        elif answer == 3:
            renpyable.delete_old_ppf_files()
        elif answer == 4:
            renpyable.delete_old_pdf_to_ppf_files()
        elif answer == 5:
            renpyable.create_test_files(20)
        elif answer == 6:
            renpyable.delete_test_files()


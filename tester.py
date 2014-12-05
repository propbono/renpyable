import os


class Tester:
    @staticmethod
    def create_test_files(directory, number):
        """
        Creates test files in proper directories defined in config file
        :param directory:
        :param number:
        """
        if os.path.exists(directory):
            Tester.delete_test_files(directory)

        os.makedirs(directory, 0o777, True)

        for i in range(1, number + 1):
            # Tif test files
            i_string = str(i)  # conversion from int to str
            name1 = "Test_file_n" + i_string + "_FRONT_.tif"
            name2 = "Test_file_n" + i_string + "_BACK.tif"
            name3 = "Ppf_Test_file_n" + i_string.zfill(3) + ".ppf"
            name4 = "Pdf_Test_file_n" + i_string.zfill(3) + ".pdf"
            name5 = "Doa_Test_file_n" + i_string.zfill(3) + "_DoA.pdf"

            file1 = open(directory + name1, 'a')
            file1.close()
            file2 = open(directory + name2, 'a')
            file2.close()
            file3 = open(directory + name3, 'a')
            file3.close()
            file4 = open(directory + name4, 'a')
            file4.close()
            file5 = open(directory + name5, 'a')
            file5.close()

    @staticmethod
    def delete_test_files(directory):
        """
        Deletes test files from directory
        :param directory:
        """
        for file in os.listdir(directory):
            os.remove(directory + file)

        os.removedirs(directory)

import unittest

from rename import Rename


class RenameTests(unittest.TestCase):
    def test_correct_filename_method_should_change_word_FRONT_to_AFRONT(self):
        filename = "Test_File_FOLD1_FRONT.tif"
        number_of_digits = 2
        result = Rename.correct_filename(filename, number_of_digits)
        expected = "test_file_fold01_afront.tif"
        self.assertEqual(expected, result, "The two filenames are not equal")

    def test_correct_filename_method_should_change_number_1_to_01(self):
        filename = "Test_File_FOLD1_FRONT.tif"
        number_of_digits = 2
        result = Rename.correct_filename(filename, number_of_digits)
        expected = "test_file_fold01_afront.tif"
        self.assertEqual(expected, result, "The two filenames are not equal")

    def test_correct_filename_method_should_change_number_2_to_02(self):
        filename = "Test_File_FOLD2_FRONT.tif"
        number_of_digits = 2
        result = Rename.correct_filename(filename, number_of_digits)
        expected = "test_file_fold02_afront.tif"
        self.assertEqual(expected, result, "The two filenames are not equal")

    def test_correct_filename_method_should_change_all_numbers_in_filename(
            self):
        filename = "Test_File_N1_FOLD1_BACK.tif"
        number_of_digits = 3
        result = Rename.correct_filename(filename, number_of_digits)
        expected = "test_file_n001_fold001_back.tif"
        self.assertEqual(expected, result, "The two filenames are not equal")

        filename = "Test_File_N2_FOLD1_BACK.tif"
        number_of_digits = 3
        result = Rename.correct_filename(filename, number_of_digits)
        expected = "test_file_n002_fold001_back.tif"
        self.assertEqual(expected, result, "The two filenames are not equal")

    def test_correct_filename_method_should_change_numbers_1_20_(self):
        filename = "1-20.pdf"
        number_of_digits = 2
        result = Rename.correct_filename(filename, number_of_digits)
        expected = "01-20.pdf"
        self.assertEqual(expected, result, "The two filenames are not equal")

    def test_correct_filename_method_should_change_numbers_01_6_(self):
        filename = "01-6.pdf"
        number_of_digits = 2
        result = Rename.correct_filename(filename, number_of_digits)
        expected = "01-06.pdf"
        self.assertEqual(expected, result, "The two filenames are not equal")

    def test_correct_filename_method_should_change_numbers_11_19_(self):
        filename = "11-19.pdf"
        number_of_digits = 3
        result = Rename.correct_filename(filename, number_of_digits)
        expected = "011-019.pdf"
        self.assertEqual(expected, result, "The two filenames are not equal")

    def test_correct_filename_method_should_not_change_word_afront_to_aafront(
            self):
        filename = "Test_File_FOLD1_FRONT.tif"
        number_of_digits = 2
        result = Rename.correct_filename(filename, number_of_digits)
        expected = "test_file_fold01_afront.tif"
        self.assertEqual(expected, result, "The two filenames are not equal")
        result2 = Rename.correct_filename(expected, number_of_digits)
        expected2 = "test_file_fold01_afront.tif"
        self.assertEqual(expected2, result2, "The two filenames are not equal")

    def extension(self, filename):
        return filename.split('.')[1]


def main():
    unittest.main()


if __name__ == '__main__':
    main()
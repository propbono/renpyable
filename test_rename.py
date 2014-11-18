import unittest

from rename import Rename


class RenameTests(unittest.TestCase):
    def test_correct_tiff_filenames_method_should_affect_files_with_tif_extension(self):
        filename = "test_file.tif"
        number_of_digits = 2
        result = Rename.correct_tiff_filenames(filename, number_of_digits)
        expected = "tif"
        self.assertTrue(result, msg="Expected extension: " + expected
                                + " Actual extension: " + self.extension( result))

    def test_correct_tiff_filenames_method_should_affect_files_with_tiff_extension(self):
        filename = "test_file.tiff"
        number_of_digits = 2
        result = Rename.correct_tiff_filenames(filename, number_of_digits)
        expected = "tiff"
        self.assertTrue(result,msg="Expected extension: " + expected + " Actual extension: " + self.extension(result))

    def test_correct_tiff_filenames_method_should_affect_also_files_with_capital_letters(self):
        filename = "test_file.TIF"
        number_of_digits = 2
        result = Rename.correct_tiff_filenames(filename, number_of_digits)
        expected = "tif"
        self.assertEqual(expected, self.extension(result),
                         msg="Expected extension: " + expected + " Actual extension: " + self.extension(
                             result))

        filename = "test_file.TIFF"
        number_of_digits = 2
        result = Rename.correct_tiff_filenames(filename, number_of_digits)
        expected = "tiff"
        self.assertEqual(expected, self.extension(result),
                         msg="Expected extension: " + expected + " Actual extension: " + self.extension(
                             result))

    def test_correct_tiff_filenames_method_should_change_word_FRONT_to_AFRONT(self):
        filename = "Test_File_FOLD1_FRONT.tif"
        number_of_digits = 2
        result = Rename.correct_tiff_filenames(filename, number_of_digits)
        expected = "test_file_fold01_afront.tif"
        self.assertEqual(expected, result, "The two filenames are not equal")

    def test_correct_tiff_filenames_method_should_change_number_1_to_01(self):
        filename = "Test_File_FOLD1_FRONT.tif"
        number_of_digits = 2
        result = Rename.correct_tiff_filenames(filename,number_of_digits)
        expected = "test_file_fold01_afront.tif"
        self.assertEqual(expected,result, "The two filenames are not equal")

    def test_correct_tiff_filenames_method_should_change_number_2_to_02(self):
        filename = "Test_File_FOLD2_FRONT.tif"
        number_of_digits = 2
        result = Rename.correct_tiff_filenames(filename,number_of_digits)
        expected = "test_file_fold02_afront.tif"
        self.assertEqual(expected,result, "The two filenames are not equal")

    def test_correct_tiff_filenames_method_should_change_all_numbers_in_filename(self):
        filename = "Test_File_N1_FOLD1_BACK.tif"
        number_of_digits = 3
        result = Rename.correct_tiff_filenames(filename, number_of_digits)
        expected = "test_file_n001_fold001_back.tif"
        self.assertEqual(expected,result, "The two filenames are not equal")

        filename = "Test_File_N2_FOLD1_BACK.tif"
        number_of_digits = 3
        result = Rename.correct_tiff_filenames(filename, number_of_digits)
        expected = "test_file_n002_fold001_back.tif"
        self.assertEqual(expected,result, "The two filenames are not equal")

    def extension(self, filename):
        return filename.split('.')[1]


def main():
    unittest.main()


if __name__ == '__main__':
    main()
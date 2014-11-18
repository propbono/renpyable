import unittest

from rename import Rename


class RenameTests(unittest.TestCase):
    def test_correct_tiff_filenames_method_should_affect_files_with_tif_extension(
            self):
        filename = "test_file.tif"
        result = Rename.correct_tiff_filenames(filename)
        expected = "tif"
        self.assertTrue(result,
                        msg="Expected extension: " + expected + " Actual extension: " + self.extension(
                            result))

    def test_correct_tiff_filenames_method_should_affect_files_with_tiff_extension(self):
        filename = "test_file.tiff"
        result = Rename.correct_tiff_filenames(filename)
        expected = "tiff"
        self.assertTrue(result,msg="Expected extension: " + expected + " Actual extension: " + self.extension(result))

    def test_correct_tiff_filenames_method_should_affect_also_files_with_capital_letters(self):
        filename = "test_file.TIF"
        result = Rename.correct_tiff_filenames(filename)
        expected = "tif"
        self.assertEqual(expected, self.extension(result),
                         msg="Expected extension: " + expected + " Actual extension: " + self.extension(
                             result))

        filename = "test_file.TIFF"
        result = Rename.correct_tiff_filenames(filename)
        expected = "tiff"
        self.assertEqual(expected, self.extension(result),
                         msg="Expected extension: " + expected + " Actual extension: " + self.extension(
                             result))

    def test_correct_tiff_filenames_method_should_change_word_FRONT_to_AFRONT(self):
        filename = "Test_File_FOLD1_FRONT.tif"
        result = Rename.correct_tiff_filenames(filename)
        expected = "test_file_fold1_afront.tif"
        self.assertEqual(result,expected, "The two filenames are not equal")


    def test_correct_tiff_filenames_method_should_change_number_1_to_01(self):
        self.assertTrue(False,"NotImplemented")

    def test_correct_tiff_filenames_method_should_change_number_10_to_010(self):
        self.assertTrue(False,"NotImplemented")

    def test_correct_tiff_filenames_method_should_change_number_100_to_0100(self):
        self.assertTrue(False,"NotImplemented")

    def test_correct_tiff_filenames_method_should_change_number_02_to_0002(self):
        self.assertTrue(False,"NotImplemented")


    def extension(self, filename):
        return filename.split('.')[1]


def main():
    unittest.main()


if __name__ == '__main__':
    main()
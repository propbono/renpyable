import re

class Rename:
    def correct_tiff_filenames(filename, number_of_digits):
        """ Function changes upper case to lower case,
            changes also word front to afront
            changes also number of digits in numbers
        """
        filename = filename.lower()
        if filename.endswith("tif") or filename.endswith('tiff'):
            filename = filename.replace("front", "afront")

            numbers_to_replace = re.findall(r'\d+',filename)
            if numbers_to_replace:
                unique_numbers_to_replace = set(numbers_to_replace)
                for number in unique_numbers_to_replace:
                    filename = filename.replace(number,
                                        number.zfill(number_of_digits))

        return filename

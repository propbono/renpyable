from operator import contains
import re


class Rename:
	@staticmethod
	def correct_filename(filename, number_of_digits):
		""" Function changes upper case to lower case,
                changes also word front to afront
                changes also number of digits in numbers i.e. 1 = 001

                :param filename:
                :param number_of_digits:
                :rtype : string
            """
		filename = filename.lower()
		if not contains(filename,"afront"):
			filename = filename.replace("front", "afront")

		numbers_to_replace = re.findall(r'\d+', filename)

		if numbers_to_replace:
			unique_numbers_to_replace = set(numbers_to_replace)
			for number in unique_numbers_to_replace:
				filename = filename.replace(number, number.zfill(number_of_digits))

		return filename

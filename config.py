# Configuration file
import os
import sys


class RealConfig:
	# Constant to control version of programm
	VERSION = "0.2.4"

	# Constant to determine where TIFF files are stored
	TIF_DIRECTORY = 'Q:\\TIFF\\Test\\'
	PPF_DIRECTORY = 'B:\\'
	PDF_ARCHIVE_DIRECTORY = 'F:\\00Archiwum - PDFdoCIP\\'
	DOA_DIRECTORY = 'W:\\'

class FakeConfig:
	# Constant to control version of programm
	VERSION = "0.2.4"

	# Constant to determine where TIFF files are stored
	TIF_DIRECTORY = os.path.dirname(sys.argv[0]) +'/tif/'	# check and change to this form os.path.dirname(sys.argv[0])
	PPF_DIRECTORY = os.path.dirname(sys.argv[0]) + '/ppf/'	# for compatibility with windows
	PDF_ARCHIVE_DIRECTORY = os.path.dirname(sys.argv[0]) + '/pdf/'
	DOA_DIRECTORY = os.path.dirname(sys.argv[0]) + '/doa/'
	


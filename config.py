# Configuration file
class RealConfig:
	# Constant to control version of programm
	VERSION = "0.1.1"

	# Constant to determine where TIFF files are stored
	TIF_DIRECTORY = 'Q:\\TIFF\\Test\\'
	PPF_DIRECTORY = 'B:\\'
	PDF_ARCHIVE_DIRECTORY = 'F:\\00Archiwum - PDFdoCIP\\'
	DOA_DIRECTORY = 'W:\\'

class FakeConfig:
	# Constant to control version of programm
	VERSION = "0.2.4"

	# Constant to determine where TIFF files are stored
	TIF_DIRECTORY = '/home/propbono/Projects/Python/RenPyAble/tif/'	# check and change to this form os.path.dirname(sys.argv[0])
	PPF_DIRECTORY = '/home/propbono/Projects/Python/RenPyAble/ppf/'	# for compatibility with windows
	PDF_ARCHIVE_DIRECTORY = '/home/propbono/Projects/Python/RenPyAble/pdf/'
	DOA_DIRECTORY = '/home/propbono/Projects/Python/RenPyAble/doa/'
	
	'''
	def getScriptPath():
    return os.path.dirname(os.path.realpath(sys.argv[0]))
	'''


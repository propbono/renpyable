class Rename:
    def correct_tiff_filenames(filename):
        """ Function changes upper case to lower case,\n"
            changes also word front to afront\n"
        """
        filename = filename.lower()
        if filename.endswith("tif") or filename.endswith('tiff'):
            filename = filename.replace("front", "afront")
            return filename

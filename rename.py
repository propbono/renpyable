class Rename:

    def rename_tiff_files(filename):
        filename = filename.lower()
        if filename.endswith("tif") or filename.endswith('tiff'):
            return filename


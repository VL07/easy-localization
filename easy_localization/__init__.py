import json
import os

class Localization:
    def __init__(self, jsonFiles: list, errorOnInvalidKey=True) -> None:
        """Load one or mores json file with all translations. Make sure the files are named after the langage so they're easier to access"""

        if not isinstance(jsonFiles, list):
            raise ValueError(f"jsonFiles parameter should be of type list, not '{str(type(jsonFiles))}'")

        if not isinstance(errorOnInvalidKey, bool):
            raise ValueError(f"errorOnInvalidKey parameter should be of type bool, not '{str(type(jsonFiles))}'")

        self.loadedFiles = {}
        self.errorOnInvalidKey = errorOnInvalidKey

        for filePath in jsonFiles:
            if not isinstance(filePath, str):
                raise ValueError(f"jsonFiles items should be of type str, not '{str(type(filePath))}'")
            
            if not os.path.exists(filePath):
                raise ValueError(f"'{filePath}' is not a path to an existing file")

            file = open(filePath, "r")
            data = file.read()
            file.close()

            filename = os.path.basename(filePath)
            filename = filename.split(".")[:-1]

            newFilename = ""
            for item in filename:
                newFilename += item
            
            filename = newFilename

            if filename in self.loadedFiles.keys():
                raise NameError(f"A file with the filename {filename} has already been loaded")
            
            self.loadedFiles[filename] = json.loads(data)

            

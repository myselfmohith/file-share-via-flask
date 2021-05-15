import os

class FileUtilities:
    def __init__(self):
        # TODO: Change Folder name to the File Name
        self.path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'File Share')
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def getFiles(self):
        filenames = []
        for i in os.listdir(self.path):
            filenames.append(i)
        return filenames

    def saveFile(self, ifile):
        ifile.save(os.path.join(self.path,ifile.filename))

    def getFilepath(self,name):
        return os.path.join(self.path,name)
from os import walk
from shutil import rmtree

settingsFile = open('./settings.txt', 'r')
directoryToReadFrom = settingsFile.readline().strip()
directorySuffix = settingsFile.readline().strip()
likedMusic = settingsFile.readline().strip()
categories = settingsFile.readline().strip().split(',')

directoriesToParse = [directoryToReadFrom]
filesFound = []

# delete any existing copied directories
for(currPath, directoryNames, fileNames) in walk(directoryToReadFrom):
    for directoryName in directoryNames:
        if directorySuffix in directoryName:
            directoryToDelete = currPath + '\\' + directoryName
            rmtree(directoryToDelete)
            print('deleted: ' + directoryToDelete)

# find files to copy
for directory in directoriesToParse:
    for(currPath, directoryNames, fileNames) in walk(directory):
        for directoryName in directoryNames:
            directoriesToParse.append(currPath + directoryName)
        for fileName in fileNames:
            filePath = currPath + '\\' + fileName
            if likedMusic in currPath and directorySuffix not in currPath:
                print('liked music: ' + filePath)
            filesFound.append(filePath)
    directoriesToParse.remove(directory)

print(filesFound)


# 1. delete existing suffixed directories
# 2. create suffixed directories
# 3. read through all files
# 4. if a liked file, copy it to the appropriate suffixed directory

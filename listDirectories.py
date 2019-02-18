from os import walk, path, makedirs, listdir
from shutil import rmtree, copyfile

# retrieve settings
settingsFile = open('./settings.txt', 'r')
directoryToReadFrom = settingsFile.readline().strip()
directoryPrefix = '_'
directorySuffix = settingsFile.readline().strip()
likedMusic = settingsFile.readline().strip()
categories = settingsFile.readline().strip().split(',')

# store files found
musicTypes = listdir(directoryToReadFrom)
directoriesToParse = [directoryToReadFrom]
filesFound = []

for musicType in musicTypes:
    musicTypePath = path.join(directoryToReadFrom, musicType)

    # delete existing flattened directories
    for musicSeries in listdir(musicTypePath):
        if directorySuffix in musicSeries:
            seriesToDelete = path.join(musicTypePath, musicSeries)
            rmtree(seriesToDelete)
            print('deleted: ' + seriesToDelete)

    # create empty directories to copy into
    for category in categories:
        flattenedDirectory = musicTypePath + '\\' + directoryPrefix + category + directorySuffix
        if not path.exists(flattenedDirectory):
            makedirs(flattenedDirectory)

# create (empty) flattened directories per child of directory
# for(currPath, directoryNames, fileNames) in walk(directoryToReadFrom):
#     for category in categories:
#         makedirs(directoryToReadFrom + '\\' + category + directorySuffix)

# find files to copy
for directory in directoriesToParse:
    for(currPath, directoryNames, fileNames) in walk(directory):
        for musicType in directoryNames:
            directoriesToParse.append(currPath + musicType)

        for fileName in fileNames:
            filePath = currPath + '\\' + fileName
            if likedMusic in currPath and directorySuffix not in currPath:
                copyfile(filePath, directoryToReadFrom + '\\' + likedMusic + directorySuffix + '\\' + fileName)
                print('liked music: ' + filePath)
            filesFound.append(filePath)
    directoriesToParse.remove(directory)

print(filesFound)

# 1. delete existing suffixed directories
# 2. create suffixed directories
# 3. read through all files
# 4. if a liked file, copy it to the appropriate suffixed directory

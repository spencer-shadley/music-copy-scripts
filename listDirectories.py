from os import walk, path, makedirs, listdir
from shutil import rmtree, copyfile

# retrieve settings
settingsFile = open('./settings.txt', 'r')
directoryToReadFrom = settingsFile.readline().strip()
directoryPrefix = '_'
directorySuffix = settingsFile.readline().rstrip()
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

# find files to copy
for musicType in listdir(directoryToReadFrom):
    musicTypePath = path.join(directoryToReadFrom, musicType)
    for musicSeries in listdir(musicTypePath):
        # for (currPath, directoryNames, fileNames) in walk(musicTypePath):
        musicSeriesPath = path.join(musicTypePath, musicSeries)
        for musicSeriesDirectory in listdir(musicSeriesPath):
            musicSeriesDirectoryPath = path.join(musicSeriesPath, musicSeriesDirectory)
            if path.isdir(musicSeriesDirectoryPath) and likedMusic in musicSeriesDirectoryPath:
                # pull out all files into the Liked flattened dir
                for likedFile in listdir(musicSeriesDirectoryPath):
                    likedFilePath = path.join(musicSeriesDirectoryPath, likedFile)
                    if not path.isdir(likedFilePath):
                        print('liked file: ' + likedFilePath)
                # look for more folders and pull those into their own categories
                print(musicSeriesDirectoryPath)
            # for fileName in fileNames:
            #     filePath = path.join(currPath, fileName)
            #     if likedMusic in currPath and directorySuffix not in currPath:
            #         print('found liked music: ' + filePath)
            #         dest = musicTypePath + ''
            #         copyfile(filePath, dest)


# for directory in directoriesToParse:
#     for(currPath, directoryNames, fileNames) in walk(directory):
#         for musicType in directoryNames:
#             directoriesToParse.append(currPath + musicType)
#
#         for fileName in fileNames:
#             filePath = currPath + '\\' + fileName
#             if likedMusic in currPath and directorySuffix not in currPath:
#                 copyfile(filePath, directoryToReadFrom + '\\' + likedMusic + directorySuffix + '\\' + fileName)
#                 print('liked music: ' + filePath)
#             filesFound.append(filePath)
#     directoriesToParse.remove(directory)

print(filesFound)

# 1. delete existing suffixed directories
# 2. create suffixed directories
# 3. read through all files
# 4. if a liked file, copy it to the appropriate suffixed directory

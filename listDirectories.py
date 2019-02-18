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
    makedirs(path.join(musicTypePath, directoryPrefix + likedMusic + directorySuffix))
    for category in categories:
        flattenedDirectory = musicTypePath + '\\' + directoryPrefix + category + directorySuffix
        if not path.exists(flattenedDirectory):
            makedirs(flattenedDirectory)

# find files to copy
for musicType in listdir(directoryToReadFrom):
    musicTypePath = path.join(directoryToReadFrom, musicType)
    flattenedMusicDirectory = path.join(musicTypePath, directoryPrefix + likedMusic + directorySuffix)
    for musicSeries in listdir(musicTypePath):
        musicSeriesPath = path.join(musicTypePath, musicSeries)
        for musicSeriesDirectory in listdir(musicSeriesPath):
            musicSeriesDirectoryPath = path.join(musicSeriesPath, musicSeriesDirectory)
            if path.isdir(musicSeriesDirectoryPath) and likedMusic in musicSeriesDirectoryPath:
                for likedFile in listdir(musicSeriesDirectoryPath):
                    likedFilePath = path.join(musicSeriesDirectoryPath, likedFile)
                    if not path.isdir(likedFilePath):
                        likedFileDestPath = path.join(flattenedMusicDirectory, likedFile)
                        copyfile(likedFilePath, likedFileDestPath)
                # TODO: look for more folders and pull those into their own categories
                print(musicSeriesDirectoryPath)

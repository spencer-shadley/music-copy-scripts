from os import path, makedirs, listdir
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
                for likedFileOrGenreDir in listdir(musicSeriesDirectoryPath):
                    likedFileOrGenreDirPath = path.join(musicSeriesDirectoryPath, likedFileOrGenreDir)
                    if path.isdir(likedFileOrGenreDirPath):
                        for genreFile in listdir(likedFileOrGenreDirPath):
                            genreFilePath = path.join(likedFileOrGenreDirPath, genreFile)
                            genreFlattenedPath = path.join(musicTypePath, directoryPrefix + likedFileOrGenreDir + directorySuffix)
                            copyfile(genreFilePath, path.join(genreFlattenedPath, genreFile))
                    else:
                        likedFileDestPath = path.join(flattenedMusicDirectory, likedFileOrGenreDir)
                        copyfile(likedFileOrGenreDirPath, likedFileDestPath)
                print(musicSeriesDirectoryPath)

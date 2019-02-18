from os import walk

categoriesFile = open('./categories.txt', 'r')
directorySuffix = categoriesFile.readline().strip()
likedMusic = categoriesFile.readline().strip()
categories = categoriesFile.readline().strip()

directoriesToParse = ['H:\\']
filesFound = []

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

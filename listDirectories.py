from os import walk

f = []
directoriesToParse = ['H:\\']

for directory in directoriesToParse:
    for(currPath, directoryNames, fileNames) in walk(directory):
        for directoryName in directoryNames:
            directoriesToParse.append(currPath + directoryName)
        for fileName in fileNames:
            print(currPath + fileName)
    directoriesToParse.remove(directory)

import os
import shutil

settingsFile = open('./flattenerSettings.txt', 'r')
directoryToReadFrom = settingsFile.readline().strip()

flattenedDirectory = directoryToReadFrom + '/_flattened-files'

print('moving files from ' + directoryToReadFrom + ' to ' + flattenedDirectory)

try:
    os.mkdir(flattenedDirectory)
except OSError:
    print('failed to create dir')

# subdirectories = os.walk(directoryToReadFrom)

for root, dirs, files in os.walk(directoryToReadFrom):
    for name in files:
        filePath = os.path.join(root, name)
        print(filePath)
        try:
            if name.lower().endswith(('.png', '.jpg', '.jpeg')):
                os.rmdir(filePath)
                print('deleted ' + filePath)
            shutil.move(filePath, flattenedDirectory + '/' + name)
        except:
            print('failed to move file')

        if not os.listdir(root):
            os.rmdir(root)

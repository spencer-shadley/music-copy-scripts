from os import walk

f = []

for(dirpath, dirnames, filenames) in walk('H:\\'):
    for dir in dirnames:
        print (dir)
    for fileName in filenames:
        f.append((dirpath + fileName))
    break

print (f)

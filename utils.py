import os
path = './test/data/TEMP'
files = os.listdir(path)
i = 0
for file in files:
   os.rename(os.path.join(path, file), os.path.join(path, 'xiao_' + str(i) + '.jpg'))
   i = i + 1
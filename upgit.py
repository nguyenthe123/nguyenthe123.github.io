import os

htmlfile = "word.html"
afile = open(htmlfile, 'r')
lines = afile.readlines()
fout = open("index.html",'w+')
for line in lines:
    if line[0:65] == ' <img src=/home/kepthe/Desktop/Gitne/trans/nguyenthe123.github.io':
        line = line[0:10] + line[65:len(line)]
        print(line)
    fout.write(line)
afile.close
fout.close

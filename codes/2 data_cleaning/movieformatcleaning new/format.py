# This file is to clean the movie information, copy each column into title_all.txt, and run format.py
# When firstly collecting the data, each line has all titles, I use this program to clean the tile,
# Now what you can see in the table is one title in one line.
f = open("title_all.txt","r")
lines = f.readlines()
new_lines = []
i = 0
title = []
test = []
old_line = ''
count = [] #The valid title name
for x in range(0,10000000):
    count.append(1)
for line in lines:
    new_line = line;
    if new_line == old_line:
        count[i] = count[i]+1
    else:
        new_lines.append(line)
        i = i+1
    old_line = line
s = []

for t in range(len(new_lines)):
    for j in range(0,count[t+1]):
        test.append(new_lines[t])
        title.append(new_lines[t].split(',')[j].replace("\n",""))






strlist="\n".join(title)
txtnew=open("new_title.txt","w", encoding="utf8")
txtnew.write(strlist)
txtnew.close()

f.close()

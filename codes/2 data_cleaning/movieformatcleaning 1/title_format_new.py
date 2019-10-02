f = open("title_all.txt","r")
lines = f.readlines()
new_lines = []
i = 0
title = []
for line in lines:
    if i%50 == 0:
        new_lines.append(line)
    i=i+1
    #for j in range(len(line)):
for t in range(len(new_lines)):
    #print (new_lines[i])
    for j in range(len(new_lines[t].split(','))):
        if new_lines[t].split(',')[j][0]!=' ':
            #print(new_lines[t].split(',')[j])
            title.append(new_lines[t].split(',')[j])
#print(title.replace())

for x in range(len(title)):
    print(title[x].replace("\n",""))

'''
while i <= 100:
    if f.readline():
        line[i] = f.readline()
        for j in range(len(line[i])):
            if line[i].split(',')[j][0]!=' ':
                print(line[i].split(',')[j])
    i = i+50
'''
f.close()
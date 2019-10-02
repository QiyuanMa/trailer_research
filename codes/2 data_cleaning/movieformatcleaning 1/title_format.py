# When firstly collecting the data, each line has all titles, I use this program to clean the tile,
# Now what you can see in the table is one title in one line.
f = open("title.txt")
line = f.readline()
count = 0
for i in range(len(line.split(','))):
    if line.split(',')[i][0]!=' ':
        print(line.split(',')[i])
        count = count + 1
print (count)

f.close()
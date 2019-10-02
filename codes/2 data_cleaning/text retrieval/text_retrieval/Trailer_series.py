# This program extract the Trailer series from the 'description' of each trailer
newlist=['']
#print (oldlist)

for line in open(r"C:\Users\student\Desktop\title.txt", encoding="ISO-8859-1"):
    t = 1
   # print(line)
    for i in range(0,len(line)):

        if (line[i]=="#" and (line[i+1]=='1' or line[i+1]=='2' or line[i+1]=='3' or line[i+1]=='4' or line[i+1]=='5'
         or line[i+1]=='6' or line[i+1]=='7' or line[i+1]=='8')):
            newlist.append(line[i+1])
            print(line[i+1])
            t=0
            break
        if (line[i]=="#" and line[i+1]==' '):
            newlist.append(line[i+2])
            print(line[i+2])
            t=0
            '''
        if (line[i] == "T" and line[i+1] == "r" and line[i+2] == "a" and line[i+3] == "i" and line[i+4] == "l" and line[i+5] == "e" and line[i+6] == "r" and line[i+7] == " " and (line[i+8]=='1' or line[i+8]=='2' or line[i+8]=='3' or line[i+8]=='4' or line[i+8]=='5'
         or line[i+8]=='6' or line[i+8]=='7' or line[i+8]=='8')):
            newlist.append(line[i+8])
            print(line[i+8])
            t = 0
            break
            '''
    if t!=0:
        newlist.append('0')
    #    print(0)

print(newlist)
strlist="\n".join(newlist)
txtnew=open("Trailer_series.txt","w", encoding="utf8")
txtnew.write(strlist)
txtnew.close()

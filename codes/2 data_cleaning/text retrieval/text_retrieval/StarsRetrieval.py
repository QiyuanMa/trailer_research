# This program extract the star name from the 'description' of each trailer
TXTtemp = open(r"C:\Users\student\Desktop\description.txt", encoding="utf8")
txtbuffer=TXTtemp.read()
#print (txtbuffer)
#i=0
oldlist=['']
newlist=['']
#for txtchar in txtbuffer:
#	oldlist.append(txtchar)
#	i=i+1
oldlist=list(txtbuffer)
#print (oldlist)
for index in range(len(txtbuffer)):
	if oldlist[index]=="S" and oldlist[index+1]=="t"and oldlist[index+2]=="a" and oldlist[index+3]=="r"\
            and oldlist[index+4]=="r" and oldlist[index+5]=="i" and oldlist[index+6]=="n"\
            and oldlist[index + 7] == "g":
                i=1
                index = index + 10
                for j in range(100):
                    if (oldlist[index+j]=="D" and oldlist[index+j+1]=="i" and oldlist[index+j+2]=="r" and oldlist[index+j+3]=="e" and oldlist[index+j+4]=="c" and oldlist[index+j+5]=="t")\
                            or(oldlist[index+j]=="S" and oldlist[index+j+1]=="t" and oldlist[index+j+2]=="o" and oldlist[index+j+3]=="r" and oldlist[index+j+4]=="y"):
                        #newlist.append("\n")
                        j=0
                        break
                    newlist.append(oldlist[index+j])
print(newlist)
strlist="".join(newlist)
txtnew=open("stars.txt","w")
txtnew.write(strlist)
txtnew.close()

TXTtemp.close()
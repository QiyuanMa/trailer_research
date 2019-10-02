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
                index = index + 9
                for j in range(100):
                    if (oldlist[index+j]=="," and oldlist[index+j+1]==" "):
                        newlist.append("\n")
                        j=0
                        break
                    newlist.append(oldlist[index+j])
print(newlist)
strlist="".join(newlist)
txtnew=open("starsOthers.txt","w",encoding="utf8")
txtnew.write(strlist)
txtnew.close()

TXTtemp.close()

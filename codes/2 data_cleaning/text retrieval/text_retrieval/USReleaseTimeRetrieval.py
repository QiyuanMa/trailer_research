# This program extract the star name from the 'USReleaseTime' of each trailer
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
    if (oldlist[index]=="U" and oldlist[index+1]=="S"and oldlist[index+2]==" " and oldlist[index+3]=="R"\
            and oldlist[index+4]=="e" and oldlist[index+5]=="l" and oldlist[index+6]=="e"\
            and oldlist[index + 7] == "a" and oldlist[index + 8] =="s" and oldlist[index + 9]) =="e":
                index = index + 17
                for j in range(1000):
                    if (oldlist[index+j+1]=="S" and oldlist[index+j+2]=="t" and oldlist[index+j+3]=="a" and oldlist[index+j+4]=="r" and oldlist[index+j+5]=="r"):
                        newlist.append("\n")
                        j=0
                        break
                    newlist.append(oldlist[index+j])
    '''
    if (oldlist[index]=="S" and oldlist[index+1]=="t"and oldlist[index+2]=="o" and oldlist[index+3]=="r"\
            and oldlist[index+4]=="y"):
                index = index + 10
                for j in range(100):
                    if (oldlist[index+j]=="S" and oldlist[index+j+1]=="y" and oldlist[index+j+2]=="n" and oldlist[index+j+3]=="o" and oldlist[index+j+4]=="p" and oldlist[index+j+5]=="s"\
                            and oldlist[index+j+5]=="i" and oldlist[index+j+5]=="s"):
                        #newlist.append("\n")
                        j=0
                        break
                    newlist.append(oldlist[index+j])
    '''
print(newlist)
strlist="".join(newlist)
txtnew=open("USReleaseTime.txt","w", encoding="utf8")
txtnew.write(strlist)
txtnew.close()

TXTtemp.close()

# This program extract the director name from the 'description' of each trailer
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
    if (oldlist[index]=="D" and oldlist[index+1]=="i"and oldlist[index+2]=="r" and oldlist[index+3]=="e"\
            and oldlist[index+4]=="c" and oldlist[index+5]=="t" and oldlist[index+6]=="e"\
            and oldlist[index + 7] == "d"):
                index = index + 13
                for j in range(100):
                    if (oldlist[index+j]=="S" and oldlist[index+j+1]=="y" and oldlist[index+j+2]=="n" and oldlist[index+j+3]=="o" and oldlist[index+j+4]=="p" and oldlist[index+j+5]=="s"\
                            and oldlist[index+j+6]=="i" and oldlist[index+j+7]=="s")\
                            or (oldlist[index+j]=="W" and oldlist[index+j+1]=="r" and oldlist[index+j+2]=="i" and oldlist[index+j+3]=="t" and oldlist[index+j+4]=="t" and oldlist[index+j+5]=="e"\
                            and oldlist[index+j+6]=="n"):
                        #newlist.append("\n")
                        j=0
                        break
                    newlist.append(oldlist[index+j])
    if (oldlist[index]=="S" and oldlist[index+1]=="t"and oldlist[index+2]=="o" and oldlist[index+3]=="r"\
            and oldlist[index+4]=="y" and oldlist[index+5]==" " and oldlist[index+6]=="B" and oldlist[index+7]=="y"):
                index = index + 10
                for j in range(100):
                    if (oldlist[index+j]=="S" and oldlist[index+j+1]=="y" and oldlist[index+j+2]=="n" and oldlist[index+j+3]=="o" and oldlist[index+j+4]=="p" and oldlist[index+j+5]=="s"\
                            and oldlist[index+j+6]=="i" and oldlist[index+j+7]=="s") \
                            or (oldlist[index + j] == "W" and oldlist[index + j + 1] == "r" and oldlist[
                        index + j + 2] == "i" and oldlist[index + j + 3] == "t" and oldlist[index + j + 4] == "t" and
                                oldlist[index + j + 5] == "e" \
                                and oldlist[index + j + 6] == "n"):
                        #newlist.append("\n")
                        j=0
                        break
                    newlist.append(oldlist[index+j])
print(newlist)
strlist="".join(newlist)
txtnew=open("Directors.txt","w", encoding="utf8")
txtnew.write(strlist)
txtnew.close()

TXTtemp.close()

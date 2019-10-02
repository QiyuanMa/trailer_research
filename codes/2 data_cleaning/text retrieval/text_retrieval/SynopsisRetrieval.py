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
    if (oldlist[index]=="S" and oldlist[index+1]=="y"and oldlist[index+2]=="n" and oldlist[index+3]=="o"\
            and oldlist[index+4]=="p" and oldlist[index+5]=="s" and oldlist[index+6]=="i"\
            and oldlist[index + 7] == "s"):
                index = index + 10
                for j in range(1000):
                    if (oldlist[index+j+1]=="W" and oldlist[index+j+2]=="a" and oldlist[index+j+3]=="t" and oldlist[index+j+4]=="c" and oldlist[index+j+5]=="h"):
                        #newlist.append("\n")
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
txtnew=open("Synopsis.txt","w", encoding="utf8")
txtnew.write(strlist)
txtnew.close()

TXTtemp.close()

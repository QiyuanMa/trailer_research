# This file deletes all the '*' and '-' which could not be recognized by re.match()
f = open("title_all.txt","r",encoding="utf-8")
lines = f.readlines()
new_lines = []
i = 0
title = []
txtnew=open(r"signal_deleted_title.txt","w", encoding="utf8")
t = "123*456"

for line in lines:
    line = line.replace("*"," ")
    line = line.replace("-"," ")
    txtnew.write('%s' % str(line))
txtnew.close()

f.close()
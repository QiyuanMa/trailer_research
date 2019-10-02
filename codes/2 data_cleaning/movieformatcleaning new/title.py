f = open("title_all.txt", "r")
lines = f.readlines()
new_lines = []
i = 0
title = []
test = []

for line in lines:
    for i in range(len(line)):
        if line[i]!='(':
            test.append(line[i])
        else:
            title.append(''.join(test))
            break
print(title)


strlist = "\n".join(title)
txtnew = open("new_title.txt", "w", encoding="utf8")
txtnew.write(strlist)
txtnew.close()

f.close()

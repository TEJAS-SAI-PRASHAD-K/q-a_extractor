with open( r"q-a_extractor/file.txt", 'r') as r, open(r'q-a_extractor/output.txt', 'w') as o: 
    for line in r: 
        if line.strip(): 
            o.write(line) 
r.close()
f = open(r"q-a_extractor/output.txt", "r")

x=f.readlines()
lst=[]
for i in x:
    lst.append(i.rstrip())
for j in lst:
    if j=="Correct" or j=="Mark 1.00 out of 1.00" or j=="Flag question" or j=="Incorrect" or j=="Mark 0.00 out of 1.00" or j=="""Mark 1.00 out of 1.00
""" or """Flag question
""" or """Correct
""" or """Incorrect
""" or """Mark 0.00 out of 1.00
""" or """Remove flag
""" or """
Mark 1.00 out of 1.00
""" or """
Mark 0.00 out of 1.00
""" or """
Mark 1.00 out of 1.00""":
        lst.remove(j)
print(lst)

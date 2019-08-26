name = input("Enter file:")
list_mail=list()
counts=dict()
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line=line.rstrip()
    wds=line.split()
    if len(wds)<3 or wds[0] !='From':
        continue
    list_mail.append(wds[1])
for word in list_mail:
    counts[word]=counts.get(word,0)+1
#print(counts)
bigmail=None
bigcount=None
for mail,count in counts.items():
    if bigcount is None or count>bigcount:
        bigmail=mail
        bigcount=count
print(bigmail,bigcount)
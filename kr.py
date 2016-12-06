with open("t.txt", "r", encoding="utf-8") as f:
        part=f.readlines()
    #print (part)
end = []
for line in part:
    a = line.split("—")
    if len (a[0].split( ))<10:
        end.append (a[0])
for el in end:
    print (el)

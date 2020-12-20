n = int(input())
newfile = open("SinhVien9.txt","w+")
for i in range(n):
    mssv = input("mssv: ").title()
    hoten = input("Nhap ho ten: ").title()
    newfile.write(mssv+","+hoten+"\n")
mssv_del = input("mssv can xoa: ")
newfile.seek(0)
read = newfile.read().strip().split("\n")
for i in range (len(read)):
    if mssv_del in read[i]:
        read.pop(i)
        break
print(read)

f = open("SinhVien9.txt","w")
for i in read:
    f.write(i+'\n')
f.close()
        


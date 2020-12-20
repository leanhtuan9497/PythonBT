n = int(input())
newfile = open("SinhVien8.txt","w+")
for i in range(n):
    hoten = input("Nhap ho ten: ").title()
    newfile.write(hoten+"\n")

ten = input("Nhap ten can tim: ").lower()
newfile.seek(0)
read_ds = newfile.read().strip()
list = read_ds.split("\n")

for x in list:   
    if ten in x.lower().split(" ")[-1]:
        print(x)


#n = int(input())
#newfile = open("SinhVien8.txt","w+")
#for i in range(n):
#    hoten = input("Nhap ho ten: ").title()
#    newfile.write(hoten+"\n")
#newfile.close()
#ten = input("Nhap ten can tim: ").lower()
#f = open("SinhVien8.txt","r")
#for x in f:   
#    if(ten.lower in x.lower().split(" ")[-1]):
#        print(x.split(" ")[-1])

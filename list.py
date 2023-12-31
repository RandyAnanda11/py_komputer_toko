'deklarasi list'
data_angka =[1,2,3,4,5,6,7,8,9,10]
# data_string = ["ahmad","zaifa"]
# data_boolean = [True,False,True]
# data_campuran = [1.2, 50, "ahmad", True]
data_nama = ["jiah","mufidah", "malik","mustakhorroh", "insaf"]
nama = "alamaik"
# 'loop dalam list'
# list_dengan_loop = [i for i in range(5)]
# print (list_dengan_loop)

# 'loop dalam list dengan pengondisian dan operator'
# list_dengan_loop2 = [i**2 for i in range(1,10)]
# print (list_dengan_loop2)

# list_dengan_loop3 = [i for i in data_angka if i%2==0] 
# print(list_dengan_loop3)

# list_dengan_loop4 = [i for i in data_campuran if i!= False]
# print(list_dengan_loop4)


'manipulasi list : print elemen dalam list'
print(f"nama ke - 1 adalah = {data_nama[0]}" )
print(f"nama terakhir adalah = {data_nama[-1]}" )

'mengecek panjang suatu list' 
print(f"panjang dari list nama adalah = {len(data_nama)}")

'memasukan elemen baru kedalam list'
data_nama.insert(1,"marve")
print (f"data setelah diinput adalah = {data_nama}")
# jika ingin memasukan ke element yang terakhir 
data_nama.append("adam")
print (f"data setelah diappend adalah ={data_nama}")

'menghapus elemen dalam list'
data_nama.remove("mufidah") 
#jika ingin menghapus elemen paling terakhir dalam list 
data_nama.pop()
print (f"data setelah dipop dan remove adalah = {data_nama}")

'jika ingin sorting list'
data_nama.sort(key=len)
print(f"data nama yang telah di sort berdasarkan panjang nama = {data_nama}")

'meng-extend data list dengan suatu list baru'
data_nama_baru = ["labibah","masruah","mirwahah","rosyidahana"]
data_nama.extend(data_nama_baru)
print(f"data nama yang telah di sort berdasarkan panjang nama = {data_nama}")

'menghitung jumlah banyak nya suatu elemen dalam list'
jumlah_huruf = [nama.count('a') for nama in data_nama]
for i, nama in enumerate(data_nama):
    print(f"Jumlah huruf a dalam '{nama}' adalah {jumlah_huruf[i]}")

'membalik isi list denga reverse'
huruf_palindrom = "kasurrusak"
if huruf_palindrom == huruf_palindrom[::-1] : #maksud :: adalah [start,stop,step] yang artinya start dimulai dari indeks pertama, berakhir di indeks terakhir, dan stepnya -1 artinya mundur
    print ("HURUF MERUPAKAN POLINDROM")
else :
    print ("HURUF bukan polindrom")
    
'dengan method reverse membalik list'
data_angka.reverse()
print(f"data angka yang sudah di reverse adalah {data_angka}")
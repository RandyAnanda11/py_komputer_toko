'deklarasi list'
data_angka =[1,2,3,4,5,6,7,8,9,10]
data_string = ["ahmad","zaifa"]
data_boolean = [True,False,True]
data_campuran = [1.2, 50, "ahmad", True]
data_nama = ["jiah","mufidah", "malik", "insaf"]

'loop dalam list'
list_dengan_loop = [i for i in range(5)]
print (list_dengan_loop)

'loop dalam list dengan pengondisian dan operator'
list_dengan_loop2 = [i**2 for i in range(1,10)]
print (list_dengan_loop2)

list_dengan_loop3 = [i for i in data_angka if i%2==0] 
print(list_dengan_loop3)

list_dengan_loop4 = [i for i in data_campuran if i!= False]
print(list_dengan_loop4)


'manipulasi list : prin elemen dalam list'


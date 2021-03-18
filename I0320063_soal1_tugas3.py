Nama_Teman = ['Fagih','Raka','Alif','Ano','Rizal','Nauval','Ahnaf','Jefri','Rafli','Hasan']
print('Nama Teman_Semula:', Nama_Teman)
print ("Nama Teman[4]:", Nama_Teman[4])
print ("Nama Teman[6]:", Nama_Teman[6])
print ("Nama Teman[7]:", Nama_Teman[7])

Nama_Teman[3] = ('Akrom')
Nama_Teman[5] = ('Rara')
Nama_Teman[9] = ('Aji')
print('Nama Teman Setelah Diubah:', Nama_Teman)

Nama_Teman.append('Ilham')
Nama_Teman.append('Rian')
print('Nama Teman setelah ditambah:', Nama_Teman)
for i in Nama_Teman:
    print(i)
print('Panjang List:', len(Nama_Teman))



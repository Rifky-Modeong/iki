print(10*'=' +"PROGRAM PEMESANAN MAKANAN" +10*'=')
Menu = [{'nama': "Bakso", 'harga' : 15000, 'stok' : 9} ]
Keranjang = []

Menu.append({'nama': "Tinutuan", 'harga': 15000, 'stok': 9})
Menu.append({'nama': "Ikang Goreng", 'harga': 14000, 'stok': 11})
Menu.append({'nama': "Ayam Geprek", 'harga' : 17000, 'stok' : 7})
Menu.append({'nama' : "KFC", 'harga' : 25000, 'stok' : 8})

# Ba pesan dulu
Pesanan = str(input("Makanan yang ingin di pesan :"))
jumlah = int(input("Jumlah porsi :"))
for i in Menu:
    if i['nama'] == Pesanan and i['stok'] >= jumlah:

       Keranjang.append({'makanan': i, 'jumlah': jumlah})
       i['stok'] -= jumlah

       print(jumlah, Pesanan, "ditambahkan ke keranjang.")
       break

# Ini harganya brooo
harga = 0
for i in Keranjang:
    harga += i['makanan']['harga'] * i['jumlah']   
diskon = 20
harga_setelah_diskon = harga * (1 - diskon / 100)
print("harga setelah diskon: ", harga_setelah_diskon)

# Ini dpe pembayaran
uang = int(input("Uang anda :"))
if uang >= harga_setelah_diskon:
    kembalian = uang - harga_setelah_diskon
    print("Kembalian:", kembalian)
else:
    print("Uang anda tidak cukup")

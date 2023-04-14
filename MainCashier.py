"""
Ini merupakan program utama (MainCashier.py) kasir self-service sederhana yang dikonsep secara modular dengan basis Object Oriented Programming. 
Program ini dapat dijalankan setelah melakukan running aplikasi MainCashier.py di terminal
"""

"""
Import class Transaction dari file ModulCashier.py
"""
from ModulCashier import Transaction

"""
Inisialisasi instance trx dari class Transaction
"""
trx=Transaction()

"""
Menampilkan menu untuk pemilihan program
"""

print("Selamat Datang di Program Self Cashier.")
print("1. Menambahkan Item")
print("2. Mengubah Nama Item")
print("3. Mengubah Jumlah Item")
print("4. Mengubah Harga per Item")
print("5. Memeriksa Pembelian")
print("6. Menampilkan Pesanan pada Keranjang")
print("7. Menghapus Sebuah Item")
print("8. Menghapus Seluruh Item")
print("9. Menampilkan Total Bayar")
print("10. Mengakhiri Program")
menu=0
"""
Loop untuk merunning input hingga user mengakhiri prgram
"""
while menu!=10:
    """
    Upaya membuat clean code melalui minimalisir error penginputan
    """
    try :
        menu=int(input("Silakan Pilih Menu yang Ingin Dilakukan : "))
    except ValueError:
        print("Input Salah. Angka yang Dimasukkan Haruslah Integer dari 1-10")
        continue
    """
    Menu untuk memilih operasi yang ingin dilakukan, jika 
    menu=1 maka akan memasukkan nama item
    menu=2 akan mengganti nama item
    menu=3 akan mengganti jumlah item sesuai nama item
    menu=4 akan mengganti harga per item sesuai nama item
    menu=5 akan memverifikasi pemesanan
    menu=6 akan menampilkan isi pesanan sementara
    menu=7 akan menghapus sebuah item
    menu=8 akan menghapus semua item
    menu=9 akan menghitung harga total yang harus dibayarkan
    menu=10 akan keluar dari program
    """
    if menu==1 :
        nama=input("Masukkan Nama Item:  ")
        try:
            jumlah=int(input("Masukkan Jumlah Item:  "))
            harga=int(input("Masukkan Harga per Item:  "))
        except ValueError:
            print("Masukkan untuk jumlah dan harga per item haruslah integer")
        trx.add_item([nama,jumlah,harga])
        trx.summary()
    elif menu==2:
        nama_ubah=input("Masukkan Nama Item yang Ingin Diubah:  ")
        nama_baru=input("Masukkan Nama Baru:  ")
        trx.update_item_name(nama_ubah,nama_baru)
        trx.summary()
    elif menu==3:
        nama_ubah_2=input("Masukkan Nama Item yang Jumlahnya Ingin Diubah:  ")
        jumlah_baru=input("Masukkan Jumlah Item Baru:   ")
        trx.update_item_qty(nama_ubah_2,jumlah_baru)
        trx.summary()
    elif menu==4:
        nama_ubah_3=input("Masukkan Nama Item yang Harga per Itemnya Ingin Diubah:  ")
        harga_baru=input("Masukkan Harga per Item Baru:   ")
        trx.update_harga_item(nama_ubah_3,harga_baru)
        trx.summary()
    elif menu==5:
        trx.check_order()
    elif menu==6:
        trx.summary()
    elif menu==7:
        nama_hapus=input("Masukkan Nama Item yang Ingin Dihapus  : ")
        trx.delete_item(nama_hapus)
        trx.summary()
    elif menu==8:
        trx.reset_transaction()
    elif menu==9:
        trx.total_price()
    else:
        print("Input Salah. Angka yang Dimasukkan Haruslah Integer dari 1-10")
    

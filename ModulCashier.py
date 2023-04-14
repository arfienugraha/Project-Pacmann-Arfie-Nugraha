"""
Pembuatan kelas Transaction yang akan direfer selama proses transaksi
"""

class Transaction:
    """
    Inisialisasi dictionary tabel belanja yang akan menjadi wadah penampung nama item, jumlah item, harga item,  dan total pembelian
    """
    def __init__(self):
        self.tabel_belanja={}
    """
    Pembuatan method add_item yang ditujukan untuk menambahkan nama item, jumlah item, harga item dari untuk selanjutnya ditampung
    pada attributes tabel belanja
    """
    def add_item(self,item_list=[]):
        self.nama_item=item_list[0]
        self.jumlah_item=item_list[1]
        self.harga_per_item=item_list[2]
        self.tabel_belanja[self.nama_item]=(self.jumlah_item,self.harga_per_item)
        return self.tabel_belanja[self.nama_item]
    """
    Pembuatan method summary yang ditujukan untuk menampilkan resume keranjang belanja 
    """
    def summary(self):
        return print(f'Item yang dibeli adalah : {self.tabel_belanja}')
    
    """
    Pembuatan method update nama item yang ditujukan untuk mengubah nama item tanpa menghapus dan mengubah data yang lain
    """
        
    def update_item_name(self,nama_item,update_nama_item):
        self.update_nama_item=update_nama_item
        self.tabel_belanja[self.update_nama_item]=self.tabel_belanja[nama_item]
        del self.tabel_belanja[nama_item]
        
    """
    Pembuatan method update item quantity yang ditujukan untuk mengubah jumlah item tanpa menghapus dan mengubah data yang lain
    """
    
    def update_item_qty(self,nama_item,update_jumlah_item):
        self.update_jumlah_item=update_jumlah_item
        self.tabel_belanja.update({nama_item:self.update_jumlah_item})
    
    """
    Pembuatan method update harga item yang ditujukan untuk mengubah harga item tanpa menghapus dan mengubah data yang lain
    """
    
    def update_harga_item(self,nama_item,update_harga_item):
        self.update_harga_item=update_harga_item
        self.tabel_belanja.update({nama_item:self.update_harga_item})
    """
    Pembuatan method untuk menghapus key dan value dictionary berdasarkan inputan key dictionary
    """
        
    def delete_item(self,nama_item):
        del self.tabel_belanja[nama_item]
    
    """
    Pembuatan method untuk menghapus seluruh data yang ditampung pada attributes tabel_belanja
    """
    
    def reset_transaction(self):
        self.tabel_belanja.clear()
        print("Semua item berhasil di delete!")
        
    """
    Pembuatan method untuk memvalidasi input yang diberikan oleh user
    """
        
    def check_order(self):
        try:
            self.jumlah_item=int(self.jumlah_item)
            self.harga_per_item=int(self.harga_per_item)
            print ("Input yang anda masukkan sudah benar")
            print(self.tabel_belanja)
        except ValueError :
            return print("Input yang ada masukkan salah, silakan masukan jumlah item dan harga per item dalam integer")
        
    """
    Pembuatan method untuk menentukan diskon dan mengkalkulasi nominal yang perlu dibayarkan saat belanja
    """   
    def total_price(self):
        total=0
        for i in self.tabel_belanja:
            total+=(self.tabel_belanja.get(i)[0]*self.tabel_belanja.get(i)[1])
        if total>500_000 :
            total=total-(0.1*total)
            print("Selamat Anda Mendapatkan Diskon 10%")
        elif total>300_000:
            total=total-(0.08*total)
            print("Selamat Anda Mendapatkan Diskon 8%")
        elif total>200_000:
            total=total-(0.05*total)
            print("Selamat Anda Mendapatkan Diskon 5%")
        else:
            total=total
            print("Anda Tidak Mendapatkan Diskon, Tambah Lagi Belanjanya untuk Mendapatkan Diskon")
        return print(f'Total belanja yang harus dibayarkan adalah Rp.{total}')

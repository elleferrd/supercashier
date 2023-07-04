#import tabulate untuk mempermudah visualisasi check order
from tabulate import tabulate

data_id = []

class Transaksi:
    """Membuat kelas transaksi"""

    #Deklarasi atribut dan elemen
    def __init__(self,idtrans, item, jumlah, harga):
        self.idtrans = idtrans
        self.item = item
        self.jumlah = jumlah
        self.harga = harga
        
    #membuat database id transaksi
    data_id = data_id

    #Membuat tabel order 
    order = {
        "Item" : ["Item"],
          "Jumlah Item" : ["Jumlah Item"],
          "Harga/Item" : ["Harga/Item"],
          "Harga Total" : ["Harga Total"]
         }
    

    #Membuat ID transaksi, masukan nama anda
    def generate_id():
        ''' Membuat id transaksi yang unik 
        index transaksi akan terus bertambah dan disimpan dalam database
        '''
        index_transaksi = len(Transaksi.data_id) + 1
        idtrans = f"T_{index_transaksi}"
        print(f" T_{index_transaksi}")
        print(f' Silahkan ketik Transaksi.add_item("{idtrans}")')
        Transaksi.data_id.append(idtrans)
       
    #Membuat fungsi menambahkan item
    def add_item(idtrans):
        ''' Menambahkan item
        1) (customer) Pertama2 customer harus memasukan kode transaksi yang telah dibuat dengan fungsi generate_id.
        Jika kode tidak ada di database, maka customer diarahkan untuk mengisi kode yang benar
        2) (system + Customer) Kemudian akan ada pertanyaan apakah sudah memasukan seluruh items, lalu tulis Tidak
        3) (system + Customer) Kemudian customer disuruh masukan item, jumlah item (harus angka) & harga item (harus angka) yang dibeli 
        4) (system+ Customer) Setelah itu akan muncul summary pesanan (termasuk total harga normal)
        dan pertanyaan apakah belanjaan sudah dimasukan semuanya?, Jawaban dapat disesuaikan.
        Jika belum maka akan kembali ke poin nomor 3, jika sudah makan akan maju ke poin nomor 5
        5) (system + Customer) Lalu akan muncul pertanyaan apakah pesanan sudah benar? Jawaban bisa disesuaikan.
        Jika sudah maka akan ada perintah untuk cek harga yang harus dibayar.
        Jika belum, maka customer akan ditanyakan jenis kesalahan dan item yang salah, kemudian diarahkan untuk melakukan revisi sesuai kesalahannya
        
        (fungsi ini menggunakan 'input agar memudahkan customer untuk input data dan
        'while' sehingga memungkinkan customer untuk menambahkan belanjaannya tanpa harus keluar dari fungsi)
        '''
        if idtrans in data_id:
            #Membuat tabel order 
            _order = {
                "Item" : ["Item"],
                  "Jumlah Item" : ["Jumlah Item"],
                  "Harga/Item" : ["Harga/Item"],
                  "Harga Total" : ["Harga Total"]
                 }
        
            #Masukan belajaan (item, jumlah, harga)
            Selesai = input("Apakah anda sudah memasukan seluruh items belanja (Ya/Tidak): ")
            while Selesai == "Tidak":
                item = input("Masukan jenis item yang anda beli: ")
                try:
                    jumlah = int(input(f"Masukan jumlah {item} yang anda beli (angka) :"))
                    harga = int(input(f"Masukan harga satuan {item} yang anda beli (dalam angka, misalnya 10000) :"))
                    if isinstance(jumlah, int) and isinstance(harga, int):
                        hargatotal = jumlah * harga
                        _order["Item"].append(item)
                        _order["Jumlah Item"].append(jumlah)
                        _order["Harga/Item"].append(harga)
                        _order["Harga Total"].append(hargatotal)
                        print(tabulate(_order))
                        Selesai = input("Apakah anda sudah memasukan seluruh items belanja (Ya/Tidak): ")
                    else:
                        raise Exception
                except Exception as e:
                    print("Mohon masukan item kembali dengan harga&jumlah yang berupa angka saja tanpa titik dan koma ataupun mata uang pada jumlah dan harga")
                
            #Cek apakah sudah benar, jika belum maka akan diarahkan untuk melakukan revisi
            Check = input("Apakah seluruh belanjaan sudah benar (Ya/Tidak): ")
            if Check != "Ya":
                Check_Update = input("Apa yang salah (Item/Jumlah/Harga/Semua): ")
                Item_Salah = input(f"Item apa yang {Check_Update} nya salah: ")
                if Check_Update == "Item":
                    print(f'Silahkan Update Item dengan ketik "Transaksi.update_item_name("{Item_Salah}", "Item yang benar")')
                elif Check_Update == "Jumlah":
                    print(f'Silahkan Update Item dengan ketik "Transaksi.update_item_qty("{Item_Salah}", Jumlah yang benar)')
                elif Check_Update == "Harga":
                    print(f'Silahkan Update Item dengan ketik "Transaksi.update_item_price("{Item_Salah}", Harga yang benar)')    
                elif Check_Update == "Harga":
                    print(f'Silahkan Delete Item dengan ketik "Transaksi.delete_item("{Item_Salah}") atau ulangi add_item')

            else:
                print('Silahkan Checkout dengan ketik "Transaksi.total_price()')
            Transaksi.order = _order
        else:
            print("Error, Mohon maaf, kode transaksi belum sesuai, coba lagi!")


     #Membuat fungsi update name item
    def update_item_name(item, update_item):
        ''' melakukan update pada nama item
        1) (customer) memasukan nama item lama dan nama item baru yang ingin diubah
        2) (system) system akan mencari index dari item lama kemudian mengganti nya dengan item baru yang telah diinput oleh customer (looping)
        3) (system) system akan melakukan update pada dictionary tabel order dan melakukan print
        '''
        def rename_value_in_dict(dictionary, key, old_value, new_value):
            if key in dictionary:
                list_value = dictionary[key]
                if isinstance(list_value, list):
                    for i in range(len(list_value)):
                        if list_value[i] == old_value:
                            list_value[i] = new_value
        rename_value_in_dict(Transaksi.order, "Item", item, update_item)
        print(tabulate(Transaksi.order))

    #fungsi Update QTY
    def update_item_qty(item, update_qty):
        ''' melakukan update pada kuantitas
        1) (customer) memasukan nama item dan jumlah baru yang ingin diubah
        2) (system) system akan mencari index dari item lama kemudian mengganti jumlah item pada index tersebut (looping)
        3) (system) system akan melakukan update pada dictionary tabel order dan melakukan print
        '''
        def rename_value_in_dict(dictionary, key, key2, key3, key4, old_value, new_value):
            if key in dictionary:
                list_value = dictionary[key]
                list_value2 = dictionary[key2]
                list_value3 = dictionary[key3]
                list_value4 = dictionary[key4]
                if isinstance(list_value, list):
                    for i in range(len(list_value)):
                        if list_value[i] == old_value:
                            list_value2[i] = new_value
                            list_value4[i] = new_value * list_value3[i]
        rename_value_in_dict(Transaksi.order, "Item", "Jumlah Item", "Harga/Item", "Harga Total", item, update_qty)
        print(tabulate(Transaksi.order))
    
        

    #fungsi Update Harga
    def update_item_price(item, update_price):
        ''' melakukan update pada harga
        1) (customer) memasukan nama item dan harga baru yang ingin diubah
        2) (system) system akan mencari index dari item lama kemudian mengganti harga item pada index tersebut (looping)
        3) (system) system akan melakukan update pada dictionary tabel order dan melakukan print
        '''
        def rename_value_in_dict(dictionary, key, key2, key3, key4, old_value, new_value):
            if key in dictionary:
                list_value = dictionary[key]
                list_value2 = dictionary[key2]
                list_value3 = dictionary[key3]
                list_value4 = dictionary[key4]
                if isinstance(list_value, list):
                    for i in range(len(list_value)):
                        if list_value[i] == old_value:
                            list_value3[i] = new_value
                            list_value4[i] = new_value * list_value2[i]
        rename_value_in_dict(Transaksi.order, "Item", "Jumlah Item", "Harga/Item", "Harga Total", item, update_price)
        print(tabulate(Transaksi.order))
        
    #fungsi Delete Item
    def delete_item(item):
        ''' menghapus item
        1) (customer) memasukan nama item yang ingin dihapus
        2) (system) system akan mencari index dari item lama kemudian menghapus seluruh informasi terkait item tersebut (looping)
        3) (system) system akan melakukan update pada dictionary tabel order dan melakukan print
        '''
        def remove_value_in_dict(dictionary, key, key2, key3, key4, item):
            if key in dictionary:
                list_value = dictionary[key]
                list_value2 = dictionary[key2]
                list_value3 = dictionary[key3]
                list_value4 = dictionary[key4]
                if isinstance(list_value, list):
                    for i in range(len(list_value)):
                        if list_value[i] == item:
                            list_value[i] = "(data yang dihapus)"
                            list_value2[i] = ""
                            list_value3[i] = ""
                            list_value4[i] = ""
        remove_value_in_dict(Transaksi.order, "Item", "Jumlah Item", "Harga/Item", "Harga Total", item)
        print(tabulate(Transaksi.order))
        
    #fungsi reset
    def reset_transaction():
        ''' menghapus seluruh data dalam tabel order'''
        Transaksi.order.clear()
        Transaksi.order = {
        "Item" : ["Item"],
          "Jumlah Item" : ["Jumlah Item"],
          "Harga/Item" : ["Harga/Item"],
          "Harga Total" : ["Harga Total"]
         }
    
    #fungsi check order
    def check_order():
        ''' mengecek order
        1) Sistem akan mencari histori data yang telah dihapus dengan lookup kalimat (data yang dihapus) kemudian akan menghapus row tersebut
        2) Jika seluruh data telah terisi maka system akan mengeluarkan pesanan sudah benar, jika belum akan memberikan notifikasi terdapat kesalahan
        3) Kemudian sistem akan melakukan print daftar pesanan
        '''
        #hapus row jika ada data yang dihapus sebelumnya
        for i in range(len(Transaksi.order["Item"])):
            if Transaksi.order["Item"][i] == "(data yang dihapus)":
                del Transaksi.order["Item"][i]
                del Transaksi.order["Jumlah Item"][i]
                del Transaksi.order["Harga/Item"][i]
                del Transaksi.order["Harga Total"][i]
        check_blank = any(value == '' for value in Transaksi.order.values())
        if check_blank == False:
            print("Pesanan sudah benar")
        else:
            print("Terdapat kesalahan input data")
        #tambahkan nomor & hapus jika data yang dihapus)
        print(tabulate(Transaksi.order))
        
    #fungsi bill
    def total_price():
        ''' menghitung jumlah harga yang harus dibayar
        1) System Menghapus data-data yang tidak penting dari dictionary (menghilangkan string agar dapat di sum)
        2) System melakukan perhitungan jumlah harga normal
        3) System melakukan perhitungan harga setelah diskon
        4) System melakukan print harga yang harus dibayar
            '''
        total = 0
        unpacked_list = [*Transaksi.order["Harga Total"]]
        unpacked_list.remove("Harga Total")
        result = sum(unpacked_list)
        if result >500000:
            bill = result * 0.9
        elif result > 300000:
            bill = result * 0.92
        elif result > 200000:
            bill = result * 0.95
        else:
            bill = result
        return bill
              
        
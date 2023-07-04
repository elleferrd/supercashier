# supercashier

# Latar Belakang (Tujuan)
Tujuan dari paper ini adalah untuk mengembangkan skrip untuk fitur kasir self service. Sebagai tambahan, paper ini juga memuat penjelasan terkait skrip yang digunakan. 

#  Requirement
Pada fitur tersebut, pelanggan dapat membuat id transaksi, memasukan, update dan menghapus jenis, jumlah dan harga barang yang dibeli. Kemudian program tersebut akan mengeluarkan summary pesananan dan harga yang harus dibayarkan (dengan mempertimbangkan diskon). 
Berikut adalah requirement yang diperlukan untuk membuat program kasir self service. Namun, perlu diperhatikan bahwa sebelum menjalankan program perlu dilakukan import tabulate untuk menunjukkan rangkuman pesanan.

Berikut adalah requirement variabel:
1. Transaksi (Class), Input: -, Output: list database (data_id)
2. generate_id (Method in class), Input: -, Output: ID Transaksi
3. add_item (Method in class), Input:, id transaksi, item, jumlah, harga, Output: dict order
4. update_item_name (Method in class), Input: nama item, update item, Output: dict order (updated)
5. update_item_qty (Method in class), Input: nama item, update kuantitas, Output: dict order (updated)
6. pdate_item_price (Method in class), Input: nama item, update harga, Output: dict order (updated)
7. delete_item (Method in class), Input: nama item, Output: dict order (updated)
8. reset_transaction (Method in class), Input: -, Output: dict order kosongan 
9. check_order (Method in class), Input: -, Output: pesan (benar/salah), summary transaksi
10. total_price (Method in class), Input: -, Output: harga yang harus dibayarkan setelah dikurani diskon (if applicable)

# Flowchart
Alur penggunaan program kasir self service adalah sebagai berikut:
1. Customer membuat id transaksi. Transaksi.generate_id()
2. Customer memasukan belanjaan dengan id transaksi yang telah dibuat sebelumnya. Transaksi.add_item("<id transaksi>")
3. Customer dapat mengecek pesanan, jika sudah sesuai dapat cek jumlah bayar. Transaksi.check_order()
4. (Optional) Namun, jika pesanan belum sesuai dapat melakukan perbaikan yaitu berupa reset transaksi, hapus item atau melakukan update baik untuk item, jumlah, maupun harga. Transaksi.reset_transaction() / Transaksi.delete_item("<item yang akan dihapus>") / Transaksi.update_item_Name("<item lama>", "<item baru>") / Transaksi.update_item_qty("<nama item>", <kuantitas baru>) / Transaksi.update_item_price("<nama item>", <harga baru>)
5. Custumer cek harga akhir setelah dikurangi diskon (jika ada). Transaksi.total_price()

# Penjelasan kode

Pertama-tama import tabulate dan membuat kelas transaksi yang berisi atribut idtrans item, jumlah, harga. Kemudian buatlah database id transaksi dan tabel order

    #Membuat kelas transaksi & Deklarasi atribut dan elemen
    class Transaksi:
      def __init__(self,idtrans, item, jumlah, harga):
          self.idtrans = idtrans
          self.item = item
          self.jumlah = jumlah
          self.harga = harga
          
      #membuat database id transaksi
      data_id = [] 
  
      #Membuat tabel order 
      order = {
          "Item" : ["Item"],
            "Jumlah Item" : ["Jumlah Item"],
            "Harga/Item" : ["Harga/Item"],
            "Harga Total" : ["Harga Total"]
           }
      
Kemudian, Membuat id transaksi yang unik, dimana index transaksi akan terus bertambah dan disimpan dalam database

  
      #Membuat ID transaksi
      def generate_id():
          index_transaksi = len(Transaksi.data_id) + 1
          idtrans = f"T_{index_transaksi}"
          print(f" T_{index_transaksi}")
          print(f' Silahkan ketik Transaksi.add_item("{idtrans}")')
          Transaksi.data_id.append(idtrans)

Langkah selanjutnya adalah membahkan item, dengan langkah sebagai berikut:
1) (customer) Pertama2 customer harus memasukan kode transaksi yang telah dibuat dengan fungsi generate_id.  Jika kode tidak ada di database, maka customer diarahkan untuk mengisi kode yang benar
2) (system + Customer) Kemudian akan ada pertanyaan apakah sudah memasukan seluruh items, lalu tulis Tidak
3)  (system + Customer) Kemudian customer disuruh masukan item, jumlah item (harus angka) & harga item (harus angka) yang dibeli
4)  (system+ Customer) Setelah itu akan muncul summary pesanan (termasuk total harga normal) d an pertanyaan apakah belanjaan sudah dimasukan semuanya?, Jawaban dapat disesuaikan.  ika belum maka akan kembali ke poin nomor 3, jika sudah makan akan maju ke poin nomor 5
5)  ( system + Customer) Lalu akan muncul pertanyaan apakah pesanan sudah benar? Jawaban bisa disesuaikan. Jika sudah maka akan ada perintah untuk cek harga yang harus dibayar. Jika belum, maka customer akan ditanyakan jenis kesalahan dan item yang salah, kemudian diarahkan untuk melakukan revisi sesuai kesalahannya

 (fungsi ini menggunakan 'input agar memudahkan customer untuk input data dan 'while' sehingga memungkinkan customer untuk menambahkan belanjaannya tanpa harus keluar dari fungsi)

        #Menambahkan item
          def add_item(idtrans):
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

Jika terdapat kesalahan input, customer dapat melakukan update nama item, jumlah atau harga, hapus item maupun reset transaksi, dengan fungsi sebagai berikut:

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

Selain dari itu customer dapat melakukan cek order kembali dengan fungsi check_order

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

Langkah terakhir, customer dapat mencari jumlah yang harus dibayarkan setelah dipotong diskon (jika ada) dengan fungsi total_price
              
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

# Test Case

![test case1](https://github.com/elleferrd/supercashier/assets/137087598/7aae007c-1884-455a-9337-e3ddbfca5657)
![test case 2](https://github.com/elleferrd/supercashier/assets/137087598/3a87ae55-9fb9-4aa0-a323-7592c9bc4393)
![test case 3](https://github.com/elleferrd/supercashier/assets/137087598/de61b85d-ad93-4dc9-849d-57fac8e0287d)

# Conclusion & Future Work

Dari program kasir self service yang telah dibuat customer dapat membuat id transaksi, memasukan belanjaannya (item, jumlah, harga), menghapus, reset transaksi, ataupun update item/jumlah/harga barang yang dibeli, melakukan cek pesanan, serta cek harga yang perlu dibayar. Pada saat yang sama, sistem melakukan penyimpanan kode transaksi yang pernah dikeluarkan dan melakukan perhitungan diskon untuk transaksi dengan minimal belanja tertentu.

Jika memiliki waktu lebih/SDM lebih banyak, terdapat beberapa hal yang dapat di improve pada program tersebut, yaitu
1. Menggunakan lebih banyak try except untuk memudahkan customer jika terjadi kesalahan input
2. Fitur penyimpanan data transaksi per transaksi id & pemangilan fungsi lainnya berdasarkan transaksi id tersebut. Jika perlu, dengan nama & nomor member customer. Sehingga, data tesebut nantinya dapat digunakan sebagai input dari marketing analytics untuk menentukan strategi dan taktik marketing.

# Lampiran (Kode Modular)
        #import kasir
        from kasir import Transaksi
        
        #generate id
        kasir.Transaksi.generate_id()
        
        #add item
        Transaksi.add_item("<id transaksi>")
        
        #update item 
        Transaksi.update_item_name("<item yang ingin diupdate>", "<item yang akan diupdate>")
        
        #update jumlah item
        Transaksi.update_item_qty("<item yang ingin diupdate>", <jumlah item>)
        
        #update harga item
        Transaksi.update_item_price("<item yang ingin diupdate>", <harga item>)
        
        #delete item
        Transaksi.delete_item("<item yang ingin diupdate>")
        
        #reset transaction
        Transaksi.reset_transaction()
        
        #check transaction
        Transaksi.check_order()

        #check price
        Transaksi.total_price()

from koordinat import *
import mysql.connector
import os

import locale
locale.setlocale(locale.LC_ALL,'')
'en_US.utf8'
def transaksi():
    #Variable koneksi ke database
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dbpersediaan"
    ) 
    
    mycursor = db.cursor()
    #proses pengisisan data berulang-ulang selama Ya
    lagi = "Y"
    while lagi.upper() !="T":
        os.system('cls')
        myCenter(2, "Transaksi Pembelian Barang") #baris kedua cetak ditengah
        gotoxy(13,4, "No. Faktur   : ")
        gotoxy(1,5,"Tgl. Faktur [yyyy-mm-dd] : " )
        gotoxy(60,4,"Kode Suplier : ")
        gotoxy(60,5,"Nama Suplier : ")
        #gotoxy untuk menentukan posisi ditulisnya
        ketemu =True
        while ketemu:
            nofak = myInput(27,4,"")
            sql = "Select * from tblbeli where nofak="+"'"+nofak+"'"
            mycursor.execute(sql)
            myresult=mycursor.fetchone()
            if myresult != None:
                pesan = "Nomor Faktur sudah digunakan"
                gotoxy(27,4,pesan)
                input()
                gotoxy(27,4," "*len(pesan))
            else:
                ketemu=False
        tglfak = myInput(27,5,"")
    
        ketemu =False 
        while not ketemu:
            kdsup = myInput(76,4,"")
            sql = "Select * from tblsuplier where kodesup="+"'"+kdsup+"'"
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            if myresult == None:
                pesan="Suplier tidak ditemukan"
                gotoxy(76,4,pesan)#mengatur letak pesan pada kolom
                input()
                gotoxy(76,4," "*len(pesan))#mengganti pesan dengan kosong
            else:
                ketemu =True    
        #Menampilkan data suplier
        nmsup =myresult[1]
        gotoxy(76,5,nmsup)
    
        hline = "-"*95
        gotoxy(1,6,hline)
        gotoxy(5, 7," No    Kode        Nama        Stok     Harga      Jumlah      Total")
        gotoxy(5, 8,"       Barang      Barang      Barang   Beli       Beli        Harga")
        gotoxy(1, 9,hline)
    
        no=1
        brs=10
        totitem=0
        totbayar=0
        kdbrg="tidak kosong"
        while kdbrg !="":
            gotoxy(5,brs,str(no))
            kdbrg=myInput(10,brs,"")
        
            if kdbrg=="":break
            sql="SELECT * FROM tblBarang WHERE kd_barang="+"'"+kdbrg+"'"
            mycursor.execute(sql)
            databrg=mycursor.fetchone()
        
            if databrg ==None:
                pesan="Kode %s Tidak Ditemukan"%kdbrg
                gotoxy(5,brs+1,pesan)
                input()
                gotoxy(5,brs+1," "*len(pesan))
            else:
                nmbrg = databrg[1]
                stok =databrg[4]
            
                gotoxy(20,brs,nmbrg)
                gotoxy(34,brs,str(stok))
                hrgbeli = int(myInput(40,brs,""))
                gotoxy(40,brs,"{:12n}".format(hrgbeli))
                jmlbeli = int(myInput(55,brs,""))
                gotoxy(55,brs,"{:6n}".format(jmlbeli))
            
                tothrg=hrgbeli*jmlbeli
                gotoxy(66,brs,"{:12n}".format(tothrg))
            
                no += 1
                brs += 1
                totitem = totitem +jmlbeli    
                totbayar = totbayar +tothrg
            
                #simpan ke tabel detail beli
                sql="INSERT INTO tbldetailbeli VALUES (%s,%s,%s)"
                val=(nofak, kdbrg, jmlbeli)
                mycursor.execute(sql,val)
                db.commit()
            
                #update data stok ditabel barang
                sql="UPDATE tblbarang SET stok = %s WHERE kd_barang=%s"
                val=(stok+jmlbeli, kdbrg)
                mycursor.execute(sql,val)
                db.commit()
            
            #Simpan ke tabl beli
        sql="INSERT INTO tblbeli VALUES (%s, %s,%s,%s,%s)"
        val=(nofak, tglfak, kdsup, totitem, totbayar)
        mycursor.execute(sql,val)
        db.commit()
    
        gotoxy(1,brs,hline)
    
        gotoxy(55,brs+1,"{:6n}".format(totitem))
        gotoxy(66,brs+1,"{:12n}".format(totbayar))
        gotoxy(1,brs+2,hline)
    
        lagi=myInput(5,brs+3,"Ada Faktur lagi [Y/T] : ")
    
        
        
    
    
     
            
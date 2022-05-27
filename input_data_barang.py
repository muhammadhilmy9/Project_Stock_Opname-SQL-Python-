from koordinat import *
import mysql.connector
import os

def barang():
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dbpersediaan"
    ) 
    mycursor = db.cursor()

    os.system('cls')
    hline = '-'*40
    myCenter(2, "INPUT DATA BARANG")
    gotoxy(30,3,hline)
    gotoxy(30,4,"Kode Barang    : ")
    gotoxy(30,5,"Nama Barang    : ")
    gotoxy(30,6,"Satuan         : ")
    gotoxy(30,7,"Harga Barang   : ")
    gotoxy(30,8,"Stok Barang    : ")
    gotoxy(30,9,hline)
    kdbrg = myInput(47,4,"")
    nmbrg = myInput(47,5,"")
    satuan=myInput(47,6,"")
    harga=myInput(47,7,"")
    stok=myInput(47,8,"")

    sql="INSERT INTO tblbarang VALUES (%s, %s, %s,%s,%s)"
    val = (kdbrg, nmbrg, satuan, harga, stok)
    mycursor.execute(sql, val)
    db.commit() #Menyimpan transaksi di sql secara permanen

    pesan = "Data Barang Berhasil di Simpan"
    gotoxy(35, 10, pesan)



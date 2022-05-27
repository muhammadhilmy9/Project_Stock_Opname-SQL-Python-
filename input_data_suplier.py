from koordinat import *
import mysql.connector
import os

def suplier():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="dbpersediaan"
    ) 
    if db.is_connected():
        print("Berhasil terhubung ke server MySQL")
    
    mycursor = db.cursor()

    os.system('cls')
    hline = '-'*40
    myCenter(2, "INPUT DATA SUPLIER")
    gotoxy(30,3,hline)
    gotoxy(30,4,"Kode Suplier    : ")
    gotoxy(30,5,"Nama Suplier    : ")
    gotoxy(30,6,"Alamat          : ")
    gotoxy(30,7,"Nomor Telpon    : ")
    gotoxy(30,8,hline)
    kd = myInput(47,4,"")
    nm = myInput(47,5,"")
    almt=myInput(47,6,"")
    tlp=myInput(47,7,"")

    sql="INSERT INTO tblsuplier VALUES (%s, %s, %s,%s)"
    val = (kd, nm, almt, tlp)
    mycursor.execute(sql, val)
    db.commit()

    pesan = "Data Suplier Berhasil di Simpan"
    gotoxy(35, 10, pesan)

import input_data_barang as brg
import transaksi_beli as trb
import input_data_suplier as ids
from koordinat import *
import mysql.connector
import os

import locale
locale.setlocale(locale.LC_ALL,'')
'en_US.utf8'

def input_sup():
    ids.suplier()
def input_brg():
    brg.barang()
def input_transaksi():
    trb.transaksi()

lagi = "T" #

while lagi.upper() != "Y":
    os.system('cls')
    hline="-"*40
    myCenter(2,"MENU UTAMA")
    gotoxy(30,3,hline)
    gotoxy(30,4,"1. Input Data Supplier")
    gotoxy(30,5,"2. Input Data Barang")
    gotoxy(30,6,"3. Transaksi Pembelian")
    gotoxy(30,7,hline)
    gotoxy(30,9,"Pilihan Anda [1/2/3] : ")
    pil =int(myInput(52,9,""))
    if pil== 1:
        input_sup()
    elif pil== 2:
        input_brg()
    else:
        input_transaksi()
    
    lagi =input("Keluar Aplikasi?? [Y/T] :")
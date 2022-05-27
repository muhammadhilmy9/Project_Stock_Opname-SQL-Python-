#Fungsi cetak pada koordinat kolom, baris tertentu

#Fungsi goto x,y
def gotoxy(x=0, y=0, user_string="Teks Default"):
    x=int(x)
    y=int(y)
    if x >= 255: x=255
    if y >= 255: y=255
    if x <= 0: x=0
    if y <= 0: y=0
    HORIZ= str(x)
    VERT= str(y)
    #Plot user_string pada posisi HORIZ, VERT posisi pencetakan 
    print("\033["+VERT+";"+HORIZ+"f"+user_string)

#fungsi untuk menentukan posisi input data
def myInput(x=0, y=0, user_string="Teks Default"):
    x=int(x)
    y=int(y)
    if x >= 255: x=255
    if y >= 255: y=255
    if x <= 0: x=0
    if y <= 0: y=0
    HORIZ= str(x)
    VERT= str(y)
    #Plot user_string pada posisi HORIZ, VERT
    teks=input("\033["+VERT+";"+HORIZ+"f"+user_string)
    return teks

#posisi baris dan teks
def myCenter(brs,teks):
    kolcenter = (100-len(teks))/2
    gotoxy(kolcenter,brs,teks)
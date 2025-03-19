import time
import sys

def typing(text, delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def luas_persegi():
    print('(!)Rumus luas persegi = sisi x sisi')
    Input_user = int(input('Masukkan sisi>> '))
    hasil = Input_user ** 2
    print('Menghitung.....')
    time.sleep(1.3)
    typing('\n L.persegi = sisi x sisi', delay=.06)
    typing(f'           = {Input_user} x {Input_user}',delay=.06)
    typing(f'           = {hasil} cm²', delay=.06)
    typing(f'           = Jadi luas persegi adalah {hasil} cm²', delay=.06)
    return hasil

def volume_persegi():
    print('(!)Rumus volume persegi = sisi x sisi x sisi') 
    Input_user = int(input('Masukkan sisi persegi>> '))
    hasil = Input_user ** 3
    print('Menghitung.....')
    time.sleep(1.3)
    typing('\n V.persegi = sisi x sisi x sisi', delay=.06)
    typing(f'           = {Input_user} x {Input_user} x {Input_user}', delay=.06)
    typing(f'           = {hasil} cm³',delay=.06)
    typing(f'           = Jadi volume persegi adalah {hasil} cm³', delay=.06)
    return hasil

def persegi():
    print('\n========================')
    print('         PERSEGI        ')
    print('========================\n')
    print('Pilih salah satu opsi dibawah:')
    print('1.Luas persegi')
    print('2.Volume persegi')
    print('3.keluar')
    Input_ussr = int(input('Masukkan pilihan>> '))
    if Input_ussr == 1:
        luas_persegi()
    elif Input_ussr == 2:
        volume_persegi()
    elif Input_ussr == 3:
        main()
    else:
        print("(!)Input yang anda masukkan tidak valid!!!")

def luas_kubus():
    print('(!)Rumus luas kubus = 6 x sisi²')
    Input_user = int(input('Masukkan sisi kubus>> '))
    hasil = 6 * Input_user * Input_user
    print('Menghitung.....')
    time.sleep(1.3)
    typing('\n L.kubus = 6 x s x s', delay=.06)
    typing(f'           = 6 x {Input_user} x {Input_user}',delay=.06)
    typing(f'           = {hasil} cm²', delay=.06)
    typing(f'           = Jadi luas kubus adalah {hasil} cm²', delay=.06)
    return hasil

def volume_kubus():
    print('(!)Rumus volume kubus = s³')
    Input_user = int(input('Masukkan sisi kubus>> '))
    hasil =  Input_user ** 3
    print('Menghitung.....')
    time.sleep(1.3)
    typing('\n V.kubus = sisi x sisi x sisi', delay=.06)
    typing(f'           = {Input_user} x {Input_user} x {Input_user}', delay=.06)
    typing(f'           = {hasil} cm³',delay=.06)
    typing(f'           = Jadi volume kubus adalah {hasil} cm³', delay=.06)
    return hasil

def kubus():
    print('\n========================')
    print('         KUBUS        ')
    print('========================\n')
    print('Pilih salah satu opsi dibawah:') 
    print('1.Luas kubus')
    print('2.Volume kubus')
    print('3.keluar')
    Input_ussr = int(input('Masukkan pilihan>> '))
    if Input_ussr == 1:
        luas_kubus()
    elif Input_ussr == 2:
        volume_kubus()
    elif Input_ussr == 3:
        main()
    else:
        print("(!)Input yang anda masukkan tidak valid!!!")

def keliling_lingkaran():
    print('(!)Rumus keliling lingkaran: 2 x π x r')
    Input_user = int(input('Masukkan jari-jari lingkaran>> '))
    hasil = 2 * 3.14 * Input_user
    print('Menghitung.....')
    time.sleep(1.3)
    typing('\n K.lingkaran = 2 x π x r', delay=.06)
    typing(f'             = 2 x {3.14} x {Input_user}', delay=.06)
    typing(f'             = {hasil} cm',delay=.06)
    typing(f'             = Jadi keliling lingkaran adalah {hasil} cm', delay=.06)
    return hasil

def luas_lingkaran():
    print('(!)Rumus luas lingkaran = π x r x r')
    Input_user = int(input('Masukkan jari-jari lingkaran>> '))
    hasil = 3.14 * Input_user * Input_user
    print('Menghitung.....')
    time.sleep(1.3)
    typing('\n L.lingkaran = π x r x r', delay=.06)
    typing(f'             = {3.14} x {Input_user} x {Input_user}',delay=.06)
    typing(f'             = {hasil} cm²', delay=.06)
    typing(f'             = Jadi luas lingkaran adalah {hasil} cm²', delay=.06)
    return hasil

def lingkaran():
    print('\n========================')
    print('         LINGKARAN      ')
    print('========================\n')
    print('Pilih salah satu opsi dibawah:')
    print('1.Keliling lingkaran')
    print('2.Luas lingkaran')
    print('3.keluar')
    Input_ussr = int(input('Masukkan pilihan>> '))
    if Input_ussr == 1:
        keliling_lingkaran()
    elif Input_ussr == 2:
        luas_lingkaran()
    elif Input_ussr == 3:
        main()
    else:
        print('(!)Input yang anda masukkan tidak valid!!!')

def keliling_persegiPanjang():
    print('(!)Rumus keliling persegi panjang = 2 x (panjang + lebar)')
    Input_user_panjang = int(input('Masukkan panjang persegi panjang>> '))
    Input_user_lebar = int(input('Masukkan lebar persegi panjang>> '))
    hasil = 2 * (Input_user_panjang + Input_user_lebar)
    print('Menghitung.....')
    time.sleep(1.3)
    typing('\n K.persegi panjang = 2 x (panjang + lebar)', delay=.06)
    typing(f'                   = 2 x ({Input_user_panjang} + {Input_user_lebar})', delay=.06)
    typing(f'                   = {hasil} cm',delay=.06)
    typing(f'                   = Jadi keliling persegi panjang adalah {hasil} cm', delay=.06)
    return hasil

def luas_pesegiPanjang():
    print('(!)Rumus luas persegi panjang = panjang x lebar')
    Input_user_panjang = int(input('Masukkan panjang persegi panjang>> '))
    Input_user_lebar = int(input('Masukkan lebar persegi panjang>> '))
    hasil = Input_user_panjang * Input_user_lebar
    print('Menghitung.....')
    time.sleep(1.3)
    typing('\n L.persegi panjang = panjang x lebar', delay=.06)
    typing(f'                   = {Input_user_panjang} x {Input_user_lebar}',delay=.06)
    typing(f'                   = {hasil} cm²', delay=.06)
    typing(f'                   = Jadi luas persegi panjang adalah {hasil} cm²', delay=.06)
    return hasil

def persegi_panjang():
    print('\n=======================')
    print('         Lingkaran')
    print('=======================')
    print('Pilih salah satu opsi dibawah:')
    print('1.Keliling persegi panjang')
    print('2.Luas persegi panjang')
    print('3.keluar')
    Input_User = int(input('Masukkan pilihan anda>> '))
    if Input_User == 1:
        keliling_persegiPanjang()
    elif Input_User == 2:
        luas_pesegiPanjang()
    elif Input_User == 3:
        main()
    else:
        print('(!)Input yang anda masukkan tidak vallid!!!')

def keliling_segitiga():
    print('(!)Rumus keliling segitiga: a + b + c')
    Input_user_a = int(input('Masukkan a>> '))
    Input_user_b = int(input('Masukkan b>> '))  
    Input_user_c = int(input('Masukkan c>> '))
    hasil = Input_user_a + Input_user_b + Input_user_c
    print('Menghitung.....')
    time.sleep(1.3)
    typing('\n K.segitiga = a + b + c', delay=.06)
    typing(f'            = {Input_user_a} + {Input_user_b} + {Input_user_c}', delay=.06)
    typing(f'            = {hasil} cm',delay=.06)
    typing(f'            = Jadi keliling segitiga adalah {hasil} cm', delay=.06)
    return hasil

def luas_segitiga():
    print('(!)Rumus luas segitiga = 1/2 x a')
    Input_user_a = int(input('Masukkan a>>'))
    hasil = 1/2 * Input_user_a
    print('Menghitung.....')
    time.sleep(1.3)
    typing('\n L.segitiga = 1/2 x a', delay=.06)
    typing(f'            = 1/2 x {Input_user_a}',delay=.06)
    typing(f'            = {hasil} cm²', delay=.06)
    typing(f'            = Jadi luas segitiga adalah {hasil} cm²', delay=.06)
    return hasil

def segitiga():
    print('\n=======================')
    print('        Segitiga')
    print('=======================')
    print('Pilih salah satu opsi dibawah:')
    print('1.Keliling segitiga')
    print('2.Luas segitiga')
    print('3.keluar')
    Input_User = int(input('Masukkan pilihan anda>> '))
    if Input_User == 1:
        keliling_segitiga()
    elif Input_User == 2:
        luas_segitiga()
    elif Input_User == 3:
        main()
    else:
        print('(!)Input yang anda masukkan tidak vallid!!!')

def luas_limas_segitiga():
    print('(!)Rumus luas limas segitiga= luas alas + jumlah luas sisi tegak')
    Input_L_alas = int(input('Masukkan luas alas>> '))
    Input_L_sisi_tegak = int(input('Masukkan luas sisi tegak>> '))
    hasil = Input_L_alas + Input_L_sisi_tegak
    print('Menghitung.....')
    time.sleep(1.3)
    typing('\n L.limas segitiga = luas alas + jumlah luas sisi tegak', delay=.06)
    typing(f'                  = {Input_L_alas} + {Input_L_sisi_tegak}',delay=.06)
    typing(f'                  = {hasil} cm²', delay=.06)
    typing(f'                  = Jadi luas limas segitiga adalah {hasil} cm²', delay=.06)
    return hasil

def volume_limas_segitiga():
    print('(!)Rumus volume limas segitiga = 1/3 x luas alas x tinggi')
    Input_luas_alas = int(input('Masukkan luas alas>> '))
    Input_tinggi = int(input('Masukkan tinggi>> '))
    hasil = 1/3 * Input_luas_alas * Input_tinggi
    print('Menghitung.....')
    time.sleep(1.3)
    typing('\n V.limas segitiga = 1/3 x luas alas x tinggi', delay=.06)
    typing(f'                  = 1/3 x {Input_luas_alas} x {Input_tinggi}', delay=.06)
    typing(f'                  = {hasil} cm³',delay=.06)
    typing(f'                  = Jadi volume limas segitiga adalah {hasil} cm³', delay=.06)
    return hasil

def limas_segitiga():
    print('\n=======================')
    print('     Limas Segitiga')
    print('=======================')
    print('Pilih salah satu opsi dibawah ini:')
    print('1.Luas limas segitiga')
    print('2.Volume limas segitiga')
    print('3.Keluar')
    Input_ussr = int(input('Masukkan pilihan anda>> '))
    
    if Input_ussr == 1:
        luas_limas_segitiga()
    elif Input_ussr == 2:
        volume_limas_segitiga()
    elif Input_ussr == 3:
        main()
    else:
        print('Input yang anda masukkan tidak valid!!!')

def keliling_balok():
    print('(!)Rumus keliling balok = 4 x (panjang + lebar + tinggi)')
    Input_panjang = int(input('Masukkan panjang>> '))
    Input_lebar = int(input('Masukkkan lebar>> '))
    Input_tinggi = int(input('Masukkan tinggi>> '))
    hasil = 4 * (Input_panjang + Input_lebar + Input_tinggi)
    print('Menghitung.....')
    time.sleep(1.3)
    typing('\n K.balok = 4 x (panjang + lebar + tinggi)', delay=.06)
    typing(f'         = 4 x {Input_panjang} + {Input_lebar} + {Input_tinggi}', delay=.06)
    typing(f'         = {hasil} cm',delay=.06)
    typing(f'         = Jadi keliling balok adalah {hasil} cm', delay=.06)
    return hasil

def luas_permukaan_balok():
    print('(!)Rumus luas balok = 2 x (panjang x lebar + panjang x tinggi + lebar x tinggi)')
    Input_panjang = int(input('Masukkan panjang>> '))
    Input_lebar = int(input('Masukkkan lebar>> '))
    Input_tinggi = int(input('Masukkan tinggi>> '))
    hasil = 2 * ((Input_panjang * Input_lebar) + (Input_panjang * Input_tinggi) + (Input_lebar * Input_tinggi))
    print('Menghitung.....')
    time.sleep(1.3)
    typing('\n L.permukaan balok = 2 x (panjang x lebar + panjang x tinggi + lebar x tinggi)', delay=.06)
    typing(f'                   = 2 x ({Input_panjang} x {Input_lebar} + {Input_panjang} x {Input_tinggi} + {Input_lebar} x {Input_tinggi})',delay=.06)
    typing(f'                   = {hasil} cm²', delay=.06)
    typing(f'                   = Jadi luas permukaan balok adalah {hasil} cm²', delay=.06)
    return hasil

def volume_balok():
    print('(!)Rumus volume balok = p x l x t')
    Input_panjang = int(input('Masukkan panjang>> '))
    Input_lebar = int(input('Masukkkan lebar>> '))
    Input_tinggi = int(input('Masukkan tinggi>> '))
    hasil = Input_panjang * Input_lebar * Input_tinggi
    print('Menghitung.....')
    time.sleep(1.3)
    typing('\n V.balok = panjang x lebar x tinggi', delay=.06)
    typing(f'         = {Input_panjang} x {Input_lebar} x {Input_tinggi}', delay=.06)
    typing(f'         = {hasil} cm³',delay=.06)
    typing(f'         = Jadi volume balok adalah {hasil} cm³', delay=.06)
    return hasil

def balok():
    print('======================')
    print('         Balok')
    print('======================')
    print('Pilih salah satu opsi dibawah ini:')
    print('1.Keliling balok')
    print('2.Luas balok')
    print('3.Volume balok')
    print('4.Keluar')
    Input_usr = int(input('Masukkan pilihan anda>> '))
    if Input_usr == 1:
        keliling_balok()
    elif Input_usr == 2:
        luas_permukaan_balok()
    elif Input_usr == 3:
            volume_balok()
    else:
        print('Input yang anda masukkan tidak valid!!!')

def main():
    while True:
        print("\n\n")
        print("=====================================")
        print("          Hitung Bangun Ruang ")
        print("=====================================")
        print('Pilih salah satu opsi dibawah ini:')
        print('1.Persegi')
        print('2.Kubus')
        print('3.Lingkaran')
        print('4.Persegi panjang')
        print('5.Segitiga')
        print("6.Limas segitiga")
        print('7.Balok')
        print('8.Keluar')
        inputUser = int(input('Masukkan pilihan anda>> '))
        typing("Memproses.....", delay=.04)
        time.sleep(2)
        
        match inputUser:
            case 1:
                persegi()
            case 2:
                kubus()
            case 3:
                lingkaran()
            case 4:
                persegi_panjang()
            case 5:
                segitiga()
            case 6:
                limas_segitiga()
            case 7:
                balok()
            case 8:
                print('Terima kasih sudah berkunjung, silahkan mencoba lagi!!!')
                break
            case _:
                print('Input yang anda masukkan tidak valid!!!')

main()
#disalin dlu lalu jalanin di vscode, compiler, atau lewat terminal. Terima Kasih

def luas_persegi():
    print('(!)Rumus luas persegi: sisi x sisi')
    Input_user = int(input('Masukkan sisi>> '))
    hasil = 2 * Input_user
    print('\n L.persegi= sisi x sisi')
    print(f'          = {Input_user} x {Input_user}')
    print(f'          = {hasil} cm²')
    return hasil

def volume_persegi():
    print('(!)Rumus volume persegi: sisi x sisi x sisi') 
    Input_user = int(input('Masukkan sisi persegi>> '))
    hasil = Input_user ** 3
    print('\n V.persegi= sisi x sisi x sisi')
    print(f'          = {Input_user} x {Input_user} x {Input_user}')
    print(f'          = {hasil} cm³')
    return hasil

def persegi():
    print('\n========================')
    print('         PERSEGI        ')
    print('========================\n')
    print('1.Luas persegi')
    print('2.Volume persegi')
    print('3.keluar')
    Input_ussr = int(input('Masukkan pilihan>> '))
    if Input_ussr == 1:
        luas_persegi()
    elif Input_ussr == 2:
        volume_persegi()
    elif Input_ussr == 3:
        banner()
    else:
        print("(!)Input yang anda masukkan tidak valid!!!")

def luas_kubus():
    print('(!)Rumus luas kubus = 6 x s²')
    Input_user = int(input('Masukkan sisi kubus>> '))
    hasil = 6 * Input_user * Input_user
    print('\n L.kubus= 6 x s²')
    print(f'          = 6 x {Input_user} x {Input_user}')
    print(f'          = {hasil} cm²')
    return hasil

def volume_kubus():
    print('(!)Rumus volume kubus = s³')
    Input_user = int(input('Masukkan sisi kubus>> '))
    hasil =  Input_user ** 3
    print('\n V.kubus= s x s x s')
    print(f'          = {Input_user} x {Input_user} x {Input_user}')
    print(f'          = {hasil} cm³')
    return hasil

def kubus():
    print('\n========================')
    print('         KUBUS        ')
    print('========================\n')
    print('1.Luas')
    print('2.Volume kubus')
    print('3.keluar')
    Input_ussr = int(input('Masukkan pilihan>> '))
    if Input_ussr == 1:
        luas_kubus()
    elif Input_ussr == 2:
        volume_kubus()
    elif Input_ussr == 3:
        banner()
    else:
        print("(!)Input yang anda masukkan tidak valid!!!")

def keliling_lingkaran():
    print('(!)Rumus keliling lingkaran: 2 x π x r')
    Input_user = int(input('Masukkan jari-jari lingkaran>> '))
    hasil = 2 * 3.14 * Input_user
    print('\n K.lingkaran= 2 x π x r')
    print(f'          = 2 x {3.14} x {Input_user}')
    print(f'          = {hasil} cm')
    return hasil

def luas_lingkaran():
    print('(!)Rumus luas lingkaran: π x r x r')
    Input_user = int(input('Masukkan jari-jari lingkaran>> '))
    hasil = 3.14 * Input_user * Input_user
    print('\n L.lingkaran= π x r x r')
    print(f'          = 3.14 x {Input_user} x {Input_user}')
    print(f'          = {hasil} cm²')
    return hasil

def lingkaran():
    print('\n========================')
    print('         LINGKARAN      ')
    print('========================\n')
    print('1.Keliling lingkaran')
    print('2.Luas lingkaran')
    print('3.keluar')
    Input_ussr = int(input('Masukkan pilihan>> '))
    if Input_ussr == 1:
        keliling_lingkaran()
    elif Input_ussr == 2:
        luas_lingkaran()
    elif Input_ussr == 3:
        banner()
    else:
        print('(!)Input yang anda masukkan tidak valid!!!')

def keliling_persegiPanjang():
    print('(!)Rumus keliling persegi panjang: 2 x (panjang + lebar)')
    Input_user_panjang = int(input('Masukkan panjang persegi panjang>> '))
    Input_user_lebar = int(input('Masukkan lebar persegi panjang>> '))
    hasil = 2 * (Input_user_panjang + Input_user_lebar)
    print('\n K.persegi panjang= 2 x (panjang + lebar)')
    print(f'          = 2x ({Input_user_panjang} + {Input_user_lebar})')
    print(f'          = {hasil} cm')
    return hasil

def luas_pesegiPanjang():
    print('(!)Rumus luas persegi panjang: panjang x lebar')
    Input_user_panjang = int(input('Masukkan panjang persegi panjang>> '))
    Input_user_lebar = int(input('Masukkan lebar persegi panjang>> '))
    hasil = Input_user_panjang + Input_user_lebar
    print('\n L.persegi panjang= panjang x lebar')
    print(f'          = {Input_user_panjang} + {Input_user_lebar}')
    print(f'          = {hasil} cm²')
    return hasil

def persegi_panjang():
    print('\n=======================')
    print('         Lingkaran')
    print('=======================')
    print('1.Keliling persegi panjang')
    print('2.Luas persegi panjang')
    print('3.keluar')
    Input_User = int(input('Masukkan pilihan anda>> '))
    if Input_User == 1:
        keliling_persegiPanjang()
    elif Input_User == 2:
        luas_pesegiPanjang()
    elif Input_User == 3:
        banner()
    else:
        print('(!)Input yang anda masukkan tidak vallid!!!')

def keliling_segitiga():
    print('(!)Rumus keliling segitiga: a + b + c')
    Input_user_a = int(input('Masukkan a>> '))
    Input_user_b = int(input('Masukkan b>> '))  
    Input_user_c = int(input('Masukkan c>> '))
    hasil = Input_user_a + Input_user_b + Input_user_c
    print('\n K.segitiga= a + b + c')
    print(f'          = {Input_user_a} + {Input_user_b} + {Input_user_c}')
    print(f'          = {hasil} cm')
    return hasil

def luas_segitiga():
    print('(!)Rumus luas segitiga: 1/2 x a')
    Input_user_a = int(input('Masukkan a>>'))
    hasil = 1/2 * Input_user_a
    print('\n L.persegi panjang= 1/2 x a')
    print(f'          = 1/2 x {Input_user_a}')
    print(f'          = {hasil} cm²')
    return hasil

def segitiga():
    print('\n=======================')
    print('        Segitiga')
    print('=======================')
    print('1.Keliling segitiga')
    print('2.Luas segitiga')
    print('3.keluar')
    Input_User = int(input('Masukkan pilihan anda>> '))
    if Input_User == 1:
        keliling_segitiga()
    elif Input_User == 2:
        luas_segitiga()
    elif Input_User == 3:
        banner()
    else:
        print('(!)Input yang anda masukkan tidak vallid!!!')

def banner():
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
        print('6.Keluar')
        inputUser = int(input('Masukkan pilihan anda>> '))
        
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
                break
            case _:
                print('Terima kasih sudah berkunjung, silahkan mencoba lagi!!!')

banner()

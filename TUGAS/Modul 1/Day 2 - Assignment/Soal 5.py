if __name__ == '__main__':
    # ANSWER

    # import math library
    import math

    # define variable jarak, kecepatan A & B, jam berangkat
    jarak = 120
    kec_A = 60
    kec_B = 40
    jam_berangkat = 9

    # define formula from variable waktu_temu
    waktu_temu = jarak/(kec_A + kec_B)

    # define formula from variable waktu_tabrakan
    waktu_tabrakan = jam_berangkat + waktu_temu

    # reformat waktu_tabrakan to more readable time format 
    jam_tabrakan = math.floor(waktu_tabrakan)
    menit_tabrakan = (waktu_tabrakan%jam_tabrakan)*60

    # print result
    print(f"A & B akan bertabrakan pada jam {jam_tabrakan} lebih {menit_tabrakan} menit")
    
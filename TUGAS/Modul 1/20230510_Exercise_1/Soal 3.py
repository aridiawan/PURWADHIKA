if __name__ == '__main__':
    # ANSWER

    # define variable jumlah hari with the values
    jumlah_hari = 485

    # define formula for every variable tahun, bulan, minggu, hari
    tahun = jumlah_hari//360
    bulan = (jumlah_hari%360)//30
    minggu = ((jumlah_hari%360)%30)//7
    hari = (((jumlah_hari%360)%30)%7)

    # print result
    print(f'{jumlah_hari} = {tahun} tahun {bulan} bulan {minggu} minggu {hari} hari')
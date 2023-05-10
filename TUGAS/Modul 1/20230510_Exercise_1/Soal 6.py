if __name__ == '__main__':
    # ANSWER

    # define variable jumlah_apel, jumlah_jeruk, jumlah_anggur
    jumlah_apel = int(input('Masukkan Jumlah Apel : '))
    jumlah_jeruk = int(input('Masukkan Jumlah Jeruk : '))
    jumlah_anggur = int(input('Masukkan Jumlah Anggur : '))

    # define variable harga apel, harga jeruk, harga anggur
    harga_apel = 10000
    harga_jeruk = 15000
    harga_anggur = 20000

    # define formula from variable total_belanja_apel, total_belanja_jeruk, total_belanja_anggur
    total_belanja_apel = jumlah_apel * harga_apel
    total_belanja_jeruk = jumlah_jeruk * harga_jeruk
    total_belanja_anggur = jumlah_anggur * harga_anggur

    # define formula to get total_belanja
    total_belanja = total_belanja_apel + total_belanja_jeruk + total_belanja_anggur

    # print keterangan detail belanja
    print('Detail Belanja')

    # print result of how each item's total belanja calculated
    print(f"Apel : {jumlah_apel} x {harga_apel} = {total_belanja_apel}")
    print(f"Jeruk : {jumlah_jeruk} x {harga_jeruk} = {total_belanja_jeruk}")
    print(f"Anggur : {jumlah_anggur} x {harga_anggur} = {total_belanja_anggur}")

    # print total belanja result
    print(f'Total Belanja : {total_belanja}')    
    
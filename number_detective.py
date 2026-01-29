import random 

print("=== Number Detective ===") 

batas_bawah = int(input("Masukkan batas bawah: ")) 
batas_atas = int(input("Masukkan batas atas: ")) 
kesempatan = int(input("Masukkan jumlah kesempatan: ")) 

if batas_bawah >= batas_atas or kesempatan <= 0: 
    print("Input tidak valid.") 
else: 
    angka_rahasia = random.randint(batas_bawah, batas_atas) 

    print(f"Tebak angka antara {batas_bawah} sampai {batas_atas}") 
    print("Jumlah kesempatan:", kesempatan) 

    while kesempatan > 0: 
        tebakan = int(input("Masukkan tebakan Anda: ")) 
  
        if tebakan < batas_bawah or tebakan > batas_atas: 
            print("Tebakan di luar range.") 
            continue 
    
        if tebakan == angka_rahasia: 
            print("Tebakan benar! Anda menang.") 
            break 
        elif tebakan > angka_rahasia: 
            print("Terlalu besar.") 
        else: 
            print("Terlalu kecil.") 
      
        kesempatan -= 1 
        print("Sisa kesempatan:", kesempatan) 
      
    if kesempatan == 0: 
        print("Kesempatan habis.") 
        print("Angka rahasia adalah:", angka_rahasia)

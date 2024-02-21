import time
import random

# Kodunuzu buraya yazınız
seninpuanin = 0
bpuani = 0
tur = 1
while True:
    print("###################################")
    print(tur,". Tur Başlıyor.")
    
    tur += 1
    print("-----------------------------------")
    time.sleep(1)
    secim = input("taş, kağıt, makas")
    if secim == "taş" or secim == "makas" or secim == "kağıt":
        bsecim = random.randint(1,3)
        if bsecim == 1:
            bsecim = "taş"
        elif bsecim == 2:
            bsecim = "kağıt"
        elif bsecim == 3:
            bsecim = "makas"
        time.sleep(1)
        print("Bilgisayarın seçtiği:", bsecim)
        
        if secim == bsecim:
            print("durum berabere.")
        elif secim == "taş" and bsecim == "makas":
            print("sen kazandın!")
            seninpuanin += 1
        elif secim == "makas" and bsecim == "kağıt":
            print("sen kazandın")
            seninpuanin += 1
        elif secim == "kağıt" and bsecim == "taş":
            print("sen kazandın")
            seninpuanin += 1
        else:
            print("bilgisayar kazandı.")
            bpuani += 1
        
        print("Senin Puanın:", seninpuanin)
        print("Bilgisayarın Puanı:", bpuani)

            
    else:
        print("lütfen taş, kağıt veya makas gir.")
    print(" ")

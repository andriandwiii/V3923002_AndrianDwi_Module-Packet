#!/usr/bin/env python
# coding: utf-8

# In[2]:


def fpb(a, b):
    while b:
        a, b = b, a % b
    return a

def kpk(a, b):
    return a * b // fpb(a, b)

def hitung_fpb_kpk():
    pilihan = input("Pilih FPB atau KPK: ").upper()
    
    if pilihan not in ['FPB', 'KPK']:
        print("Peringatan: Pilihan tidak valid.")
        return
    
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    
    if pilihan == 'FPB':
        print(f"FPB dari {angka1} dan {angka2} adalah {fpb(angka1, angka2)}")
        
    elif pilihan == 'KPK':
        print(f"KPK dari {angka1} dan {angka2} adalah {kpk(angka1, angka2)}")

hitung_fpb_kpk()


# In[ ]:





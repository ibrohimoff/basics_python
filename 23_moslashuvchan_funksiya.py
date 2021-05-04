# def summa(*sonlar):
#    return sum(sonlar)
# print(summa(23,345,45,56))


# def summa(x,y,*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return x*y+sum(sonlar)
# print(summa(2,3,23))

# def multiply(*sonlar):
#     kopaytma = 1
#     for son in sonlar:
#         kopaytma*=son
#     return kopaytma

# print(multiply(23,54))

def avto_info(kompaniya,model,**malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar
avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)
print(avto2)


def talaba_info(ism, familiya, **malumotlar):
    malumotlar['ism'] = ism
    malumotlar['familiya'] = familiya
    return malumotlar
tal1 = talaba_info('Husan', 'Qodir', yil = 2000)
tal2 = talaba_info('ali', 'vali', joy = 'Andijon')
print(tal2)
    
    
    
    
    
    
    
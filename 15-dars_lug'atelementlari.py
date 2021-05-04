# talaba_0 = {
#             'ism':'ali',
#             'sharif':'valiyev', 
#             't_yil':1999
#             }

# print(talaba_0.items())
# # print(talaba_0.keys())

# # for keys, values in talaba_0.items():
# #     print(f"Keys : {keys}")
# #     print(f"Values : {values}")
    
    
    
# telefonlar = {
#             'ali':'iphone x',
#             'vali':'samsung s20',
#             'olim':'huawei p40',
#             'orif':'mi note10'  
#               }

# print(telefonlar.values())

# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q.title()}")


# mahsulotlar = { # Do'kondagi mahsulotlar
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }

# print(mahsulotlar.keys())
    

# # print("do'kondagi mahsulotlar: ")
# # for mahsulot in mahsulotlar.keys():
# #     print(mahsulot)

# bozorlik = ['anor','uzum','non','baliq']
# # for mahsulot in mahsulotlar:
# #     if mahsulot in bozorlik:
# #         print(f"{mahsulot} {mahsulotlar[mahsulot]}")

# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"iltimos do'koningizga {buyum} ham olib keling")

# for  mahsulot in  sorted(mahsulotlar):
#     print(mahsulot.title())

# lugat = {'float': "o'nlik son", 'integer':'butun son', 'boolean':'mantiqiy qiymat', 
#          'for':'biror amalni bajarish tsikli', 'if':'shartlarni tekshirish operatori' }
# for k,q in lugat.items():
#     print(f"{k.capitalize()} - {q.capitalize()}")

# davlatlar = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'
#     }


# print("Dunyo davlatlari: ")
# for davlat in sorted(davlatlar):
#     print(davlat.upper())
# print("\n")
    
# print("Dunyo poytaxtlari : ")
# for poytaxt in davlatlar.values():
#     print(poytaxt.title())  
    
# country = input("Qaysi davlat poytaxtini bilishni istaysiz? ")
# capital = davlatlar.get(country)
# if capital==None:
#     print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
# else:
#     print(f"{country.upper()}ning poytaxti {capital.title()} shahri")
    
    
# menu = {
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000,
#     'osh':15000,
#     "do'lma":10000,
#     'qisqichbaqa':50000,
#     'pizza':50000 
#     }

# print("3 ta taomga buyurtma bering: ")
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-taom:").lower())
    
# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f"{buyurtma.title()} {menu[buyurtma]} so'm ")
#      else:
#         print(f"Kechirasiz, bizda {buyurtma} yo'q.")
        
        
# print('3 ta taom buyurtma bering.')
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-taom:").lower())

# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
#     else:
#         print(f"Kechirasiz, bizda {buyurtma} yo'q.")        






    

    















    










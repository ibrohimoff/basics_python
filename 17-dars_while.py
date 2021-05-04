# ism = input('Ismingiz nima? ')
# savol = f"Salom {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)
# yosh = int(yosh)
# height = input("Bo'yingiz necha metr? ")
# height = float(height)
# print(ism.title(), yosh, height)

# son = 1
# while son<=5:
#     print(son, end = ' ')
#     son = son + 1

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing)  "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing)  "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         ishora = False
#         print(float(qiymat)**2)

# son = 0
# while son<10:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)

# savol = "Sevimli kitobingizni kiriting: "
# savol += "(dasturdan chiqish uchun 'stop' deb yozing)"
# while True:
#     kitob = input(savol)
#     if kitob == 'stop':
#         break
# print('Rahmat')


# savol = "Yoshingizni kiriting: "
# savol += "(dasturdan chiqish uchun 'exit' yoki 'quit' so'zidan birini kiriting)"
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
#     if yosh<7:
#         narh = 2000
#     elif 7<=yosh<18:
#         narh = 3000
#     elif 18<=yosh<65:
#         narh = 10000
#     else: narh = 0
    
#     if narh==0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Chipta {narh} so'm")

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat =='exit':
#         break
#     elif float(qiymat)<0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")


# ismlar = []
# print= "Do'stlaringiz ro'yxatini tuzamiz: "
# n = 1

# while True:
#     savol = f"{n}-do'stingizni kiriting: "
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha / yo'q)")
#     if javob == 'ha':
#         n += 1
#         continue
#     else:
#         break
    
    
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())
    


# ismlar = []

# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break

# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())

# dostlar = {}
# ishora = True

# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)
    
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob !='ha':
#         ishora = False


# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} da")

# cars = ['nexia', 'malibu', 'matiz', 'nexia', 'bmw', 'nexia']
# while 'nexia' in cars:
#     cars.remove("nexia")
# print(cars)


# talabalar = ['hasan', 'husan', 'orif', 'olim']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba}ning bahosini kiriting:\n")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = int(baho)

# print(baholangan_talabalar)


# savat = []
# while True:
#     mahsulot= input("Mahsulotni kiriting: ")
#     savat.append(mahsulot)
    
#     savol = input("Yana mahsulot qo'shasizmi(ha/yo'q)")
#     if savol != 'ha':
#         break

# mahsulotlar = {}
# while True:
#     mahsulot = input("Mahsulot nomini kiriting: ")
#     narh = input(f"{mahsulot.title()}ning narhini kiriting: ")
#     mahsulotlar[mahsulot] = narh
#     javob = input("Yana mahsulot qo'shasizmi?(ha/yo'q)")
#     if javob != 'ha':
#         break

buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narx = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} {narx} so'm ")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q")






























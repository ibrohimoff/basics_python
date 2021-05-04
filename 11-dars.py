# kun = input("Bugun haftaning qaysi kuni?\n")
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print('Bugun dam olish kuni')
# else:
#     print('Bugun ish kuni')

# kun = input("Bugun haftaning qaysi kuni? ")
# harorat = float(input("Havo harorati qancha? "))
# if kun.lower() == 'yakshanba' or kun.lower() == 'shanba' and  harorat >=30:
#     print('Ketdik, cho\'milgani')
# elif kun.lower() == 'yakshanba' or kun.lower() == 'shanba' and  harorat <30:
#     print('Uyda dam olamiz')

# yosh = int(input("Yoshingiz nechida? : "))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 4000
# elif yosh<=33:
#     price = 8000
# elif yosh<= 65:
#     price = 10000
# print(f"Sizga kirish {price} so'm bo'ladi")

# kun = input("Bugun haftaning qaysi kuni? ")

# if kun.lower() == 'yakshanba' and  kun.lower() == 'shanba':
#     print("Dam olamiz")
# else:
#     print("Ishga boramiz")

# narx = 15000
# choy  = 1
# salat = 0

# if choy and salat:
#     narx = narx + 10000
# if choy or salat:
#     narx = narx + 5000
    
# print (f"Jami {narx} so'm. ")

# menu = ['manti', 'somsa', 'osh', 'lavash', 'kompot']
# ovqat = input("Nima ovqat yeysiz?>>>\n")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi")
# else:
#     print("Afsus bizda bunday taom yo'q")
    

# son = int(input("Juft son kiriting: "))
# if son%2:
#     print(f"{son} juft emas")
# else:
#     print("Rahmat")


# yosh = int(input("Yoshingiz nechida?>>>\n"))
# if yosh<=4 or yosh>=65:
#     price = 0
# elif yosh<=18:
#     price = 10000
# elif yosh>=18:
#     price = 20000
# print(f"Sizga kirish {price} so'm bo'ladi")

# a = yosh = float(input("1-sonni kiriting:>>>\n"))
# b = yosh = float(input("2-sonni kiriting:>>>\n"))
# if a==b:
#     print(f"{a} = {b}")
# elif a>b:
#     print(f"{a} > {b}")
# else:
#     print(f"{a} < {b}")

# mahsulotlar = ["anor", 'uzum', 'kartoshka', 'tovuq', 'kolbasa', 'pista', 'bodom',
#                'un', "yog'", "sovun", 'tuxum', 'piyoz']

# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1} mahsulotni qo'shing: "))
    
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q")



# users = ["Ali".lower(), "Aziz".lower(), "Umar".lower(), "Abbos".lower(), "Anas".lower()]
# login = input("Yangi login kiriting: ")

# if login in users:
#     print("Login band, yangi login tanlang! ")
# else:
#     print(f"Xush kelibsiz, {login.title()}")

son = int(input("Istalgan butun son kiriting: "))

for n in range(1,101):
    if not son%n:
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

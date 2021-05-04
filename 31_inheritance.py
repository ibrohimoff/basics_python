
# # class Shaxs:
# #     __num_talabalar = 0
# #     """Shaxslar haqida ma'lumot"""
# #     def __init__(self,ism,familiya,passport,tyil):
# #         """Shaxsning xususiyatlari"""
# #         self.ism = ism
# #         self.familiya = familiya
# #         self.passport = passport
# #         self.__tyil = tyil
# #         Shaxs.__num_talabalar += 1
    
# #     @classmethod
# #     def get_num_std(cls):
# #         return cls.__num_talabalar
       
    
# #     def get_info(self):
# #         """Shaxs haqida ma'lumot"""
# #         info = f"{self.ism} {self.familiya}. "
# #         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
# #         return info
# #     def get_age(self,yil):
# #         """Shaxsning yoshini qaytaruvchi metod"""
# #         return yil - self.__tyil
    
# #     def act_age(self):
# #         return self.__tyil
    
# #     def talabalar_soni(self):
# #         self.talaba += 1

# # talaba1 = Shaxs('Olim', 'Qodirov', 'AB3465', 1990)
# # talaba2 = Shaxs('alim', 'Qodirov', 'AB34455', 1998)
# # talaba3 = Shaxs('salim', 'Qodirov', 'AB34235', 2005)

# # print(Shaxs.get_num_std())
  
# from uuid import uuid4
# class Avto:
#     """Avtomobil klassi"""
#     __num_avto = 0
#     def __init__(self,make,model,rang,yil,narh,km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
#         Avto.__num_avto += 1
    
#     @classmethod
#     def get_num_avto(cls):
#         return cls.__num_avto
    
#     def get_km(self):
#         return self.__km
    
#     def get_id(self):
#         return self.__id
    
#     def add_km(self,km):
#         """Mashinaning km ga yana km qo'shish"""
#         if km>=0:
#             self.__km += km
#         else:
#             print("Mashina km kamaytirib bo'lmaydi")
            
# avto1 = Avto("GM","Malibu","Qora",2020,40000,100000)
# print(f"ID: {avto1.get_id()}")
# avto1.add_km(-1500)
# print(avto1.get_km())
# print(Avto.get_num_avto())


    
n = 5
for i in range(n):
    for j in range(i):
        print('*',end=' ')
    print('')
for i in range(n,0,-1):
    for j in range(i):
        print('*', end = ' ')
    print(' ')







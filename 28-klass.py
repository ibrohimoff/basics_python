# class User:
#     def __init__(self, ism, fism, email):
#         self.ism = ism
#         self.fism = fism
#         self.email = email
#     def get_name(self):
#         return  self.ism          

#     def full_name(self):
#         return f"Men : {self.ism} {self.fism}, email : {self.email}"
    
# user1 = User('Olim', 'Orif', '@olimbey')

# user2 = User('Abror', 'Alimov','@AAlimov')
# user3 = User('Shahzod', 'Akmalov', '@SHAHA')
# print(user1.full_name())
# print(user2.full_name())
# print(user3.full_name())


class Avto:
    def __init__(self, kompaniya, model, rang, narh):
        self.komp = kompaniya
        self.m  = model
        self.r = rang
        self.n = narh
        # self.kil = 1
        
    def comp(self):
        return self.komp
    
    def Model(self):
        return self.m
    
    def R_rang(self):
        return self.r
    
    def s_narh(self):
        return self.n
    
    def s_kil(self,kilometr):
        self.kil = kilometr
        
    def update_kil(self):
        self.kil += 5
    
    def full_info(self):
        return f" Kompaniya : {self.komp}, model : {self.m}, rang : {self.r}, narh : {self.n}, kilometr : {self.kil}"
    
    # def set_bosqich(self,bosqich):
    #     """Talabaning kursini yangilovchi metod"""
    #     self.bosqich = bosqich
        
    # def update_bosqich(self):
    #     """Talabanining bosqichini 1taga ko'paytirish"""
    #     self.bosqich += 1
    
    
    
avtolar = Avto('BMW', 'AMG', 'Green', 20000)
print(avtolar.s_kil(65))
print(avtolar.update_kil())
print(avtolar.full_info())







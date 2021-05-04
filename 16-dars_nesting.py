# def salom_ber(ism):
#     print(f"Assalomu alaykum, {ism.title()}")
    
# salom_ber('husan')
# salom_ber('hasan')
# salom_ber('olim')

# def toliq_ism(ism, familiya):
#     print(f"Assalomu alaykum, {ism.title() }"
#           f" {familiya.title()}")
    
# toliq_ism('olim', 'hakimov')

# def yosh_hisobla(ism, t_yil):
#     print(f"{ism.title()} {2021-t_yil} yoshda")
    
# yosh_hisobla('olim', 1999)
# yosh_hisobla(1999, 'olim')  ### xato
# yosh_hisobla(t_yil = 1999, ism = 'olim')

# def toliq_ism(ism, familiya):
#     print(f"{ism.title()} {familiya.title()}")
    
# i = input("Ism kiriting: ")
# f = input("Familiyangizni kiriting: ")
# toliq_ism(i,f)


'''Kvadrat, kub hisobla'''
# def kub_kvhisobla(son):
#     print(f"{son}ning kvadrati = {son**2}, {son}ning kubi =  {son**3}")
    
# k = int(input("Sonni kiriting: "))

# kub_kvhisobla(k)
    
'''Juftmi toqmin top'''
# def juftmi(son):

#     if son%2:
#         print(f"{son} -  toq")
#     else:
#         print(f"{son} - juft")
    
# juftmi(5)
# juftmi(6)

'''Katta-kichik hisobla'''
# def hisobla(x,y):
    
#     if x>y:
#         print(f"{x} > {y}")
#     elif x<y:
#         print(f"{x} < {y}")
#     else:
#         print('Both are equal')
        
# hisobla(5.4, 5.6)


"""Sonning darajasi"""
# def xY(x,y = 2):
#     print(f"{x} ning {y} darajasi = {x**y}")
    
# xY(89)

def bolinish(son):
    
    for n in range(1,11):
        if not son%n:
            print(f"{son} {n}ga qoldiqsiz bo'linadi")
            
bolinish(8)




    
    
    
    
    



    
    
    
    
    
    
    


    
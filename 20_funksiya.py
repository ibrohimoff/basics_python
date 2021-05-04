# def toliq_ism_yasa(ism, familiya):
#     toliq_ism = f"{ism}{familiya}"
#     return toliq_ism
# talaba1  = toliq_ism_yasa("Olim ", "Hakimov,")
# talaba2 = toliq_ism_yasa("Orif ", "Olimov")
# print(f"Darsga kelmagan talabalar {talaba1} {talaba2}")


# def toliq_ism_yasa(ism, familiya, otasining_ismi = ''):
   
#     if otasining_ismi:
#        toliq_ism =  f"{ism} {familiya} {otasining_ismi}"
#     else: 
#         toliq_ism = f"{ism} {familiya} {otasining_ismi}"
#     return toliq_ism
# talaba1  = toliq_ism_yasa("Olim ", "Hakimov", "Abrorovich")
# talaba2 = toliq_ism_yasa("Orif ", "Olimov")
# print(f"Darsga kelmagan talabalar :  {talaba1}, {talaba2}")

# def avto_info(kompaniya, model, rangi, korobka, yili, narx = None):
#     avto = {
#         'kompaniya': kompaniya,
#         'model': model,
#         'rangi': rangi,
#         'korobka': korobka,
#         'yili': yili,
#         'narxi': narx
#         }
#     return avto


# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")

# def talaba_info(ism, familiya, t_yil, tel_raqami = '', email = ''):
#     if tel_raqami and email:
#         talaba = f"{ism} {familiya} {t_yil}, {tel_raqami}, {email}"
#     else:
#         talaba = f"{ism} {familiya} {t_yil}"
#     return talaba

#     print(f"{talaba1}, {talaba2}")
    
#     tal = {
#         'Ismi':ism, 
#         'Familiyasi':familiya,
#         "Tug'ilgan yili": t_yil,
#         "Telefon raqami":tel_raqami,
#         "Email":email
#         }
 

# talaba1 = talaba_info('Olim', "Orif", 2000, 2000505, '@olimbek')
# talaba2 = talaba_info('Hasan', 'Qodirov', 2001)
    
# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)        
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar

# print(fibonacci(10))

        






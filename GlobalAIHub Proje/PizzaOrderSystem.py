import csv
from datetime import datetime
import time
import pandas as pd
import os
import pymysql.cursors
import random

#Mysql bağlantı kodlarımız 
db = pymysql.connect(host='localhost',
                        user='*******',
                        password='******', # Bilgisayarında Mysql olanlar için user ve password alanları kendi mysqllerine göre yazılmalıdır.
                        db='projeglobalaıhub',
                        cursorclass=pymysql.cursors.DictCursor)
connection = db.cursor()


# Her yerde erişmek istediğimiz değişkenleri tanımladık.
global sosPrice,total_price,count,i,sosListe,pizza_name,userid_list

userid_list = []
sosPrice = 0
sosListe = []
count = 0
i = 0

# Üst Pizza sınıfımızı tanımladık.
class Pizza():

  def __init__(self, description, cost):
    self.__description = description,
    self.__cost = cost

  #Encapsulation ile cost ve description tanımladık
  def get_description(self):
    return self.__description

  def set_description(self,description_):
    self.__description = description_    

  def get_cost(self):
    return self.__cost
  
  def set_cost(self,cost_):
    self.__cost = cost_

# Alt sınıflarımız Pizza üst sınıfından kalıtım almasını sağladık.
class Classic(Pizza):
  def __init__(self,description, cost):
    super().__init__(description, cost)

class Margherita(Pizza):
  def __init__(self,description, cost):
    super().__init__(description, cost)

class TurkPizza(Pizza):
  def __init__(self,description, cost):
    super().__init__(description, cost)

class Dominos(Pizza):
  def __init__(self,description, cost):
    super().__init__(description, cost)  


# Nesnelerimizi oluşturarak pizzalar için sabit değerlerini tanımladık. 
pizCls = Classic("Klasik Pizza",100)
# Fiyatın cost methoduna açıklamanın ise description methoduna atanmasının doğruluğunu kontrol etmek için yazdırdık.
# print("Pizza İsmi:{acıklama} \nPizza Fiyatı:{fiyat} ".format(acıklama = pizCls.get_description(),fiyat = pizCls.get_cost()))

pizMar = Margherita("Margeritha Pizza", 135)
# print("Pizza İsmi:{acıklama} \nPizza Fiyatı:{fiyat} ".format(acıklama = pizMar.get_description(),fiyat = pizMar.get_cost()))

pizTurk = TurkPizza("Türk Pizza", 120)
# print("Pizza İsmi:{acıklama} \nPizza Fiyatı:{fiyat} ".format(acıklama = pizTurk.get_description(),fiyat = pizTurk.get_cost()))

pizDo = Dominos("Dominos Pizza", 150)
# print("Pizza İsmi:{acıklama} \nPizza Fiyatı:{fiyat} ".format(acıklama = pizDo.get_description(),fiyat = pizDo.get_cost()))

print("\n")

 #Soslar için süper sınıf olan decorator'ın Pizza üst sınıfından kalıtım almasını saülıyoruz
class Decorator(Pizza):
  # Cost ve description  özelliklerimizi tanımlıyoruz
  def __init__(self, description, cost):
    self._description = description,
    self._cost = cost


  #Encapsulation ile cost ve description tanımlanması
  def get_description(self):
    return self._description

  def set_description(self,description_):
    self._description = description_    

  def get_cost(self):
    return self._cost
  
  def set_cost(self,cost_):
    self._cost = cost_
  

# Zeytin, Mantar, Keçi Peyniri, Et, Soğan ve Mısır atl sınıflarımızın decorator sınıfından kalıtım almasını sağladık. 
class Zeytin(Decorator):
  def __init__(self,description, cost):
    super().__init__(description, cost) 

class Mantar(Decorator):
  def __init__(self,description, cost):
    super().__init__(description, cost)   

class KeciPeyniri(Decorator):
  def __init__(self,description, cost):
    super().__init__(description, cost)   

class Et(Decorator):
  def __init__(self,description, cost):
    super().__init__(description, cost)   

class Sogan(Decorator):
  def __init__(self,description, cost):
    super().__init__(description, cost)   

class Misir(Decorator):
  def __init__(self,description, cost):
    super().__init__(description, cost)

# Sos nesnelerini tanımladık.
sosZeytin = Zeytin("Siyah Zeytin",5)

# Fiyatın cost methoduna açıklamanın ise description methoduna atanmasının doğruluğunu kontrol etmek için yazdırdık.
# print("Sos İsmi:{acıklama} \nSos Fiyatı:{fiyat} ".format(acıklama = sosZeytin.get_description(),fiyat = sosZeytin.get_cost()))

sosMantar = Mantar("Kültür Mantarı",12)
# print("Sos İsmi:{acıklama} \nSos Fiyatı:{fiyat} ".format(acıklama = sosmantar.get_description(),fiyat = sosmantar.get_cost()))

sosKeciPeyniri = KeciPeyniri("Keçi Peyniri 50gr",25)
# print("Sos İsmi:{acıklama} \nSos Fiyatı:{fiyat} ".format(acıklama = sosKeciPeyniri.get_description(),fiyat = sosKeciPeyniri.get_cost()))

sosEt = Et("Dana Eti 100gr",32)
# print("Sos İsmi:{acıklama} \nSos Fiyatı:{fiyat} ".format(acıklama = sosEt.get_description(),fiyat = sosEt.get_cost()))

sosSogan = Sogan("Soğan",7)
# print("Sos İsmi:{acıklama} \nSos Fiyatı:{fiyat} ".format(acıklama = sosSogan.get_description(),fiyat = sosSogan.get_cost()))

sosMisir= Misir("Süt Mısır 35gr",9)
# print("Sos İsmi:{acıklama} \nSos Fiyatı:{fiyat} ".format(acıklama = sosMisir.get_description(),fiyat = sosMisir.get_cost()))

# Ödeme işlemi her pizza ayrı description'a sahip olduğundan bu şekilde tanımladık. Koşullarımız description'dan gelen isim'e göre yönlendirilmektedir.

# def listToString(s):
#   sosListe = " "
#   for ele in s:
#       sosListe += ele
#   return sosListe

def payment_Process():
  os.system('cls')

  if pizza_name == "Klasik Pizza":
    name = pizza_name

    # Alınan liste verilerinin list tipinden string tipine çeviriyoruz.
    liste = convertList(sosListe)
    print('Total prices for Pizza: {pizza} + Sauces: {sos} = {totalPrice}'.format(pizza = name,sos = liste, totalPrice = total_price))
    credit_card_username = input('Name on credit card: ')

    # Oluşturulan user_id'lerin listeye atılması ve 2 kişinin aynı id ye sahip olmamasını sağlamak için koşul koyduk.
    if userid in userid_list:
      print('Bu id de bir kayıt zaten mevcut! ')

    else:
      userid = random.randint(0,1000)
      userid_list.append(userid)

    userid = str(userid)
    order_description = name + liste
    order_time = datetime.now()
    credit_card_number = input('Enter credit card number: ')
    credit_card_last_time = input('Enter credit card last time (Exp:02/24): ')
    cvv = input("Enter CVV: ")
    credit_card_password = input("Enter credit card password: ")
    connection.execute('INSERT INTO ordersystem VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(None,credit_card_username,userid,order_description,order_time,credit_card_number,credit_card_last_time,cvv, credit_card_password))
    db.commit()

  if pizza_name == "Margeritha Pizza":
    name = pizza_name
    liste = convertList(sosListe)
    print('Total prices for Pizza: {pizza} + Sauces: {sos} = {totalPrice}'.format(pizza = name,sos = liste, totalPrice = total_price))
    credit_card_username = input('Name on credit card: ')

    if userid in userid_list:
      print('Bu id de bir kayıt zaten mevcut! ')

    else:
      userid = random.randint(0,1000)
      userid_list.append(userid)

    userid = str(userid)
    order_description = name
    order_time = datetime.now()
    credit_card_number = input('Enter credit card number: ')
    credit_card_last_time = input('Enter credit card last time: ')
    cvv = input("Enter CVV: ")
    credit_card_password = input("Enter credit card password: ")
    connection.execute('INSERT INTO ordersystem VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(None,credit_card_username,userid,order_description,order_time,credit_card_number,credit_card_last_time,cvv, credit_card_password))
    db.commit()

  if pizza_name == "Türk Pizza":
    name = pizza_name
    liste = convertList(sosListe)
    print('Total prices for Pizza: {pizza} + Sauces: {sos} = {totalPrice}'.format(pizza = name,sos = liste, totalPrice = total_price))
    credit_card_username = input('Name on credit card: ')

    if userid in userid_list:
      print('Bu id de bir kayıt zaten mevcut! ')

    else:
      userid = random.randint(0,1000)
      userid_list.append(userid)

    userid = str(userid)
    order_description = name
    order_time = datetime.now()
    credit_card_number = input('Enter credit card number: ')
    credit_card_last_time = input('Enter credit card last time: ')
    cvv = input("Enter CVV: ")
    credit_card_password = input("Enter credit card password: ")
    connection.execute('INSERT INTO ordersystem VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(None,credit_card_username,userid,order_description,order_time,credit_card_number,credit_card_last_time,cvv, credit_card_password))
    db.commit()

  if pizza_name == "Dominos Pizza":
    name = pizza_name
    liste = convertList(sosListe)
    print('Total prices for Pizza: {pizza} + Sauces: {sos} = {totalPrice}'.format(pizza = name,sos = liste, totalPrice = total_price))
    credit_card_username = input('Name on credit card: ')

    if userid in userid_list:
      print('Bu id de bir kayıt zaten mevcut! ')

    else:
      userid = random.randint(0,1000)
      userid_list.append(userid)

    userid = str(userid)
    order_description = name + liste
    order_time = datetime.now()
    credit_card_number = input('Enter credit card number: ')
    credit_card_last_time = input('Enter credit card last time: ')
    cvv = input("Enter CVV: ")
    credit_card_password = input("Enter credit card password: ")
    connection.execute('INSERT INTO ordersystem VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(None,credit_card_username,userid,order_description,order_time,credit_card_number,credit_card_last_time,cvv, credit_card_password))
    db.commit()


# get_description()'dan gelen isim verilerimizin tuple tipinden string tipine dönüştürmek için kullanılan fonksiyon 
def convertTuple(tup):
  pizza_name = ''.join(tup)
  return pizza_name

def convertList(lis):
  sosListe = ' '.join(lis)
  return sosListe

# Main fonksiyonumuz
if __name__ == "__main__":
  df = pd.read_csv("Menu.txt") 
  print(df.head(4))
  selection = input("Pizza Seçiminiz: ")

# Pizzalar için dictionary tanımladık.
  casesPizza={
    1:pizCls,
    2:pizMar,
    3:pizTurk,
    4:pizDo
  }

  # Soslar için dictionary tanımladık.
  casesSos ={
        1:sosZeytin,
        2:sosMantar,
        3:sosKeciPeyniri,
        4:sosEt,
        5:sosSogan,
        6:sosMisir
      }

# Pizza seçimlerinin sağlandığı koşul bloğumuz
if selection == "1":
  os.system('cls')
  classic_pizza_price = pizCls.get_cost()
  print(convertTuple(pizCls.get_description()) , ' seçtiniz ')
  time.sleep(3)

  do_you_want_sos = input("Sos ister misiniz(e/h): ") 
  if do_you_want_sos == "e":

    os.system('cls')
    print("Bilgilendirme: Sos seçimi için 3 hakkınız var\n")

    count = 3
    while count > i:
      df2 = pd.read_csv("Menu2.txt") #Sosların bulunduğu dosyayı okuyoruz.
      print(df2.head(6))

      sos = str(input("Hangi sosu istersiniz: "))

      if sos == "1":
        sos_name = convertTuple(sosZeytin.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = convertTuple(sosZeytin.get_description()),fiyat = sosZeytin.get_cost()))
          print("-------------------------------")

          sosZeytin_price = sosZeytin.get_cost()
          sosPrice = sosPrice + sosZeytin_price
          time.sleep(1)
          os.system('cls')
      else:
        print('Hatalı seçim yaptınız.!. Tekrar deneyiniz...')

      if sos == "2":
        sos_name = convertTuple(sosMantar.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosMantar.get_cost()))
          print("-------------------------------")

          sosMantar_price = sosMantar.get_cost()
          sosPrice = sosPrice + sosMantar_price
          time.sleep(1)
          os.system('cls')
      else:
        print('Hatalı seçim yaptınız.!. Tekrar deneyiniz...')

      if sos == "3":
        sos_name = convertTuple(sosKeciPeyniri.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')

        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosKeciPeyniri.get_cost()))
          print("-------------------------------")

          sosKeciPeyniri_price = sosKeciPeyniri.get_cost()
          sosPrice = sosPrice + sosKeciPeyniri_price
          time.sleep(1)
          os.system('cls')
      else:
        print('Hatalı seçim yaptınız.!. Tekrar deneyiniz...')

      if sos == "4":
        sos_name = convertTuple(sosEt.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosEt.get_cost()))
          print("-------------------------------")

          sosEt_price = sosEt.get_cost()
          sosPrice = sosPrice + sosEt_price
          time.sleep(1)
          os.system('cls')
      else:
        print('Hatalı seçim yaptınız.!. Tekrar deneyiniz...')

      if sos == "5":
        sos_name = convertTuple(sosSogan.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosSogan.get_cost()))
          print("-------------------------------")

          sosSogan_price = sosSogan.get_cost()
          sosPrice = sosPrice + sosSogan_price
          time.sleep(1)
          os.system('cls')
      else:
        print('Hatalı seçim yaptınız.!. Tekrar deneyiniz...')

      if sos == "6":
        sos_name = convertTuple(sosMisir.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosMisir.get_cost()))
          print("-------------------------------")

          sosMisir_price = sosMisir.get_cost()
          sosPrice = sosPrice + sosMisir_price
          time.sleep(1)
          os.system('cls')
      else:
        print('Hatalı seçim yaptınız.!. Tekrar deneyiniz...')

  else:
    total_price = classic_pizza_price + sosPrice
    pizza_name = convertTuple(pizCls.get_description())
    payment_Process()

  os.system('cls')
  total_price = classic_pizza_price + sosPrice
  print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
  time.sleep(3)
  pizza_name = convertTuple(pizCls.get_description())
  payment_Process()
   
  
if selection == "2":
  os.system('cls')
  mar_pizza_price = pizMar.get_cost()
  print(convertTuple(pizMar.get_description()) , ' seçtiniz ')
  time.sleep(3)

  do_you_want_sos = input("Sos ister misiniz(e/h): ") 
  if do_you_want_sos == "e":

    os.system('cls')
    print("Bilgilendirme: Sos seçimi için 3 hakkınız var\n")

    count = 3
    while count > i:
      df2 = pd.read_csv("Menu2.txt") #Sosların bulunduğu dosyayı okuyoruz.
      print(df2.head(6))

      sos = str(input("Hangi sosu istersiniz: "))

      if sos == "1":
        sos_name = convertTuple(sosZeytin.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = convertTuple(sosZeytin.get_description()),fiyat = sosZeytin.get_cost()))
          print("-------------------------------")

          sosZeytin_price = sosZeytin.get_cost()
          sosPrice = sosPrice + sosZeytin_price
          time.sleep(1)
          os.system('cls')
      else:
        print('Hatalı seçim yaptınız.!. Tekrar deneyiniz...')

      if sos == "2":
        sos_name = convertTuple(sosMantar.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosMantar.get_cost()))
          print("-------------------------------")

          sosMantar_price = sosMantar.get_cost()
          sosPrice = sosPrice + sosMantar_price
          time.sleep(1)
          os.system('cls')
      else:
        print('Hatalı seçim yaptınız.!. Tekrar deneyiniz...')

      if sos == "3":
        sos_name = convertTuple(sosKeciPeyniri.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')

        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosKeciPeyniri.get_cost()))
          print("-------------------------------")

          sosKeciPeyniri_price = sosKeciPeyniri.get_cost()
          sosPrice = sosPrice + sosKeciPeyniri_price
          time.sleep(1)
          os.system('cls')
      else:
        print('Hatalı seçim yaptınız.!. Tekrar deneyiniz...')

      if sos == "4":
        sos_name = convertTuple(sosEt.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosEt.get_cost()))
          print("-------------------------------")

          sosEt_price = sosEt.get_cost()
          sosPrice = sosPrice + sosEt_price
          time.sleep(1)
          os.system('cls')
      else:
        print('Hatalı seçim yaptınız.!. Tekrar deneyiniz...')

      if sos == "5":
        sos_name = convertTuple(sosSogan.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosSogan.get_cost()))
          print("-------------------------------")

          sosSogan_price = sosSogan.get_cost()
          sosPrice = sosPrice + sosSogan_price
          time.sleep(1)
          os.system('cls')
      else:
        print('Hatalı seçim yaptınız.!. Tekrar deneyiniz...')

      if sos == "6":
        sos_name = convertTuple(sosMisir.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosMisir.get_cost()))
          print("-------------------------------")

          sosMisir_price = sosMisir.get_cost()
          sosPrice = sosPrice + sosMisir_price
          time.sleep(1)
          os.system('cls')
      else:
        print('Hatalı seçim yaptınız.!. Tekrar deneyiniz...')

  else:
    total_price = mar_pizza_price + sosPrice
    pizza_name = convertTuple(pizMar.get_description())
    payment_Process()

  os.system('cls')
  total_price = mar_pizza_price + sosPrice
  print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
  time.sleep(3)
  pizza_name = convertTuple(pizMar.get_description())
  payment_Process()

  
  
if selection == "3":
  os.system('cls')
  tr_pizza_price = pizTurk.get_cost()
  print(convertTuple(pizTurk.get_description()) , ' seçtiniz ')
  time.sleep(3)

  do_you_want_sos = input("Sos ister misiniz(e/h): ") 
  if do_you_want_sos == "e":

    os.system('cls')
    print("Bilgilendirme: Sos seçimi için 3 hakkınız var\n")

    count = 3
    while count > i:
      df2 = pd.read_csv("Menu2.txt") #Sosların bulunduğu dosyayı okuyoruz.
      print(df2.head(6))

      sos = str(input("Hangi sosu istersiniz: "))

      if sos == "1":
        sos_name = convertTuple(sosZeytin.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = convertTuple(sosZeytin.get_description()),fiyat = sosZeytin.get_cost()))
          print("-------------------------------")

          sosZeytin_price = sosZeytin.get_cost()
          sosPrice = sosPrice + sosZeytin_price
          time.sleep(1)
          os.system('cls')
      else:
        print('Hatalı seçim yaptınız.!. Tekrar deneyiniz...')
        
      if sos == "2":
        sos_name = convertTuple(sosMantar.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosMantar.get_cost()))
          print("-------------------------------")

          sosMantar_price = sosMantar.get_cost()
          sosPrice = sosPrice + sosMantar_price
          time.sleep(1)
          os.system('cls')
      else:
        print('Hatalı seçim yaptınız.!. Tekrar deneyiniz...')
      if sos == "3":
        sos_name = convertTuple(sosKeciPeyniri.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')

        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosKeciPeyniri.get_cost()))
          print("-------------------------------")

          sosKeciPeyniri_price = sosKeciPeyniri.get_cost()
          sosPrice = sosPrice + sosKeciPeyniri_price
          time.sleep(1)
          os.system('cls')
      else:
        print('Hatalı seçim yaptınız.!. Tekrar deneyiniz...')

      if sos == "4":
        sos_name = convertTuple(sosEt.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosEt.get_cost()))
          print("-------------------------------")

          sosEt_price = sosEt.get_cost()
          sosPrice = sosPrice + sosEt_price
          time.sleep(1)
          os.system('cls')
      else:
        print('Hatalı seçim yaptınız.!. Tekrar deneyiniz...')      
      if sos == "5":
        sos_name = convertTuple(sosSogan.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosSogan.get_cost()))
          print("-------------------------------")

          sosSogan_price = sosSogan.get_cost()
          sosPrice = sosPrice + sosSogan_price
          time.sleep(1)
          os.system('cls')
      else:
        print('Hatalı seçim yaptınız.!. Tekrar deneyiniz...')

      if sos == "6":
        sos_name = convertTuple(sosMisir.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosMisir.get_cost()))
          print("-------------------------------")

          sosMisir_price = sosMisir.get_cost()
          sosPrice = sosPrice + sosMisir_price
          time.sleep(1)
          os.system('cls')
      else:
        print('Hatalı seçim yaptınız.!. Tekrar deneyiniz...')

  else:
    total_price = tr_pizza_price + sosPrice
    pizza_name = convertTuple(pizTurk.get_description())
    payment_Process()

  os.system('cls')
  total_price = tr_pizza_price + sosPrice
  print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
  time.sleep(3)
  pizza_name = convertTuple(pizTurk.get_description())
  payment_Process()

  
if selection == "4":
  os.system('cls')
  do_pizza_price = pizDo.get_cost()
  print(convertTuple(pizDo.get_description()) , ' seçtiniz ')
  time.sleep(3)

  do_you_want_sos = input("Sos ister misiniz(e/h): ") 
  if do_you_want_sos == "e":

    os.system('cls')
    print("Bilgilendirme: Sos seçimi için 3 hakkınız var\n")

    count = 3
    while count > i:
      df2 = pd.read_csv("Menu2.txt") #Sosların bulunduğu dosyayı okuyoruz.
      print(df2.head(6))

      sos = str(input("Hangi sosu istersiniz: "))

      if sos == "1":
        sos_name = convertTuple(sosZeytin.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = convertTuple(sosZeytin.get_description()),fiyat = sosZeytin.get_cost()))
          print("-------------------------------")

          sosZeytin_price = sosZeytin.get_cost()
          sosPrice = sosPrice + sosZeytin_price
          time.sleep(1)
          os.system('cls')
      else:
        print('Hatalı seçim yaptınız.!. Tekrar deneyiniz...')
        
      if sos == "2":
        sos_name = convertTuple(sosMantar.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosMantar.get_cost()))
          print("-------------------------------")

          sosMantar_price = sosMantar.get_cost()
          sosPrice = sosPrice + sosMantar_price
          time.sleep(1)
          os.system('cls')
      else:
        print('Hatalı seçim yaptınız.!. Tekrar deneyiniz...')

      if sos == "3":
        sos_name = convertTuple(sosKeciPeyniri.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')

        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosKeciPeyniri.get_cost()))
          print("-------------------------------")

          sosKeciPeyniri_price = sosKeciPeyniri.get_cost()
          sosPrice = sosPrice + sosKeciPeyniri_price
          time.sleep(1)
          os.system('cls')
      else:
        print('Hatalı seçim yaptınız.!. Tekrar deneyiniz...')

      if sos == "4":
        sos_name = convertTuple(sosEt.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosEt.get_cost()))
          print("-------------------------------")

          sosEt_price = sosEt.get_cost()
          sosPrice = sosPrice + sosEt_price
          time.sleep(1)
          os.system('cls')
      else:
        print('Hatalı seçim yaptınız.!. Tekrar deneyiniz...')

      if sos == "5":
        sos_name = convertTuple(sosSogan.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosSogan.get_cost()))
          print("-------------------------------")

          sosSogan_price = sosSogan.get_cost()
          sosPrice = sosPrice + sosSogan_price
          time.sleep(1)
          os.system('cls')
      else:
        print('Hatalı seçim yaptınız.!. Tekrar deneyiniz...')

      if sos == "6":
        sos_name = convertTuple(sosMisir.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosMisir.get_cost()))
          print("-------------------------------")

          sosMisir_price = sosMisir.get_cost()
          sosPrice = sosPrice + sosMisir_price
          time.sleep(1)
          os.system('cls')
      else:
        print('Hatalı seçim yaptınız.!. Tekrar deneyiniz...')

  else:
    total_price = do_pizza_price + sosPrice
    pizza_name = convertTuple(pizDo.get_description())
    payment_Process()

  os.system('cls')
  total_price = do_pizza_price + sosPrice
  print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
  time.sleep(3)
  pizza_name = convertTuple(pizDo.get_description())
  payment_Process()

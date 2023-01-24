import requests

istekadres = input("Adres(Linki) :")
method = int(input("Post/'1' Get İçin/'2' : "))

if method == 1:
    istekpost = requests.post(istekadres) 

if method == 2:
    istekget = requests.get(istekadres)

print("İstekler Başarılı Bir Şekilde Gönderildi.")

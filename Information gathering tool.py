import os
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from colorama import init
from termcolor import colored
import instaloader
import time
import random
import requests
import geocoder
import folium
import requests
import socket

def banner():
    init()

def kontrol(email):
    return email.count('@') == 1

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_adress = s.getsockname()[0]
    s.close()
    return ip_adress

def get_location(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/').json()

    if "city" in response and "region" in response and "country_name" in response:
        location_data = {
            "Ip Adres": ip,
            "Şehir": response.get("city"),
            "Bölge": response.get("region"),
            "Ülke": response.get("country_name")
        }
        return location_data
    else:
        return "Konum verisi bulunamadı."

def get_followers(L, account):
    profile = instaloader.Profile.from_username(L.context, account)
    for follower in profile.get_followers():
        print(follower.username)
        time.sleep(time_amount)

def get_following(L, account):
    profile = instaloader.Profile.from_username(L.context, account)
    for followee in profile.get_followees():
        print(followee.username)
        time.sleep(time_amount)

def mega_data(L, account):
    profile = instaloader.Profile.from_username(L.context, account)
    data = profile._metadata()
    biography = data["biography"]
    followers = data["edge_followed_by"]["count"]
    follow = data["edge_follow"]["count"]
    full_name = data["full_name"]
    username = data["username"]
    print(biography, followers, follow, full_name, username)
    time.sleep(time_amount)

def get_followers_list(L, accounts):
    for account in accounts:
        profile = instaloader.Profile.from_username(L.context, account)
        for follower in profile.get_followers():
            print(follower.username)
            time.sleep(time_amount)

def get_following_list(L, accounts):
    for account in accounts:
        profile = instaloader.Profile.from_username(L.context, account)
        for followee in profile.get_followees():
            print(followee.username)
            time.sleep(time_amount)

def mega_data_list(L, accounts):
    for account in accounts:
        profile = instaloader.Profile.from_username(L.context, account)
        data = profile._metadata()
        biography = data["biography"]
        followers = data["edge_followed_by"]["count"]
        follow = data["edge_follow"]["count"]
        full_name = data["full_name"]
        username = data["username"]
        print(biography, followers, follow, full_name, username)
        time.sleep(time_amount)

def generate_random_password(length, count):
    characters = "abcdefghklmnopqrstuvwxyzABCGHKLMNOPQRSTUVWXYZ1234567890!#$&"
    passwords = []
    for _ in range(count):
        password = ''.join(random.choice(characters) for _ in range(length))
        passwords.append(password)
    return passwords

def main_menu():
    exit_program = False

    while not exit_program:
        islem = input(
            "1] Telefon Numarası ile bilgi topla.\n"
            "2] Instagram İşlemleri. (İki faktörlü doğrulama devre dışı)\n"
            "3] Instagram random şifre oluşturucu.\n"
            "4] Mail kontrolü.\n"
            "5] TC No kontrolü.\n"
            "6] IP adres kontrolü.\n"
            "7] IP konum tespiti.\n"
            "8] IP adresim.\n"
            "9] Çıkış\n"
            "Seçiminiz: "
        )

        if islem == "9":
            exit_program = True
        
        if islem == "8":
            ip_address = get_ip_address()
            print("IP adresim:", ip_address)
            
        elif islem == "7":
            user = input("IP adres girin: ")
            location = get_location(user)
            print(location)

            g = geocoder.ip(user)
            latlng = g.latlng

            if latlng is not None:
                user_map = folium.Map(location=latlng, zoom_start=12)
                folium.Marker(location=latlng, popup=f"IP Adres: {user}").add_to(user_map)
                user_map.save("C:/Users/user/Desktop/chatbot/deneme/test/my_map.html")
                print("Harita oluşturuldu: my_map.html")
            else:
                print("Konum bilgisi bulunamadı.") 
        
        elif islem == "6":
            user = input("IP adres girin: ")
            location = get_location(user)
            print(location)

        elif islem == "5":
            tcno = input("TC No kontrolü: ")

            if len(tcno) != 11:
                print("11 hane girin!")
            else:
                ilkonrakam = tcno[:10]
                sonrakam = tcno[10]
                toplam = sum(int(rakam) for rakam in ilkonrakam)
                toplam = str(toplam)
                if toplam[-1] == sonrakam:
                    print("TC No geçerli/doğru!\n")
                else:
                    print("Geçersiz TC No!\n")
        elif islem == "4":
            mail = input('Mail Adresiniz: ')

            if kontrol(mail):
                print('Mail Adresi Doğru')
            else:
                print('Mail Adresi Yanlış')
        elif islem == "3":
            password_length = int(input("Şifre kaç karakter olsun: "))
            password_count = int(input("Kaç adet şifre olsun: "))
            passwords = generate_random_password(password_length, password_count)
            for password in passwords:
                print("Rastgele Oluşturulan Şifreniz:", password)
        elif islem == "2":
            username = input("Lütfen Kullanıcı Adını Giriniz: ")
            password = input("Lütfen Parolayı Giriniz: ")
            print("Lütfen Bekleyiniz...")

            try:
                L = instaloader.Instaloader()
                L.login(username, password)

                while True:
                    islem_2 = input(
                        "1-Takip Edilen Bilgisini Al\n"
                        "2-Takipçi Bilgisini Al\n"
                        "3-Hesap Bilgisini Al\n"
                        "4-Çıkış\n"
                        "Seçiminiz: "
                    )

                    if islem_2 == "4":
                        print("Çıkış Yapıldı.")
                        break
                    elif islem_2 == "1":
                        secenek = input("1-Bir Kullanıcı\n2-Birden Fazla Kullanıcı\nSeçiminiz: ")

                        if secenek == "1":
                            account = input("Lütfen Takipçi Bilgisi Alınacak Kişinin Kullanıcı Adını Giriniz: ")
                            get_following(L, account)
                        elif secenek == "2":
                            account = input("Lütfen Kullanıcı Adlarını Aralarında Boşluk Bırakarak Giriniz: ")
                            accounts = account.split()
                            get_following_list(L, accounts)
                    elif islem_2 == "2":
                        secenek = input("1-Bir Kullanıcı\n2-Birden Fazla Kullanıcı\nSeçiminiz: ")

                        if secenek == "1":
                            account = input("Lütfen Takipçi Bilgisi Alınacak Kişinin Kullanıcı Adını Giriniz: ")
                            get_followers(L, account)
                        elif secenek == "2":
                            account = input("Lütfen Kullanıcı Adlarını Aralarında Boşluk Bırakarak Giriniz: ")
                            accounts = account.split()
                            get_followers_list(L, accounts)
                    elif islem_2 == "3":
                        secenek = input("1-Bir Kullanıcı\n2-Birden Fazla Kullanıcı\nSeçiminiz: ")

                        if secenek == "1":
                            account = input("Lütfen Takipçi Bilgisi Alınacak Kişinin Kullanıcı Adını Giriniz: ")
                            mega_data(L, account)
                        elif secenek == "2":
                            account = input("Lütfen Kullanıcı Adlarını Aralarında Boşluk Bırakarak Giriniz: ")
                            accounts = account.split()
                            mega_data_list(L, accounts)
                    else:
                        print("Lütfen 1-4 Aralığında Değer Giriniz.")
            except Exception as err:
                print("Bağlantı Sağlanamadı. Lütfen Tekrar Deneyiniz.")
                print(err)
        elif islem == "1":
            banner()
            number = input(colored("Telefon Numarasını ülke kodu ile birlikte girin.(Türkiye (+90)): ", "red"))
            phone_number = phonenumbers.parse(number, None)
            #print("Ülke/Şehir: ", geocoder.description_for_number(phone_number, 'tr'))
            print("Saat dilimi: ", timezone.time_zones_for_number(phone_number))
            print("Operatör: ", carrier.name_for_number(phone_number, 'tr'))
        else:
            print("Lütfen seçeneklerden birini seçin.")

if __name__ == "__main__":
    name = input("Kullanıcı adı girin: ")
    print(name + " giriş sağladı!")
    time_amount = 0.5
    main_menu()

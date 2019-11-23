#coding=utf-8
#coding=utf-8
try:
    from PIL import Image
    from PIL import ImageFile
except:
    import os
    os.system('pip install Pillow')
    from PIL import Image
    from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES=True

def full_eight(str):
    return str.zfill(8)
def get_text_bin(strr):
    string=""
    s_text=strr.encode()
    for i in range(len(s_text)):
        string=string+full_eight(bin(s_text[i]).replace('0b',''))
    return string
def mod(x,y):
    return x%y
def tell_you_bad(str1,str2,str3):
    im=Image.open(str1)
    width=im.size[0]
    height=im.size[1]
    count=0
    key=get_text_bin(str2)
    keylen=len(key)
    for h in range(0,height):
        for w in range(0,width):
            pixel=im.getpixel((w,h))
            a=pixel[0]
            b=pixel[1]
            c=pixel[2]
            if count==keylen:
                break
            a=a-mod(a,2)+int(key[count])
            count+=1
            if count==keylen:
                im.putpixel((w,h),(a,b,c))
                break
            b=b-mod(b,2)+int(key[count])
            count+=1
            if count==keylen:
                im.putpixel((w,h),(a,b,c))
                break
            c=c-mod(c,2)+int(key[count])
            count+=1
            if count==keylen:
                im.putpixel((w,h),(a,b,c))
                break
            if count%3==0:
                im.putpixel((w,h),(a,b,c))
    im.save(str3)
def tell_you_fun(le,str1):
    a=""
    b=""
    im = Image.open(str1)
    lenth = le*8
    width = im.size[0]
    height = im.size[1]
    count = 0
    for h in range(0, height):
        for w in range(0, width):
            pixel = im.getpixel((w, h))
            if count%3==0:
                count+=1
                b=b+str((mod(int(pixel[0]),2)))
                if count ==lenth:
                    break
            if count%3==1:
                count+=1
                b=b+str((mod(int(pixel[1]),2)))
                if count ==lenth:
                    break
            if count%3==2:
                count+=1
                b=b+str((mod(int(pixel[2]),2)))
                if count ==lenth:
                    break
        if count == lenth:
            break
    st=""
    for i in range(0,len(b),8):
        stra = int(b[i:i+8],2)
        st+=chr(stra)
    return st
def main():
    print("------------------------------------------------------------------------------------------------------------")
    print("| _______   _          _                          _________        __   __  ____  ____                     |")
    print("||_   __ \ (_)        / |_                       |  _   _  |      [  | [  ||_  _||_  _|                    |")
    print("|  | |__) |__   .---.`| |-'__   _   _ .--.  .---.|_/ | | \_|.---.  | |  | |  \ \  / / .--.   __   _        |")
    print("|  |  ___/[  | / /'`\]| | [  | | | [ `/'`\]/ /__\\   | |   / /__\\ | |  | |   \ \/ // .'`\ \[  | | |         |")
    print("| _| |_    | | | \__. | |, | \_/ |, | |    | \__.,  _| |_  | \__., | |  | |   _|  |_| \__. | | \_/ |,      |")
    print("||_____|  [___]'.___.'\__/ '.__.'_/[___]    '.__.' |_____|  '.__.'[___][___] |______|'.__.'  '.__.'_/ v0.1 |")
    print("------------------------------------------------------------------------------------------------------------")
    print("                         BY-SRPIHOT*  BLOG'S Srpihot.site ANTI-TECH/Painter/0e0w")
    print("加密(1) OR 解密(2):",end=' ')
    choice=int(input())
    if choice==1:
        try:
            print("[+]加密图片:",end=' ')
            old=input()
            print("[+]加密文字(以#号结束):",end=' ')
            kkk=input()
            print("[+]加密图片保存重命名:",end=' ')
            new=input() 
            tell_you_bad(old,kkk,new)
            print("[+]Fun Picture done!")
        except:
            print("[-]未找到此图片，请检查图片名和路径")

    if choice==2:
        le = 30
        try:
            print("[+]解密图片:",end=' ')
            new = input()
            word=tell_you_fun(le,new).split('#')
            print('[+]Picture Tell You: ',word[0])
        except:
            print("[-]未找到此图片，请检查图片名和路径")
if __name__=="__main__":
    main()
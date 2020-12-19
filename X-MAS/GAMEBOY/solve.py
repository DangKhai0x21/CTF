# tshark -r capture.pcapng -T fields -e data -e tcp.port | tr '\n' '-' > data.txt
# You can use scapy to extract data & analyze
# https://bgb.bircd.org/bgblink.html
# https://datacrystal.romhacking.net/wiki/Pok%C3%A9mon_Red_and_Blue:TBL
# python3

list_ = {"4F":" " ,"57":"#","51":"*","52":"A1","53":"A2","54":"POKé","55":"+","58":"$","75":"…","7F":" ","80":"A","81":"B","82":"C","83":"D","84":"E","85":"F","86":"G","87":"H","88":"I","89":"J","8A":"K","8B":"L","8C":"M","8D":"N","8E":"O","8F":"P","90":"Q","91":"R","92":"S","93":"T","94":"U","95":"V","96":"W","97":"X","98":"Y","99":"Z","9A":"(","9B":")","9C":":","9D":";","9E":"[","9F":"]","A0":"a","A1":"b","A2":"c","A3":"d","A4":"e","A5":"f","A6":"g","A7":"h","A8":"i","A9":"j","AA":"k","AB":"l","AC":"m","AD":"n","AE":"o","AF":"p","B0":"q","B1":"r","B2":"s","B3":"t","B4":"u","B5":"v","B6":"w","B7":"x","B8":"y","B9":"z","BA":"é","BB":"'d","BC":"'l","BD":"'s","BE":"'t","BF":"'v","E0":"'","E1":"{","E2":"}","E3":"-","E4":"'r","E5":"'m","E6":"?","E7":"!","E8":".","ED":"→","EE":"↓","EF":"♂","F0":"¥","F1":"×","F3":"/","F4":",","F5":"♀","F6":"0","F7":"1","F8":"2","F9":"3","FA":"4","FB":"5","FC":"6","FD":"7","FE":"8","FF":"9"}


def parse_pk(dt_pk,port,f1,fm):
	port = port.split(",")[0]
	d = ""
	if port == "1337":
		d = "1"
	else:
		d = "0"	
	cmd = parse_command(dt_pk[:2])

	if cmd == "version":
		return parse_version(dt_pk,d)

	b2 = dt_pk[2:4]
	b2_bin = bin(int(b2,16))[2:]
	b2_bin_full = b2_bin + '0'*(8-len(b2_bin))

	if cmd == "joypad":
		return parse_joypad(dt_pk,b2_bin_full,d)

	b3 = bin(int(dt_pk[4:6],16))[2:]
	b3_bin_full = b3 + '0'*(8-len(b3))

	if cmd == "syn1":
		z = parse_syn1(dt_pk,b3_bin_full,d,fm)
		f1.write(z + "\r\n")
		return z

	if cmd == "syn2":
		return parse_syn2(dt_pk,d)

	if cmd == "syn3":
		return parse_syn3(dt_pk,d)

	if cmd == "status":
		return parse_status(dt_pk,d)		

def parse_command(b1):
	if b1 == "01":
		return "version"
	if b1 == "65":
		return "joypad"
	if b1 == "68":
		return "syn1"
	if b1 == "69":
		return "syn2"
	if b1 == "6a":
		return "syn3"
	if b1 == "6c":
		return "status"					

def parse_version(dt_pk,d):
	return "{} version: b1:{} b2:{} b3:{} b4:{} i1:{}".format(d,dt_pk[:2],dt_pk[2:4],dt_pk[4:6],dt_pk[6:8],dt_pk[8:])

def parse_joypad(dt_pk,b2_bin_full,d):
	pr_rl = ""
	if b2_bin_full[3] == 1:
		pr_rl = "pressed"
	else:
		pr_rl = "released"
	return "{} joypad: b1:{} b2:{} b3:{} b4:{} i1:{}".format(d,dt_pk[:2],pr_rl,0,0,0)

def parse_syn1(dt_pk,b3_bin_full,d,messenge):
	for key,value in list_.items():
		if key == dt_pk[2:4].upper():
			fm.write(value)
	return "{} syn1 b1:{} b2:{} b3:h-{}:d-{} b4:{} i1:{}".format(d,dt_pk[:2],dt_pk[2:4],b3_bin_full[1],b3_bin_full[2],0,dt_pk[8:])

def parse_syn2(dt_pk,d):
	return "{} syn2 b1:{} b2:{} b3:{} b4:{} i1:{}".format(d,dt_pk[:2],dt_pk[2:4],dt_pk[4:6],0,0)	

def parse_syn3(dt_pk,d):
	return "{} syn3 b1:{} b2:{} b3:{} b4:{} i1:{}".format(d,dt_pk[:2],dt_pk[2:4],dt_pk[4:6],dt_pk[6:8],dt_pk[8:])

def parse_status(dt_pk,d):		
	return "{} status b1:{} b2:{} b3:{} b4:{} i1:{}".format(d,dt_pk[:2],dt_pk[2:4],0,0,0)

if __name__ == '__main__':
	fp = open("data1.txt","r").read()
	fw = open("result.txt","w")
	f1 = open("syn1.txt","a")
	fm = open("messenge.txt","a")
	cipher = fp.split("-")
	mess = ""
	for i in range(0,len(cipher)):
		if len(cipher[i]) < 13:
			continue
		rs = parse_pk(cipher[i].split("\t")[1],cipher[i].split("\t")[0],f1,fm)
		mess += rs + "\r\n"

	print ("[+] Data analysis pcap save as data1.txt")
	print ("[+] Data analysis syn1 save as syn1.txt")
	print ("[+] messenge save as messenge.txt")		
	fw.write(mess)
	fw.close()

import base64

fp = open("z","r").read()

base64_message = fp

while True:
	base64_byte = base64_message[::-1]
	base64_bytes = base64_byte.encode('ascii')
	message_bytes = base64.b64decode(base64_bytes)
	base64_message = message_bytes.decode('ascii')
	if "CTF" in base64_message:
		print base64_message
		break

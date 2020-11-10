from PIL import Image

folder_broken = "./QuickFix/"

total_frame = 100

png_header = "89504e470d0a1a0a0000000d"
jpg_header = "ffd8ffe000104a4649460000000d"


def fix_magic_bytes():
	# image size 20x20 -> flag image after concat with size 20 * 100 x 20 *100
	flag = Image.new('RGB',(2000,2000))

	for first in range(total_frame):
		for second in range(total_frame):
			fp_read = open("{}flag_{}_{}.jpg".format(folder_broken,first,second),"rb")
			hex_file_broken = (fp_read.read()).encode("hex")

			hex_file_fixed  = hex_file_broken.replace(jpg_header,png_header)

			fp_write = open("temp.png","wb")
			fp_write.write(hex_file_fixed.decode("hex"))
			fp_write.close()

			img_open = Image.open("temp.png")
			flag.paste(img_open,(first*20,second*20))

			fp_read.close()

	flag.save("flag.png")
	print "[+] Open flag.png to get flag"		

if __name__ == '__main__':
	fix_magic_bytes()

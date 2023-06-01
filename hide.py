from PIL import Image

def genData(data):

		newd = []

		for i in data:
			newd.append(format(ord(i), '08b'))
		return newd


def main():
	a = int(input(":: Welcome to Steganography ::\n"
						"1. Encode\n2. Decode\n"))
	if (a == 1):
		encode()

	elif (a == 2):
		print("Decoded Word : " + decode())
	else:
		raise Exception("Enter correct input")
	    
def modPix(pix, data):

	datalist = genData(data)
	lendata = len(datalist)
	imdata = iter(pix)

	for i in range(lendata):

		
		pix = [value for value in imdata.__next__()[:3] +
								imdata.__next__()[:3] +
								imdata.__next__()[:3]]

		
		for j in range(0, 8):
			if (datalist[i][j] == '0' and pix[j]% 2 != 0):
				pix[j] -= 1

			elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
				if(pix[j] != 0):
					pix[j] -= 1
				else:
					pix[j] += 1
				# pix[j] -= 1

		
		if (i == lendata - 1):
			if (pix[-1] % 2 == 0):
				if(pix[-1] != 0):
					pix[-1] -= 1
				else:
					pix[-1] += 1

		else:
			if (pix[-1] % 2 != 0):
				pix[-1] -= 1

		pix = tuple(pix)
		yield pix[0:3]
		yield pix[3:6]
		yield pix[6:9]

def encode_enc(newimg, data):
	

    print("what is image size: ",newimg.size)
    w=newimg.size[0]
    (x,y)=(0,0)
    for pixel in modPix(newimg.getdata(),data):
        print("what is pixel:",pixel)
        newimg.putpixel((x,y),pixel)
        if(x==w-1):
            x = 0
            y += 1
            
        else:
            x +=1
	    
def encode():
	img=input("enter image (with ext and png format): ")
	myimg=Image.open(img,"r")
	data= input("enter data to be encoded: ")
	if(len(data)==0):
		raise ValueError("data is empty")
	newimg=myimg.copy()
	encode_enc(newimg,data)
	finalImag_name=input("enter the name of the image(with ext and ong format): ")
	newimg.save(finalImag_name,str(finalImag_name.split(".")[1].upper()))




def decode():
	img=input("enter image (with ext and png format): ")
	myimg=Image.open(img,"r")
	data=""
	imageData=iter(myimg.getdata())
	print(imageData)
	while True:
		pixels= [value for value in imageData.__next__()[:3] +
                imageData.__next__()[:3] +
                imageData.__next__()[:3]]
		print("what is pixels",pixels)
		binstr=""
		for i in pixels[:8]:
			if (i%2 == 0):
				binstr+="0"
			else:
				binstr+="1"
		data+=chr(int(binstr,2))
		print("what is the data",data)
		if(pixels[-1] % 2 !=0):
			return data
		
	
	
		

	   
	
	
    


# Driver Code
if __name__ == '__main__' :

	# Calling main function
	main()
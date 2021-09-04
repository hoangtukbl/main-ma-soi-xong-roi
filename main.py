def tim(a,n,ten):				#tim nguoi con song
	p=1000
	for i in range(n):
		string=a[i]
		if string.find(ten) != -1 :
			p=0
	return p		


def chon(p):					#chon
	m = int(input(p))
	return m


#dem soi
def lsoi(n,a):
	dem =0 
	for i in range(n):
		string=a[i]
		if string.find("soi") != -1 :
			dem = dem +1
	return dem


#dem dan
def ldan(n,a):
	dem = 0 
	for i in range(n):
		string=a[i]
		if string != 'chet' :
			if string.find("soi") == -1 :
				dem = dem +1
	return dem


#giet
def giet(a,i):
	if a[i]=='hunter':
		keo=chon('chọn người để kéo theo: ')
		giet(a,keo)
	a[i]='chet'
	return


import random					#random

# Input
n = int(input("Nhập số lượng người chơi:"))
role = ["baove", "phuthuy", "soi1", "soi2", "dan1", "dan2",
        "ban", "hunter", "truonglang", "soi3", "dan3", "boi"]
#          0         1        2        3      4       5
#          6          7        8         9          10      11


# Random Role
a = []
m = random.sample(range(n), n)
for i in range(0, n):
    b = m[i]
    a.append(role[b])
print(a)

#gan san
dcv2=1000
cuu=0
doc=1000

while lsoi(n,a)!=0 :
	
	#baove
	if tim(a,n,'baove') == 0 :
		dcv1=chon("chọn người để bảo vệ: ")
		while dcv1 == dcv2:
			dcv1=chon("chọn lại đi mày chọn nó hôm qua r: ")
		dcv2 = dcv1
	else:
		dcv2=1000
	
	#soi
	if tim(a,n,'soi')==0:
		can = chon('vote người để cắn: ')
		while a[can]=='chet':
			can=chon('chọn lại đi nó chết rồi để nó yên nghỉ: ')
	
	#boi
	if tim(a,n,'boi')==0 :
		xrole=chon('chọn người để xem role: ')
		while a[xrole]=='chet' :
			xrole=chon('chọn lại đi nó chết rồi để nó yên nghỉ: ')
		if a[xrole].find("soi") != -1 :
			print('sói')
		else:
			print('dân')

	#phu thuy
	if tim(a,n,'phuthuy')==0:
		print(can,' sẽ bị cắn, nhập 1 để cứu, 0 để không cứu: ')
		if cuu == 0:
			cuu=chon(' ')
			if cuu == 1:
				can = 1000
		if doc == 1000:
			doc=chon('chọn người để đầu đọc, nhập 1000 để không chọn ai cả: ')
			if doc <= n :
				while a[doc]=='chet':
					doc = chon('chọn lại đi nó chết rồi để nó yên nghỉ: ')
				giet(a,doc)
	

	if can == dcv2 :
		can = 1000
	if can <= n:
		if a[can]=='ban':
			a[can]='soi'
		else:

			giet(a,can)
	treoco=chon('chọn người để treo cổ: ')
	while a[treoco]=='chet':
		treoco=chon('chọn lại đi nó chết rồi để nó yên nghỉ: ')
	giet(a,treoco)

	print(a)

	if lsoi(n,a) == ldan(n,a):
		print('sói thắng')
		break
	if lsoi(n,a) == 0:
		print('dân thắng')
		break

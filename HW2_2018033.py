# CSE 101 - IP HW2
# K-Map Minimization 
# Name: DUSHYANT PANCHAL
# Roll Number: 2018033
# Section: A
# Group: 1
# Date: 12-10-2018


def Bin(dec,bits):
#Returns binary form of the decimal number in string form.
	temp=dec
	
	b=''
	for i in range(bits):
		b = str(temp%2) + b
		temp//=2

	return b


def binNext(string):
#Returns next binary number having same number of bits
#provided the input is not the largest possible bin no.

	n=len(string)
	k=string[::-1].find('0')
	k=n-k-1
	string1=''
	for i in range(n):
		if(i==k):
			string1+='1'
		elif(i>k):
			string1+='0'
		else:
			string1+=string[i]
	return string1


def getDiffDigit(string1, string2, bits):
#Inputs string1 and string2 should be binary
#no.s in string form having 'bits' number of bits.
#Returns index having different digit in case the two
#numbers differ by only one digit and else returns -1.

	diff=-1
	ctr=0
	for i in range(bits):
		if(string1[i]!=string2[i]):
			diff=i
			ctr+=1

	if(ctr==1):
		return diff
	else:
		return -1


def listInput(string,bits):
#Decodes the input string to the required format of the program
#Returns a list having 2**bits integer elements 0, 1 or 2.
#2 represents a don't care condition.

	beg=string.find('(') + 1
	end=string.find(')')

	if(string[beg:end].find(",")!=-1):
		ones=list(map(int,(string[beg:end].split(","))))
	elif(string[beg:end].isdigit()):
		ones=list()
		ones.append(int(string[beg:end]))
	else:
		ones=list()
	#Getting the minterms.

	b1=string.find('d (')
	dontCares=list()
	if(b1!=-1):
		b1+=3
		e1=string.find(')',b1)
		dontCares=list(map(int,(string[b1:e1]).split(",")))
	#Getting the don't cares

	kmap=list()
	for i in range(2**bits):
		if(i in ones):
			kmap.append(1)
		elif(i in dontCares):
			kmap.append(2)
		else:
			kmap.append(0)

	return kmap


def expression(sop,bits):
#Returns the final expression from the encoded
#minimized sop as calculated by the program.
#sop - should be a list containing sop terms.
	#print("SOP: ",sop)

	if('_'*bits in sop):
		return '1'
	elif(len(sop)==0):
		return '0'
	else:
		exp=''
		for i in sop:
			for j in range(bits):
				if(j==0 and i[j]=='0'):
					exp+='w\'.'
				elif(j==0 and i[j]=='1'):
					exp+='w.'
				elif(j==1 and i[j]=='0'):
					exp+='x\'.'
				elif(j==1 and i[j]=='1'):
					exp+='x.'
				elif(j==2 and i[j]=='0'):
					exp+='y\'.'
				elif(j==2 and i[j]=='1'):
					exp+='y.'
				elif(j==3 and i[j]=='0'):
					exp+='z\'.'
				elif(j==3 and i[j]=='1'):
					exp+='z.'
			
			exp=exp[:-1]
			exp+=' + '

		return (exp[:len(exp)-3])


def minimize(kmap,bits):
#The core function of this module
#Minimizes the given boolean expression
#in case of no don't care condition

	minTerms=list()
	for i in range(2**bits):
		if(kmap[i]==1):
			minTerms.append(Bin(i,bits))
	#print(minTerms)

	for g in range(bits):

		temp=list()
		for b in minTerms:
			temp.append(b)

		l=len(minTerms)

		for i in range(l-1):
			for j in range(i+1,l):
				k=getDiffDigit(minTerms[i],minTerms[j],bits)
				if(k!=-1):
					red=''
					for p in range(bits):
						if(p==k):
							red+='_'
						else:
							red+=minTerms[j][p]

					#print(g+1,"=>",i,j,red, minTerms,":",temp)
					if((minTerms[i] in temp) or (minTerms[j] in temp)):
						temp.append(red)					
					if((minTerms[i] in temp) and minTerms[i]!=red):
						temp.remove(minTerms[i])
					if((minTerms[j] in temp) and minTerms[i]!=red):
						temp.remove(minTerms[j])
					#print(g+1,"  ",i,j,red, minTerms,":",temp)

		minTerms=list()
		for a in temp:
			if(a not in minTerms):
				minTerms.append(a)
		
		#print(minTerms)

		if(g==bits-1):
			return (minTerms)


def KmapsDC(kmap,dontCares,bits):
#Finds and compares possible solutions and returns the
#simplest expression when don't care condition given.

	n=len(dontCares)
	BIN='0'*n

	minSOP=list()

	for i in range(2**n):
		for j in range(n):
			kmap[dontCares[j]]=int(BIN[j])
		sop=minimize(kmap,bits)
		minSOP.append(expression(sop,bits))
		BIN=binNext(BIN)


	print("\nPOSSIBLE EXPRESSIONS:")
	for a in minSOP:
		print("->",a)

	operCount=list()
	for i in minSOP:
		operCount.append(i.count('.')+i.count('+'))

	m=min(operCount)

	stringOut=''
	print("\nSIMPLEST EXPRESSION(s):")
	for i in range(len(operCount)):
		if(operCount[i]==m):
			print("->",minSOP[i])
			stringOut+=minSOP[i] + " OR "

	return stringOut[:-4]


def minFunc(var, string):
	"""
        This python function takes function of maximum of 4 variables
        as input and gives the corresponding minimized function(s)
        as the output (minimized using the K-Map methodology),
        considering the case of Don’t Care conditions.

	Input is a string of the format (a0,a1,a2, ...,an) d(d0,d1, ...,dm)
	Output is a string representing the simplified Boolean Expression in
	SOP form.

	"""
	
	#var=int(input("Enter number of variables: "))
	#string=input("Enter minterms as per the format:")

	kmap=listInput(string,var)	

	if(var==2):
		# 2 variable
		print()
		print("   \\x              ")
		print("   w\\   0      1   ")
		print("     \\_____________")
		print("     |      |      |")
		print("  0  |  %d   |  %d   |"%(kmap[0],kmap[1]))
		print("     |______|______|")
		print("     |      |      |")
		print("  1  |  %d   |  %d   |"%(kmap[2],kmap[3]))
		print("     |______|______|")
		print("\n(-> 2 represents Don\'t care conditions.)\n")

	elif(var==3):
		# 3 variable
		print()
		print("   \\xy                            ")
		print("   w\\   00     01     11     10   ")
		print("     \\___________________________ ")
		print("     |      |      |      |      |")
		print("  0  |  %d   |  %d   |  %d   |  %d   |"%(kmap[0],kmap[1],kmap[3],kmap[2]))
		print("     |______|______|______|______|")
		print("     |      |      |      |      |")
		print("  1  |  %d   |  %d   |  %d   |  %d   |"%(kmap[4],kmap[5],kmap[7],kmap[6]))
		print("     |______|______|______|______|")
		print("\n(-> 2 represents Don\'t care conditions.)\n")

	elif(var==4):
		# 4 variable
		print()
		print("   \\yz                            ")
		print("  wx\\   00     01     11     10   ")
		print("     \\___________________________ ")
		print("     |      |      |      |      |")
		print("  00 |  %d   |  %d   |  %d   |  %d   |"%(kmap[0],kmap[1],kmap[3],kmap[2]))
		print("     |______|______|______|______|")
		print("     |      |      |      |      |")
		print("  01 |  %d   |  %d   |  %d   |  %d   |"%(kmap[4],kmap[5],kmap[7],kmap[6]))
		print("     |______|______|______|______|")
		print("     |      |      |      |      |")
		print("  11 |  %d   |  %d   |  %d   |  %d   |"%(kmap[12],kmap[13],kmap[15],kmap[14]))
		print("     |______|______|______|______|")
		print("     |      |      |      |      |")
		print("  10 |  %d   |  %d   |  %d   |  %d   |"%(kmap[8],kmap[9],kmap[11],kmap[10]))
		print("     |______|______|______|______|")
		print("\n(-> 2 represents Don\'t care conditions.)\n")

	stringOut=''
	if(2 not in kmap):
		sop=minimize(kmap,var)
		minSOP=expression(sop,var)
		print("\nMINIMIZED SOP EXPRESSION: ",minSOP)
		stringOut=minSOP
	
	else:
		ds=list()
		for i in range(len(kmap)):
			if(kmap[i]==2):
				ds.append(i)

		stringOut=KmapsDC(kmap,ds,var)

	return stringOut
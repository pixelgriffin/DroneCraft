import sys

avg = 0
bracket1 = []
bracket2 = []
bracket3 = []
bracket4 = []
bracket5 = []
bracket6 = []

with open (sys.argv[1], 'r') as results:
	for line in results:
		if int(line) >= 0 and int(line) <= 1999:
			bracket1.append(line) 
		if int(line) >= 2000 and int(line) <= 3999:
			bracket2.append(line) 
		if int(line) >= 4000 and int(line) <= 5999:
			bracket3.append(line) 
		if int(line) >= 6000 and int(line) <= 7999:
			bracket4.append(line) 
		if int(line) >= 8000 and int(line) <= 9999:
			bracket5.append(line) 
		#if int(line) >= 5000:
		#	bracket6.append(line) 
		avg += int(line)
'''
file1 = open ("range0-999", 'w')
file2 = open ("range1000-1999", 'w')
file3 = open ("range2000-2999", 'w')
file4 = open ("range3000-3999", 'w')
file5 = open ("range4000-4999", 'w')
file6 = open ("range5000-inf", 'w')
numFile = open ("distribution", 'w')
			
for i in range (0, len(bracket1)):
	file1.write (bracket1[i])
for i in range (0, len(bracket2)):
	file2.write (bracket2[i])
for i in range (0, len(bracket3)):
	file3.write (bracket3[i])
for i in range (0, len(bracket4)):
	file4.write (bracket4[i])
for i in range (0, len(bracket5)):
	file5.write (bracket5[i])
for i in range (0, len(bracket6)):
	file6.write (bracket6[i])

numFile.write (str(len(bracket1)) + "\n")
numFile.write (str(len(bracket2)) + "\n")
numFile.write (str(len(bracket3)) + "\n")
numFile.write (str(len(bracket4)) + "\n")
numFile.write (str(len(bracket5)) + "\n")
numFile.write (str(len(bracket6)) + "\n")
'''
avg /= 500
			
print (avg)
print ("0-1999: " + str(len(bracket1)))
print ("2000-3999: " + str(len(bracket2)))
print ("4000-5999: " + str(len(bracket3)))
print ("6000-7999: " + str(len(bracket4)))
print ("8000-9600: " + str(len(bracket5)))
#print ("=<5000: " + str(len(bracket6)))

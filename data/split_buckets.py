import os
import sys

args = sys.argv
filename = args[1]

if os.path.exists(f"{filename}_buckets"):
	print("already exist")
	sys.exit()

os.mkdir(f"{filename}_buckets")
os.chdir(f"{filename}_buckets")

test0 = open("test0.gsp", "w")
test1 = open("test1.gsp", "w")
test2 = open("test2.gsp", "w")
test3 = open("test3.gsp", "w")
test4 = open("test4.gsp", "w")
test5 = open("test5.gsp", "w")
test6 = open("test6.gsp", "w")
test7 = open("test7.gsp", "w")
test8 = open("test8.gsp", "w")
test9 = open("test9.gsp", "w")

train0 = open("train0.gsp", "w")
train1 = open("train1.gsp", "w")
train2 = open("train2.gsp", "w")
train3 = open("train3.gsp", "w")
train4 = open("train4.gsp", "w")
train5 = open("train5.gsp", "w")
train6 = open("train6.gsp", "w")
train7 = open("train7.gsp", "w")
train8 = open("train8.gsp", "w")
train9 = open("train9.gsp", "w")

with open(f"../{filename}.gsp", "r") as f:
	i = 0
	flag = True
	for line in f:
		if line != "\n":
			word = line.split()
			if word[0] == "t":
				if word[3] == "-1":
					flag = False

		if flag == True:
			if i % 10 == 0:
				test0.write(line)
				train1.write(line)
				train2.write(line)
				train3.write(line)
				train4.write(line)
				train5.write(line)
				train6.write(line)
				train7.write(line)
				train8.write(line)
				train9.write(line)
			elif i % 10 == 1:
				train0.write(line)
				test1.write(line)
				train2.write(line)
				train3.write(line)
				train4.write(line)
				train5.write(line)
				train6.write(line)
				train7.write(line)
				train8.write(line)
				train9.write(line)
			elif i % 10 == 2:
				train0.write(line)
				train1.write(line)
				test2.write(line)
				train3.write(line)
				train4.write(line)
				train5.write(line)
				train6.write(line)
				train7.write(line)
				train8.write(line)
				train9.write(line)
			elif i % 10 == 3:
				train0.write(line)
				train1.write(line)
				train2.write(line)
				test3.write(line)
				train4.write(line)
				train5.write(line)
				train6.write(line)
				train7.write(line)
				train8.write(line)
				train9.write(line)
			elif i % 10 == 4:
				train0.write(line)
				train1.write(line)
				train2.write(line)
				train3.write(line)
				test4.write(line)
				train5.write(line)
				train6.write(line)
				train7.write(line)
				train8.write(line)
				train9.write(line)
			elif i % 10 == 5:
				train0.write(line)
				train1.write(line)
				train2.write(line)
				train3.write(line)
				train4.write(line)
				test5.write(line)
				train6.write(line)
				train7.write(line)
				train8.write(line)
				train9.write(line)
			elif i % 10 == 6:
				train0.write(line)
				train1.write(line)
				train2.write(line)
				train3.write(line)
				train4.write(line)
				train5.write(line)
				test6.write(line)
				train7.write(line)
				train8.write(line)
				train9.write(line)
			elif i % 10 == 7:
				train0.write(line)
				train1.write(line)
				train2.write(line)
				train3.write(line)
				train4.write(line)
				train5.write(line)
				train6.write(line)
				test7.write(line)
				train8.write(line)
				train9.write(line)
			elif i % 10 == 8:
				train0.write(line)
				train1.write(line)
				train2.write(line)
				train3.write(line)
				train4.write(line)
				train5.write(line)
				train6.write(line)
				train7.write(line)
				test8.write(line)
				train9.write(line)
			elif i % 10 == 9:
				train0.write(line)
				train1.write(line)
				train2.write(line)
				train3.write(line)
				train4.write(line)
				train5.write(line)
				train6.write(line)
				train7.write(line)
				train8.write(line)
				test9.write(line)

		if line == "\n":
			if flag==True:
				i += 1
			else:
				flag = True

with open(f"../{filename}.gsp", "r") as f:
	i = 0
	flag = True
	for line in f:
		if line != "\n":
			word = line.split()
			if word[0] == "t":
				if word[3] == "1":
					flag = False

		if flag == True:
			if i % 10 == 0:
				test0.write(line)
				train1.write(line)
				train2.write(line)
				train3.write(line)
				train4.write(line)
				train5.write(line)
				train6.write(line)
				train7.write(line)
				train8.write(line)
				train9.write(line)
			elif i % 10 == 1:
				train0.write(line)
				test1.write(line)
				train2.write(line)
				train3.write(line)
				train4.write(line)
				train5.write(line)
				train6.write(line)
				train7.write(line)
				train8.write(line)
				train9.write(line)
			elif i % 10 == 2:
				train0.write(line)
				train1.write(line)
				test2.write(line)
				train3.write(line)
				train4.write(line)
				train5.write(line)
				train6.write(line)
				train7.write(line)
				train8.write(line)
				train9.write(line)
			elif i % 10 == 3:
				train0.write(line)
				train1.write(line)
				train2.write(line)
				test3.write(line)
				train4.write(line)
				train5.write(line)
				train6.write(line)
				train7.write(line)
				train8.write(line)
				train9.write(line)
			elif i % 10 == 4:
				train0.write(line)
				train1.write(line)
				train2.write(line)
				train3.write(line)
				test4.write(line)
				train5.write(line)
				train6.write(line)
				train7.write(line)
				train8.write(line)
				train9.write(line)
			elif i % 10 == 5:
				train0.write(line)
				train1.write(line)
				train2.write(line)
				train3.write(line)
				train4.write(line)
				test5.write(line)
				train6.write(line)
				train7.write(line)
				train8.write(line)
				train9.write(line)
			elif i % 10 == 6:
				train0.write(line)
				train1.write(line)
				train2.write(line)
				train3.write(line)
				train4.write(line)
				train5.write(line)
				test6.write(line)
				train7.write(line)
				train8.write(line)
				train9.write(line)
			elif i % 10 == 7:
				train0.write(line)
				train1.write(line)
				train2.write(line)
				train3.write(line)
				train4.write(line)
				train5.write(line)
				train6.write(line)
				test7.write(line)
				train8.write(line)
				train9.write(line)
			elif i % 10 == 8:
				train0.write(line)
				train1.write(line)
				train2.write(line)
				train3.write(line)
				train4.write(line)
				train5.write(line)
				train6.write(line)
				train7.write(line)
				test8.write(line)
				train9.write(line)
			elif i % 10 == 9:
				train0.write(line)
				train1.write(line)
				train2.write(line)
				train3.write(line)
				train4.write(line)
				train5.write(line)
				train6.write(line)
				train7.write(line)
				train8.write(line)
				test9.write(line)

		if line == "\n":
			if flag==True:
				i += 1
			else:
				flag = True

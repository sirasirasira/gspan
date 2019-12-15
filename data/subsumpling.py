import os
import sys
import random

args = sys.argv
filename = args[1]

if os.path.exists(f"{filename}_subsample"):
	print("already exist")
	sys.exit()

os.mkdir(f"{filename}_subsample")
os.chdir(f"{filename}_subsample")

data_num = 0
with open(f"../{filename}.gsp", "r") as f:
	for line in f:
		if line == "\n":
			data_num += 1

sample_num = int(data_num * 0.1)
index_list = list(range(data_num))

for i in range(100):
	random.shuffle(index_list)
	sample_index = index_list[0 : sample_num]
	output = open(f"sample{i}.gsp", "w")

	with open(f"../{filename}.gsp", "r") as f:
		j = 0
		for line in f:
			if j in sample_index:
				output.write(line)
			if line == "\n":
				j += 1

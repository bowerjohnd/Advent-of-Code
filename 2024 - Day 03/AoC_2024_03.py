import re


######################
######################
# Part 1 : success with minimal difficulty
#		- read input file, use regex to find valid items and put into a regex list
#		- iterate through list, used regex to separate integers into a temporary list
#			- multiplied temporary list items together and added to answer sum
# Part 2 : similar to part 1, however, I included the do() and don't() finds with a | in the regex
#		- I included all valid do() and don't() found, using a | (OR) in the regex
#		- iterate through regex list
#			- use a boolean, set by do() or don't() to determine whether to use items in list
#


regex_list = []
answer_sum = 0

fin = open("AoC_2024_03_input.txt", "rt")

while True :
	line = fin.readline()
	if line == "" :
		break

	# 721 indexes found with if m if u if l if ( substring [i:i+12]
	# 691 indexes with regex (30 results invalid in previous method)
	# regex "mul\([0-9]{1,3}\,[0-9]{1,3}\)"gm

	# part 1
	#regex_list += re.findall("mul\([0-9]{1,3}\,[0-9]{1,3}\)", line)

	# part 2
	regex_list += re.findall("mul\([0-9]{1,3}\,[0-9]{1,3}\)|do\(\)|don\'t\(\)", line)

fin.close()

#####################
#####################
# 
# part 1
#
# search through input and find a valid mul(###,###) where ### can be 1-3 digits
# multiply the two integers together and add them to the answer sum
#
#####################
#####################

# iterate through regex list, multiply integers together, add to answer_sum

#for i in range(len(regex_list)) :
	#temp_int_list = re.findall("[0-9]{1,3}", regex_list[i])
	#answer_sum += (int(temp_int_list[0]) * int(temp_int_list[1]))
	#print(i, "\t", regex_list[i], "\t", temp_int_list[0], "*", temp_int_list[1], "=", (int(temp_int_list[0]) * int(temp_int_list[1])), "\t", answer_sum)

#print(answer_sum)

# 175615763 correct answer (personal reminder to copy and paste answers for 



#####################
#####################
# 
# part 2
#
# only use the valid multipliers sums following a do() unless a don't is found
# skip all mulitipliers following a don't() until a do() is found
#
#####################
#####################

answer_sum = 0

# 691 indexes without do() and don't()
# 763 indexes, including do() and don't()

do_count = 0
dont_count = 0
mul_count = 0
#for i in range(len(regex_list)) :
#
#	if regex_list[i] == "do()" :
#		do_count += 1
#	elif regex_list[i] == "don't()" :
#		dont_count += 1
#	else :
#		mul_count += 1
#	print(i, "\t", regex_list[i])
#
#print("do", do_count, "don't", dont_count, "mul", mul_count)
#print("total", do_count + dont_count + mul_count)
# 34 do, 38 don't, 692 mul

answer_sum = 0
use_item = True
use_count = 0
not_use_count = 0

for i in range(len(regex_list)) :

	if regex_list[i] == "do()" :
		use_item = True
		do_count += 1
	elif regex_list[i] == "don't()" :
		use_item = False
		dont_count += 1
	else :
		mul_count += 1

	if use_item == True :
		temp_int_list = re.findall("[0-9]{1,3}", regex_list[i])
		#print(i, "   ", regex_list[i], "\t", temp_int_list)
		
		if len(temp_int_list) > 0 :
			use_count += 1
			answer_sum += (int(temp_int_list[0]) * int(temp_int_list[1]))
		else :
			not_use_count += 1
	else :
		not_use_count += 1

print("do", do_count, "don't", dont_count, "mul", mul_count, "\t", do_count + dont_count + mul_count)
print("use", use_count, "not_use", not_use_count, "\t", use_count + not_use_count)
print("answer sum", answer_sum)

# 74361272 is correct

# Python
# Advent of Code - 2024 - Day 1

#
# Final Result: Both parts are correct on first try.
#
# Sequence of solving:
#	Part 1:
#		- copy, paste, save input to input.txt
#		- open input.txt, read in each line
#			- remove whitespace, add delimiter
#			- split, convert to int, append values in two separate lists
#		- close input.txt
#		- sort lists, ascending
#		- compare one list with the other by same index value
#			- sum up the absolute distance between all pairs
#	Part 2:
#		- loop through left list
#			- loop through right list
#				- count same value
#			- multiply count of same values in right list by the left list value, add to total
#
#
# Part 1 (of 2):
#	Goal: find the sum of the distances between the numbers of each list
#		starting from the lowest number of each list.
#

total_distance = 0

left_list = [ ]
right_list = [ ]

fin = open('AoC_2024_01_input.txt', 'rt')
#input = fin.read()
#fin.close()

#print(len(input))

while True:

	line = fin.readline()
	
	if not line:
		break
	
	line = ",".join(line.split())		# remove whitespace gap
	#print(line)

	line = line.split(',')			# separate values into a list
	#print(line)	
	
	left_list.append(int(line[0]))		# convert to int and append left side of input to left list
	right_list.append(int(line[1]))		# convert to int and append right side of input to right list

fin.close()

# checking that lists are same length and print last value

#print(len(left_list), left_list[-1])
#print(len(right_list), right_list[-1])

# sort the left and right lists

left_list.sort()
right_list.sort()
#print(left_list)

# starting from the lowest number in each list, add the distance between the numbers to total_distance

count = 0
length_of_lists = len(left_list)

if len(left_list) == len(right_list) :

	while count < length_of_lists :
		total_distance += abs(left_list[count] - right_list[count])
		count += 1
else :
	print("Length of left list and right list are not the same.")

print("Total Distance:", total_distance)

#
#
#
# Part 2 (of 2):
#	Goal: Find similar numbers in left list with right list
#		 - if found, times(*) that number by number of occurances to get similarity score
#		 - add up all the scores
#
#
#

count_left = 0
count_right = 0

similar_occurances = 0
total_similarities = 0
total_similarity_score = 0

while count_left < length_of_lists :
	
	while count_right < length_of_lists :
		
#		print(left_list[count_left], " == ", right_list[count_right],
#			left_list[count_left] == right_list[count_right])
		if left_list[count_left] == right_list[count_right] :
			similar_occurances += 1
		count_right += 1

	if similar_occurances > 0 :
		print(left_list[count_left], " * ", similar_occurances)

	total_similarities += similar_occurances
	total_similarity_score += (left_list[count_left] * similar_occurances)
	similar_occurances = 0

	count_right = 0;
	count_left += 1

#print(left_list[0], left_list[-1], count_left)
print("Total Similarities:", total_similarities)
print("Similarity Score:", total_similarity_score)
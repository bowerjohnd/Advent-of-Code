######################
######################
# Part 1 : 
#
#
# Part 2 : 
#
#


# general use variables

map_input = []
guard_row_position = 0
guard_col_position = 0
guard_direction = ""

###################
###################
# open input file, format as needed, and save to variables
###################
###################

fin = open("AoC_2024_06_input.txt", "rt")

while True :
	line = fin.readline()
	if line == "" :
		break
	
	map_input.append(line)

fin.close()

###################

#find starting position and direction of the guard

for i in range(len(map_input)) :
	print(i, map_input[i], end="")

	for j in range(len(map_input[i])) :
		if map_input[i][j] == "<" :
			guard_row_position = i
			guard_col_position = j
			guard_direction = "left"
		if map_input[i][j] == ">" :
			guard_row_position = i
			guard_col_position = j
			guard_direction = "right"
		if map_input[i][j] == "^" :
			guard_row_position = i
			guard_col_position = j
			guard_direction = "up"
		if map_input[i][j] == "v" or map_input[i][j] == "V" :
			guard_row_position = i
			guard_col_position = j
			guard_direction = "down"

print("")
print("guard - row", guard_row_position, "col", guard_col_position, "facing", guard_direction)

###################
###################
# Part 1: including starting position, find out how many positions on the map the 
#		guard will occupy (not repeated), turning right at every '#' obstacle, 
#		until the guard leaves the map.
#
#		- thoughts: like instructions, change path to X, then count all X's at end
###################
###################

# testing first path

path_row = guard_row_position
path_col = guard_col_position

#map_input[path_row] = map_input[path_row][:path_col] + "X" + map_input[path_row][path_col+1:]



while path_row > 0 and path_row < len(map_input)-1 and path_col > 0 and path_col < len(map_input[0])-1 :

	try :

		################### direction up ###################

		while path_row > 0 :
			map_input[path_row] = map_input[path_row][:path_col] + "X" + map_input[path_row][path_col+1:]
		
			if map_input[path_row-1][path_col] == "#" :
				print("row", path_row, "col", path_col, "go right")
				guard_direction = "right"
				break
			path_row -= 1


		################### direction right ###################

		while path_col < len(map_input[0]) :
			map_input[path_row] = map_input[path_row][:path_col] + "X" + map_input[path_row][path_col+1:]

			if map_input[path_row][path_col+1] == "#" :
				print("row", path_row, "col", path_col, "go down")
				guard_direction = "down"
				break
			path_col += 1

		################### direction down ###################

		while path_col < len(map_input) :
			map_input[path_row] = map_input[path_row][:path_col] + "X" + map_input[path_row][path_col+1:]

			if map_input[path_row+1][path_col] == "#" :
				print("row", path_row, "col", path_col, "go left")
				guard_direction = "left"
				break
			path_row += 1

		################### direction left ###################

		while path_col > 0 :
			map_input[path_row] = map_input[path_row][:path_col] + "X" + map_input[path_row][path_col+1:]

			if map_input[path_row][path_col-1] == "#" :
				print("row", path_row, "col", path_col, "go up")
				guard_direction = "up"
				break
			path_col -= 1
	except IndexError :
		print("--------")
		print("finished")
		print("--------")
		

map_input[path_row] = map_input[path_row][:path_col] + " <--------\n"

###################


answer_sum = 0

for i in range(len(map_input)) :
	print(i, map_input[i], end="")


	for j in range(len(map_input[i])) :
		if map_input[i][j] == "X" :
			answer_sum += 1
print("")
print("answer sum", answer_sum)



###################
###################

# Part 1: answer sum 4647 submitted, success!



###################
###################
# Part 2: 
#
###################
###################

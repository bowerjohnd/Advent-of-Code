######################
######################
# Part 1 : success with minimal difficulty (Note: there are 2 versions of part 1, same results)
#		- read input file, append each readline into a list
#		- iterate through list
#			- iterate through each char
#				- set if statements to prevent index out of bounds
#					- check for "XMAS" in every direction
# Part 2 : success with quick addition to part 1 iterations
#					- check for "MAS" in 4 different X patterns
#



xmas_list = []

fin = open("AoC_2024_04_input.txt", "rt")

while True :
	line = fin.readline()
	if line == "" :
		break
	
	xmas_list.append(line.strip())

fin.close()

#print(len(xmas_list), len(xmas_list[0]))
# length of list 140, length of line 140

###################
###################
# inefficient version, iterate for each direction (cleaned up, more efficient version after this)
###################
###################

#
# horizontal forward
#
#   XMAS
#
#

row_check = 0
col_check = 0
horiz_forw_count = 0

for i in range(len(xmas_list)) :
	for j in range(len(xmas_list)-3) :
		temp = xmas_list[i][j] + xmas_list[i][j+1] + xmas_list[i][j+2] + xmas_list[i][j+3]
		#print(temp)
		if temp == "XMAS" :
			horiz_forw_count += 1
		col_check += 1
	row_check += 1

#print("row", row_check, "col", col_check)


#
# horizontal backward
#
#   SAMX
#
#

row_check = 0
col_check = 0
horiz_back_count = 0

for i in range(len(xmas_list)) :
	for j in range(len(xmas_list)-3) :
		temp = xmas_list[i][j] + xmas_list[i][j+1] + xmas_list[i][j+2] + xmas_list[i][j+3]
		#print(temp)
		if temp == "SAMX" :
			horiz_back_count += 1
		col_check += 1
	row_check += 1

#print("row", row_check, "col", col_check)

#
# vertical down
#   X
#   M
#   A
#   S

row_check = 0
col_check = 0
vert_down_count = 0

for i in range(len(xmas_list)-3) :
	for j in range(len(xmas_list)) :
		temp = xmas_list[i][j] + xmas_list[i+1][j] + xmas_list[i+2][j] + xmas_list[i+3][j]
		#print(temp)
		if temp == "XMAS" :
			vert_down_count += 1
		col_check += 1
	row_check += 1

#print("row", row_check, "col", col_check)

#
# vertical up
#   S
#   A
#   M
#   X

row_check = 0
col_check = 0
vert_up_count = 0

for i in range(len(xmas_list)-3) :
	for j in range(len(xmas_list)) :
		temp = xmas_list[i][j] + xmas_list[i+1][j] + xmas_list[i+2][j] + xmas_list[i+3][j]
		#print(temp)
		if temp == "SAMX" :
			vert_up_count += 1
		col_check += 1
	row_check += 1

#print("row", row_check, "col", col_check)

#
# diagonal down right
#   X
#    M
#     A
#      S

row_check = 0
col_check = 0
diag_dr_count = 0

for i in range(len(xmas_list)-3) :
	for j in range(len(xmas_list)-3) :
		temp = xmas_list[i][j] + xmas_list[i+1][j+1] + xmas_list[i+2][j+2] + xmas_list[i+3][j+3]
		#print(temp)
		if temp == "XMAS" :
			diag_dr_count += 1
		col_check += 1
	row_check += 1

#print("row", row_check, "col", col_check)

#
# diagonal up right
#      S
#     A
#    M
#   X

row_check = 0
col_check = 0
diag_ur_count = 0

for i in range(len(xmas_list)-3) :
	for j in range(len(xmas_list)-3) :
		temp = xmas_list[i][j+3] + xmas_list[i+1][j+2] + xmas_list[i+2][j+1] + xmas_list[i+3][j]
		#print(temp)
		if temp == "SAMX" :
			diag_ur_count += 1
		col_check += 1
	row_check += 1

#print("row", row_check, "col", col_check)



# diagonal down left
#      X
#     M
#    A
#   S

row_check = 0
col_check = 0
diag_dl_count = 0

for i in range(len(xmas_list)-3) :
	for j in range(len(xmas_list)-3) :
		temp = xmas_list[i][j+3] + xmas_list[i+1][j+2] + xmas_list[i+2][j+1] + xmas_list[i+3][j]
		#print(temp)
		if temp == "XMAS" :
			diag_dl_count += 1
		col_check += 1
	row_check += 1

#print("row", row_check, "col", col_check)

#
# diagonal up left
#   S
#    A
#     M
#      X

row_check = 0
col_check = 0
diag_ul_count = 0

for i in range(len(xmas_list)-3) :
	for j in range(len(xmas_list)-3) :
		temp = xmas_list[i][j] + xmas_list[i+1][j+1] + xmas_list[i+2][j+2] + xmas_list[i+3][j+3]
		#print(temp)
		if temp == "SAMX" :
			diag_ul_count += 1
		col_check += 1
	row_check += 1

#print("row", row_check, "col", col_check)
#
#print("####################")
#print("####################")
#print("####################")
#
#total_count = (horiz_forw_count + horiz_back_count 
#	+ vert_down_count + vert_up_count 
#	+ diag_dr_count + diag_dl_count 
#	+ diag_ur_count + diag_ul_count)
#
#print("horiz forw      \t", horiz_forw_count)
#print("horiz back      \t", horiz_back_count)
#print("vert down       \t", vert_down_count)
#print("vert up         \t", vert_up_count)
#print("")
#print("diag down right \t", diag_dr_count)
#print("diag up right   \t", diag_ur_count)
#print("diag down left  \t", diag_dl_count)
#print("diag up left    \t", diag_ul_count)
#print("")
#print("total           \t", total_count)
#
#
# submitted 2401, fail, too low ... total_count used sum of wrong variables...
# submitted 2468 with correct variables, success!

###################
###################
# more efficient version, one iteration 
###################
###################


horiz_forw_count = 0
horiz_back_count = 0
vert_down_count = 0
vert_up_count = 0
diag_dr_count = 0
diag_dl_count = 0
diag_ur_count = 0
diag_ul_count = 0

#part 2
ex1 = 0
ex2 = 0
ex3 = 0
ex4 = 0

for i in range(len(xmas_list)) :

	for j in range(len(xmas_list)) :

		#
		# horizontal forward
		#
		#   XMAS
		#
		# horizontal backward
		#
		#   SAMX
		#
		if j+3 < len(xmas_list) :
			temp = xmas_list[i][j] + xmas_list[i][j+1] + xmas_list[i][j+2] + xmas_list[i][j+3]
			if temp == "XMAS" :
				horiz_forw_count += 1
			if temp == "SAMX" :
				horiz_back_count += 1

		#
		# vertical down		vertical up
		#   X			  S		
		#   M			  A
		#   A			  M
		#   S			  X
		#
		if i+3 < len(xmas_list) :
			temp = xmas_list[i][j] + xmas_list[i+1][j] + xmas_list[i+2][j] + xmas_list[i+3][j]
			if temp == "XMAS" :
				vert_down_count += 1
			if temp == "SAMX" :
				vert_up_count += 1



		#
		# diagonal down right	diagonal up left
		#   X			  S
		#    M			   A
		#     A			    M
		#      S		     X
		#
		if i+3 < len(xmas_list) and j+3 < len(xmas_list) :
			temp = xmas_list[i][j] + xmas_list[i+1][j+1] + xmas_list[i+2][j+2] + xmas_list[i+3][j+3]
			if temp == "XMAS" :
				diag_dr_count += 1
			if temp == "SAMX" :
				diag_ul_count += 1

		#
		# diagonal down left	diagonal up right
		#      X		    S
		#     M			   A
		#    A			  M
		#   S			 X
		#
		

			temp = xmas_list[i][j+3] + xmas_list[i+1][j+2] + xmas_list[i+2][j+1] + xmas_list[i+3][j]
			if temp == "XMAS" :
				diag_dl_count += 1
			if temp == "SAMX" :
				diag_ur_count += 1

###################
#
# part 2, looking for MAS in an X shape
#
# M M	S S	M S	S M
#  A	 A	 A	 A
# S S	M M	M S	S M  
#---------------------------
# ex1	ex2	ex3	ex4
###################
		if i+2 < len(xmas_list) and j+2 < len(xmas_list) :
			temp_tl_br = xmas_list[i][j] + xmas_list[i+1][j+1] + xmas_list[i+2][j+2]
			temp_tr_bl = xmas_list[i][j+2] + xmas_list[i+1][j+1] + xmas_list[i+2][j]

			if temp_tl_br == "MAS" :
				if temp_tr_bl == "MAS" :
					ex1 += 1
				if temp_tr_bl == "SAM" :
					ex3 += 1
			if temp_tl_br == "SAM" :
				if temp_tr_bl == "MAS" :
					ex4 += 1
				if temp_tr_bl == "SAM" :
					ex2 += 1

###################
###################
###################
###################
###################



print("####################")
print("####################")
print("####################")
#print("row", row_check, "col", col_check/row_check)

total_count = (horiz_forw_count + horiz_back_count 
	+ vert_down_count + vert_up_count 
	+ diag_dr_count + diag_dl_count 
	+ diag_ur_count + diag_ul_count)

print("horiz forw      \t", horiz_forw_count)
print("horiz back      \t", horiz_back_count)
print("vert down       \t", vert_down_count)
print("vert up         \t", vert_up_count)
print("")
print("diag down right \t", diag_dr_count)
print("diag up left    \t", diag_ul_count)
print("diag down left  \t", diag_dl_count)
print("diag up right   \t", diag_ur_count)
print("")
print("total           \t", total_count)

print("####################")
print("####################")
print("####################")

print("ex1", ex1)
print("ex2", ex2)
print("ex3", ex3)
print("ex4", ex4)


print("")
print("total", (ex1 + ex2 + ex3 + ex4))

print("####################")
print("####################")
print("####################")

# part 2, 1864, success!
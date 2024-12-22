good_total = 0
safe_with_errors_total = 0
bad_total = 0


######################
######################
# Part 1 : success with minimal difficulty
# Part 2 : ~7 failed attempts, difficulties, though thought process was correct
#		- failed attempts with added rules in initial validity check
#		- separated validity check into it's own function
#			- breaks messed up counts, keeping track of wrong data, cycle count incorrect
#		- success after seeing printed results and correcting the above mentioned bugs
######################
######################

def check_valid(line) :

	count = 0
	error_count = 0

	while count < (len(line)-1) :
		if line[0] > line[1] :					# descending
			if line[count] > line[count+1] :
				if (line[count] - line[count+1]) > 3 :
					error_count += 1
					#print("descending - bad gap", line)
					break
			else :
				error_count += 1
				#print("descending - bad direction", line)
				break
		
		if line[0] < line[1] :					# ascending
			if line[count] < line[count+1] :
				if (line[count+1] - line[count]) > 3 :
					error_count += 1
					#print("ascending - bad gap", line)
					break
			else :
				error_count += 1
				#print("ascending - bad direction", line)
				break

		if line[0] == line[1] :
			error_count += 1
			#print("equal - no gap", line)
			break

		count += 1

	if error_count == 0 :
		#print("good", line)
		return 0
	else :
		return error_count
		

######################
######################
#
######################
######################

fin = open("input.txt", "rt")

while True :

	report = fin.readline()
	if report == "" :
		break
	
	report = report.split()
	report = [int(num) for num in report]
	
######################
######################
# part 1 - success - 411 good 589 bad
######################
######################
#
#	result = check_valid(report)
#
#	if result == 0 :
#		good_total += 1
#	else :
#		bad_total += 1


######################
######################
# part 2 - allow to remove 1 level to make safe - 7 fail before success - 465 good (411 + 54 with errors)
######################
######################

	safe_count = 0
	error_count = 0
	index = 0

	# check report, if no errors, add to good total and continue to next report

	result = check_valid(report)
		
	if result == 0 :
		good_total += 1
		continue

	# if error found
	# 	- remove 1 level, recheck validity, restore report and repeat for each level
	#		- if a safe report is found, add to safe with errors total

	for index in range(len(report)) :
		
		temp_report = report.copy()
		temp_report.pop(index)

		result = check_valid(temp_report)
		
		if result == 0 :
			safe_count += 1
		else :
			error_count += 1

	if safe_count == 0 :
		bad_total += 1
		#print(safe_count, "|", error_count, "- len", len(report), "\t", report)
	if safe_count > 0 :
		safe_with_errors_total += 1
		#print(safe_count, "|", error_count, "- len", len(report), "\t", report)


fin.close()


print("--------------------")
print("good with 0 bad", good_total)
print("good with errors", safe_with_errors_total, "\t(removing a level produces a safe result)")
print("")
print("good total", good_total + safe_with_errors_total)
print("bad total", bad_total)
print("")
print("total reports:", good_total + safe_with_errors_total + bad_total)
print("--------------------")


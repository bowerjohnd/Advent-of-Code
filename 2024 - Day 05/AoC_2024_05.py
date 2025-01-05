######################
######################
# Part 1 : success with minimal difficulty
#		- read input file, check length of readline, separate rules and pages into separate lists
#		- iterate through pages, send to validation function
#			- validation function checks one page, iterating through every rule
#				- if errors found, append failed page to a failed page list (for part 2)
#			- if success, determine center index, add value to answer sum
#
# Part 2 : success, got lost at first trying to keep fixed pages separated in iteration loop
#		- iterate through failed pages from part 1, send each to fix page function
#			- failed page stays in fix page function until 0 errors are found, returns fixed page
#			- fixed page gets added to fixed page list
#		- repeat part 1 with fixed page list


rules_list = []
pages_list = []
failed_pages_list = []
fixed_pages_list = []

###################
###################
# open input file, format as needed, and save to variables
###################
###################

fin = open("AoC_2024_05_input.txt", "rt")

while True :
	line = fin.readline()
	if line == "" :
		break
	
	if len(line) == 6 :
		line = line.strip()
		rules_list.append(line.split('|'))
	if len(line) > 6 :
		line = line.strip()
		pages_list.append(line.split(','))

fin.close()

# double check all 1364 input lines are accounted for
print("----------")
print("file line count:", len(rules_list) + 1 + len(pages_list))
print(len(rules_list), "rules + 1 empty +", len(pages_list), "pages")
print("----------")
print("")
print("")

print("----------")
print("part 1: pages_list", len(pages_list))
print("----------")

###################
###################
# part 1 
###################
###################

######################
# Check pages against all rules
######################


def check_valid(line) :
	
	pass_count = 0
	fail_count = 0
	not_applicable = 0
	page_index_before = 999
	page_index_after = 999
	rules_list_fail_index = 999
	page_list_fail_before = 999
	page_list_fail_after = 999

	for i in range(len(rules_list)) :

		rule_check_before = rules_list[i][0]
		rule_check_after = rules_list[i][1] 

		for page_index in range(len(line)) :

			if line[page_index] == rule_check_before:
				page_index_before = page_index
			if line[page_index] == rule_check_after:
				page_index_after = page_index

		if page_index_before == 999 or page_index_after == 999 :
			not_applicable += 1
		elif page_index_before < page_index_after :
			pass_count += 1
		elif page_index_before > page_index_after :
			fail_count += 1
			rules_list_fail_index = i
			page_list_fail_before = page_index_before
			page_list_fail_after = page_index_after
		else :
			pass

		page_index_before = 999
		page_index_after = 999


	return [pass_count, fail_count, not_applicable, rules_list_fail_index, page_list_fail_before, page_list_fail_after]


###################
###################
###################

answer_sum = 0
total_pass = 0
total_fail = 0
total_checked = 0

for check_page in range(len(pages_list)) :

	results = check_valid(pages_list[check_page])

	if results[1] == 0 :
		#print("pass")
		total_pass += 1
		middle_index = int(len(pages_list[check_page])/2)
		answer_sum += int(pages_list[check_page][middle_index])
	if results[1] > 0 :
		#print("fail")
		failed_pages_list.append(pages_list[check_page])	# use in part 2 below
		total_fail += 1
	total_checked += 1

print("---- PART 1 complete------")
print("totals")
print("pass:", total_pass, "fail:", total_fail, "pages checked:", total_checked)
print("answer sum:", answer_sum)
print("----------")

# answer sum 5509 submitted, success!



###################
###################
# Part 2: Start
###################
###################

# fix/correct only the failed pages, then add up center page numbers


print("")
print("")

print("----------")
print("part 2: failed_pages_list", len(failed_pages_list))
print("----------")


###################
###################
# Part 2: check validation of page, fix error, repeat until 0 errors
###################
###################

def fix_page(line) :
	count = 0
	errors = True
	while errors :
		count += 1
		results = check_valid(line)

		if results[1] == 0 :
			errors = False
		if results[1] > 0 :
			line.insert(results[5], line.pop(results[4]))
	print("\t fix count", count)
	return [line, count]


###################
###################
# Part 2: iterate through failed_pages_list, send each page to fix_page()
###################
###################

answer_sum = 0
total_fixes = 0

for check_page in range(len(failed_pages_list)) :
	print("\t failed page", check_page, "  ", end=" ")
	line = fix_page(failed_pages_list[check_page])
	
	failed_pages_list[check_page] = line[0]
	total_fixes += line[1]
	fixed_pages_list.append(failed_pages_list[check_page])
	
print("")


###################
###################
# Part 2: check validation of fixed_pages_list
###################
###################

answer_sum = 0
total_pass = 0
total_fail = 0
total_checked = 0

for check_page in range(len(fixed_pages_list)) :
	results = check_valid(fixed_pages_list[check_page])

	if results[1] == 0 :
		total_pass += 1
		middle_index = int(len(fixed_pages_list[check_page])/2)
		answer_sum += int(fixed_pages_list[check_page][middle_index])
	if results[1] > 0 :
		total_fail += 1
	total_checked += 1


print("")
print("---- PART 2 complete------")
print("totals")
print("pass:", total_pass, "- fail:", total_fail, "- pages checked:", total_checked, "- fixes:", total_fixes)
print("answer sum:", answer_sum)
print("----------")
# submitted 4407, correct

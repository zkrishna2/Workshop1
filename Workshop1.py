def calculator (operator, A, B):
	if operator == '+':
		return A+B
	elif operator == '-':
		return A-B
	elif operator == 'x':
		return A*B
	elif operator == '/':
		return A/B
	else:
		return 0

def read_file (file_path):
	with open(file_path,'r') as f:
		file_contents=f.read()
	return [line.split() for line in file_contents.splitlines()]

def parse_goto(line):
	if line[1]=='calc':
		line_number = calculator(line[2],int(line[3]),int(line[4]))
	else:
		line_number = int(line[1])
	return int(line_number)

calcs = read_file("D:\Documents\Documents\Family\Krishna\Studies\DevOps\Workshop\Workshop1\step_2.txt")
goto = read_file("D:\Documents\Documents\Family\Krishna\Studies\DevOps\Workshop\Workshop1\step_3.txt")

lines_read=[]
curr_line=0
while curr_line not in lines_read:
	lines_read.append(curr_line)
	curr_line=parse_goto(goto[curr_line])
print(goto[curr_line], curr_line)	

# 	result+=calc_line(line)
#print(calc_line(goto[18]))
# for line in lines:
# 	split_line=line.split()
# 	operator = split_line[1]
# 	A = int(split_line[2])
# 	B = int(split_line[3])
# 	result+=calculator(operator,A,B)
# print(result)

import random
import statistics
import math
def isfloat(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False

matchbook_a = []
matchbook_b = []
matchbook_c = []
z_a = {}
z_b = {}
z_c = {}

participants = []
participants_scores = []

def setup():
	global matchbook_a
	global matchbook_b
	global matchbook_c
	global z_a
	global z_b
	global z_c
	matchbook_a = ["set", "add", "mul", "div", "sub", "sdsd", "print", "goto", "ifg", "end"]
	matchbook_b = "abcdef0123456789"
	matchbook_c = "abcdef0123456789"
	for i in range(0, len(matchbook_a)):
		z_a[matchbook_a[i]] = i
	for i in range(0, len(matchbook_b)):
		z_b[matchbook_b[i]] = i
	for i in range(0, len(matchbook_c)):
		z_c[matchbook_c[i]] = i
	
def translate_to_coords(s):
	coors = []
	for i in s:
		l = i.split(' ')
		coors.append([z_a[l[0]], z_b[l[1]], z_c[l[2]]])

	return coors

def translate_to_code(coors):
	s = []
	for i in coors:
		s.append(matchbook_a[i[0]] + " " + matchbook_b[i[1]] + " " + matchbook_c[i[2]])
	
	return s

def execute(s, v=0):
	variables = {}
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	for i in alphabet:
		variables[i] = 0
		
	# This takes an array of commands set out like "set a 1" etc.
	zs = len(s)
	f = 0
	i = 0
	n = 0
	ci = 0
	while (i < zs and n < 300):
		#print(str(i) + ": " + s[i] + " /"+str(n))
		l = s[i].split(' ')
		ci = i
		i += 1
		n += 1
		for sd in alphabet:
			if (math.isinf(variables[sd])):
				variables[sd] = 0
				return 0
		if (len(l) >= 3):

			if (l[0] == "set"):
				try:
					if (isfloat(l[1]) == False):
						if (isfloat(l[2]) == False):
							variables[l[1]] = variables[l[2]]
						else:
							variables[l[1]] = float(l[2])
				except ValueError:
					f = f + 1
			elif (l[0] == "add"):
				try:
					if (isfloat(l[1]) == False):
						if (isfloat(l[2]) == False):
							variables[l[1]] = variables[l[1]] + variables[l[2]]
						else:
							variables[l[1]] = variables[l[1]] + float(l[2])
				except ValueError:
					f = f + 1
			elif (l[0] == "mul"):
				try:
					if (isfloat(l[1]) == False):
						if (isfloat(l[2]) == False):
							variables[l[1]] = variables[l[1]] * variables[l[2]]
						else:
							variables[l[1]] = variables[l[1]] * float(l[2])
				except ValueError:
					f = f + 1
			elif (l[0] == "div"):
				try:
					if (isfloat(l[1]) == False):
						if (isfloat(l[2]) == False):
							if (variables[l[2]] != 0):
								variables[l[1]] = variables[l[1]] / variables[l[2]]
							else:
								f = f + 1
						else:
							if (float(l[2]) != 0):
								variables[l[1]] = variables[l[1]] / float(l[2])
							else:
								f = f + 1
				except ValueError:
					f = f + 1
			elif (l[0] == "sub"):
				try:
					if (isfloat(l[1]) == False):
						if (isfloat(l[2]) == False):
							variables[l[1]] = variables[l[1]] - variables[l[2]]
						else:
							variables[l[1]] = variables[l[1]] - float(l[2])
				except ValueError:
					f = f + 1
			#elif (l[0] == "print"):
			#	try:
			#		if (isfloat(l[1]) == False):
			##			print(variables[l[1]])
			#		else:
			#			print(l[1])
			#	except ValueError:
			#		f = f + 1
			elif (l[0] == "goto"):
				try:
					if (isfloat(l[1]) == False):
						if (int(variables[l[1]]) > 0 and int(variables[l[1]]) < zs and int(variables[l[1]]) != i):
							i = int(variables[l[1]])
							
					else:
						if (int(l[1]) > 0 and int(l[1]) < zs and int(l[1]) != i):
							i = int(l[1])
				except ValueError:
					f = f + 1
			elif (l[0] == "ifg"):
				try:
					a = 0
					b = 0
					if (isfloat(l[1]) == False):
						a = variables[l[1]]
					else:
						a = float(l[1])
					if (isfloat(l[2]) == False):
						b = variables[l[2]]
					else:
						b = float(l[2])

					if (a <= b):
						i = i + 1
				except ValueError:
					f = f + 1
			elif (l[0] == "end"):
				
				f += 1
				break
			else:
				f += 1
		if (v == 1):
			print(str(ci) + "; " + s[ci] + "  \t\t"+str(variables['a'])+"\t"+str(variables['b'])+"\t"+str(variables['c'])+"\t"+str(variables['d'])+"\t"+str(variables['e'])+"\t"+str(variables['f']))
	
	
	
	score = 0
	#score = pow(variables['a'] - 12, 2.0)
	#if (v == 1):
	#	print(str(score) + ", " + str(f))
	p = n - zs
	#return 1000 - score - pow(f, 3) - p
	for i in alphabet:
		score += variables[i]
	# I want this number to be 42
	diff = abs(42 - score)
	if (v == 1):
		print(str(score) + ", " + str(diff) + ", " + str(f))
	return 1000-pow(diff, 2) - pow(f, 3) - p
	
setup()

LINES_OF_CODE = 50
PARTICIPANTS = 200
PROGENY = 10
TOPNUM = 20
RANDOMS = 30

# create the initial participants.

for i in range(0, PARTICIPANTS): ## Participants
	l = []
	for p in range(0, LINES_OF_CODE): ## Lines of code
		q = []
		q.append(random.randint(0, len(matchbook_a)-1))
		q.append(random.randint(0, len(matchbook_b)-1))
		q.append(random.randint(0, len(matchbook_c)-1))
		l.append(q)
	participants.append(l)
	
	score = execute(translate_to_code(l))#
	participants_scores.append(score)

#print(participants_scores)


generation = 0
new_participants = []

while (generation < 400):
	max_scores = sorted(range(len(participants_scores)), key=lambda i: participants_scores[i])[-TOPNUM:] # get the maximum scores
	#print(max_scores)
	#print("\n\n")
	print(""+str(generation) +", "+str(participants_scores[max_scores[len(max_scores)-1]]) + ", " + str(statistics.mean(participants_scores)) + ", " + str(statistics.median(participants_scores)))
	ks = translate_to_code(participants[max_scores[len(max_scores)-1]])

	#execute(ks, 1)
	
	#print("\n\n")
	new_participants_scores = []
	new_participants = []
	for i in range(0, RANDOMS):
		l = []
		for p in range(0, LINES_OF_CODE): ## Lines of code
			q = []
			q.append(random.randint(0, len(matchbook_a)-1))
			q.append(random.randint(0, len(matchbook_b)-1))
			q.append(random.randint(0, len(matchbook_c)-1))
			l.append(q)
			
		new_participants.append(l)
	
		score = execute(translate_to_code(l))#
		new_participants_scores.append(score)
			
			
	for i in range(0, TOPNUM):
		# max_scores[i] reproducing
		for iu in range(0, PROGENY):
			ds = []
			for x in range(0, len(participants[max_scores[TOPNUM-1-i]])):
			
				ds.append([])
				for y in range(0, len(participants[max_scores[TOPNUM-1-i]][0])):
					
					ds[x].append(participants[max_scores[TOPNUM-1-i]][x][y])
			#ds = participants[max_scores[1-i]]
			
			x = random.randint(0, 2)
			lk = random.randint(0, LINES_OF_CODE-1)
			nm = random.randint(-1, 1)
			if (random.randint(0, 5) == 1):
				nm = random.randint(-3, 3)

			if (iu == 0):
				#print("TADA - " + str(participants_scores[max_scores[1-i]]))
				#print("NO MUTATION")
				nm = 0
			if (x == 0):
				q = ds[lk][x]
				ds[lk][x] += nm
				if (ds[lk][x] < 0):
					ds[lk][x] = 0
				elif (ds[lk][x] > len(matchbook_a) - 1):
					ds[lk][x] = len(matchbook_a)-1
			elif (x == 1):
				q = ds[lk][x]
				ds[lk][x] += nm
				if (ds[lk][x] < 0):
					ds[lk][x] = 0
				elif (ds[lk][x] > len(matchbook_b) - 1):
					ds[lk][x] = len(matchbook_b)-1
			elif (x == 2):
				q = ds[lk][x]
				ds[lk][x] += nm
				if (ds[lk][x] < 0):
					ds[lk][x] = 0
				elif (ds[lk][x] > len(matchbook_c) - 1):
					ds[lk][x] = len(matchbook_c)-1
			new_participants.append(ds)
			score = execute(translate_to_code(ds))#
			new_participants_scores.append(float(score))
			#print(len(new_participants))
			
	#print(new_participants_scores)
	participants = []
	participants = new_participants
	participants_scores = new_participants_scores
	generation+=1
		
print(participants_scores)
print("\n\n\n\n\n")
max_scores = sorted(range(len(participants_scores)), key=lambda i: participants_scores[i])[-10:] # get the maximum scores
#print(max_scores)
ks = translate_to_code(participants[max_scores[len(max_scores)-1]])
for i in ks:
	print(i)
	
execute(ks, 1)

import sys

def main():
	pos = [0,0]
	dupe = [0,0]
	array = [[1,0],[0,1],[-1,0],[0,-1]]
	dir = 0
	raw = input("Entry: ")
	raw_split = raw.split(", ")
	history = [[0,0]]
	first_duplicate = False
	
	for i in raw_split:
		turn = i[0]
		if turn == 'R':
			dir = dir + 1
			if dir > 3:
				dir = 0
		else: #Blindly assume it's an L :D
			dir = dir - 1
			if dir < 0:
				dir = 3
		
		parts = i.split(turn)
		
		value = int(parts[1])
		for x in range(0, value):
			pos[0] += array[dir][0]
			pos[1] += array[dir][1]
			if first_duplicate == False:
				for y in history:
					if pos[0] == y[0] and pos[1] == y[1]:
						dupe[0] = pos[0]
						dupe[1] = pos[1]
						first_duplicate = True
				history.append([pos[0],pos[1]])
	print("Total Dist: ", abs(pos[0])+abs(pos[1]))
	print("Dist to first dupe: ", abs(dupe[0])+abs(dupe[1]))
main()
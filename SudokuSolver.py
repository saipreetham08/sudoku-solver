import time
def updateRow(ans,row,ele,queue):
	for i in range(9):
		if type(ans[row][i]) == list:
				if ele in ans[row][i]:
					ans[row][i].remove(ele)
					if len(ans[row][i]) == 1 :
						queue.append((row,i))
						ans[row][i] = ans[row][i][0]
						#print(queue[-1],ans[row][i], "Appended during updateRow")

def updateCol(ans,col,ele,queue):
	for i in range(9):
		if type(ans[i][col]) == list:
				if ele in ans[i][col]:
					ans[i][col].remove(ele)
					if len(ans[i][col]) == 1 :
						queue.append((i,col))
						ans[i][col] = ans[i][col][0]
						#print(queue[-1],ans[i][col], "Appended during updateCol")

def updateGrid(ans,row,col,ele,queue):
	start_row,start_col = getGridStart(row,col)
	for i in range(start_row,start_row+3):
		for j in range(start_col, start_col+3):
			if type(ans[i][j]) == list:
				if ele in ans[i][j]:
					ans[i][j].remove(ele)
					if len(ans[i][j]) == 1 :
						queue.append((i,j))
						ans[i][j] = ans[i][j][0]
						#print(queue[-1],ans[i][j], "Appended during updateGrid")

def findByElim(ans,row,col,queue):
	affectedGrids = findAffectedGrids(row,col)
	for start_row,start_col in affectedGrids:
		ele_grid = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
		for i in range(start_row,start_row+3):
			for j in range(start_col, start_col+3):
				if type(ans[i][j]) == list:
					for ele in ans[i][j]:
						if type(ele_grid[ele]) == list:
							ele_grid[ele].append((i,j))
				else :
					ele_grid[ans[i][j]] = -1

		for key in ele_grid:
			if type(ele_grid[key]) == list and len(ele_grid[key]) == 1:
				#print(key, ele_grid[key])
				queue.append(ele_grid[key][0])
				ans[ele_grid[key][0][0]][ele_grid[key][0][1]] = key
				#print(queue[-1],ans[ele_grid[key][0][0]][ele_grid[key][0][1]], "Appended during findByElim")


def findAffectedGrids(row,col):
	start_row, start_col = getGridStart(row, col)
	d = {0: [(0,0),(0,3),(0,6),(3,0),(6,0)],  3:[(0,0),(0,3),(0,6),(3,3),(6,3)],  6:[(0,0),(0,3),(0,6),(3,6),(6,6)],27:[(0,0),(3,0),(3,3),(3,6),(6,0)], 30:[(3,0),(3,3),(3,6),(0,3),(6,3)], 33:[(3,0),(3,3),(3,6),(0,6),(6,6)], 54:[(6,0),(6,3),(6,6),(0,0),(3,0)], 57:[(6,0),(6,3),(6,6),(0,3),(3,3)], 60:[(6,0),(6,3),(6,6),(0,6),(3,6)]}
	return d[start_row*9 + start_col]

def findByElimInRow(ans,row,queue):
	ele_grid = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
	for i in range(9):
		if type(ans[row][i]) == list:
			for ele in ans[row][i] :
				if type(ele_grid[ele]) == list: 
					ele_grid[ele].append((row,i))
		else :
			ele_grid[ans[row][i]] = -1
	for key in ele_grid:
		if type (ele_grid[key]) == list and len(ele_grid[key]) == 1:
			queue.append(ele_grid[key][0])
			ans[ele_grid[key][0][0]][ele_grid[key][0][1]] = key
			#print("Appended in findByElimInRow")

def findByElimInCol(ans,col,queue):
	ele_grid = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
	for i in range(9):
		if type(ans[i][col]) == list:
			for ele in ans[i][col] :
				if type(ele_grid[ele]) == list: 
					ele_grid[ele].append((i,col))
		else :
			ele_grid[ans[i][col]] = -1
	for key in ele_grid:
		if type (ele_grid[key]) == list and len(ele_grid[key]) == 1:
			queue.append(ele_grid[key][0])
			ans[ele_grid[key][0][0]][ele_grid[key][0][1]] = key
			#print("Appended in findByElimInCol")

def getGridStart(row,col):
	return ((row // 3) * 3, (col // 3) * 3)

def updateUsingPairInGrid(ans,row,col,queue):
	grid_start_row,grid_start_col = getGridStart(row,col)
	ele_grid = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
	for i in range(grid_start_row,grid_start_row+3):
		for j in range(grid_start_col,grid_start_col+3):
			if type(ans[i][j]) == list:
				for ele in ans[i][j]:
					if type(ele_grid[ele]) == list:
						ele_grid[ele].append((i,j))
			else :
				ele_grid[ans[i][j]] = -1

	for num in ele_grid:
		if type(ele_grid[num]) != list:
			continue
		pos_rows = {}
		pos_cols = {}
		for pos_row, pos_col in ele_grid[num]:
			if pos_row in pos_rows:
				pos_rows[pos_row].append((pos_row,pos_col))
			else :
				pos_rows[pos_row] = [(pos_row,pos_col)]

			if pos_col in pos_cols:
				pos_cols[pos_col].append((pos_row,pos_col))
			else :
				pos_cols[pos_col] = [(pos_row,pos_col)]
		
		if len(pos_rows) == 1:
			req_row = pos_rows[list(pos_rows.keys())[0]][0][0]
			for i in range(9):
				found = 0
				for xyz_r,xyz_c in pos_rows[req_row]:
					if req_row == xyz_r and i == xyz_c :
						found = 1
						break
				if found == 1:
					continue 
				if type(ans[req_row][i]) != list:
					continue
				if num in ans[req_row][i]:
					ans[req_row][i].remove(num)
					if len(ans[req_row][i]) == 1:
						queue.append((req_row,i))
						ans[req_row][i] = ans[req_row][i][0]
						#print("Appeneded during Naked Pair Row Update")

		if len(pos_cols) == 1:
			req_col = pos_cols[list(pos_cols.keys())[0]][0][1]
			for i in range(9):
				found = 0
				for xyz_r,xyz_c in pos_cols[req_col]:
					if i == xyz_r and req_col == xyz_c:
						found = 1
						break
				if found == 1:
					continue
				if type(ans[i][req_col]) != list:
					continue
				if num in ans[i][req_col]:
					ans[i][req_col].remove(num)
					if len(ans[i][req_col]) == 1:
						queue.append((i,req_col))
						ans[i][req_col] = ans[i][req_col][0]
						#print("Appended during Nake Pair Column Update")

def updateUsingPairInRow(ans,row,col,queue):
	ele_grid = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
	for i in range(9):
		if type(ans[row][i]) == list:
			for ele in ans[row][i]:
				if type(ele_grid[ele]) == list:
					ele_grid[ele].append((row,i))
		else :
			ele_grid[ans[row][i]] = -1

	for num in ele_grid:
		if type(ele_grid[num]) != list:
			continue
		grids = set()
		for pos_r,pos_c in ele_grid[num]:
			grid_start_row,grid_start_col = getGridStart(pos_r, pos_c)
			grid_number = grid_start_row * 9 + grid_start_col
			grids.add(grid_number)

		if len(grids) == 1:
			grid_start_row, grid_start_col = list(grids)[0] // 9, list(grids)[0] % 9
			for i in range(grid_start_row, grid_start_row + 3):
				for j in range(grid_start_col, grid_start_col + 3):
					if type(ans[i][j]) != list :
						continue
					found = 0
					for pos_r,pos_c in ele_grid[num]:
						if i == pos_r and j == pos_c:
							found = 1
							break
					if found == 1:
						continue
					if num in ans[i][j]:
						ans[i][j].remove(num)
						if len(ans[i][j]) == 1:
							queue.append((i,j))
							ans[i][j] = ans[i][j][0]
							#print("Appened in updateUsingPairInRow")

def updateUsingPairInCol(ans,row,col,queue):
	ele_grid = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
	for i in range(9):
		if type(ans[i][col]) == list:
			for ele in ans[i][col]:
				if type(ele_grid[ele]) == list:
					ele_grid[ele].append((i,col))
		else :
			ele_grid[ans[i][col]] = -1

	for num in ele_grid:
		if type(ele_grid[num]) != list:
			continue
		grids = set()
		for pos_r,pos_c in ele_grid[num]:
			grid_start_row,grid_start_col = getGridStart(pos_r, pos_c)
			grid_number = grid_start_row * 9 + grid_start_col
			grids.add(grid_number)

		if len(grids) == 1:
			grid_start_row, grid_start_col = list(grids)[0] // 9, list(grids)[0] % 9
			for i in range(grid_start_row, grid_start_row + 3):
				for j in range(grid_start_col, grid_start_col + 3):
					if type(ans[i][j]) != list :
						continue
					found = 0
					for pos_r,pos_c in ele_grid[num]:
						if i == pos_r and j == pos_c:
							found = 1
							break
					if found == 1:
						continue
					if num in ans[i][j]:
						ans[i][j].remove(num)
						if len(ans[i][j]) == 1:
							queue.append((i,j))
							ans[i][j] = ans[i][j][0]
							#print("Appened in updateUsingPairInRow")

def checkDict(d):
	for i in range(1,10):
		if i not in d:
			return False
	return True

def checkRow(row, ans):
	d = {}
	for i in range(9):
		d[ans[row][i]] = 1
	return checkDict(d)

def checkCol(col,ans):
	d = {}
	for i in range(9):
		d[ans[i][col]] = 1
	return checkDict(d)

def checkGrid(start_row,start_col,ans):
	d = {}
	for i in range(start_row, start_row+3):
		for j in range(start_col, start_col+3):
			d[ans[i][j]] = 1
	return checkDict(d)

def isValid(ans):
	for i in range(9):
		if not checkRow(i,ans):
			return False
		if not checkCol(i,ans):
			return False

	grid_coded = [0,3,6,27,30,33,54,57,60]
	for grid in grid_coded:
		start_row,start_col = grid // 9, grid % 9
		if not checkGrid(start_row,start_col,ans):
			return False
	return True
	
def checkDupInRow(row, mat):
	d = {}
	for i in range(9):
		if type(mat[row][i]) != list:
			if mat[row][i] in d:
				return True
			else :
				d[mat[row][i]] = 1
	return False

def checkDupInCol(col, mat):
	d = {}
	for i in range(9):
		if type(mat[i][col]) != list:
			if mat[i][col] in d:
				return True
			else :
				d[mat[i][col]] = 1
	return False

def checkDupInGrid(row, col, mat) :
	start_row,start_col = getGridStart(row,col)
	d = {}
	for i in range(start_row, start_row + 3):
		for j in range(start_col, start_col + 3):
			if type(mat[i][j]) != list:
				if mat[i][j] in d:
					return True
				else :
					d[mat[i][j]] = 1
	return False

def checkDuplicates(row, col, mat):
	return (checkDupInRow(row, mat) | checkDupInCol(col, mat) | checkDupInGrid(row,col,mat))

def backTracking(row, col, ans):
	if row == 9:
		if isValid(ans): #Extra check; May not be required as duplicate checks already being performed
			return True

	if type(ans[row][col]) != list:
		if col == 8:
			return backTracking(row+1, 0, ans)
		else :
			return backTracking(row, col+1, ans)

	pos = ans[row][col]
	for i in range(len(pos)):
		ans[row][col] = pos[i]
		if not checkDuplicates(row,col,ans):
			if col == 8:
				res = backTracking(row+1,0,ans)
			else :
				res = backTracking(row,col+1,ans)
			if res:
				return True
	ans[row][col] = pos
	return False

def Solver(mat):
	start = time.time()
	ans,queue = [],[]

	for i in range(9):
		row = []
		for j in range(9):
			if mat[i][j] != 0:
				queue.append((i,j))
				row.append(mat[i][j])
			else :
				row.append([1,2,3,4,5,6,7,8,9])
		ans.append(row)

	displayUnsolvedSudoku(ans)

	index = 0
	while index < len(queue) and len(queue) < 81:
		cur_row,cur_col = queue[index]
		updateRow(ans,cur_row,ans[cur_row][cur_col],queue)
		updateCol(ans,cur_col,ans[cur_row][cur_col],queue)
		updateGrid(ans,cur_row,cur_col,ans[cur_row][cur_col],queue)
		findByElim(ans,cur_row,cur_col,queue)
		findByElimInRow(ans,cur_row,queue)
		findByElimInCol(ans,cur_col,queue)
		updateUsingPairInGrid(ans,cur_row,cur_col,queue)
		updateUsingPairInRow(ans,cur_row,cur_col,queue)
		updateUsingPairInCol(ans,cur_row,cur_col,queue)
		index += 1

		if index < len(queue) and len(queue) < 81:
			continue

		ans_copy = []
		for i in range(9):
			temp_row = []
			for j in range(9):
				temp_row.append(ans[i][j])
			ans_copy.append(temp_row)

		for cur_row in range(9):
			for cur_col in range(9):
				updateRow(ans,cur_row,ans[cur_row][cur_col],queue)
				updateCol(ans,cur_col,ans[cur_row][cur_col],queue)
				updateGrid(ans,cur_row,cur_col,ans[cur_row][cur_col],queue)
				findByElim(ans,cur_row,cur_col,queue)
				findByElimInRow(ans,cur_row,queue)
				findByElimInCol(ans,cur_col,queue)
				updateUsingPairInGrid(ans,cur_row,cur_col,queue)
				updateUsingPairInRow(ans,cur_row,cur_col,queue)
				updateUsingPairInCol(ans,cur_row,cur_col,queue)
		if ans_copy == ans:
			break
		else :
			index = 0
			
	if len(queue) == 81:
		if isValid(ans):
			print("Solved successfully!!!")
			displaySudoku(ans)
		else :
			print("Unknown error occurred!")
	else :
		if backTracking(0,0,ans):
			print("Solution")
			displaySudoku(ans)
		else :
			print("This sudoku cannot be solved")
			print("Please check the input")
	end = time.time()
	print("Time taken:","{:.5f}".format((end - start)), "seconds")

def displayUnsolvedSudoku(ans):
	print("Your Sudoku puzzle is: ")
	temp = []
	for i in range(9):
		temp_row = []
		for j in range(9):
			if type(ans[i][j]) == list:
				temp_row.append(' ')
			else :
				temp_row.append(ans[i][j])
		temp.append(temp_row)
	displaySudoku(temp)

def displaySudoku(ans):
	print("||-|-|-||-|-|-||-|-|-||")
	for i in range(9):
		print(f'||{ans[i][0]}|{ans[i][1]}|{ans[i][2]}||{ans[i][3]}|{ans[i][4]}|{ans[i][5]}||{ans[i][6]}|{ans[i][7]}|{ans[i][8]}||')
		if i%3 == 2:
			print("||-|-|-||-|-|-||-|-|-||")

print("Sai's Sudoku solver")
print("Enter the rows of the Sudoku (Enter 0 for blank spaces)")
mat = []
for i in range(9):
	row = []
	x = input()
	for j in range(9):
		row.append(int(x[j]))
	mat.append(row)
Solver(mat)

'''
Puzzle 200
000900340
900010062
060000100
200080000
600391005
000040003
006000050
840050001
057006000
'''
from time import sleep


n=int(input("Enter number of queens"))
map=[]
for i in range (n):
    list=n*[0]
    map.append(list)

# print(map)
columns=[]
for i in range(n):
    columns.append(i)
# print(columns)
Queens=8

def isvalid(row,col):
    if row<0 or row>=n or col<0 or col>=n:
        return False
    return True 

def print_map():
    for i in map:
        for j in i:
            print(j,end=" ")
        print()

def issafe(row,col):
    # Left Up
    for i in range(n):
        if isvalid(row-i,col-i):
            if map[row-i][col-i]=='q':
                return False
        else:
            break    
    # Right up
    for i in range(n):
        if isvalid(row-i,col+i):
            if map[row-i][col+i]=='q':
                return False
        else:
            break    
    # Left Down
    for i in range(n):
        if isvalid(row+i,col-i):
            if map[row+i][col-i]=='q':
                return False
        else:
            break    
    # Right Down
    for i in range(n):
        if isvalid(row+i,col+i):
            if map[row+i][col+i]=='q':
                return False
        else:
            break
        
        
    return True    




def solve(row):
    # print_map()
    if row==n:
        print_map()
        exit(0)
        
    if 'q' in map[row]:
        solve(row+1)
    
    else:
        for col in columns:
            # print(row,col)
            if issafe(row,col):
                map[row][col]='q'
                columns.remove(col)
                solve(row+1)
                columns.append(col)
                map[row][col]=0
    
    return 0
                
solve(0)
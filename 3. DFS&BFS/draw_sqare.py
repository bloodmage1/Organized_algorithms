# case 1

## 풀이 1

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
result = 9

print(len(board), len(board[0]))

max_num = 0
for i in range(1, len(board)):
    for j in range(1, len(board[i])):
        if board[i][j] == 1:
            board[i][j] = min(board[i-1][j-1], board[i-1][j], 
                            board[i][j-1]) + 1
        else:
            board[i][j] = min(board[i-1][j-1], board[i-1][j], 
                            board[i][j-1])
            
    if max_num < max(board[i]):
        max_num = max(board[i])

print(max_num**2)

## 풀이 2

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
result = 9

print(len(board), len(board[0]))

max_num = 0
for i in range(1, len(board)):
    for j in range(1, len(board[i])):
        if board[i][j] == 1:
            board[i][j] = min(board[i-1][j-1], board[i-1][j], 
                            board[i][j-1]) + 1
            
            if max_num < board[i][j]:
                max_num = board[i][j]

print(max_num**2)

## 풀이 3

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
result = 9

board = [[1,0],[0,0]]
result = 1
print(len(board), len(board[0]))

max_num = 1
for i in range(1, len(board)):
    for j in range(1, len(board[0])):
        if board[i][j] == 1:
            board[i][j] = min(board[i-1][j-1], board[i-1][j], 
                            board[i][j-1]) + 1
            
            if max_num < board[i][j]:
                max_num = board[i][j]
if all(1 not in l for l in board):
    max_num = 0

print(max_num**2)


# # case 2

# board = [[0,0,1,1],[1,1,1,1]]
# result = 4
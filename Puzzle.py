
def solve_puzzle(Board, Source, Destination):
    rows = len(Board)
    columns = len(Board[0])
    path = [Source]
    directions = [(0,-1), (0,1), (-1,0), (1,0)]

    def valid(row,column):

        if 0 <= column < columns and 0 <= row < rows and Board[row][column] == '-':
            return True

        else:
            return False

    bfs = []
    bfs.append([Source, path])
    searched = []
    while len(bfs) != 0:
        item = bfs.pop(0)
        a,b = item[0]
        current = [(a,b)]
        path = item[1]

        searched.append((current[0][0], current[0][1]))
        if (Destination == (current[0][0], current[0][1])):
            return path

        for x, y in directions:
            neighbor_column = y + current[0][1]
            neighbor_row = x + current[0][0]
            neighbor = [(neighbor_row, neighbor_column)]

            if valid(current[0][0], current[0][1]) and (neighbor_row,neighbor_column) not in searched:
                continued_path = path[:]
                continued_path.append((neighbor[0][0],neighbor[0][1]))
                bfs.append([(neighbor[0][0], neighbor[0][1]), continued_path])

    return None



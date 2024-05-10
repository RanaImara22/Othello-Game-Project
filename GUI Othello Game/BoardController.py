class BoardController:    
    def flip_cells(starting_cell, cells_to_flip, players, current_index, board , fake = False):
        x, y = starting_cell
        BoardController.change_color(board , x , y , players[current_index].color , fake)
        if(fake == False): players[current_index].score += 1
        for cell in cells_to_flip:
            BoardController.change_color(board , cell[0] , cell[1] , players[current_index].color , fake)
            if(fake == False):
                players[current_index].score += 1
                players[abs (1 - current_index)].score -= 1
    
    @staticmethod
    def change_color(board , x , y , color , fake = False):
        if(fake == False):
            board.buttons[x][y].change_oval_color(color)
        else:
            board[x][y] = color

    @staticmethod
    def getColor(board , x , y , fake):
        if(fake == False):
            return board.buttons[x][y].color
        else:
            return board[x][y]
      
    @staticmethod
    def valid_moves(players, currentIndex, board, fake=False):
        opponent_color = 'B' if players[currentIndex].color == 'W' else 'W'
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        valid_cells = []

        def is_valid_cell(x, y):
            return 0 <= x < 8 and 0 <= y < 8

        def find_valid_direction(dx, dy, x, y):
            nx, ny = x + dx, y + dy
            path = []
            while is_valid_cell(nx, ny) and BoardController.getColor(board, nx, ny, fake) == opponent_color:
                path.append((nx, ny))
                nx += dx
                ny += dy
            if is_valid_cell(nx, ny) and BoardController.getColor(board, nx, ny, fake) == '.' and path:
                valid_cells.append(((nx, ny), path))
        for x in range(8):
            for y in range(8):
                if BoardController.getColor(board, x, y, fake) == players[currentIndex].color:
                    for dx, dy in directions:
                        find_valid_direction(dx, dy, x, y)

        combined_moves = {}
        for cell, path in valid_cells:
            if cell in combined_moves:
                combined_moves[cell].extend(path)
            else:
                combined_moves[cell] = path

        combined_valid_cells = [(cell, path) for cell, path in combined_moves.items()]

        return combined_valid_cells
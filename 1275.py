class Solution:
    def check_victory(self,board:List[List[str]], player:str, move:List[int]) -> bool:
        # check horizontal victory
        player_wins = True
        row = move[0]
        for position in board[row]:
            if position != player:
                player_wins = False
                break
        if player_wins:
            return True
        # check vertical victory
        player_wins = True
        col = move[1]
        for row in range(3):
            if board[row][col] != player:
                player_wins = False
                break
        if player_wins:
            return True
        # check left to right diagonal victory
        if move[0] == move[1] or abs(move[0] - move[1]) == 2:
            player_wins = True
            for col_row in range(3):
                if board[col_row][col_row] != player:
                    player_wins = False
                    break
            if player_wins:
                return True
            player_wins = True
            for row in range(3):
                col = 2-row
                if board[row][col] != player:
                    player_wins = False
                    break
            if player_wins:
                return True
        return False
        
    def tictactoe(self, moves: List[List[int]]) -> str:
        # current_move: set to 'A' or 'B' to indicate who is moving
        player = 'A'
        game_over = False
        current_move_index = 0
        board = [[""] * 3 for _ in range(3)]

        while not game_over and current_move_index < len(moves):
            move_to_place = moves[current_move_index]
            board[move_to_place[0]][move_to_place[1]] = player
            if self.check_victory(board,player,move_to_place):
                return player
            if player == 'A':
                player = 'B'
            else:
                player = 'A'
            current_move_index += 1
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"

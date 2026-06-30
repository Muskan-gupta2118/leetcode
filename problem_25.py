#chess game design

# ---------- Base Piece Class ----------

class Piece:
    def __init__(self, color):
        self.color = color

    def symbol(self):
        return "?"

    def move(self, start, end):
        print(f"{self.symbol()} moves from {start} to {end}")


# ---------- Individual Pieces ----------

class King(Piece):
    def symbol(self):
        return "♔" if self.color == "White" else "♚"


class Queen(Piece):
    def symbol(self):
        return "♕" if self.color == "White" else "♛"


class Rook(Piece):
    def symbol(self):
        return "♖" if self.color == "White" else "♜"


class Bishop(Piece):
    def symbol(self):
        return "♗" if self.color == "White" else "♝"


class Knight(Piece):
    def symbol(self):
        return "♘" if self.color == "White" else "♞"


class Pawn(Piece):
    def symbol(self):
        return "♙" if self.color == "White " else "♟"


# ---------- Player ----------

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color


# ---------- Board ----------

class Board:

    def __init__(self):

        self.board = [[None for _ in range(8)] for _ in range(8)]

        self.setup_board()

    def setup_board(self):

        # White Pieces

        self.board[7][0] = Rook("White")
        self.board[7][1] = Knight("White")
        self.board[7][2] = Bishop("White")
        self.board[7][3] = Queen("White")
        self.board[7][4] = King("White")
        self.board[7][5] = Bishop("White")
        self.board[7][6] = Knight("White")
        self.board[7][7] = Rook("White")

        for i in range(8):
            self.board[6][i] = Pawn("White")

        # Black Pieces

        self.board[0][0] = Rook("Black")
        self.board[0][1] = Knight("Black")
        self.board[0][2] = Bishop("Black")
        self.board[0][3] = Queen("Black")
        self.board[0][4] = King("Black")
        self.board[0][5] = Bishop("Black")
        self.board[0][6] = Knight("Black")
        self.board[0][7] = Rook("Black")

        for i in range(8):
            self.board[1][i] = Pawn("Black")

    def display(self):

        print("\n========= CHESS BOARD =========\n")

        for row in self.board:

            for piece in row:

                if piece:
                    print(piece.symbol(), end=" ")

                else:
                    print(".", end=" ")

            print()

    def move_piece(self, sr, sc, er, ec):

        piece = self.board[sr][sc]

        if piece is None:
            print("No Piece Found")
            return

        self.board[er][ec] = piece
        self.board[sr][sc] = None

        piece.move((sr, sc), (er, ec))


# ---------- Game ----------

class ChessGame:

    def __init__(self):

        self.board = Board()

        self.player1 = Player("Player 1", "White")
        self.player2 = Player("Player 2", "Black")

        self.turn = "White"

    def play(self):

        while True:

            self.board.display()

            print("\nCurrent Turn :", self.turn)

            print("Enter Move")

            sr = int(input("Start Row : "))
            sc = int(input("Start Column : "))

            er = int(input("End Row : "))
            ec = int(input("End Column : "))

            self.board.move_piece(sr, sc, er, ec)

            if self.turn == "White":
                self.turn = "Black"
            else:
                self.turn = "White"

            ch = input("Continue (y/n): ")

            if ch.lower() != "y":
                break


# ---------- Main ----------

game = ChessGame()

game.play()
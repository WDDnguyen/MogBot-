class TicTacToe():

    board = None
    boardSize = None

    player1Marker = "X"
    player2Marker = "O"

    currentMarker = "X"

    def __init__(self,boardSize):
        self.boardSize = boardSize

    def initializeBoard(self):
        initialValue = " "
        self.board = [[initialValue for x in range(self.boardSize)] for y in range(self.boardSize)]
        for index in range(self.boardSize):
            print (self.board[index])

        self.currentMarker = "X"

    def alternateMarker(self):

        if self.currentMarker == self.player2Marker:
            self.currentMarker = self.player1Marker
        else:
            self.currentMarker = self.player2Marker


    def placeMarker(self,playerInput):

        if self.board[playerInput[0]][playerInput[1]] == " ":
            self.board[playerInput[0]][playerInput[1]] = self.currentMarker
            print("---------------------------------\n")
            self.alternateMarker()
            self.printBoard()
            self.statusOfGame()

        else :
            print ("There is already a marker there, please try again")

    def printBoard(self):
        for index in range(self.boardSize):
            print(self.board[index])

    def wonByRow(self):
        player1RowCounter = 0
        player2RowCounter = 0

        for row in range(self.boardSize):
            for column in range(self.boardSize):
                if self.board[row][column] == self.player1Marker:
                    player1RowCounter = player1RowCounter + 1
                elif self.board[row][column] == self.player2Marker:
                    player2RowCounter = player2RowCounter + 1

            if player1RowCounter == self.boardSize:
                print("Player1 Won By Row")

            if player2RowCounter == self.boardSize:
                print("Player2 Won By Row")

            player1RowCounter = 0
            player2RowCounter = 0

    def wonByColumn(self):
        player1ColumnCounter = 0
        player2ColumnCounter = 0

        for column in range(self.boardSize):
            for row in range(self.boardSize):
                if self.board[row][column] == self.player1Marker:
                    player1ColumnCounter = player1ColumnCounter + 1
                elif self.board[row][column] == self.player2Marker :
                    player2ColumnCounter = player2ColumnCounter + 1

            if player1ColumnCounter == self.boardSize:
                print("Player1 Won By Column")

            if player2ColumnCounter == self.boardSize:
                print("Player2 Won By Column")

            player1ColumnCounter = 0
            player2ColumnCounter = 0

    def wonByDiagonal(self):
        player1DiagonalCounter = 0
        player2DiagonalCounter = 0

        for diagonal in range(self.boardSize):

            if self.board[diagonal][diagonal] == self.player1Marker:
                player1DiagonalCounter = player1DiagonalCounter + 1
            elif self.board[diagonal][diagonal] == self.player2Marker:
                player2DiagonalCounter = player2DiagonalCounter + 1

        if player1DiagonalCounter == self.boardSize:
            print("Player1 Won By Diagonal")

        if player2DiagonalCounter == self.boardSize:
            print("Player2 Won By Diagonal")

    def statusOfGame(self):
        self.wonByRow()
        self.wonByColumn()
        self.wonByDiagonal()



def main():

    boardSize = 3

    #Won by Row
    player1Input1 = [1,0]
    player1Input2 = [1,1]
    player1Input3 = [1,2]

    player2Input1 = [2, 2]
    player2Input2 = [0, 0]

    TTT = TicTacToe(boardSize)
    TTT.initializeBoard()

    TTT.placeMarker(player1Input1)
    TTT.placeMarker(player2Input1)
    TTT.placeMarker(player1Input2)
    TTT.placeMarker(player2Input2)
    TTT.placeMarker(player1Input3)

    TTT.initializeBoard()

    player1Input1 = [0, 1]
    player1Input2 = [1, 1]
    player1Input3 = [2, 1]

    player2Input1 = [2, 2]
    player2Input2 = [0, 0]

    TTT.placeMarker(player1Input1)
    TTT.placeMarker(player2Input1)
    TTT.placeMarker(player1Input2)
    TTT.placeMarker(player2Input2)
    TTT.placeMarker(player1Input3)

    TTT.initializeBoard()

    player1Input1 = [1, 1]
    player1Input2 = [0, 0]
    player1Input3 = [2, 2]

    player2Input1 = [2, 1]
    player2Input2 = [0, 1]

    TTT.placeMarker(player1Input1)
    TTT.placeMarker(player2Input1)
    TTT.placeMarker(player1Input2)
    TTT.placeMarker(player2Input2)
    TTT.placeMarker(player1Input3)

if __name__ == '__main__':
    main();



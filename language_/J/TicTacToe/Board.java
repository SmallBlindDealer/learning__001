

public class Board {
    public Piece[][] grid;
    public int size;

    Board(int size){
        this.size=size;
        this.grid = new Piece[size][size];
    }

    public boolean isValidMove(int x, int y) {
        if (grid[x][y]!=null) {
            return false;
        }
        return true;
    }

    public void makeMove(int x, int y, Piece piece) {
        this.grid[x][y]=piece;
    }

    public boolean isPieceWin(Piece piece) {
        return false;
    }

    public void printBoard() {
        
    }
}

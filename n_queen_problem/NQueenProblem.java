/*
 * Following code is the implementation of the N-queen problem.
 * The solution is to place the queens on board such that no queen is under attack by another queen.
 * There can be a number of possible solutions for a given length of board.
 * This implementation prints only one valid solution, it can be extended to print all possible valid solutions.
 */

import java.util.Arrays;

public class NQueenProblem {

    private static boolean isQueenSafe(int[][] board, int row, int column) {
        int i;
        int j;
        int boardLength = board[0].length;
        for (i = 0; i < column; ++i)
            if (board[row][i] == 1)
                return false;  // If there's another Queen present in the same row.

        for (i = row, j = column; i >= 0 && j >= 0; --i, --j)
            if (board[i][j] == 1)
                return false;  // If there's another Queen present in the upper diagonal.

        for (i = row, j = column; j >= 0 && i < boardLength; ++i, --j)
            if (board[i][j]==1)
                return false;  // If there's another Queen present in the lower diagonal.

        return true;
    }

    private static boolean solveNQueen(int[][] board, int column) {
        int boardLength = board[0].length;
        if (column >= boardLength)
            return true;

        for (int i = 0; i < boardLength; ++i) {
            if (isQueenSafe(board, i, column)) {
                board[i][column] = 1;  // Place queen on (row, column) = (i, column).
                if (solveNQueen(board, column + 1))  // Recurse for remaining board
                    return true;
                else
                    board[i][column] = 0;
            }
        }
        return false;
    }

    public static final boolean solveNQueen(int[][] board) {
        return solveNQueen(board, 0);
    }

    public static void main(String[] args) {
        int boardLength = 8;
        int[][] board = new int[boardLength][boardLength];
        if (!solveNQueen(board)) {
            System.out.println("There is no possible answer for this boardLength");
        } else {
            System.out.println("A possible answer for given boardLength is:");
            for (int i = 0; i < boardLength; ++i) {
                System.out.println(Arrays.toString(board[i]));
            }
        }
    }
}

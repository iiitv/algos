/*
 * Implementation of popular N-Queen Problem using Backtracking algorithm.
 * The size of a chess board is given, suppose n, then we have to suggest such a configuration than n queens could be placed on the chess board and no queen is under attack
 * There can be a number of possible solutions for a specific board.
 * This implementation prints only one valid configuration, it can be extended to print all possible valid configurations.
 * A good example of recursion.
 * You can see the solution for various sizes by changing the value of Size in 14th line..
 */
#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

#define side 8                          /* Size of the board = (side X side) */
                              
/* The Queen is safe, if
 * There's no other Queen in the same row.
 * There's no other Queen in the same column.
 * There's no other Queen in the same diagonal.
 */
bool queen_is_safe(int board[side][side], int row, int col) {
    int i,j;
    for (i = 0; i < col; i++)
        if (board[row][i]==1)
            return false;  // * return false, if there's another Queen present in the same row.

    for (i=row, j=col; i>=0 && j>=0; i--, j--)
        if (board[i][j]==1)
            return false;  // * return false, if there's another Queen present in the upper diagonal.

    for (i=row, j=col; j>=0 && i<side; i++, j--)
        if (board[i][j]==1)
            return false;  // * return false, if there's another Queen present in the lower diagonal.

    return true;
}

bool find_solution(int board[side][side], int col) {
    if (col >= side)
        return true;       // * return true,

    for (int i = 0; i < side; i++) {
        if ( queen_is_safe(board, i, col) ) {
            board[i][col] = 1;                       // * A queen is placed on (i, col).
            if (find_solution(board, col + 1) )      // * Calling Find_solution() to place the rest of the queens.
                return true;
            else
                board[i][col] = 0;                   // * Backtrack
        }
    }
    return false;
}

int main() {
    int board[side][side];                  // * A chess board of rows = Size & columns = Size.
    memset(board, 0, sizeof(board));        // * Initially the board is empty, so all elements of 2-D array board are 0.

    if ( find_solution(board, 0) == false ) {
      printf("No possible configuration exists.");
      return 0;
    }
    // * Printing the answer.
    cout<<endl<<"No. of queens = Chess board size = "<<side<<" X "<<side<<endl<<endl<<endl;
    
   for (int i = 0; i < side; i++) {
        for (int j = 0; j < side; j++)
            cout<<board[i][j]<<"   ";
        cout<<"\n\n";
    }
    return 0;
}

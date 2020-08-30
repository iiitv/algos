/*
 * Implementation of popular N-Queen Problem using Backtracking algorithm.
 * The size of a chess board is given, suppose n, then we have to suggest such a configuration than n queens could be placed on the chess board and no queen is under attack
 * There can be a number of possible solutions for a specific board.
 * This implementation prints only one valid configuration, it can be extended to print all possible valid configurations.
 * A good example of recursion.
 * You can see the solution for various sizes by changing the value of Size in 13th line..
 */
#include <iostream>
#include <cstring>
using namespace std;

#define SIDE 8  /* Size of the board = (SIDE X SIDE) */

/* The Queen is safe, if
 * There's no other Queen in the same row.
 * There's no other Queen in the same column.
 * There's no other Queen in the same diagonal.
 */
bool queen_is_safe(int board[SIDE][SIDE], int row, int col) {
	int i,j;
	for (i = 0; i < col; i++) {
		if (board[row][i] == 1) {
			return false;  // * return false, if there's another Queen present in the same row.
		}
	}

	for (i = row, j = col; i >= 0 && j >= 0; i--, j--) {
		if (board[i][j] == 1) {
			return false;  // * return false, if there's another Queen present in the upper diagonal.
		}
	}

	for (i = row, j = col; j >= 0 && i < SIDE; i++, j--) {
		if (board[i][j]==1) {
			return false;  // * return false, if there's another Queen present in the lower diagonal.
		}
	}

	return true;
}

bool n_queen_solution(int board[SIDE][SIDE], int col) {
	if (col >= SIDE) {
		return true;  // * return true,
	}

	for (int i = 0; i < SIDE; i++) {
		if ( queen_is_safe(board, i, col) ) {
			board[i][col] = 1;  // * A queen is placed on (i, col).
			if (n_queen_solution(board, col + 1)) {  // * Calling n_queen_solution() to place the rest of the queens.
				return true;
			} else {
				board[i][col] = 0;  // * Backtrack
			}
		}
	}
	return false;
}

int main() {
	int board[SIDE][SIDE];  // * A chess board of rows = SIDE & columns = SIDE.
	memset(board, 0, sizeof(board));  // * Initially the board is empty, so all elements of 2-D array board are 0.

	if ( n_queen_solution(board, 0) == false ) {
		cout << "No possible configuration exists.\n\n";
		return 0;
	}
	// * Printing the answer.
	cout << "\n No. of queens = " << SIDE << "\n";
	cout << "\n Chess board size = " << SIDE << " X " << SIDE << "\n\n";

	for (int i = 0; i < SIDE; i++) {
		for (int j = 0; j < SIDE; j++) {
			cout << "  "<<board[i][j];
		}
		cout << "\n\n";
	}
	return 0;
}

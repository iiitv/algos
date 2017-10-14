// Given a chess board having N×N cells
// place N queens on the board in such a way that no queen attacks any other queen.

// There can be a number of possible solutions for a given length of board.
// This implementation prints only one valid solution, it can be extended to print all possible valid solutions.

package main

import "fmt"

func main() {
	n := 8 // size of chess board (n x n)

	// make board
	b := make([][]int, n)
	for i := range b {
		b[i] = make([]int, n)
	}

	if placeQueen(&b, n) {
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				fmt.Printf("%d ", b[i][j])
			}
			fmt.Print("\n")
		}
	} else {
		fmt.Println("Not possible")
	}
}

func isAttacked(b *[][]int, x, y, n int) bool {
	for i := 0; i < n; i++ {
		if (*b)[x][i] == 1 {
			return true
		}
		if (*b)[i][y] == 1 {
			return true
		}
		for j := 0; j < n; j++ {
			if (i-j == x-y) || (i+j == x+y) {
				if (*b)[i][j] == 1 {
					return true
				}
			}
		}
	}
	return false
}

func placeQueen(b *[][]int, n int) bool {
	if n == 0 {
		return true
	}
	for i := 0; i < len(*b); i++ {
		for j := 0; j < len(*b); j++ {
			if !(isAttacked(b, i, j, len(*b))) {
				(*b)[i][j] = 1
				if placeQueen(b, n-1) {
					return true
				}
				(*b)[i][j] = 0
			}
		}
	}
	return false
}

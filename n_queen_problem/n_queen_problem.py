"""
Following code is the implementation of the N-queen problem.
The solution is to place the queens on board such that
no queen is under attack by another queen.
This implementation computes all solutions for a board,
then prints the number of solutions. The number of solutions
follows the OEIS sequence https://oeis.org/A000170.
"""


def is_queen_under_attack(col, queens):
    """
    :param col: int
        Column of queen to test
    :param queens: list of tuple of int
        List of coordinates of other queens
    :return: boolean
        True if and only if queen in given position is under attack
    """

    left = right = col
    for coords in reversed(queens):
        left, right = left - 1, right + 1
        if coords[1] in (left, col, right):
            return True
    return False


def get_solutions(board_size, queens):
    """
    :param board_size: int
        Size of board to solve
    :param queens: int
        Number of queens to place in board
    :return: list of list of tuple of int
        Finds solutions of problem
    """

    smaller_solutions = n_queen_problem(board_size, queens - 1)
    solutions = []
    for solution in smaller_solutions:
        for column in range(1, board_size + 1):
            if not is_queen_under_attack(column, solution):
                solutions.append(solution + [(queens, column)])

    return solutions


def n_queen_problem(board_size, queens):
    """
    :param board_size: int
        Size of board to solve
    :param queens: int
        Number of queens to place in board
    :return: list of list of tuple of int
        Each list contains the coordinates of the queens
        that solve the problem
    """

    if queens < 1:  # there are no queens to place
        return [[]]  # 1 solution only: not place any queen

    if queens > board_size:  # more queens than the board can contain
        return []  # pigeonhole principle -> 0 solutions

    return get_solutions(board_size, queens)


def main():
    board_size = 10
    solutions = n_queen_problem(board_size, board_size)
    print(len(solutions))


if __name__ == '__main__':
    main()

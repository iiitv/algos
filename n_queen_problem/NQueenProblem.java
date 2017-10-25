import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.Iterator;
import java.util.List;


/**
 * <p>This class solves the N Queens Problem.</p>
 *
 * <p>Once you create an object with the desired board size, you can get an iterator that lazily will create each
 * possible solution is there's any. The code will create all solutions, not jut unique ones</p>
 *
 * <p>This way you have flexibility on how to use solutions, you can get only one or all.</p>
 *
 * @see <a href="https://en.wikipedia.org/wiki/Eight_queens_puzzle">N Queens Problem</a>
 */
public class NQueenProblem implements Iterable<NQueenProblem.Solution> {

    private final int size;

    /**
     * Creates an NQueens object to solve the N Quees Problems on board of size n
     *
     * @param n
     */
    public NQueenProblem(final int n) {
        this.size = n;
    }

    /**
     * Returns an Iterator over the solutions for this N Queens Problem.
     */
    @Override
    public Iterator<Solution> iterator() {
        return new NQueenIterator();
    }

    /**
     * <p>This class represents a Solution for the N Queen problem.</p>
     *
     * <p>Internally a solution is encoded as a list of integers. If in the index i there's integer j
     * it means that one of the queens should be placed on the square (i, j)</p>
     *
     */
    public static class Solution {

        private final List<Integer> board;
        private static char QUEEN = 'Q';
        private static char EMPTY_SQUARE = '.';
        private static String NEW_LINE = String.format("%n"); // platform independent new line character.

        public Solution(final List<Integer> board) {
            this.board = board;
        }

        /**
         * <p>Returns an String that looks like a board where '.' represents an empty square and 'Q' represents an square with a queen</p>
         */
        @Override
        public String toString() {
            StringBuilder builder = new StringBuilder();
            for (int i = 0; i < board.size(); ++i) {
                for (int j = 0; j < board.size(); ++j) {
                    if (board.get(i) == j) {
                        builder.append(QUEEN);
                    } else {
                        builder.append(EMPTY_SQUARE);
                    }
                }
                builder.append(NEW_LINE);
            }
            return builder.toString();
        }
    }

    private class NQueenIterator implements Iterator<Solution> {

        /**
         * Queue to store the intermediate boards necessary to build all solutions.
         */
        private final Deque<List<Integer>> queue;
        /**
         * Next solution to be returned.
         */
        private Solution next;

        /**
         * Initializes the queue and adds an empty board to it.
         */
        private NQueenIterator() {
            this.queue = new ArrayDeque<>();
            queue.add(new ArrayList<>(size));
        }

        /**
         * <p>Returns true is there's one more solution.</p>
         *
         * <p>It uses a backtracking algorithm to check for a possible solution. It removes the last board enqueued
         * and for the next empty column it tries to place a queen in every square. If that queen doesn't attack any of the already
         * placed queens, it queues a board with that queen. Once it removes a board with 8 queens, it stops and returns true</p>
         */
        @Override
        public boolean hasNext() {
            while (!queue.isEmpty()) {
                List<Integer> current = queue.removeLast();
                if (current.size() == size) {
                    this.next = new Solution(current);
                    return true;
                }
                int column = current.size();
                for (int row = 0; row < size; ++row) {
                    if (isValid(current, column, row)) {
                        List<Integer> next = new ArrayList<>(current);
                        next.add(row);
                        queue.addLast(next);
                    }
                }
            }
            return false;
        }

        @Override
        public Solution next() {
            return next;
        }

        /**
         * <p>Returns true if is isValid to place a queen on the square (column, row)</p>
         *
         * <p>A queen can be placed if it doesn't attack any of the already placed queens: there can't be a queen
         * already in the same row, and the queen can't be collinear with any other.</p>
         *
         * @param board a representation of the current board as explained in {@link Solution}
         * @param column the column we want to test to see if a queen can be placed without attacking any existing one
         * @param row the row we want to test to see if a queen can be placed without attacking any existing one
         * @return true if a queen can be placed on (column, row) without attacking any queens already in board
         */
        private boolean isValid(List<Integer> board, int column, int row) {
            for (int j = 0; j < column; ++j) {
                if (board.get(j) == row) {
                    return false;
                }
                if (areCollinear(column, j, board.get(j), row)) {
                    return false;
                }
            }
            return true;
        }

        /**
         * Verifies that the square (x, y) is not collinear with square (x1, y1)
         *
         * @param x
         * @param y
         * @param x1
         * @param y1
         * @return
         */
        private boolean areCollinear(int x, int y, int x1, int y1) {
            return Math.abs(y - x) == Math.abs(x1 - y1);
        }
    }

    public static void main(String[] args) {
        NQueenProblem queens = new NQueenProblem(5);
        for (Solution s : queens) {
            System.out.println(s);
        }
    }
}

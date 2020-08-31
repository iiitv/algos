public class Sqaure_matrix_multiplication {

    public int[][] SMMR(int[][] A, int[][] B) {
        double alen = A.length;
        int n = (int) Math.ceil(Math.log(alen) / Math.log(2));
        n = (int) Math.pow(2, n);
        if (n != alen) {    
            int[][] a = copyArray(A, n);
            int[][] b = copyArray(B, n);
            int[][] C = SMMR(a, b, 0, 0, 0, 0, n);
            int[][] c = new int[A.length][A.length];
            for (int i = 0; i < A.length; i++)
                for (int j = 0; j < A.length; j++)
                    c[i] = C[i];
            return c;
        } else
            return SMMR(A, B, 0, 0, 0, 0, n);
    }

    private int[][] SMMR(int[][] A, int[][] B, int rowA, int colA, int rowB, int colB, int n) {
        int[][] C = new int[n][n];
        int m = n / 2;
        if (n == 1)
            C[0][0] = A[rowA][colA] * B[rowB][colB];
        else {
            addMAt(C, SMMR(A, B, rowA, colA, rowB, colB, m), SMMR(A, B, rowA, colA + m, rowB + m, colB, m), 0, 0);

            addMAt(C, SMMR(A, B, rowA, colA, rowB, colB + m, m), SMMR(A, B, rowA, colA + m, rowB + m, colB + m, m), m,
                    0);
            addMAt(C, SMMR(A, B, rowA, colA, rowB, colB + m, m), SMMR(A, B, rowA, colA + m, rowB + m, colB, m), 0, m);

            addMAt(C, SMMR(A, B, rowA + m, colA, rowB, colB + m, m),
                    SMMR(A, B, rowA + m, colA + m, rowB + m, colB + m, m), m, m);

        }
        return C;
    }

    int[][] copyArray(int a[][], int n) {
        int[][] x = new int[n][n];
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a.length; j++)
                x[i][j] = a[i][j];
        }
        return x;
    }

    void addMAt(int[][] ans, int[][] A, int[][] B, int row, int col) {
        int n = A.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                ans[i + row][j + col] = A[i][j] + B[i][j];
            }
        }
    }

    void show(int[][] a) {
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a.length; j++) {
                System.out.print(a[i][j] + "\t");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int[][] a = { { 11, 2, 3, 4, -15, 6, 17, 8 }, { 3, -7, 16, 5, 14, 3, 22, 1 }, { 22, 3, 6, 25, 24, 23, 12, 3 },
                { 7, 6, 35, 4, 23, 2, -11, 22 }, { 25, 6, 7, 28, 11, -12, 3, 4 }, { 6, -15, 8, 7, 24, 3, 23, -4 },
                { -11, 2, 2, -11, 5, 6, 27, 18 }, { 12, 7, 24, 15, 6, 17, 8, 19 } };
        int[][] b = { { 5, 12, 8, -11, 4, 18, 6, 2 }, { -23, 15, 9, 7, 22, 11, 14, 16 },
                { -5, -18, 23, 28, -34, 24, 6, 9 }, { 7, 14, 11, 6, 9, -4, -7, 6 }, { 4, 5, -6, -7, 8, 9, 10, -11 },
                { 12, -13, 14, 15, 16, -17, 18, 19 }, { -20, 21, 22, -23, 24, -25, 26, 27 },
                { 4, 3, 2, 1, 9, 8, 7, 6 } };
        Sqaure_matrix_multiplication ob = new Sqaure_matrix_multiplication();
        int n = a.length;
        int[][] c = new int[n][n];
        c = ob.SMMR(a, b);
        ob.show(c);
    }
}
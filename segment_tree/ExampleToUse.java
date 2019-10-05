import java.util.Scanner;

public class ExampleToUse {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        long[] a = new long[n];
        for (int i = 0; i < n; i++) a[i] = in.nextLong();

        SegmentTree tree = new SegmentTree(a, new MaxOperation());
        int m = in.nextInt();
        for (int i = 0; i < m; i++) {
            char[] s = in.next().toCharArray();
            if (s[0] == 'm') {
                int l = in.nextInt(), r = in.nextInt();
                System.out.println(tree.query(l, r));
            } else {
                int p = in.nextInt(), x = in.nextInt();
                tree.update(p, x);
            }
        }
    }
}

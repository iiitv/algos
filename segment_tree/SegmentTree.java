public class SegmentTree {

    private long[] tree;
    private int n;

    private IOperation iOperation;

    private void build(long a[], int v, int l, int r) {
        if (l == r) tree[v] = a[l];
        else {
            int m = l + (r - l) / 2;
            build(a, v * 2 + 1, l, m);
            build(a, v * 2 + 2, m + 1, r);
            tree[v] = iOperation.call(tree[v * 2 + 1], tree[v * 2 + 2]);
        }
    }

    private long _query(int v, int l, int r, int L, int R) {
        if (r < L || R < l) return 0;
        if (L <= l && r <= R) return tree[v];
        int m = l + (r - l) / 2;
        return iOperation.call(_query(v * 2 + 1, l, m, L, R), _query(v * 2 + 2, m + 1, r, L, R));
    }

    private void _update(int v, int l, int r, int p, int x) {
        if (l == r) tree[v] = x;
        else {
            int m = l + (r - l) / 2;
            if (p <= m) _update(v * 2 + 1, l, m, p, x);
            else _update(v * 2 + 2, m + 1, r, p, x);
            tree[v] = iOperation.call(tree[v * 2 + 1], tree[v * 2 + 2]);
        }
    }

    public SegmentTree(long[] a, IOperation iOperation) {
        this.n = a.length;
        tree = new long[4 * n + 1];
        this.iOperation = iOperation;
        build(a, 0, 0, n - 1);
    }

    public long query(int l, int r) {
        return this._query(0, 0, n - 1, l - 1, r - 1);
    }

    public void update(int index, int value) {
        this._update(0, 0, n - 1, index - 1, value);
    }
}

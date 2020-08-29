//package algos.segment_tree;

public class Segment_Tree {
    int min(int a, int b)// min function to compute minimum of 2 values
    {
        if (a < b)
            return a;
        return b;
    }

    void build(int left, int right, int tree[], int arr[], int index)// to recursively contruct the segment tree in O(n)
    {
        if (left == right) {
            tree[index] = arr[left];
            return;
        } else {
            int mid = (left + right) / 2;
            build(left, mid, tree, arr, 2 * index + 1);// to build the left subtree
            build(mid + 1, right, tree, arr, 2 * index + 2);// to build the right subtree
            tree[index] = min(tree[2 * index + 1], tree[2 * index + 2]);
            return;
        }

    }

    void update(int left, int right, int tree[], int arr[], int index, int ind, int value)// to update a value at an index

    {
        if (right < ind || left > ind)
            return;

        if (left == right && left == ind) {
            tree[index] = value;
            return;
        }

        int mid = (left + right) / 2;
        update(left, mid, tree, arr, 2 * index + 1, ind, value);
        update(mid + 1, right, tree, arr, 2 * index + 2, ind, value);
        tree[index] = min(tree[2 * index + 1], tree[2 * index + 2]);

    }

    int ans(int left, int right, int initial, int last, int tree[], int arr[], int index)// to provide the minimum value
    {
        if (left <= initial && right >= last)
            return tree[index];
        if (right < initial || left > last)
            return (int) 1e9;

        int mid = (initial + last) / 2;
        return min(ans(left, right, initial, mid, tree, arr, 2 * index + 1),
                ans(left, right, mid + 1, last, tree, arr, 2 * index + 2));
    }

    public static void main(String args[]) {
        int tc = 1;

        while ((tc--) != 0) {
            int n;

            int arr[] = { 9, 4, 5, 3, 6, 2, 10 };
            n = 7;
            Segment_Tree sg = new Segment_Tree();

            int tree[] = new int[14];// to contruct a seg tree in the form of array
            sg.build(0, n - 1, tree, arr, 0);// to construct segment tree in O(n)

            int l = 1, r = 5;
            System.out.println(
                    "the min value in the range 1 to 5 inclusive is:\n" + sg.ans(l - 1, r - 1, 0, n - 1, tree, arr, 0));

            int ind = 3, value = -20;
            sg.update(0, n - 1, tree, arr, 0, ind - 1, value);// to update the value at index ind in array
            System.out.println("the new min value in the range 1 to 5 inclusive is:\n"
                    + sg.ans(l - 1, r - 1, 0, n - 1, tree, arr, 0));

        }
    }

}

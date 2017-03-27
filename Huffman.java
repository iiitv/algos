import java.math.*;
public class Huffman{
	NodeH[] a;
	Node head;
	int n;
	public Huffman(NodeH[] A, int len){
		this.a=A;
		n=len;
	}
	public void encryptHuff(){

		MergeSort ms= new MergeSort();
		ms.mergeSort(a,0,n-1);
		 head=makeTree();																															

	}
	public String getHuff(int num){
		String ret;
		Node temp=head;
		while(temp.data!=num&&temp.left!=null&&temp.right.!=null){
  			

		}


	}
	public Node makeTree(){
		int i=2;
		Node newN= new Node(a[1].freq+a[0].freq);
		newN.left=new Node(a[0].freq);
		newN.right=new Node(a[1].freq);
		while(i!=n){
			Node head = new Node(a[i-1].freq+a[i].freq);
			head.left=new Node(Math.min(a[i].freq,newN.data));
			head.right=new Node(Math.max(a[i].freq,newN.data));
			i++;
			newN=head;
		}

		return newN;
	}

	
}
class NodeH{
	char ch;
	int freq;
	int pos;
	public NodeH(char c, int f){
		ch=c;
		freq=f;
	}
}
class Node{
	Node left;
	Node right;
	int data;
	public Node(int data){
		this.data=data;
		left=null;
		right=null;
	}

}
class MergeSort {

    static void merge(NodeH[] a, int first, int mid, int last) {
        int l = mid - first + 1;
        int r = last - mid;
        NodeH[] left = new NodeH[l];
        NodeH[] right = new NodeH[r];

        for (int i = 0; i < l; i++) {  //copy left
            left[i] = a[first + i];
        }
        for (int j = 0; j < r; j++) {  //copy right
            right[j] = a[mid + j + 1];
        }
        int i = 0;
        int j = 0;
        int k = first;
        while (i < l && j < r) {  //merging 
            if (left[i].freq <= right[j].freq) {
                a[k] = left[i];
                i++;
            } else {
                a[k] = right[j];
                j++;
            }
            k++;
        }
        while (i < l) {  //remainig left element
            a[k] = left[i];
            i++;
            k++;
        }
        while (j < r) {  //remainig right element
            a[k] = right[j];
            j++;
            k++;
        }
    }

    static void mergeSort(NodeH[] a, int first, int last) {
        if (first < last) {
            int mid = (first + last) / 2;  //find the middle
            mergeSort(a, first, mid);  //sort left half 
            mergeSort(a, mid + 1, last);  //sort right half
            merge(a, first, mid, last);  //merge above two sorted halves
        }
    }
}

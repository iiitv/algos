
//Time Complexity O(n)-> avg case and O(n^2)-> Worst Case
//constraints:- 0<=A[i]<1

public class BinSort {
    double a[];
    Node b[] = new Node[10];
    public BinSort(double A[]){
        a=A;
    }
    public void binSort() {
        for(int i=0;i<a.length;i++){
          int ins=(int)(a[i]*10);
          if(b[ins]==null){
              b[ins]=new Node(a[i]);
          }
          else {
              boolean check =true;
              Node temp=b[ins];
              while(temp.next!=null){
                  if(a[i]>temp.next.data){
                      temp=temp.next;
                  }
                  else {
                      if(a[i]<temp.data)
                          break;
                      Node newNode= new Node(a[i]);
                      newNode.next=temp.next;
                      temp.next=newNode;
                      check=false;
                      break;
                     }
              }
                  if(check) {
                      if(a[i]>=temp.data) {
                          Node newNode= new Node(a[i]);
                          temp.next=newNode;
                      }
                      else {
                          double loc=temp.data;
                          temp.data=a[i];
                          Node newNode = new Node(loc);
                          newNode.next=temp.next;
                          temp.next=newNode;
                      }
                  }
              }
          }
        int j=0;
        for(int i=0;i<10;i++) {
            while(b[i]!=null) {
                a[j++]=b[i].data;
                b[i]=b[i].next;
            }
        }
    }
}

class Node {
    double data;
    Node next;
    public Node(double data) {
         this.data=data;
         next=null;
        }
} 

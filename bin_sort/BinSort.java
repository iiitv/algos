import java.util.Random;

public class BinSort{


	public static void main(String[] args) {
		Random rand = new Random();
		int n=1000;
		double[] a = new double[n];
		Node[] b = new Node[10];
		for(int i = 0;i < n;i++) {
			a[i]=rand.nextDouble();
		}
		binSort(a, b);
		for(int i=0;i<n;i++){
			System.out.print(a[i]+ " ");
		}
	}

	public static void binSort(double[] a,Node[] b) {
        
        for(int i = 0;i < a.length;i++){
          int ins=(int)(a[i]*10);
          if(b[ins]==null){
              b[ins] = new Node(a[i]);
          }
          else{
              boolean check =true;
              Node temp = b[ins];
              while(temp.next != null) {
                  if(a[i] > temp.next.data) {
                      temp = temp.next;
                  }
                  else{
                      if(a[i] < temp.data)
                          break;
                      Node newNode = new Node(a[i]);
                      newNode.next = temp.next;
                      temp.next = newNode;
                      check = false;
                      break;
                     }
              }
                  if(check) {
                      if(a[i] >= temp.data) {
                          Node newNode = new Node(a[i]);
                          temp.next = newNode;
                      }
                      else {
                          double loc = temp.data;
                          temp.data = a[i];
                          Node newNode = new Node(loc);
                          newNode.next = temp.next;
                          temp.next = newNode;
                      }
                  }
                  
              }
          }
          
        int j=0;
        for(int i=0;i<10;i++){
            while(b[i]!=null){
                a[j++]=b[i].data;
                b[i]=b[i].next;
            }
        }
        
        
    }

	
}

class Node{
    double data;
    Node next;
    public Node(double data){
         this.data=data;
         next=null;
        }
} 

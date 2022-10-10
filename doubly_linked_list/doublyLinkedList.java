public class DoublyLinkedList {

    protected Node firstNode;
    protected Node lastNode;
    protected int size;

    public DoublyLinkedList(){this.size=0;}

    public void getLastNode(){
        Node temp = firstNode;
        while(temp.next != null){
            temp = temp.next;
        }
        lastNode = temp;
    }
    
    public void insertFirst(Object val){
        Node node = new Node(val);
        node.next = firstNode;
        node.prev = null;
        if (firstNode != null) {
            firstNode.prev = node;
        }
        firstNode = node;
        size ++;
    }

    public void insertLast(Object val){
        getLastNode();
        Node newNode = new Node(val);
        lastNode.next = newNode;
        newNode.prev = lastNode;
        size++;
    }

    public void checkpos(int pos){
        if(pos<0 || pos>size){
            System.out.println("Wrong Position Entered");
            System.exit(0);
        }
    }

    public void checkposition(int pos){
        if(pos<0 || pos>=size){
            System.out.println("Wrong Position Entered");
            System.exit(0);
        }
    }

    public void add(int pos, Object val){
        checkpos(pos);
        Node newNode = new Node(val);
        Node temp = firstNode;
        if(pos == 0){
            insertFirst(val);
        }else {
            while (pos-- > 1) {
                temp = temp.next;
            }
            newNode.next = temp.next;
            if(temp.next !=null){
                temp.next.prev = newNode;}
            newNode.prev = temp;
            temp.next = newNode;
            size++;
        }
    }

    public int size(){
        return size;
    }

    public void display(){
        Node temp = firstNode;
        System.out.print("START ");
        while(temp != null){
            System.out.print(temp.data+" <-> ");
            temp = temp.next;
        }
        System.out.print("END\n");
    }

    public Object get(int pos){
        checkposition(pos);
        Node temp = firstNode;
        while(pos-- >0){
            temp = temp.next;
        }
        return temp.data;
    }

    public Object remove(int pos){
        checkposition(pos);
        Node temp = firstNode;
        Node RE = new Node();
        if(pos == 0){
            RE = firstNode;
            firstNode = temp.next;
            temp.next.prev = null;
            size--;
            return RE.data;
        }
        else if(pos == size - 1){
            getLastNode();
            RE = lastNode;
            temp = lastNode;
            lastNode = temp.prev;
            temp.prev.next = null;
            size--;
            return RE.data;
        }
        while(pos-- > 1){
            temp = temp.next;
        }
        RE = temp.next;
        temp.next = temp.next.next;
        temp.next.prev = temp;
        size--;
        return RE.data;
    }

    public void reverseDisplay(){
        getLastNode();
        Node last = lastNode;
        System.out.print("START ");
        while(last != null){
            System.out.print(last.data+" <-> ");
            last = last.prev;
        }
        System.out.print("END\n");
    }

    public static void main(String[] args) {
        DoublyLinkedList d = new DoublyLinkedList();
        d.insertFirst(21);
        d.insertFirst(23);
        d.insertFirst(24);
        d.add(3,"hello");
        d.display();
        System.out.println("Size of the list is: "+ d.size());
        System.out.println("Removing Element");
        System.out.println(d.remove(3)); //displays the removed element
        d.display(); //displays the list after removal
        d.add(1,"hello"); //adds hello at 1st index
        d.insertLast(54);
        d.insertLast(421);
        System.out.println("After adding few more elements");
        d.display();
        System.out.println("Size of the list is: "+ d.size());
        System.out.println("Get Element at 0"+d.get(0));
        System.out.println("Reverse the List");
        d.reverseDisplay();
    }
}

class Node {
    Object data;
    Node next;
    Node prev;

    public Node() {}

    public Node(Object value) {
        this.data = value;
    }

    public Node(Object value, Node next, Node prev) {
        this.data = value;
        this.next = next;
        this.prev = prev;
    }
}

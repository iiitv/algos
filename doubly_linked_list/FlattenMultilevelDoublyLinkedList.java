class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;

    public Node() {}

    public Node(int val) {
        this.val = val;
    }
}

public class FlattenMultilevelDoublyLinkedList {
    public Node flatten(Node head) {
        if (head == null) {
            return null;
        }
        
        Node current = head;
        while (current != null) {
            if (current.child != null) {
                // Store the next node and flatten the child list
                Node next = current.next;
                Node childTail = flatten(current.child);
                
                // Connect the current node to the child list
                current.next = current.child;
                current.child.prev = current;
                current.child = null;

                // Connect the child list to the next node
                if (next != null) {
                    childTail.next = next;
                    next.prev = childTail;
                }
            }
            current = current.next;
        }
        
        return head;
    }
}

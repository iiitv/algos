package main

import "fmt"

type Node struct {
	Key   int
	Value int
	Left  *Node
	Right *Node
}

// Insert inserts a key-value pair into the node
// If the node's key is equal to the given key
// the node's value will be overwritten, and no
// new node will be added to the tree
func (n *Node) Insert(key, value int) {
	switch {
	case key == n.Key:
		n.Value = value
	case key < n.Key:
		if n.Left == nil {
			n.Left = &Node{Key: key, Value: value}
		} else {
			n.Left.Insert(key, value)
		}
	default:
		if n.Right == nil {
			n.Right = &Node{Key: key, Value: value}
		} else {
			n.Right.Insert(key, value)
		}
	}
}

// Max returns the max node and its parent
func (n *Node) Max(parent *Node) (*Node, *Node) {
	if n.Right == nil {
		return n, parent
	}
	return n.Right.Max(n)
}

// Replace replaces parent's child with node.
func (n *Node) Replace(parent, replacement *Node) {
	if n == parent.Left {
		parent.Left = replacement
	} else {
		parent.Right = replacement
	}
}

func (n *Node) Delete(key int, node *Node) {
	switch {
	case key < n.Key:
		n.Left.Delete(key, n)
	case key > n.Key:
		n.Right.Delete(key, n)
	default:
		if n.Left == nil && n.Right == nil {
			n.Replace(node, nil)
		} else if n.Left == nil {
			n.Replace(node, n.Right)
		} else if n.Right == nil {
			n.Replace(node, n.Left)
		} else {
			replacement, parent := n.Left.Max(n)
			n.Key = replacement.Key
			n.Value = replacement.Value
			replacement.Delete(replacement.Key, parent)
		}
	}
}

type BST struct {
	Root *Node
}

// Insert adds an element to the BST
// Insertion is O(log n)
func (bst *BST) Insert(key, value int) {
	if bst.Root == nil {
		bst.Root = &Node{
			Key:   key,
			Value: value,
		}
	} else {
		bst.Root.Insert(key, value)
	}
}

// Search traverses the tree trying to find a node
// with given key. If successfull, the value of the node
// will be returned with a true value. Otherwise 0 and false
// Search is O(log n)
func (bst *BST) Search(key int) (int, bool) {
	for node := bst.Root; node != nil; {
		if key == node.Key {
			return node.Value, true
		}
		if key < node.Key {
			node = node.Left
		} else {
			node = node.Right
		}
	}
	return 0, false
}

func (bst *BST) Delete(key int) {
	if bst.Root != nil {
		parent := &Node{Right: bst.Root}
		bst.Root.Delete(key, parent)
	}
}

func (bst *BST) Traverse(f func(key, value int)) {
	traverse(bst.Root, f)
}

func traverse(node *Node, f func(key, value int)) {
	if node == nil {
		return
	}
	traverse(node.Left, f)
	f(node.Key, node.Value)
	traverse(node.Right, f)
}

func main() {
	// create empty bst
	var bst BST
	// add some key value pairs
	bst.Insert(8, 9)
	bst.Insert(4, 2)
	bst.Insert(12, 19)
	bst.Insert(2, 8)
	bst.Insert(1, 200)
	bst.Insert(10, 16)

	// Print in order. Should print from lowest key to highest
	bst.Traverse(func(key, value int) {
		fmt.Printf("Key: %d, Value: %d\n", key, value)
	})

	// Searching for a key. Should return value and whether key was found or not
	value, ok := bst.Search(12)
	if ok {
		fmt.Printf("Key 12 was found! It's value is %d\n", value)
	}

	// Delet a key
	bst.Delete(12)
	// Search for same key again
	_, ok = bst.Search(12)
	if ok {
		fmt.Println("This shouldn't happen, since key should have been deleted")
	} else {
		fmt.Println("12 was not found :)")
	}
}

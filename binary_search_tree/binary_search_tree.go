package main

import "fmt"

type node struct {
	Key   int
	Value int
	Left  *node
	Right *node
}

// Insert inserts a key-value pair into the node
// If the node's key is equal to the given key
// the node's value will be overwritten, and no
// new node will be added to the tree
func (n *node) Insert(key, value int) {
	switch {
	case key == n.Key:
		// if same key, overwrite value
		n.Value = value
	case key < n.Key:
		// if key is lower
		if n.Left == nil {
			// create new left node if no left node exists
			n.Left = &node{Key: key, Value: value}
		} else {
			// otherwise, call insert on left node
			n.Left.Insert(key, value)
		}
	default:
		// if key is higher
		if n.Right == nil {
			// create new right node if no right node exists
			n.Right = &node{Key: key, Value: value}
		} else {
			// otherwise, call insert on right node
			n.Right.Insert(key, value)
		}
	}
}

// Max returns the max node and its parent
func (n *node) Max(parent *node) (*node, *node) {
	if n.Right == nil {
		// if node right node is null, this node must be max node.
		return n, parent
	}
	// call Max on right node
	return n.Right.Max(n)
}

// Replace replaces parent's child with node.
func (n *node) Replace(parent, replacement *node) {
	if n == parent.Left {
		// if this node is parents left node, replace parent left node with replacement
		parent.Left = replacement
	} else {
		// otherwise replae parents right node
		parent.Right = replacement
	}
}

// Delete will find the given key and delete the corresponding node
func (n *node) Delete(key int, node *node) {
	switch {
	case key < n.Key:
		// if key is lower call delete on left node
		if n.Left != nil {
			n.Left.Delete(key, n)
		}
	case key > n.Key:
		// if key is higher call delete on right node
		if n.Right != nil {
			n.Right.Delete(key, n)
		}
	default:
		// if keys are equal
		if n.Left == nil && n.Right == nil {
			// if node has no children, replace node with nil
			n.Replace(node, nil)
		} else if n.Left == nil {
			// if key has no left node, replace node with right node
			n.Replace(node, n.Right)
		} else if n.Right == nil {
			// if key has no right node, replace node with left node
			n.Replace(node, n.Left)
		} else {
			replacement, parent := n.Left.Max(n)
			n.Key = replacement.Key
			n.Value = replacement.Value
			replacement.Delete(replacement.Key, parent)
		}
	}
}

// BST (Binary Search Tree) struct just contains the root node
// so client code doesnt have to work with the nodes
type BST struct {
	root *node
}

// Insert adds an element to the BST
// Insertion is O(log n)
func (bst *BST) Insert(key, value int) {
	if bst.root == nil {
		// if root is nil, i.e. the tree is empty,
		// just assign new node to root
		bst.root = &node{
			Key:   key,
			Value: value,
		}
	} else {
		// otherwise call insert on root node
		bst.root.Insert(key, value)
	}
}

// Search traverses the tree trying to find a node
// with given key. If successfull, the value of the node
// will be returned with a true value. Otherwise 0 and false
// Search is O(log n)
func (bst *BST) Search(key int) (int, bool) {
	// start at root and traverse tree
	for node := bst.root; node != nil; {
		if key == node.Key {
			// if keys are equal: success
			return node.Value, true
		}
		if key < node.Key {
			// if key is lower, continue loop with left node
			node = node.Left
		} else {
			// if key is higher, continue loop with right node
			node = node.Right
		}
	}
	return 0, false
}

// Delete removes a node in the tree with the corresponding key
func (bst *BST) Delete(key int) {
	if bst.root != nil {
		// create fake parent node
		parent := &node{Right: bst.root}
		// call delete on root node
		bst.root.Delete(key, parent)
	}
}

// Traverse traverses the tree in order (https://en.wikipedia.org/wiki/Tree_traversal#In-order)
// and calls the supplied function for each node
func (bst *BST) Traverse(f func(key, value int)) {
	// call helper function on root
	traverse(bst.root, f)
}

// helper for traverse
func traverse(node *node, f func(key, value int)) {
	if node == nil {
		// stop if given node is nil
		return
	}
	// traverse down left subtree
	traverse(node.Left, f)
	// call function on node
	f(node.Key, node.Value)
	// traversen down right subtree
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
	searchKey := 12
	value, ok := bst.Search(searchKey)
	if ok {
		fmt.Printf("Key %d was found! It's value is %d\n", searchKey, value)
	}

	// Delete a key
	bst.Delete(searchKey)
	// Search for same key again
	_, ok = bst.Search(searchKey)
	if ok {
		fmt.Println("This shouldn't happen, since key should have been deleted")
	} else {
		fmt.Printf("Key %d was not found :)\n", searchKey)
	}
}

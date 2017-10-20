package main

import (
	"fmt"
)

// AlphabetSize is the size of the alphabet used.
// All nodes will have an array of pointers to other nodes,
// and this array will have the size of the alphabet.
// Setting to a smaller size (in allowed alphabet) will
// lower the space needed for the trie
const AlphabetSize int = 256

// inner node of trie
type node struct {
	value string
	next  [AlphabetSize]*node
}

// Helper methods:

// get traverses the trie byte by byte. returns a pointer
// to the final node (nil if key does not exist in trie)
func get(currentNode *node, key []byte, keyIndex int) *node {
	if currentNode == nil {
		return nil
	}
	if keyIndex == len(key) {
		// we've looked at each byte of the key
		// and must be at final node. return it
		return currentNode
	}
	// we still got bytes left in the key.
	// pick the next byte from the key
	c := key[keyIndex]
	// and get the next node at position c
	// also increment keyIndex.
	return get(currentNode.next[c], key, keyIndex+1)
}

// put returns a pointer to a node (representing a subtrie)
func put(currentNode *node, key []byte, value string, keyIndex int) *node {
	if currentNode == nil {
		// if given node is nil, create a new node
		currentNode = &node{}
	}
	if keyIndex == len(key) {
		// if we're at the end of the key bytes, set
		// the current node's value to the given value
		// and return it.
		currentNode.value = value
		return currentNode
	}
	// we still got bytes left in the key.
	// pick the next byte from the key
	c := key[keyIndex]
	// Set the next node at position c
	currentNode.next[c] = put(currentNode.next[c], key, value, keyIndex+1)
	return currentNode
}

// Trie is a wrapper around the the node struct
type Trie struct {
	root *node
}

// Get returns the value and whether the key
// exists in the trie or not. If the key does
// not exists, the returned string will be the
// empty string
func (t *Trie) Get(key string) (string, bool) {
	node := get(t.root, []byte(key), 0)
	if node == nil {
		return "", false
	}
	return node.value, true
}

// Put inserts a key/value pair into the trie
func (t *Trie) Put(key, value string) {
	t.root = put(t.root, []byte(key), value, 0)
}

func main() {
	keyValuePairs := map[string]string{
		"hello":  "world",
		"hola":   "mundo",
		"hej":    "verden",
		"sveika": "pasaule",
		"alofa":  "lalolagi",
	}

	var trie Trie

	for key, value := range keyValuePairs {
		trie.Put(key, value)
	}

	for _, key := range []string{"hello", "goodbye", "alofa", "tofa"} {
		value, ok := trie.Get(key)
		if ok {
			fmt.Printf("Key '%s' was in the trie with value '%s'\n", key, value)
		} else {
			fmt.Printf("Key '%s' was not in the trie\n", key)
		}
	}
}

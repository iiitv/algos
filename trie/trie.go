package main

import (
	"fmt"
)

const AlphabetSize int = 256 // bytesize

// inner node of trie
type node struct {
	value string
	next  [AlphabetSize]*node
}

// Helper methods:

// get traverses the trie byte by byte. returns a pointer
// to the final node (nil if key does not exist in trie)
func get(node *node, key []byte, d int) *node {
	if node == nil {
		return nil
	}
	if d == len(key) {
		// we've looked at each byte of the key
		// and must be at final node. return it
		return node
	}
	// we still got bytes left in the key.
	// pick the next byte from the key
	c := key[d]
	// and get the next node at position c
	// also increment d.
	return get(node.next[c], key, d+1)
}

// put returns a pointer to a node (representing a subtrie)
func put(nnode *node, key []byte, value string, d int) *node {
	if nnode == nil {
		// if given node is nil, create a new node
		nnode = &node{}
	}
	if d == len(key) {
		// if we're at the end of the key bytes, set
		// the current node's value to the given value
		// and return it.
		nnode.value = value
		return nnode
	}
	// we still got bytes left in the key.
	// pick the next byte from the key
	c := key[d]
	// Set the next node at position c
	nnode.next[c] = put(nnode.next[c], key, value, d+1)
	return nnode
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

package main

import (
	"fmt"
)

const AlphabetSize int = 256 // bytesize

type node struct {
	value string
	next  [AlphabetSize]*node
}

// Helper methods
func get(node *node, key []byte, d int) *node {
	if node == nil {
		return nil
	}
	if d == len(key) {
		return node
	}
	c := key[d]
	return get(node.next[c], key, d+1)
}

func put(nnode *node, key []byte, value string, d int) *node {
	if nnode == nil {
		nnode = &node{}
	}
	if d == len(key) {
		nnode.value = value
		return nnode
	}
	c := key[d]
	nnode.next[c] = put(nnode.next[c], key, value, d+1)
	return nnode
}

type Trie struct {
	root *node
}

func (t *Trie) Get(key string) (string, bool) {
	node := get(t.root, []byte(key), 0)
	if node == nil {
		return "", false
	}
	return node.value, true
}

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

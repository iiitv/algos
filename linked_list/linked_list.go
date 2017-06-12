package main

import (
	"errors"
	"fmt"
)

// List is a A general List interface
type List interface {
	Add(newVal int)
	Len() int
	PeekLast() (int, error)
	PeekFirst() (int, error)
	ToSlice() []int
}

type linkedListNode struct {
	value int
	next  *linkedListNode
}

// LinkedList is a singly-linked LinkedList
type LinkedList struct {
	root   *linkedListNode
	tail   *linkedListNode
	length int
}

// Len returns the length of the LinkedList
func (ll *LinkedList) Len() int { return ll.length }

// Add adds a new element to the LinkedList Time Complexity: O(1)
func (ll *LinkedList) Add(newVal int) {
	newNode := new(linkedListNode)
	newNode.value = newVal
	if ll.length == 0 {
		ll.root = newNode
		ll.root.next = nil
	} else if ll.length == 1 {
		ll.tail = newNode
		ll.root.next = ll.tail
	} else {
		ll.tail.next = newNode
		ll.tail = newNode
	}

	ll.length++
}

// RemoveFirst removes the first element from the LinkedList Time Complexity: O(1)
func (ll *LinkedList) RemoveFirst() (val int, err error) {
	if ll.length == 0 {
		return 0, errors.New("there is nothing to remove")
	} else if ll.length == 1 {
		val = ll.root.value
		ll.root = nil
	} else if ll.length == 2 {
		val = ll.root.value
		ll.root = ll.tail
		ll.tail = nil
	} else {
		val = ll.root.value
		ll.root = ll.root.next
	}

	ll.length--
	return
}

// ToSlice converts the LinkedList to a Slice Time Complexity: O(n)
func (ll *LinkedList) ToSlice() []int {
	var sliceList []int

	for currNode := ll.root; currNode != nil; currNode = currNode.next {
		sliceList = append(sliceList, currNode.value)
	}

	return sliceList
}

// PeekLast returns the last element of the LinkedList, without removing it Time Complexity: O(1)
func (ll *LinkedList) PeekLast() (val int, err error) {
	if ll.length == 0 {
		return 0, errors.New("there is nothing to peek")
	} else if ll.length == 1 {
		val = ll.root.value
	} else {
		val = ll.tail.value
	}

	return val, nil
}

// PeekFirst returns the first element of the LinkedList, without removing it Time Complexity: O(1)
func (ll *LinkedList) PeekFirst() (val int, err error) {
	if ll.length == 0 {
		return 0, errors.New("there is nothing to peek")
	}

	val = ll.root.value

	return val, nil
}

func main() {
	var ll LinkedList
	ll.Add(10)
	ll.Add(15)
	ll.Add(25)
	first, err := ll.RemoveFirst()
	for err == nil {
		fmt.Println(first)
		first, err = ll.RemoveFirst()
	}
}

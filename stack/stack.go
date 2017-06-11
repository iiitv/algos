package main

import (
	"errors"
	"fmt"
)

// Stack implements stack DS
type Stack struct {
	list []int
}

// Push pushes to stack
func (s *Stack) Push(data int) error {
	s.list = append(s.list, data)
	return nil
}

// Pop pops from stack
func (s *Stack) Pop() (int, error) {
	if len(s.list) == 0 {
		return -1, errors.New("pop from empty stack")
	}
	last := s.list[len(s.list)-1]
	s.list = s.list[:len(s.list)-1]
	return last, nil
}

func main() {
	var s Stack
	s.Push(2)
	s.Push(3)
	s.Push(5)
	last, err := s.Pop()
	for err == nil {
		fmt.Println(last)
		last, err = s.Pop()
	}
}

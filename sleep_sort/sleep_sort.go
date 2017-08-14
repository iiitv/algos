package main

import (
	"fmt"
	"time"
)

func SleepSort(numbers []int) []int {

	channel := make(chan int, len(numbers))

	for _, n := range numbers {
		go func(n int) {
			time.Sleep(time.Duration(n) * time.Second)
			channel <- n

		}(n)

	}

	sorted := make([]int, len(numbers))

	//  Get the result
	for i := 0; i < len(numbers); i++ {
		sorted[i] = <-channel
	}

	return sorted

}

func main() {
	sorted := SleepSort([]int{2, 3, 0, 4, 1})
	fmt.Println(sorted)
}

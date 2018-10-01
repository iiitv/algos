package main

import (
	"fmt"
	"math/rand"
	"sort"
)

// Bucket is a type alias of []float32. It is used in BucketSort() to represent
// individual buckets.
type Bucket []float32

// Methods required for sort.Sort()
func (b Bucket) Len() int {
	return len(b)
}

func (b Bucket) Swap(i, j int) {
	b[i], b[j] = b[j], b[i]
}

func (b Bucket) Less(i, j int) bool {
	return b[i] < b[j]
}

// BucketSort sorts provided slice of floats using Bucket Sort algorithm
// Time Complexity: O(n)-> Avg case and O(n^2)-> Worst Case
// Constraints: 0 <= arr[i] <= 1
func BucketSort(arr []float32) []float32 {
	n := len(arr)

	// Create n empty buckets, each can hold up to n elements
	buckets := make([]Bucket, n)
	for i := 0; i < n; i++ {
		// Set length to 0, but allocate memory for n elements
		buckets[i] = make([]float32, 0, n)
	}

	// Place all the elements into corresponding buckets
	for i := 0; i < n; i++ {
		bi := int(float32(n) * arr[i])
		buckets[bi] = append(buckets[bi], arr[i])
	}

	// Sort elements in each bucket
	for i := 0; i < n; i++ {
		sort.Sort(buckets[i])
	}

	// Put sorted elements into the resulting array
	sorted := make([]float32, 0, n)
	for i := 0; i < n; i++ {
		for j := 0; j < len(buckets[i]); j++ {
			sorted = append(sorted, buckets[i][j])
		}
	}
	return sorted
}

func makeRandomNumbers(n int) []float32 {
	arr := make([]float32, n)
	for i := range arr {
		arr[i] = rand.Float32()
	}
	return arr
}

func main() {
	n := 10
	arr := makeRandomNumbers(n)
	sorted := BucketSort(arr)
	fmt.Println(sorted)
}

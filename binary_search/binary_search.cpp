#include <iostream>
#include <vector>
using namespace std;

//------------------------------------------------
// Performs a binary search.
// Collection to be searched must be sorted.
// Worst case complexity O(log n).
// 
// INPUTS
// vector<int> list: collection of elements.
// int target: element to search for.
//
// OUTPUT
// int: index of target if it exists, else -1.
//------------------------------------------------
int binary_search(vector<int> list, int target) {
	int first = 0;
	int last = list.size() - 1;
	while (first <= last) {
		int mid = (first + last) / 2;
		if (list[mid] == target) {
			return mid;
		}
		else if (list[mid] > target) {
			last = mid - 1;
		}
		else {
			first = mid + 1;
		}
	}
	return -1;
}

//------------------------------------------------
// Test binary_search().
//------------------------------------------------
int main() {
	vector<int> list;
	list.push_back(1);
	list.push_back(2);
	list.push_back(5);
	int target = 2;
	int idx = binary_search(list, target);
	if (idx == -1) {
		cout << "Target not in list." << endl;
	}
	else {
		cout << "Target is at index " << idx << endl;
	}
}

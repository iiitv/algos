#include <iostream>
#include <vector>
#include <cmath>

// Use '-std=c++11' or higher flag while compiling
// g++ -std=c++11 -o ShellSort ShellSort.cpp

using namespace std;

// Worst case time complexity = O(n^2)
// Best case complexity = O(nlog(n))

vector<int> shellSort(vector<int> data) {
	for (int i = static_cast<int>(data.size() / 2); i > 0; i /= 2) {
		for (int j = i; j < data.size(); ++j) {
			for (int k = j - i; k >= 0; k -= i) {
				if (data[k+i] >= data[k]) {
					break;
				} else {
					swap(data[k], data[k+i]);
				}
			}
		}
	}
	return data;
}

void print(vector<int> data) {
	for (auto item : data) {
		cout << item << " ";
	}
	cout << '\n';
}

int main() {
	vector<int> data = {1000, 45, -45, 121, 47, 45, 65, 121, -1, 103, 45, 34};
	cout << "Data to be sorted:" << '\n';
	print(data);
	cout << "Sorted data:" << '\n';
	data = shellSort(data);
	print(data);
	return 0;
}

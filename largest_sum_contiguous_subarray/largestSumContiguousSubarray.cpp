#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

int largestSumContiguousSubarray(const vector<int>& v) {
	int largest = 0;
	int current = 0;
	int n = v.size();
	for (int i = 0; i < n; ++i) {
		current += v[i];
		if (current > largest) {
			largest = current;
		}
		if (current < 0) {
			current = 0;
		}
	}
	return largest;
}

int main() {
	vector<int> v;
	cout << "Array:";
	for (int i = 0; i < 10; ++i) {
		v.push_back(rand() % 11 - 5);
		cout << " " << v[i];
	}
	cout << endl;
	cout << "Largest sum: " << largestSumContiguousSubarray(v) << endl;
}

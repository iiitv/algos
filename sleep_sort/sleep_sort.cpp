#include <iostream>
#include <thread>
#include <vector>
#include <chrono>

using namespace std;
/*
 * Function implementing sleep sort
 * args:
 * 		ar      : Initial array containing elements (unsorted)
 * 		ans     : sorted array elements vector
 * 		threads : vector containing threads for each array element
 */
void sleep_sort(int ar[], vector<int> &ans) {
	vector<thread> threads;
	for (int i = 0; i < 4; ++i) {
		threads.emplace_back([i, &ar, &ans]() {
				this_thread::sleep_for(chrono::seconds(ar[i]));
				ans.push_back(ar[i]);
				});
	}
	for (auto& th : threads) {
		th.join();
	}
}

// Driver function
int main() {
	int ar[] = {8, 4, 9, 1};
	vector<int> sorted_number;
	sleep_sort(ar, sorted_number);
	for (auto& item : sorted_number) {
		cout << item << endl;
	}
	return 0;
}

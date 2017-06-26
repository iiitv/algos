#include <iostream>
#include <thread>
#include <vector>
#include <chrono>

using namespace std;
/*
 * Function implementing sleep sort
 * args:
 *		ar		: Initial array containing elements (unsorted)
 *		ans		: sorted array elements vector
 *		threads : vector containing threads for each array element
 * Time Complexity : O(max(input))
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

/*
 * Driver function
 * For compilation of the code use -pthread
 * compilation looks like : g++ -std=c++11 sleep_sort.cpp -o sleep_sort -pthread
 */
int main() {
	int ar[] = {8, 4, 9, 1};
	vector<int> sorted;
	sleep_sort(ar, sorted);
	for (auto& item : sorted) {
		cout << item << endl;
	}
	return 0;
}

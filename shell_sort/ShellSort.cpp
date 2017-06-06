#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

// Worst case time complexity = O(n^2)
// Best case complexity = O(nlog(n))

vector<int> shellSort(vector<int> data) {
    for (int i = static_cast<int>(data.size() / 2); i > 0; i /= 2) {
        for (int j = i; j < data.size(); j++) {
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

int main() {
    vector<int> data = {1000, 45, -45, 121, 47, 45, 65, 121, -1, 103, 45, 34};
    cout << "Data to be sorted:" << '\n';
    for (auto item : data) {
        cout << item << " ";
    }
    cout << '\n' << "Sorted data:" << '\n';
    data = shellSort(data);
    for (auto item : data) {
        cout << item << " ";
    }
    cout << '\n';
    return 0;
}

#include <stdio.h>

// Time Complexity : O(log (power))
long long modularExponential(long long base, long power, long long mod) {
	long long answer = 1;
	base = base % mod;
	while (power) {
		if (power & 1) {
			answer = (answer * base) % mod;
		}
		power = power >> 1;
		base = (base * base) % mod;
	}
	return answer;
}

int main() {
	long long base = 2;
	long power = 10;
	long long mod = 100000;
	printf("%lld\n", modularExponential(base, power, mod));
	return 0;
}

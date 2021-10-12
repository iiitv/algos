// C program to find the nth fibonacci number.
// @author Manas Gupta (@heisenberg-2505)
#include <stdio.h>
typedef long long LL;

// Function to calculate the nth fibonacci number.
LL fibonacci (LL n) {
  if (n == 1 || n == 2) {
    return (n - 1);
  } else {
    // Variable to store the second last fibonacci number wrt current fibonacci number.
    LL secondLastFib = 0;
    // Variable to store the last fibonacci number wrt current fibonacci number.
    LL lastFib = 1;
    // Variable to store the current fibonacci number.
    LL currentFib = 0;
    for (LL i = 2; i < n; i++) {
      currentFib = secondLastFib + lastFib;
      secondLastFib = lastFib;
      lastFib = currentFib;
    }
    return currentFib;
  }
}

int main () {
  // Change here to change the value of n.
  LL n = 10;
  if (n <= 0) {
    printf ("The value of n should be a positive integer.\n");
    return 1;
  }
  printf ("The %lldth fibonacci number is %lld \n", n, fibonacci (n));
  return 0;
}

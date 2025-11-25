#include <stdio.h>
int multiply(int a, int b) {
    return a * b;
}
int main() {
   int num1, num2, result;
   result = multiply(5, 10);
   printf("The multiply of 5 and 10 is: %d\n", result);
    return 0;
}
#include <stdio.h>
#include <stdlib.h>

int main() {
    int a, b;
    int olis[8]; // Array to hold results (from 3 to 10)
    
    // Input values
    scanf("%d", &a);
    scanf("%d", &b);

    // Calculate results
    for (int c = 3; c <= 10; c++) {
        olis[c - 3] = (c - a) + (b - c);
    }

    // Sort the array (simple bubble sort for demonstration)
    for (int i = 0; i < 7; i++) {
        for (int j = 0; j < 7 - i; j++) {
            if (olis[j] > olis[j + 1]) {
                int temp = olis[j];
                olis[j] = olis[j + 1];
                olis[j + 1] = temp;
            }
        }
    }

    // Print the smallest value
    printf("%d\n", olis[0]);

    return 0;
}
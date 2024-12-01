#include <stdio.h>
#include <stdlib.h>


int main() {
    FILE *input;
    input = fopen("input", "r");

    unsigned int num, count;
    unsigned int sol2 = 0;

    // wc -l input
    unsigned int input_arr_1[1000], input_arr_2[1000];


    for (size_t i=0; i<1000; ++i) {
        fscanf(input, "%u   %u", &input_arr_1[i], &input_arr_2[i]);
    }

    for (size_t i=0; i<1000; ++i) {
        count = 0;
        num = input_arr_1[i];
        for (size_t j=0; j<1000; ++j) {
            if (num == input_arr_2[j]) count++;
        }
        sol2 += num * count;
    }

    printf("Advent of Code 2024 (day 1)\n");
    printf("Solution for part 2: %u\n", sol2);
}

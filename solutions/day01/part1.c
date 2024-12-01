#include <stdio.h>
#include <stdlib.h>


int cmp(const void *a, const void *b) {
    unsigned int arg1 = *(const unsigned int*) a;
    unsigned int arg2 = *(const unsigned int*) b;

    if (arg1 < arg2) return -1;
    if (arg1 > arg2) return 1;
    return 0;
}

int main() {
    FILE *input;
    input = fopen("input", "r");

    unsigned int sol1 = 0;

    // wc -l input
    unsigned int input_arr_1[1000], input_arr_2[1000];


    for (size_t i=0; i<1000; ++i) {
        fscanf(input, "%u   %u", &input_arr_1[i], &input_arr_2[i]);
    }

    qsort(input_arr_1, 1000, sizeof(unsigned int), cmp);
    qsort(input_arr_2, 1000, sizeof(unsigned int), cmp);

    for (size_t i=0; i<1000; ++i) {
        int diff = input_arr_1[i] - input_arr_2[i];
        sol1 += abs(diff);
    }

    printf("Advent of Code 2024 (day 1)\n");
    printf("Solution for part 1: %u\n", sol1);
    return 0;
}

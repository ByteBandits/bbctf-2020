
#include <stdio.h>
#include <stdlib.h>

char *alpha = "XnlpZrfctgAoQkuRKvqDTSjsPwJELO";
void auth() {
    int password[40] = {
        15,
        4,
        23,
        11,
        8,
        13,
        21,
        17,
        1,
        20,
        5,
        7,
        6,
        14,
        16,
        10,
        25,
        2,
        22,
        24,
        0,
        3,
        19,
        9,
        18,
        12,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    };
    char input[41];
    int len = 26;
    fgets(input, len+1, stdin);
    for (int i=0; i<len; i++) {
        if (input[i] != alpha[password[i]]) {
            puts("Wrong pass");
            exit(1);
        }
    }
    printf("good job");
}

int main() {
    auth();
}

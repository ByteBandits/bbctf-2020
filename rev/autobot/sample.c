#include <stdio.h>
#include <stdlib.h>

char *alpha = "abcdefghijklmnopqrstuvwxyz";
void auth() {
    int password[40] = {
        00,
        01,
        01,
        04,
        01,
        01,
        01,
        02,
        01,
        02,
        03,
        01,
        02,
        01,
        05,
        02,
        02,
        02,
        01,
        01,
        02,
        07,
        04,
        03,
        03,
        04,
        12,
        11,
        11,
        06,
        06,
        11,
        16,
        05,
        01,
        01,
        02,
        05,
        06,
        02,
    };
    char input[40];
    int len = 20;
    fgets(input, len+1, stdin);
    for (int i=0; i<len; i++) {
        /*printf("%c", alpha[password[i]]);*/
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

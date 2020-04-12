#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

char other_buf[0x100];

int get_int() {
    char buf[0x10];
    fgets(buf, 10, stdin);
    return atoi(buf);
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);

    int c;
    char buf[0x100];
    printf("Choose your name\n");
    printf("1. Lelouch 2. Saitama 3. Eren\n");
    printf("Choice: ");
    c = get_int();

    if (c == 2) {
        puts("Good job. I'll give you a gift.");
        /*fgets(buf, 0x100, stdin);*/
        int n = read(0, buf, 0x100);
        snprintf(other_buf, 0x100, buf);
        system("echo 'saitama, the real hero'");
    }
}

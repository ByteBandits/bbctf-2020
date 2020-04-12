#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    char c[2];
    uint64_t ptr, val;
    printf("puts: %p\n", puts);
    printf("stack: %p\n", &val);
    while (1) {
        puts("===Menu===");
        puts("(w)rite");
        puts("(q)uit");
        fgets(c, 2, stdin);
        switch (c[0]) {
            case 'w':
                printf("ptr: ");
                scanf("%lu", &ptr);
                printf("val: ");
                scanf("%lu", &val);
                *(uint64_t *)ptr = val;
                break;
            case 'q':
                exit(0);
                break;
            default:
                break;
        }
    }
}


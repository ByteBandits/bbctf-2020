#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

static int score = 0;

u_int64_t get_number(char *buf) {
    fgets(buf, sizeof(buf), stdin);
    return strtoul(buf, NULL, 10);
}

int main() {
    char buf[0x20];
    if (score == 0) {
        setvbuf(stdout, NULL, _IONBF, 0);
        setvbuf(stdin, NULL, _IONBF, 0);
    } else if (score == 1) {
        printf("puts: %p\n", puts);
    }

    u_int64_t d, idx;
    printf("size: ");
    /*scanf("%d", &d);*/
    d = get_number(buf);
    char *t = malloc(d);
    printf("idx: ");
    /*scanf("%d", &idx);*/
    idx = get_number(buf);
    t[idx] = '\x01';

    u_int64_t where;
    int how_much;
    printf("where: ");
    /*scanf("%ld", &where);*/
    where = get_number(buf);
    /*printf("how much: ");*/
    /*scanf("%ld", &where);*/
    read(0, (void *)where, 8);
    /*fgets((void *)where, 8, stdin);*/
    score = 1;
}

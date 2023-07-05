
#include <stdio.h>

int main (int argc, char *argv[]) {
    int height = atoi(argv[1]);

    for (int i = 0; i < height; i++) {
        for (int k = 0; k < height - i; k++) {
            printf(" ");
        }
        for (int j = 0; j <= i; j++) {
            printf("#");
        }
        printf(" ");
        for (int j = 0; j <= i; j++) {
            printf("#");
        }
        printf("\n");
    }
}
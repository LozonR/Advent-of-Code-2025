#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define STARTING_POINT 50
#define LOWER_BOUND 0
#define UPPER_BOUND 99

int main(int argc, char *argv[]) {
  int location = STARTING_POINT;
  int count = 0;

  int dir;
  int amount;
  char buf[10];
  int c;

  FILE* input = fopen(argv[1], "r");

  while (fgets(buf, 10, input)) {
    printf("%s\n\n", buf);
    
    char amountBuf[10];
    dir = (buf[0] == 'R') ? 1 : -1;

    strcpy(amountBuf, buf + 1);
    amount = atoi(amountBuf);

    location = (location + dir*amount) + LOWER_BOUND % (UPPER_BOUND - LOWER_BOUND + 1);

    printf("Dir: %d\nAmount: %d\nLocation: %d\n", dir, amount, location);
    
    if ((location % 100) == 0) count += 1;

  }

  fclose(input);

  printf("Solution: %d\n", count);
}

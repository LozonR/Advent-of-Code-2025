#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define STARTING_POINT 50

int main(int argc, char *argv[]) {
  int prevLocation;
  int location = STARTING_POINT;
  int count = 0;
  int prevCount;

  int dir;
  int amount;
  char buf[10];
  int c;

  FILE *input = fopen(argv[1], "r");

  while (fgets(buf, 10, input)) {
    printf("%s\n\n", buf);

    char amountBuf[10];
    dir = (buf[0] == 'R') ? 1 : -1;

    strcpy(amountBuf, buf + 1);
    amount = atoi(amountBuf);

    prevCount = count;

    if (location != 0) {        
      if (dir == -1) {
        if (location + dir*(amount % 100) <= 0) count += 1; // if barely crosses 0
        printf("%d\n", location + dir*(amount % 100));
      } else {
        if (location + dir*(amount % 100) >= 100) count += 1; // if barely crosses 0
        printf("%d\n", location + dir*(amount % 100));
      }
    }

    if (amount >= 100) {
      count += amount / 100; // multiples of 100
    }

    prevLocation = location;

    location = (location + dir * amount) % 100;
    if (location < 0) location = 100 + location;

    printf("Dir: %d\nAmount: %d\nLocation: %d\n", dir, amount, location);
    printf("Added: %d\nCount: %d\nPrev: %d\n\n", count - prevCount, count, prevCount);


  }

  fclose(input);

  printf("Solution: %d\n", count);
}

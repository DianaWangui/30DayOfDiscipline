#include <stdio.h>
#include <stdlib.h>
int main(void)
{
  int number;
  char *data;
  FILE *ptr;
  ptr = fopen("writing.txt", "r");
  if (ptr == NULL)
  {
    printf("Error opening file!\n");
    exit(EXIT_FAILURE);
  }
  data = (char *)malloc(20);
  if (data == NULL)
  {
    perror("Failed to allocate memeory\n");
    exit(EXIT_FAILURE);
  }
  if (fgets(data, 100, ptr) == NULL)
  {
    perror("Failed to read data\n");
  }
  printf("DATA READ: %s", data);
  fclose(ptr);
  return (0);
}
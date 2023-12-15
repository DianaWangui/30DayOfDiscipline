#include <stdio.h>
#include <stdlib.h>
/**
 * main- a main function that reads information
 * from a file and append new information
 */
int main(void)
{
  char *data;
  FILE *ptr;

  ptr = fopen("writing.txt", "r");
  if (ptr == NULL)
  {
    printf("Error opening file!\n");
    exit(EXIT_FAILURE);
  }
  /* Allocating memory dynamically for the buffer to store the data read*/
  data = (char *)malloc(20);
  if (data == NULL)
  {
    perror("Failed to allocate memeory\n");
    exit(EXIT_FAILURE);
  }
  /* Reading all characters using fgets() upto to the size allocated, if null print error*/
  if (fgets(data, 20, ptr) == NULL)
  {
    perror("Failed to read data\n");
    exit(EXIT_FAILURE);
  }
  /* Printing the data read to the stdout after success reading using fgets()*/
  printf("DATA READ: %s", data);
  free(data);
  fclose(ptr);
  return (0);
}
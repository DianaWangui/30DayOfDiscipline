#include <stdio.h>
#include <stdlib.h>
int main(void)
{
  char *data;
  FILE *ptr;
  size_t size;
  ptr = fopen("writing.txt", "r");
  if (ptr == NULL)
  {
    printf("Error opening file!\n");
    exit(EXIT_FAILURE);
  }
  /* Allocating memory dynamically for the buffer to store the data read*/
  data = (char *)malloc(20);
  if (data == NULL) /* checking condition where malloc fails and exit*/
  {
    perror("Failed to allocate memeory\n");
    exit(EXIT_FAILURE);
  }
  if (fgets(data, 20, ptr) == NULL) /* Reading all characters using fgets() upto to the size allocated*/
  {
    perror("Failed to read data\n");
  }
  printf("DATA READ: %s", data); /* Printing the data read to the stdout*/
  free(data);                    /* free the allocated memory after use*/
  fclose(ptr);                   /* close the file*/
  return (0);
}
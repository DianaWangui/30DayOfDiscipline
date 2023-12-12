#include <stdio.h>
#include <stdlib.h>
/**
 * main- a function that reads int values from a file
 * first opens the file using fopen() and checks if its opens
 * if not exit with an error message otherwise continues to read
 * the int value using fscanf() then prints out the value
 * using printf to the stdout
 */
int main(void)
{
  int number;
  FILE *ptr;

  ptr = fopen("writing.txt", "r"); /* Opening the file in read mode to read integer*/
  if (ptr == NULL)                 /* Handle when failed to open file and exit with error msg*/
  {
    printf("Error opening file!\n");
    exit(EXIT_FAILURE);
  }
  fscanf(ptr, "%d", &number);      /* If open is success read data using fscanf() and store read data to number*/
  printf("DATA READ: %d", number); /* print the read data to stdout*/

  fclose(ptr);
  return (0);
}
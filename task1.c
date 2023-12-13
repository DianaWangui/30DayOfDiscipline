#include <stdio.h>
#include <stdlib.h>
/**
 * main- a main function for reading data from a file
 * @fptr:  pointer to the file being read
 * @read: stored the number of char read
 * @str: pointer to the space we are storing data being read
 * @len: used to check the lenght of char read
 * Return: 0 on success
 */
int main(void)
{
  FILE *fptr;
  char *str = NULL;
  size_t read;
  size_t len = 0;
  size_t read_char = 0;

  /* using a file pointer to open our file for reading operation */
  fptr = fopen("writing.txt", "r");

  if (fptr == NULL)
  {
    perror("Error! opening file writing.txt\n");
    exit(1);
  }

  /* using the getline function to allocate memory for the file being read*/
  while (read = getline(&str, &len, fptr) != -1)
  {
    printf("%s", str);
    /* checking number of characters read */
    read_char += read;
  }

  /* %zu is the specifier to print charater read using getline*/
  printf("\n%zu", read_char);

  /* using ferror() to check whether an error has occurred on when reading data in the file*/
  if (ferror(fptr))
  {
    perror("Error! Reading file writing.txt\n");
  }

  /* free the memeory allocated by getline*/
  free(str);
  /* closing the file*/
  fclose(fptr);
  return (0);
}
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <sys/types.h>

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
  FILE *fptr, *temp;
  char *str = NULL;
  size_t read;
  size_t len = 0;
  size_t read_char = 0;
  ssize_t i;

  /* using a file pointer to open our file for reading operation */
  fptr = fopen("writing.txt", "r");

  if (fptr == NULL)
  {
    perror("Error! opening file writing.txt\n");
    exit(1);
  }

  temp = fopen("reading.txt", "w");
  if (temp == NULL)
  {
    perror("Could not open file reading.txt.\n");
  }
  /* using the getline function to allocate memory for the file being read*/
  while (read = getline(&str, &len, fptr) != -1)
  {
    for (i = 0; i < read; i++)
    {
      /* Manipulating the data in the file char by char to upper case using toupper()*/
      str[i] = toupper(str[i]);
    }

    /*Write the manipulated line back to the file*/
    fwrite(str, 1, read, temp);
  }

  /* using ferror() to check whether an error has occurred on when reading data in the file*/
  if (ferror(fptr))
  {
    perror("Error! Reading file writing.txt\n");
  }
  /* closing the file*/
  fclose(fptr);
  fclose(temp);

  /* Removing the original file */
  remove("writing.txt");

  /* rename the temp file back to original file*/
  rename("reading.txt", "writing.txt");

  /* free the memory allocated by getline*/
  free(str);
  return (0);
}
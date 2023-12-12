#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  FILE *fptr;
  char ch[20];
  fptr = fopen("writing.txt", "w"); /* open file in writing mode if no file, create new file*/
  if (fptr == NULL)                 /* check if the file is opened successfully or not */
  {
    perror("file not found");
    exit(1);
  }
  printf("Enter your text here: ");
  if (fgets(ch, sizeof(ch), stdin) != NULL) /* reading the user input from stdin*/
  {
    fputs(ch, fptr); /*writing into the file the user input*/
  }
  else
  {
    perror("Error reading input");
    exit(2);
  }
  /* This will be printed when the program is successfull*/
  printf("\nYour entered text has been written to testfile.txt\n");
  fclose(fptr);
  return (0);
}
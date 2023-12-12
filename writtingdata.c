#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  FILE *fptr;
  char ch[10];
  fptr = fopen("writing.txt", "w"); /* open file in writing mode if no file, create new file*/
  if (fptr == NULL)                 /* check if the file is opened successfully or not */
  {
    perror("file not found");
    exit(1);
  }
  printf("Enter your text here: ");
  if (fgets(ch, sizeof(ch), stdin) != NULL)
  {
    fprintf(fptr, "%s", ch);
  }
  else
  {
    perror("Error reading input");
    exit(2);
  }
  // fputs(ch, fptr);   /* write into the file what user has entered */
  printf("\nYour entered text has been written to testfile.txt\n");
  fclose(fptr);
  return (0);
}
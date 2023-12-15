#include <stdio.h>
#include <stdlib.h>
/**
 * main - a function that creates/opens a file using FILE *fptr.
 * if the file is not availabe its created in writing mode
 * if file fails to open exit with an error of file not found
 * using fgets() to read input from user, you can also read
 * from another file by changing stdin to the file pointer
 * that you want to read from.
 * using fputs() to write the input from user/file to the other file
 * if its not possible to read the input print an error message
 * also implemented the input of int values
 */
int main(void)
{
  FILE *fptr, *appendptr; /* A pointer to the file we are writing to*/
  char ch[20];            /* Character array we are reading from user and writing to the file*/
  int number;             /* integer we are reading from user and writing to the file */

  fptr = fopen("writing.txt", "w"); /* open file in writing mode if no file, create new file*/
  if (fptr == NULL)                 /* check if the file is opened successfully, if not print error msg and exit */
  {
    perror("file not found\n");
    exit(EXIT_FAILURE);
  }
  printf("Enter your text here: ");         /* For now we are taking input from user/you can take input from another file*/
  if (fgets(ch, sizeof(ch), stdin) != NULL) /* reading the user input from stdin/ you can also read from another file*/
  {
    fputs(ch, fptr); /*writing into the file the user input*/
  }
  else
  {
    perror("Error reading input\n"); /* print error if cant read from user input/file stream*/
    exit(EXIT_FAILURE);
  }
  printf("\n");
  fclose(fptr);

  /* Opening file for appending some int value and a string*/
  appendptr = fopen("writing.txt", "a");
  if (appendptr == NULL)
  {
    perror("Failed to open the file for appending.\n");
    xit(EXIT_FAILURE);
  }
  printf("Enter a line of text: ");
  if (fgets(ch, sizeof(ch), stdin) == NULL)
  {
    perror("NULL");
    exit(EXIT_FAILURE);
  }
  printf("Number: ");
  if (scanf("%d", &number) != 1)
  {
    perror("error: invalid number format\n");
    exit(EXIT_FAILURE);
  }
  /* Write the entered text followed by a newline character to the file.*/
  fprintf(appendptr, "%s %d\n", ch, number);

  /* printing out the appended text to the stdout*/
  printf("%s %d\n", ch, number);
  /* Close the file. */
  fclose(appendptr);
  return (0);
}

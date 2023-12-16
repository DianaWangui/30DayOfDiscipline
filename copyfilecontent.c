#include <stdio.h>
#include <stdlib.h>
int main(void)
{
  FILE *writeptr, *copyptr;
  int id;
  char name[20];
  int salary;
  char store_read_data[200];

  /* wrinting data to the file before copying it*/
  writeptr = fopen("employee_data.txt", "w+");
  if (writeptr == NULL)
  {
    perror("Error opening file\n");
    exit(EXIT_FAILURE);
  }
  printf("Enter Employee name: ");
  scanf("%[^\n]%*c", &name);
  printf("Enter Employee ID: ");
  scanf("%d", &id);
  printf("Enter Employee salary: ");
  scanf("%d", &salary);
  /* writing to the file using fprintf */
  fprintf(writeptr, "Name = %s\nID =  %d\nSalary = %d\n", name, id, salary);

  /* Lets now copy the data to a new file that will be created*/
  copyptr = fopen("copy_of_employee_data.txt", "w");
  if (copyptr == NULL)
  {
    perror("Error creating copy of file\n");
    exit(EXIT_FAILURE);
  }
  rewind(writeptr); // Go back to start of read pointer
  while ((fgets(store_read_data, sizeof(store_read_data), writeptr)) != NULL)
  {
    fputs(store_read_data, copyptr);
  }
  fclose(copyptr);
  fclose(writeptr);
}
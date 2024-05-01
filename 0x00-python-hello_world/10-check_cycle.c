#include "lists.h"

/**
* check_cycle - checl if passed linked list has a cycle in it
* @list: head of the list
* Return: 1 if yes, 0 if no
*/
int check_cycle(listint_t *list)
{
	listint_t *current;
	
	current = list;
	while (current)
	{
		if (current->next == list)
			return (1);
		current = current->next;
	}
	return(0);
}

#include "lists.h"

/**
 * check_cycle - check if the passed singly linked list is cyclic or not
 * @list: passed list
 * Return: 1 if it is cyclic, 0 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *current = NULL;

	current = list->next;
	while (1)
	{
		if (current->next == list)
			return (1);
		else if (current->next == NULL)
			return (0);
		current = current->next;
	}	
}

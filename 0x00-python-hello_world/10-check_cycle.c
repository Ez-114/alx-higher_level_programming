#include "lists.h"

/**
 * check_cycle - check if the passed singly linked list is cyclic or not
 * @list: passed list
 * Return: 1 if it is cyclic, 0 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *current = NULL, *fast_current = NULL;

	if (list == NULL)
		return (0);

	current = list;
	fast_current = list;
	while (fast_current != NULL && fast_current->next != NULL)
	{
		current = current->next;
		fast_current = fast_current->next->next;
		if (fast_current == current)
			return (1);
	}	
	return (0);
}

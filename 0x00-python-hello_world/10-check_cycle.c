#include "lists.h"

/**
* check_cycle - checl if passed linked list has a cycle in it
* @list: head of the list
* Return: 1 if yes, 0 if no
*/
int check_cycle(listint_t *list)
{
	listint_t *low, *high;
	
	low = list;
	high = list
	while (high && high->next)
	{
		low = low->next;
		high = high->next->next;
		if (high == low)
			return (1);
	}
	return(0);
}

#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert a node in a sorted ll
 * @head: head of the ll
 * @number: value inside the node to be inserted
 *
 * Return: address of the new node, NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL;
	listint_t *tail_node = NULL;
	listint_t *front_node = NULL;

	if (head == NULL)
	{
		return (NULL);
	}

	/* allocate memory for the new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	/* insert 'number' in the new node */
	new_node->n = number;
	new_node->next = NULL;

	/* what if the list is already empty? */
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	tail_node = (*head);
	front_node = (*head)->next;

	/* search for its sutable place in the list */
	if (tail_node->n > number)
	{
		tail_node->next = new_node;
		new_node->next = front_node;
		return (new_node);
	}
	while (front_node)
	{
		if (tail_node->n < number && front_node->n > number)
		{
			tail_node->next = new_node;
			new_node->next = front_node;
			return (new_node);
		}
		tail_node = front_node;
		front_node = front_node->next;
	}
	free(new_node);
	return (NULL);
}

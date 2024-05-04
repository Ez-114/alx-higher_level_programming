#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a new number in a sorted linked list
 * @head: head pointer pointing to the passed linked list
 * @number: integer value to insert in the sorted ll
 *
 * Return: Address of the new node, NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *curr, *prev;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
        return NULL;

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return new_node;
	}

	prev = NULL;
	curr = *head;
    while (curr != NULL && curr->n < number)
	{
		prev = curr;
		curr = curr->next;
	}

	new_node->next = curr;
    if (prev != NULL)
		prev->next = new_node;

	return new_node;
}

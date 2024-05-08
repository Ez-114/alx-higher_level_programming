#include "lists.h"

/**
 * is_palindrome - recursivly palindrome check
 * @head: head list
 * Return: 0 if not 1 if yes
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (palind(head, *head));
}

/**
 * palind - helper function
 * @head: head list
 * @end: end list
 * Return: 1 if yes , 0 if no
 */
int palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

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
    listint_t *curr = NULL, *new_node = NULL, *prev = NULL;

    new_node = malloc(sizeof(listint_t));
    if (!new_node)
        return (NULL);

    new_node->n = number;
    new_node->next = NULL;

    if (*head == NULL)
    {
        *head = new_node;
        return (new_node);
    }

    curr = (*head)->next;
    prev = *head;
    while (curr->next != NULL)
    {
        if (curr->n > number)
        {
            prev->next = new_node;
            new_node->next = curr;
            break;
        }
        prev = curr;
        curr = curr->next;
    }
    return (new_node);
}

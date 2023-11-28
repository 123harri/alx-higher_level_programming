#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Function to check if a singly linked list has a cycle
 * @list: Pointer to the head of the linked list
 * Return: 1 if there is a cycle, 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list;

	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
		{
			return (1);
		}
	}
	return (0);
}

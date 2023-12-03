#include "lists.h"

/**
 * is_palindrome - Check if a singly linked list is a palindrome
 * @head: Pointer to the head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL, *tmp;

	if (!head || !*head)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;

		tmp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = tmp;
	}

	if (fast)
		slow = slow->next;

	while (slow)
	{
		if (slow->n != prev->n)
			return (0);
		slow = slow->next;
		prev = prev->next;
	}

	return (1);
}

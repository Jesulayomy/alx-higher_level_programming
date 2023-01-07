#include "lists.h"

/**
 * is_palindrome - checks a listfor palindromes
 * @head: the list
 * Return: 0 if not and 1 if
 */
int is_palindrome(listint_t **head)
{
	listint_t *reversed;
	listint_t *temp = *head;

	while (temp)
	{
		reversed->n = temp->n;
	}

	if (head == NULL)
	{
		return (1);
	}

	reverse_listint(&reversed);

	while (temp)
	{
		printf("comparing %d and %d\n", temp->n, reversed->n);

		if (temp->n != reversed->n)
		{
			return (0);
		}

		temp = temp->next;
		reversed = reversed->next;
	}

	return (1);
}

	/* reverse_listint(&reversed); */
/**
 * reverse_listint - reverses a list int
 * @head: the list
 *
 * Return: a pointer to the first node of the reveresd list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *before = NULL, *next;

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = before;
		before = *head;

		*head = next;
	}

	*head = before;

	return (*head);
}

#include "lists.h"

/**
 * check_cycle - check if a list has a cycle
 * @list: list to check
 *
 * Return:	0 if no cycle
 *					1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *n, *nn;

	if (!list || !list->next)
		return (0);

	n = list;
	nn = list;

	while (nn->next && nn->next->next)
	{
		n = n->next;
		nn = nn->next->next;

		if (n == nn)
			return (1);
	}

	return (0);
}

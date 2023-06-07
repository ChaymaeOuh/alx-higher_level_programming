#include "lists.h"

/**
 * check_cycle - check if a linked list contain a cycle on it
 * @list: the linked list
 *
 * Return: 1(it has a cycle) 0 doesn't
 */
int check_cycle(listint_t *list)
{
listint_t *s = list;
listint_t *f = list;

if (!list)
return (0);

while (s && f && f->next)
{
s = s->next;
f = f->next;
if (s == f)
return (1);
}
return (0);
}


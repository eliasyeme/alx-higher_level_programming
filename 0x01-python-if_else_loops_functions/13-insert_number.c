#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the list
 * @number: number to insert
 *
 * Return:	address on the new node on success
 * 					NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number);

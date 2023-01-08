#include <stdio.h>

/**
 * print_python_list_info - prints some basic info on lists
 * @p: a python object
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	long int i, list_size;
	PyListObject *list;
	PyObject *item;

	list_size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", list_size);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < list_size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

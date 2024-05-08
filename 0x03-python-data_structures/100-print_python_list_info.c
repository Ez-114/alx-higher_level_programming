#define Py_LIMITED_API 0x03040000

#include <Python.h>
#include <stddef.h>
#include <stdio.h>

/**
 * print_python_list_info - prints basic info about python lists
 * @p: A PyObject list
 */
void print_python_list_info(PyObject *p)
{
	int size = Py_SIZE(p);
	int alloc =((PyListObject *)p)->allocated;
	int i;
	PyObject *ob;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		ob = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}

	return (0);
}

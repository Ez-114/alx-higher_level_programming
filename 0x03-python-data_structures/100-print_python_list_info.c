#define PY_LIMITED_API 0x03040000

#include <Python.h>
#include <stddef.h>
#include <stdio.h>

/**
 * print_python_list_info - print some info about py lists
 * @p: py object
 */
void print_python_list_info(PyObject *p)
{
	size_t size = Py_SIZE(p), i;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}

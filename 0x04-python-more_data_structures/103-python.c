#define PY_LIMITED_API 0x03040000

#include <Python.h>
#include <stddef.h>
#include <stdio.h>
#include <string.h>

/**
 * print_python_bytes - prints some information about python bytes object
 * @p: Python Object
 */
void print_python_bytes(PyObject *p)
{
	ssize_t i, firstXbytes;
	size_t byte_size;
	char *Object_str_content;


	if (strcmp((p->ob_type)->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	byte_size = PyBytes_Size(p);
	Object_str_content = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", byte_size);
	printf("  trying string: %s\n", Object_str_content);

	if (((PyVarObject *)p)->ob_size > 10)
		firstXbytes = 10;
	else
		firstXbytes = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", firstXbytes);
	for (i = 0; i < firstXbytes; i++)
	{
		printf("%02hhx", Object_str_content[i]);
		if (i == (firstXbytes - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_list - prints some information about python list object
 * @p: Python Object
 */
void print_python_list(PyObject *p)
{
	size_t i, size;
	const char *py_type;
	PyObject *curr_obj;

	if (!PyList_Check(p))
		return;

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		curr_obj = PyList_GET_ITEM(p, i);
		py_type = (curr_obj->ob_type)->tp_name;
		printf("Element %ld: %s\n", i, py_type);
		if (strcmp(py_type, "bytes") == 0)
			print_python_bytes(curr_obj);
	}
}

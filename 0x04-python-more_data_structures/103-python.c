#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information about a Python list
 * @p: Pointer to a Python object
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid Python List\n");
		return;
	}

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List: %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < PyList_Size(p); ++i)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to a Python object
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Invalid Python Bytes Object\n");
		return;
	}

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", PyBytes_Size(p));
	printf("  trying string: %s\n", PyBytes_AsString(p));

	printf("  first 10 bytes: ");
	for (Py_ssize_t i = 0; i < PyBytes_Size(p) && i < 10; ++i)
	{
		printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);
		if (i + 1 < PyBytes_Size(p) && i + 1 < 10)
			printf(" ");
	}
	printf("\n");
}

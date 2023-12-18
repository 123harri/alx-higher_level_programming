#include <Python.h>
#include <floatobject.h>
#include <bytesobject.h>
#include <listobject.h>

/**
 * print_python_list - prints information about Python lists
 * @p: PyObject representing a Python list
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid List Object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - prints information about Python bytes
 * @p: PyObject representing a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	char *str = PyBytes_AsString(p);
	int i;

	printf("[.] bytes object info\n");
	printf("size: %ld\n", size);
	printf("trying string: %s\n", str ? str : "(null)");

	printf("first 10 bytes: ")
		for (i = 0; i < 10 && i < size; i++)
		{
			printf("%02hhx", str[i]);
			if (i + 1 < 10 && i + 1 < size)
			{
				printf(" ");
			}
		}
	printf("\n");
}

/**
 * print_python_float - prints information about Python floats
 * @p: PyObject representing a Python float
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "Invalid Float Object\n");
		return;
	}

	printf("[.] float object info\n");
	printf("value: %f\n", ((PyFloatObject *)p)->ob_fval);
}

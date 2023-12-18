#include <Python.h>
#include <stdio.h>

/**
 * custom_print_python_float - provides information about the PyFloatObject
 * @p: the PyObject
 */
void custom_print_python_float(PyObject *p)
{
	double float_value = 0;
	char *str_representation = NULL;

	fflush(stdout);
	printf("[.] float object details\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	float_value = ((PyFloatObject *)p)->ob_fval;
	str_representation = PyOS_double_to_string(float_value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str_representation);
}

/**
 * custom_print_python_bytes - provides information about the PyBytesObject
 * @p: the PyObject
 */
void custom_print_python_bytes(PyObject *p)
{
	Py_ssize_t byte_size = 0, i = 0;
	char *byte_string = NULL;

	fflush(stdout);
	printf("[.] bytes object details\n");

	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
   
		return;
	}

	byte_size = PyBytes_Size(p);
	printf("  size: %zd\n", byte_size);
	byte_string = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", byte_string);
	printf("  first %zd bytes:", byte_size < 10 ? byte_size + 1 : 10);

	while (i < byte_size + 1 && i < 10)
	{
		printf(" %02hhx", byte_string[i]);
		i++;
	}

	printf("\n");
}

/**
 * custom_print_python_list - provides information about the PyListObject
 * @p: the PyObject
 */
void custom_print_python_list(PyObject *p)
{
	Py_ssize_t list_size = 0;
	PyObject *list_item;
	int index = 0;

	fflush(stdout);
	printf("[*] Custom Python list details\n");

	if (PyList_CheckExact(p))
	{
		list_size = PyList_GET_SIZE(p);
		printf("[*] Size of the Custom Python List = %zd\n", list_size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		while (index < list_size)
		{
			list_item = PyList_GET_ITEM(p, index);
			printf("Element %d: %s\n", index, list_item->ob_type->tp_name);

			if (PyBytes_Check(list_item))
				custom_print_python_bytes(list_item);
			else if (PyFloat_Check(list_item))
				custom_print_python_float(list_item);

			index++;
		}
	}
	else
	{
		printf("  [ERROR] Invalid List Object\n");
	}
}

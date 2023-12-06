#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Bytes Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
    char *byte_string;
    long int byte_size, index, limit;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    byte_size = PyBytes_Size(p);
    byte_string = ((PyBytesObject *)p)->ob_sval;

    printf("  size: %ld\n", byte_size);
    printf("  trying string: %s\n", byte_string);

    limit = (byte_size >= 10) ? 10 : byte_size + 1;

    printf("  first %ld bytes:", limit);

    for (index = 0; index < limit; index++)
        printf(" %02x", (unsigned char)byte_string[index]);

    printf("\n");
}

/**
 * print_python_list - Prints list information
 *
 * @p: Python List Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
    long int list_size, i;
    PyListObject *list_obj;
    PyObject *element;

    list_size = PyList_Size(p);
    list_obj = (PyListObject *)p;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", list_size);
    printf("[*] Allocated = %ld\n", list_obj->allocated);

    for (i = 0; i < list_size; i++)
    {
        element = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
        if (PyBytes_Check(element))
            print_python_bytes(element);
    }
}

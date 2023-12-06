#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p)
{
    long int byte_size;
    int i;
    char *byte_string = NULL;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    PyBytes_AsStringAndSize(p, &byte_string, &byte_size);

    printf("  size: %li\n", byte_size);
    printf("  trying string: %s\n", byte_string);

    if (byte_size < 10)
        printf("  first %li bytes:", byte_size + 1);
    else
        printf("  first 10 bytes:");

    for (i = 0; i <= byte_size && i < 10; i++)
        printf(" %02hhx", byte_string[i]);

    printf("\n");
}

void print_python_list(PyObject *p)
{
    long int list_size = PyList_Size(p);
    int i;
    PyListObject *python_list = (PyListObject *)p;
    const char *element_type;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %li\n", list_size);
    printf("[*] Allocated = %li\n", python_list->allocated);

    for (i = 0; i < list_size; i++)
    {
        element_type = (python_list->ob_item[i])->ob_type->tp_name;
        printf("Element %i: %s\n", i, element_type);

        if (!strcmp(element_type, "bytes"))
            print_python_bytes(python_list->ob_item[i]);
    }
}

import py_compile
import dis

py_compile.compile('hidden_4.py')

compiled_module = __import__('hidden_4')

module_names = dir(compiled_module)

for name in sorted(module_names):
    if not name.startswith('__'):
        print(name)

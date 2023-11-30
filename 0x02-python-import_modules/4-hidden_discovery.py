#!/usr/bin/python3

def print_sorted_names():
    import hidden_4

    for name in sorted(dir(hidden_4)):
        if name[:2] != '__':
            print("{}".format(name))

if __name__ == "__main__":
    print_sorted_names()

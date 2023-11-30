#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    def print_sorted_names():
        for name in sorted(dir(hidden_4)):
            if name[:2] != '__':
                print("{}".format(name))

    # Call the function when the script is executed directly
    print_sorted_names()

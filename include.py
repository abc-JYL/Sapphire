include_list = []
include_list.clear()
def include(file):
    with open(file, "r") as file:
        for i in file:
            include_list.append(i)
        return include_list

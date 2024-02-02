loop_list = []

def loop(times, code):
    loop_list.clear()
    for i in range(int(times)):
        loop_list.insert(0, code)
    return loop_list
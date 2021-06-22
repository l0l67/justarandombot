import psutil

def cpu():
    global total
    total = psutil.cpu_percent()
    return total


def bytes_to_GB(bytes):
    gb = bytes/(1024*1024*1024)
    gb = round(gb, 2)
    return gb

def ram():
    # Using the virtual_memory() function it will return a tuple
    virtual_memory = psutil.virtual_memory()

    global used
    used = bytes_to_GB(virtual_memory.used)
    return used

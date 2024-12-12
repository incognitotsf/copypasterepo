def read_data(path):
    f = open(path, "r")
    data = f.read()
    return data

def write_data(path, content):
    f = open(path, "w")
    f.write(content)
    f.close()
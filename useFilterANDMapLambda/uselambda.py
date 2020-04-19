import dis

x = (lambda x: x + 1)(2)

def add(x, y): return x + y
type(add)

dis.dis(add)


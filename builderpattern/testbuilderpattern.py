
"Failure"
class Row_Builder(object):
    def __init__(self):
        self.row = ['' for i in range(100)]

    def with_name(self, name):
        self.row[name] = name
        return self

    def with_address(self, address):
        self.row[address] = address
        return self

    def build(self):
        return self.row

if __name__ == '__main__':
    name = 'Ruman'
    address = 'lalitpur'
    row_name_address = Row_Builder.with_name(name).with_address(address).build()
    print(row_name_address)

class Dates:
    def __init__(self, file_entrance, file_result):
        self.file_entrance = file_entrance
        self.file_result = file_result

    def readers(self):
        with open(self.file_entrance, 'r') as ff:
            for v in ff:
                yield v[:-1]

    def writers(self, lines):
        with open(self.file_result, 'a') as ff:
            ff.writelines(str(lines) + '\n')

    def gen_lines(self, val):
        pass


l1 = Dates('data.csv', 'res.txt')
for i in l1.readers():
    a = i.split(' ')
    print(a)

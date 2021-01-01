class Dates:
    def __init__(self, file_entrance, file_result):
        self.file_entrance = file_entrance
        self.file_result = file_result

    def readers(self):
        with open(self.file_entrance, 'r') as ff:
            count = 0
            if 'фио' in ff.readline():
                pass
            while count < 10:
                count += 1
                yield ff.readline()[:-1]

    def writers(self, lines):
        with open(self.file_result, 'a') as ff:
            ff.writelines(str(lines) + '\n')

    def gen_lines(self, val):
        pass


l1 = Dates('data.csv', 'res.txt')
for i in l1.readers():
    print(i)

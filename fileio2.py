class Student ():
    def __init__(self, r, n, m1,m2,m3, m4):
        self.rollno=r
        self.name =n
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.total = self.m1+ self.m2 + self.m3 + self.m4

    def avg(self):
        return  (self.total)/4

def readFile(filename):
    with open(filename, mode="r+t") as infile:
        return infile.readlines()


def processLines(lines):
    students = []
    for line in lines:
        x = line.split(",")
        s = Student( x [0], x[1], int(x[2]) , int(x[3]) , int(x[4]) , int(x[5]) )
        students.append(s)
    return students


def writeToFile(filename, data):
    outfile = open(filename, "w")
    for x in data:
        str1 = x.rollno + "," + x.name + "," + str( x.total ) +  "," + str( x.avg() ) +"\n"
        outfile.write(str1)


def main():
    try:
        in_filename = "data.csv"
        out_filename = "student_mark2.csv"
        lines = readFile(in_filename)
        data = processLines(lines)

        print(data)
        data.sort(key=lambda x: x.total, reverse=True)
        writeToFile(out_filename, data)
        data.sort(key=lambda x: x.name)
        writeToFile("student_mark_name2.csv", data)
        data.sort(key=lambda x: x.rollno)
        writeToFile("student_mark_rollno2.csv", data)

    except FileNotFoundError:
        print("Invalid File name")


main()




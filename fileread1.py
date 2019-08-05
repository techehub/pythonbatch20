def readFile (filename):
    try :
        infile = open(filename, mode="r+t", )
        return  infile.readlines()
    finally:
        infile.close()


def readFile (filename):
    with open(filename, mode="r+t" ) as infile:
        return infile.readlines()


def processLines( lines):
    students= []
    for line in  lines:
        x= line.split(",")
        total = int ( x[2])+  int (x[3])+ int (x[4])+ int (x[5])
        students.append((x[0], x[1], total ))
    return students


def writeToFile(filename, data):
    outfile = open (filename, "w")
    for x in data:
        str1= x[0] + "," + x[1]+ "," + str (x[2])+ "\n"
        outfile.write (str1)

def main ():
    try :
        in_filename = "dta.csv"
        out_filename= "student_mark.csv"
        lines= readFile(in_filename)
        data= processLines(lines)

        print (data)
        data.sort(key= lambda  x : x[2], reverse=True)
        writeToFile(out_filename,data)
        data.sort(key= lambda  x : x[1])
        writeToFile("student_mark_name.csv",data)
        data.sort(key= lambda  x : x[0])
        writeToFile("student_mark_rollno.csv",data)

    except FileNotFoundError:
        print ("Invalid File name")
main()




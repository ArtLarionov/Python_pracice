inputf = "/Users/Artem/Desktop/dataset_3363_4.txt"
outputf = "/Users/Artem/Desktop/output.txt"
students = []
p1 = 0
p2 = 0
p3 = 0

with open(inputf, 'r') as file_r:
    for line in file_r:
        line = line.strip().split(';')
        students.append(line)

with open(outputf, 'w') as file_wr:
    for x in students:
        p1 += float(x[1])
        p2 += float(x[2])
        p3 += float(x[3])
        file_wr.write(str((float(x[1]) + float(x[2]) + float(x[3]))/3) + "\n")
    file_wr.write(str(p1/len(students)) + " " + str(p1/len(students)) + " " + str(p1/len(students)))

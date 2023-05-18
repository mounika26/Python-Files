if __name__ == '__main__':
    # n = int(input())
    student_marks = {'a':[10,20],'b':[30,40],'c':[10,10]}
    # for _ in range(n):
    #     name, *line = input().split()
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    query_name = input()
    sum = 0
    # for d in student_marks:
    #     if d==query_name:
    x = ((float(student_marks[query_name][0]) + float(student_marks[query_name][1]) + float(student_marks[query_name][2])) / 3)
    print('%.2f' % x)

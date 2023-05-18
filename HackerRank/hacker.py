if __name__ == '__main__':
    students=[]
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     students.append([name,score])
    students = [['Shadab', 8], ['Varun', 8.9], ['Sarvesh', 9.5], ['Harsh', 10]]
    # records1=sorted(students1, key=lambda x: x[1])
    # # students1.sort()
    # print(records1)

    # students = [['Harsh', 20], ['Beria', 20],['Varun', 19], ['Kakunami', 19], ['Vikas', 21]]
#     students=[['Harry', 37.21], ['Berry', 37.21],['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
#     if students[0][1]==students[1][1]:
#         second_largest=students[1][1]
#         # print(students[0][0])
#     else:
#         students=sorted(students,key=lambda x:x[1])
#         print(students)
#         second_largest=students[1][1]
#
#
# for i in range(len(students)):
#     if students[i][1]== second_largest:
#             records3 = sorted(students, key=lambda x: x[0])
#             print(records3)
#             for i in range(len(records3)):
#                 if records3[i][1]==second_largest:
#                     print(records3[i][0])
#             else:
#                 break
#     elif students[i][1] != second_largest:
#             print(students[1][0])
#             break



#2nd approach

if __name__ == '__main__':
    # students = []
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     students.append([name, score])
    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    sort_scores = sorted(set([i[1] for i in students]))
    print(sort_scores)
    slg_name = sorted([i[0] for i in students if i[1] == sort_scores[1]])

    for name in slg_name:
        print(name)
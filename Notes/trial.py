def list_of_students(nested_score):
    score=[]
    for student in nested_score:
        score.append(student[1])

    sorted_list = sorted(set(score))

    print(sorted_list)

    second_lowest = sorted_list[1]
    
    print(second_lowest)
    second_low_students =[]
    for non_studious in nested_score:
        if non_studious[1] == second_lowest:
            second_low_students.append(non_studious[0])

    # newest_list = sorted(second_high)
    print(second_low_students)        


if __name__ == '__main__':
    nested_score = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        nested_score.append([name, score])
              
list_of_students(nested_score)  
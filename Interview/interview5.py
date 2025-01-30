def runner_up(array_students):
    array_students = list(array_students)
    array_students.sort(reverse=True)

    for score in range(len(array_students)):
        if array_students[score] != array_students[score+1]:
            runner_up = array_students[score+1]
            break
        else:
            continue
    print(runner_up)

if __name__ == '__main__':
    n = int(input("Enter the number of students:"))
    arr = map(int, input("Enter the scores separated by space:").split())
    runner_up(arr)    

# modified code

def runner_up(array_students):
    # Convert the input to a list and sort it in descending order
    array_students = list(array_students)
    array_students.sort(reverse=True)
    
    runner_up_score = None  # Renamed for clarity

    # Loop to find the runner-up (second highest score)
    for i in range(len(array_students) - 1):  # Avoid out-of-range error
        if array_students[i] != array_students[i + 1]:
            runner_up_score = array_students[i + 1]
            break

    # Print the runner-up score if found, otherwise print a message
    if runner_up_score is not None:
        print(runner_up_score)
    else:
        print("No distinct runner-up score found.")

if __name__ == '__main__':
    n = int(input("Enter the number of students: "))
    arr = map(int, input("Enter the scores separated by space: ").split())

    arr = list(arr)  # Convert to a list to ensure we can iterate multiple times

    # Check if the number of scores matches `n`
    if len(arr) != n:
        print(f"Error: Expected {n} scores, but got {len(arr)}.")
    else:
        runner_up(arr)

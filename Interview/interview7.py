names_scores = [['amol', 10], ['julie', 20], ['rahul', 10], ['amit', 50], ['arjun', 40], ['ketan', 20]]

scores = []
for student in names_scores:
    scores.append(student[1])
    
# [10, 20, 10, 50, 40, 20]

sorted_scores = sorted(set(scores))
second_lowest = sorted_scores[1]


names_second_lowest = []
for student in names_scores:
    if student[1] == second_lowest:
        names_second_lowest.append(student[0])
names_second_lowest = sorted(names_second_lowest)
print(names_second_lowest)
# for name in names_second_lowest:
#     print(name)
       


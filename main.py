# YOUR CODE HERE
def summation():
    n = int(input())
    lst1 = []
    lst2 = []
    updated_list = []
    for i in range(n):
        num_lst1 = int(input())
        lst1.append(num_lst1)
    for i in range(n):
        num_lst2 = int(input())
        lst2.append(num_lst2)
    for i in range(n):
        lst12 = lst1[i] + lst2[i]
        updated_list.append(lst12)
    print(updated_list)
    return updated_list

def find_min_max():
    min_max_summation = summation()
    return min(min_max_summation), max(min_max_summation)

print(find_min_max())

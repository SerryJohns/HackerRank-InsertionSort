def format_print(arr):
    temp_list = []
    for var in arr:
        temp_list.append(str(var))
    return ' '.join(temp_list)

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

arr.reverse()
print(format_print(arr))

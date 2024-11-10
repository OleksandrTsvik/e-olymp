n, m = map(int, input().split())

arr_n = list(map(int, input().split()))[:n]
arr_m = list(map(int, input().split()))[:m]

num = []
min_n = min(arr_n)
min_m = min(arr_m)

if min_n == min_m:
    arr_n = list(filter(lambda x: x != min_n, arr_n))
    arr_m = list(filter(lambda x: x != min_m, arr_m))

    tmp_min_n = min(arr_n)
    tmp_min_m = min(arr_m)

    if tmp_min_n < tmp_min_m:
        num.append(tmp_min_n)
        num.append(min_m)
    else:
        num.append(tmp_min_m)
        num.append(min_m)
elif min_n < min_m:
    num.append(min_n)
    num.append(min_m)
else:
    num.append(min_m)
    num.append(min_n)

print(*num, sep='')

arr=list(map(int,input("enter the values").split()))
sorted_arr=sorted(arr)
ranked_map={num:rank for rank,num in enumerate(sorted_arr,start=1)}
print(ranked_map)
ranked_arr=[ranked_map[num] for num in arr]
print(*ranked_arr)
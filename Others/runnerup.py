n = int(input())  
arr = list(map(int, input().split())) 

unique_scores = sorted(set(arr), reverse=True)  

if len(unique_scores) < 2:
    print("No runner-up")  
else:
    print(unique_scores[1])

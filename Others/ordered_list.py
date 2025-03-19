n=int(input("enter a range: "))
scores={}
for i in range(n):
    name=input("enter name:")
    score=float(input("enter the score:"))
    scores[name]=score
print(scores)
low=min(scores,key=scores.get)
print("low is: ",low)
low_pop=scores.pop(low)
print("after removing low: " ,scores)
min_score=min(scores.values())
print("the new low is : ",min_score)
# min_names=[name for name,score in scores.items() if score==min_score]
# print(min_names)
min_names=sorted([name for name , score in scores.items() if score==min_score])
for name in min_names:
    print(name)

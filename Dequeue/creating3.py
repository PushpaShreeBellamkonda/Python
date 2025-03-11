from collections import deque
q=deque([10,20,30,40,50])
q.rotate(2)
print(q)
q.rotate(-2)
print(q)
q.reverse()
print(q)
q[2]=100
print(q)
print(q[0])
print(q[-1])
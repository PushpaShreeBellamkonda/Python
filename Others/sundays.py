def sundays(n,day):
    days=["mon","tue","wed","thur","fri","sat","sun"]
    start_ind=days.index(day.lower())
    first_sun=7-start_ind if start_ind!=6 else 0
    if first_sun <=n:
        count=1+(n-first_sun)//7
    else:
        count=0
    return count
n=int(input("enter the no of days: "))
day=input("enter the start day: ")
print(sundays(n,day))
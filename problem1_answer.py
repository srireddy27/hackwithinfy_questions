t=int(input())
for _ in range(t):
    stk=[]
    s=input()
    for i in s:
        if(i=="("):
            stk.append(i)
        else:
            if(stk==[] or stk[-1]==")"):
                stk.append(i)
            else:
                stk.pop()
    front=0
    end=0
    for i in stk:
        if(i==")"):
            front+=1
        else:
            end+=1
    print(("("*front)+s+(")"*end))

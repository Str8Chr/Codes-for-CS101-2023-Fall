seq=[int(input())for _ in range(int(input()))]
if len(seq)==1:print(0);exit()
v=temp=0;trend,op=seq[1]-seq[0],(lambda x, y:y,min,max)
for i in range(2,len(seq)):
    if trend*(seq[i]-seq[i-1])>0:temp+=abs(seq[i-1]-seq[i-2])
    else:v,temp,seq[i-1]=v+temp+abs(trend),0,op[(trend>0)+(trend!=0)](seq[i],seq[i-2])
    trend=seq[i]-seq[i-1]
print(v+temp+abs(seq[-1]-seq[-2]))
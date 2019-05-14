def sum_of_integers(x):
    s=0
    while(x>0):
        s+=x%10
        x//=10
    return s

def sortkey_sum_of_integers(x):
    return soi(x)

def sortkey_string(x):
    return str(x)


in = list(map(int, input().rstrip().split()))
in = sorted(in,key=sortkey_sum_of_integers)

output=[]
in=0
while( i<len(in) ):
    temp=[in[i]]
    while(i<len(in)-1 and sum_of_integers(in[i])==sum_of_integers(in[i+1])):
        temp.append(in[i+1])
        i+=1
    temp=sorted(temp,key=sortkey_string)
    for x in temp:
        output.append(x)
    i+=1
print(output)
print("Successful")

def i_p(s,start,end):
    while start <end:
        if s[start]!=s[end]:
            return False
        start+=1
        end-=1
    return True

def l(s):
    m=left=right=0
    for i in range(len(s)):
        for j in range(i,len(s)):
            if i_p(s,i,j):
                if (j-i+1)>m:
                    left,right=i,j
                    m=j-i+1
    return s[left:right+1]

print(l('cbbd'))

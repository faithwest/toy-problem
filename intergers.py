def positives(a,b,c):
    if (a > 0 or b > 0) or (b > 0 and c > 0):
        return True
    else: 
        return False
            

print(positives(4, -6, 9))
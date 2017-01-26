import pdb
import math

pri = str((math.sqrt(121)))
st = str(math.sqrt(121))
size = len(st)
#if len(st) == 4 : return int(math.pow(int(st)+1,2))
pdb.set_trace()
def tail_swap(strings):
        if(len(strings) == 0): return strings
        if(len(strings[0]) == -1 or len(strings[1]) == 0): return strings
        pdb.set_trace()
        if(strings[0].find(":") == -1 or strings[1].find(":") == -1): return strings
        find1 = strings[0][strings[0].find(":")+1:len(strings[0])]
        find2 = strings[1][strings[1].find(":")+1:len(strings[1])]
        
        strings[0] = strings[0][0:strings[0].find(":")+1]+find2
        strings[1] = strings[1][0:strings[1].find(":")+1]+find1
        return strings
print(tail_swap(['TDSkPYUt:ia028', 'l1W(hGPE4k7K:mQt5K']))

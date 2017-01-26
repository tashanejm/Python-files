import random
import sys
#import pdb

def main():
    articles = ["the","a","another","an","some"]
    subjects = ["cat","dog","man","woman","girl","boy","mouse"]
    verbs = ["sang","ran","jumped","hoped","laughed","cried","walked","talked"]
    adverbs = ["loudly","quietly","well","badly","early","easily","quickly"]

    choice1 = [articles, subjects, verbs, adverbs]
    choice2 = [articles, subjects, verbs]
    choices = [choice1, choice2]
    try:
        num = sys.argv[1]
        for n in range(1,int(num)):
            go = random.randint(0,len(choices)-1)
            select = choices[go]
            if n != 0 : print("")
            for m in (select):  print(m[random.randint(0,len(m)-1)], end=" ")
    except IndexError:
        for n in range(5):
            go = random.randint(0,len(choices)-1)
            select = choices[go]
            if n != 0 : print("")
            for m in (select):  print(m[random.randint(0,len(m)-1)], end=" ")
    except ValueError as err:
        print(err,"Integers only please", num)
main()

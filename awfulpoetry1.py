import random


def main():
    articles = ["the","a","another"]
    subjects = ["cat","dog","man","woman"]
    verbs = ["sang","ran","jumped","hoped","laughed"]
    adverbs = ["loudly","quietly","well","badly"]
    
    for n in range(5):
        go = random.randint(0,1)
        art = random.randint(0,2)
        sub = random.randint(0,3)
        verb = random.randint(0,4)
        adverb = random.randint(0,3)
        if go == 0: print(articles[art], subjects[sub], verbs[verb], adverbs[adverb])
        else:   print(articles[art], subjects[sub], verbs[verb])

main()

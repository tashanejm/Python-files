import sys
import fileinput
import pdb

def main():
    strings = []
    filename = []
    for files in sys.argv[1:]:                          #reads in command line as string
        filename.append(files)
        text = open(files,'r').read().replace("\n"," ") #open, read and remove next-line in text file
        strings.append(text)                            #add file to list

    words =[[] for count in range(len(strings))]
    for col in range(0,len(strings)):
        words[col] = strings[col].split(" ")


    common_file =[[] for count in range(len(filename))]
    in_file = [[True]for count in range(len(filename))]
    common_words =""
    #count = 0
    for list_count in range(0,len(words)):
        for n in words[list_count]:
            for list_files in range(0, len(words)):
                #if list_count == 3: pdb.set_trace()
                if list_files != list_count and n in words[list_files]:
                    if n not in common_words: common_words += n + " "
                    #
                    if in_file[list_count] and filename[list_files] not in common_file[list_count]:
                        #pdb.set_trace()
                        common_file[list_count].append(filename[list_files])
                        in_file[list_files] = False
    
    print("Common Words",common_words, sep="\n")
    print()
    for n in range(0,len(filename)):
        if in_file[n]:
            print("".join(filename[n]) +":",end=" ")
            print(" ".join(common_file[n]))
    
main()

#write a program to find the most common words in a text file


def find_most_common_word(filename):
    words_frequency={}
    max_word=''
    max_count=0
    with open(filename,'r') as readFile:
        #iterate over each line in the text
        for line in readFile:
            words=line.lower().replace(',','').replace("'","").replace(';', '').replace('\n','').replace("!","").split(' ')
            #iterate over each word from the line
            for word in words:
                if( word in words_frequency):
                    words_frequency[word]+=1
                else:
                    words_frequency[word]=1
                if (words_frequency[word]>max_count):
                    max_word=word
                    max_count=words_frequency[word]
    print (words_frequency)
    return (max_word, max_count)

#driver code
if __name__=="__main__":
    test_file="comm_word.txt"
    result=find_most_common_word(test_file)
    print("the most common word found: ")
    print(result)





    




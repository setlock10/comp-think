class Entry :
    def __init__(self, input_word, input_synonyms) :
        self.word = input_word
        self.synonyms = input_synonyms

e1=Entry("angry",['mad', 'annoyed'])
e2=Entry("mad",['angry', 'annoyed'])
e3=Entry("annoyed",['angry', 'mad'])
e4=Entry("sad",['upset', 'depressed', 'unhappy'])
e5=Entry("upset",['sad', 'depressed', 'unhappy'])
e6=Entry("depressed",['sad', 'upset', 'unhappy'])
e7=Entry("unhappy",['depressed', 'sad', 'upset'])
e8=Entry("happy",['glad', 'pleased', 'delighted', 'joyous'])

Thesaurus = [e1, e2, e3, e4, e5, e6, e7, e8]


def search(keyword) :

   # implement the function here
   all_words=[]
   tuples=[]
   all_words.append(keyword)
   for entry in Thesaurus:
    if keyword==entry.word:
        for word in entry.synonyms:
            all_words.append(word)

   print (all_words)
   for search_word in all_words:
    count=0
    for doc in Corpus:
        for word in doc:
            if search_word==word:
                count+=1
    temp=(search_word,count)
    tuples.append(temp)

   

   return tuples# modify to return a list of tuples+


Corpus=[['you', 'bet', 'i', 'am', 'angry'], ['i', 'am', 'angry', 'with', 'her'], ['i', 'know', 'you', 'are', 'angry'], ['i', 'was', 'angry', 'at', 'myself'], ['i', 'get', 'angry', 'when', 'i', 'am', 'hungry'], ['i', 'was', 'happy', 'when', 'i', 'was', 'able', 'to', 'complete', 'that', 'level', 'in', 'angry', 'birds'], ['that', 'made', 'me', 'so', 'mad'], ['i', 'am', 'sorry', 'i', 'got', 'mad'], ['i', 'am', 'not', 'mad', 'anymore'], ['i', 'cannot', 'stay', 'mad', 'at', 'you'], ['i', 'got', 'pretty', 'annoyed', 'with', 'how', 'happy', 'she', 'seemed', 'about', 'the', 'news'], ['it', 'has', 'been', 'a', 'difficult', 'week', 'and', 'i', 'cannot', 'say', 'i', 'am', 'sad', 'that', 'it', 'is', 'over'], ['i', 'am', 'sad', 'to', 'see', 'you', 'go'], ['the', 'ending', 'of', 'that', 'movie', 'made', 'me', 'really', 'sad'], ['i', 'was', 'pretty', 'sad', 'when', 'we', 'moved', 'to', 'our', 'new', 'apartment'], ['i', 'am', 'still', 'upset', 'about', 'what', 'happened', 'last', 'night'], ['i', 'got', 'really', 'depressed', 'thinking', 'about', 'their', 'break-up', 'but', 'i', 'know', 'it', 'was', 'for', 'the', 'best', 'and', 'i', 'suppose', 'i', 'am', 'happy', 'for', 'them'], ['you', 'make', 'me', 'happy'], ['i', 'am', 'in', 'my', 'happy', 'place', 'now'], ['i', 'can', 'die', 'happy', 'now'], ['i', 'was', 'so', 'happy'], ['i', 'am', 'happy', 'that', 'the', 'weekend', 'is', 'finally', 'here'], ['i', 'am', 'always', 'happy', 'to', 'help'], ['i', 'was', 'pretty', 'upset', 'to', 'hear', 'that', 'news', 'but', 'then', 'i', 'realized', 'that', 'i', 'just', 'want', 'her', 'to', 'be', 'happy'], ['i', 'am', 'perfectly', 'happy', 'right', 'where', 'i', 'am'], ['we', 'are', 'just', 'one', 'big', 'happy', 'family'], ['i', 'am', 'really', 'not', 'too', 'happy', 'about', 'how', 'angry', 'she', 'became'], ['a', 'hug', 'from', 'you', 'would', 'make', 'me', 'happy'], ['i', 'am', 'glad', 'you', 'came', 'to', 'this', 'party', 'it', 'is', 'really', 'nice', 'to', 'see', 'you'], ['i', 'am', 'so', 'glad', 'that', 'is', 'over'], ['i', 'was', 'delighted', 'that', 'my', 'sister', 'was', 'able', 'to', 'come', 'visit', 'us', 'for', 'the', 'holiday'], ['i', 'was', 'pleased', 'with', 'the', 'result', 'but', 'not', 'as', 'happy', 'as', 'my', 'cousin', 'was'], ['it', 'was', 'a', 'fairly', 'joyous', 'occasion', 'and', 'i', 'could', 'see', 'how', 'delighted', 'my', 'niece', 'was', 'to', 'receive', 'so', 'many', 'gifts'], ['i', 'try', 'not', 'to', 'get', 'too', 'depressed', 'when', 'i', 'think', 'about', 'the', 'past', 'but', 'i', 'was', 'so', 'happy', 'back', 'then'], ['it', 'really', 'pleased', 'me', 'to', 'know', 'that', 'she', 'found', 'a', 'new', 'job']]

input = "happy"
output = search(input) # invoke the method using a test input
print(output) # prints the output of the function
# do not remove this line!

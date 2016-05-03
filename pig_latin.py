def pig_latin(word):
    if(word[0]=='a' or word[0]=='e' or word[0]=='i' or 
       word[0]=='o' or word[0]=='u'):
        word1=word[1:]+word[0]+"ay"
    else:
        word1=word+"way"
    
    print word1




def test(word):
    pig_latin(word)

test("ocean")
test("sky")
test("limit")
test("sense")
test("alaska")

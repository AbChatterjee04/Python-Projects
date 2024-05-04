def word_replace():
    str = 'Hickory dickory dock. The mouse went up the clock The clock struck one. The mouse went down Hickory dickory dock tick tock, tick tock, tick tock, tick tock A snake Hickory dickory dock.The snake went up the clock The clock struck two. The snake went down Hickory dickory dock tick tock, tick tock, tick tock, tick tock'
    
    word_to_replace = input("Enter the word you want replace: ")
    word_replace_with = input("Enter the word you want to replace with: ")
    
    print(str.replace(word_to_replace,word_replace_with))
    

word_replace() # replacing tick tock with tik tok ;)
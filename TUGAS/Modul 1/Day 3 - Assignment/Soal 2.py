'''
## Question-2

Find-and-replace is a standard feature in text editors, IDEs, and word processor software. 
Even the Python language comes with a `replace()` string method since programs often use it. 
In this exercise, you’ll reimplement this common string operation.

Write a simple program that has three main variable: 

- `text` is the string with text to be replaced
- `oldText` is the text to be replaced
- `newText` is the replacement text.

Keep in mind that this function must be case-sensitive: if you are replacing 'dog' with 'fox', 
then the 'DOG' in ‘MY DOG JONESY' won’t be replaced. Your solution is correct if produce following output:

text = 'The Fox and fox.'
oldText = 'fox' 
newText = 'dog'

output:
'The Fox and dog.'
'''

if __name__ == '__main__':
    # ANSWER

    # input text, oldtext, newtext
    text = input('type your text:')
    oldText = input('find text:')
    newText = input('replace text with:')

    # define lenght of each text
    lText = len(text)
    lOldText = len(oldText)
    lNewText = len(newText)

    # define the variable to skip the satisfied text
    skip = lOldText

    # create output variable that contain the result
    output = ''

    i = 0

    # loop until the length of text
    while i < (lText):
        # define the sText as result of sliced text
        sText = text[i:lOldText]
        # check whether sText same with oldText or not
        # if true, add new text, skip use the length of skip variable
        if sText == oldText:
            output += f'{newText}'
            i += skip
            lOldText += skip
        # if false, add first char of sText, skip 1 char
        else:
            output += f'{sText[0]}'
            i += 1
            lOldText += 1
    
    # print the result
    print(output)




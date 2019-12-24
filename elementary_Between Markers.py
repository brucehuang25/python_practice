
# CHECKIO | Elementary | Between Markers
# https://py.checkio.org/en/mission/between-markers/

"""
You are given a string and two markers (the initial and final). You have to find a substring enclosed between these two markers. But there are a few important conditions:

The initial and final markers are always different.
If there is no initial marker, then the first character should be considered the beginning of a string.
If there is no final marker, then the last character should be considered the ending of a string.
If the initial and final markers are missing then simply return the whole string.
If the final marker comes before the initial marker, then return an empty string.
Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.

Output: A string.

Example:

between_markers('What is >apple<', '>', '<') == 'apple'
between_markers('No[/b] hi', '[b]', '[/b]') == 'No'
1
2
How it is used: for parsing texts

Precondition: can't be more than one final marker and can't be more than one initial
"""


## My version
def between_markers(text, begin, end):
    
    index_f = int(text.find(begin))
    index_b = int(text.find(end))
    
    if index_b == -1:
        index_b = len(text)
        
    if index_f > index_b:
        return ""
    
    if index_f == -1:
        return text[:index_b]
    
    else:
        return text[(index_f+len(begin)):index_b]
    
## Most sexy version
def between_markers(text: str, begin: str, end: str) -> str:
    start = text.find(begin) + len(begin) if begin in text else None
    stop = text.find(end) if end in text else None
    return text[start:stop]


        
print(between_markers("What is >apple<",">","<"))

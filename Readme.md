# NLP Assignment 6
#### Yunhao Li
#### NetID: yl6220

## Features tried
1.  len(token): The length of the token.
2.  token: The string of the token
3.  pre[0]: The precedent token. If the current token is the first word, this is chosen as "None".
4.  post[0]: The succeeding token. If the current token is the last word, this is chosen as "None".
5.  pos: The pos tag of current token.
6.  bio: The bio tag of current token. 
7.  token.islower(): The bool whether all the chars in the token is in lower case.
8.  "-" in token: The bool whether there is a "-" in the token.
9.  prev_tag: The name tag of the previous token. If the current token is the first word, then this item is "@@"
10. token_lower: The lowercase string of the token
11. pre[0].lower(): The lowercase string of the precedent token
12. upper_char_count: The number of the chars in uppercase in the token. 
13. upper_char_count / len(token): The fraction of the the number of the chars in uppercase in the token.
14. token_lower.find("bach"): The location where the substring "bach" in token. If not found, this item is -1.

## Features finally chosen
1.  len(token), 
2.  token, 
3.  pre[0], 
4.  post[0], 
5.  pos, 
6.  bio, 
7.  token.islower(), 
8.  "-" in token, 
9.  prev_tag,
10. token_lower, 
11. pre[0].lower(), 
12. upper_char_count, 
13. upper_char_count / len(token),
14. token_lower.find("bach")

## The highest F-1 measure tested on the development corpus
  precision: 83.94<br>
  recall:    81.88<br> 
  F1:        82.90<br>
  
## The design of the program

## How to run it
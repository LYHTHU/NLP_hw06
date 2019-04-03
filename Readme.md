# NLP Assignment 6
#### Yunhao Li
#### NetID: yl6220

## Features tried
1.  `len(token)`: The length of the token.
2.  `token`: The string of the token
3.  `pre[0]`: The precedent token. If the current token is the first word, this is chosen as "None".
4.  `post[0]`: The succeeding token. If the current token is the last word, this is chosen as "None".
5.  `pos`: The pos tag of current token.
6.  `bio`: The bio tag of current token. 
7.  `token.islower()`: The bool whether all the chars in the token is in lower case.
8.  `"-" in token`: The bool whether there is a "-" in the token.
9.  `prev_tag`: The name tag of the previous token. If the current token is the first word, then this item is "@@"
10. `token_lower`: The lowercase string of the token
11. `pre[0].lower()`: The lowercase string of the precedent token
12. `upper_char_count`: The number of the chars in uppercase in the token. 
13. `upper_char_count / len(token)`: The fraction of the the number of the chars in uppercase in the token.
14. `token_lower.find("bach")`: The location where the substring "bach" in token. If not found, this item is -1.
15. `pre[1]`： The pos tag of the precedent token. If no precedent, then it is `"start"`.
16. `post[1]`: The pos tag of the succeeding token. If no succeeding token, then it is `"end"`.
17. `pre[2]`: The bio tag of the precedent token. If no precedent, then it is `0`.
18. `post[2]`: The bio tag of the succeeding token. If no succeeding token, then it is `0`.
## Features finally chosen
1.  `len(token)` 
2.  `token`
3.  `pre[0]`
4.  `post[0]` 
5.  `pos` 
6.  `bio`
7.  `token.islower()` 
8.  `"-" in token` 
9.  `prev_tag`
10. `token_lower`
11. `pre[0].lower()`
12. `upper_char_count`
13. `upper_char_count / len(token)`
14. `token_lower.find("bach")`

## The highest F-1 measure tested on the development corpus
  precision: 83.94<br>
  recall:    81.88<br> 
  F1:        82.90<br>
  
## The design of the program
I created a class `FeatureBuilder` to read a tagged/untagged file with pos and bio. There is a variable named `train_mode`.
It can be set by construction function or directly. When `train_mode` is true, it will create a feature file with tag, 
otherwise it will create the feature file without tag. <br>
The `run` function is the main part of a builder. <br>
I use a python list named `all_feature` to store all the features I have tried. And I create a mask vector named `enable_list`
to activate and deactivate the features. Each item of `enable_list` is a binary integer, and when the item is `1` then 
the corresponding feature is activated, and if it is `0` then the feature is disabled.<br>
Given an input file whose path is like `[filepath].[suffix]`, then create a `FeatureBuilder` object `builder` and call 
`builder.run()`. It will generated a file whose path is `[filepath].feature`.

## How to run it
Put the training file and development file and the Jar file in the same folder with the `FeatureBuilder.py.`<br>
Run `"python3 FeatureBuilder.py"`.<br>
The python script will automatically build the feature file of training file, and compile and run `MEtrain` to train on it.
Then it will build the feature file of the development file and test file. Then run the MEtag to tag them, and finally 
run `score.name.py` to estimate the result.<br>
<br>
The class `FeatureBuilder` has 2 arguments, `input_path` and `train_mdoe`. The default file path is `"./CONLL_train.pos-chunk-name"`. And the default value of `train_mode` is `true`. <br>
<br>
If you want to use this class to build a feature of a given `.pos-chunk` file, just create a `FeatureBuilder` object `builder` with its path. If it is a train file then the `train_mode` is true, else it is `false`.
Then call `builder.run()`, then the feature file will be generated.

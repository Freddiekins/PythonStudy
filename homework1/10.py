str = "night after night she came to tuck me in even long after my childhood years following her longstanding custom she would lean down and push my long hair out of the way then kiss my forehead"
dict = {'night': 1, 'she': 1}
words = str.split()
print(words)
for i in words:
    if i in dict:
        dict[i] = dict[i] + 1
    else:
        dict.update({i: 1})
print(dict)

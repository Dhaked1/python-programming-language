from collections import Counter
language = ['php','php','python','php','python','javascript','php','python']
print("original list:")
print(language)
cnt = Counter(language)
print("most comman element of the said list:")
print(cnt.most_common(1)[0][0])
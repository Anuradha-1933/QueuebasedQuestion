# problem:Max substring
s=str(input())
ws = max_length = 0
dict = {}
for i in range(len(s)):
    if s[i] in dict and ws <= dict[s[i]]:
        ws = dict[s[i]] + 1
    else:
        max_length = max(max_length, i - ws + 1)
    dict[s[i]] = i
print(max_length)

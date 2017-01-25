# 4 ways to make a string
str1 = 'This is a string. We built it with single quotes.'
str2 = "This is also a string, built with double quotes"
str3 = '''This is built using triple quotes,
so it can span multiple lines.'''
str4 = """This too
is a multiline one
built with triple double-quotes"""

print str1
print str2
print str3
print str4

print len(str1)


# indexing and slicing strings
s = "The trouble is you think you have time."
print s[0]          # indexing at position 0, which is the first char
print s[5]          # indexing at position 5, which is the 6th char
print s[:4]         # slicing, we specify only the stop position
print s[4:]         # slicing, we specify only the start position
print s[2:14]       # slicing, both start and stop positions
print s[2:14:3]     # slicing, start, stop and step (every 3 chars)
print s[:]          # quick way of making a copy
print len(s)
print s[::-1]       # Can you fnd a way to get the reversed copy of a string using slicing?

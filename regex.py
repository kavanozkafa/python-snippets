#find adverbs
import re
text = "hello my lovely son"
for m in re.finditer(r"\w+ly",text):
	print('%d-%d:%s' % (m.start(), m.end(), m.group(0)))

#remove between ()

items = ["edx(.org)", "github(.com)"]
for item in items:
	print(re.sub(r" ?\([^)]+\)", "", item))
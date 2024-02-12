# Pip Camelcase
from camelcase import CamelCase
c=CamelCase()
text="this is a camelcase library"
output=c.hump(text)
print(output)


# Or

import camelcase
s=camelcase.CamelCase()
txt='this is a camelcase library'
ot=s.hump(txt)
print(ot)
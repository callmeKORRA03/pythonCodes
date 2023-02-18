# f = open('Coditions.py')
# txt = f.readlines()
# print(type(txt))
# print(txt)
# f.close()

import os
if os.path.exists('hehehe.py'):
    os.remove('hehehe.py')
else:
    print('File does not exist')

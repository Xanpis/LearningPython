import re 

def check (string):
   rule = re.compile(r'[^a-zA-Z0-9]')
   result = rule.search(string)
   return not bool(result)


print(check('gaeEta'))

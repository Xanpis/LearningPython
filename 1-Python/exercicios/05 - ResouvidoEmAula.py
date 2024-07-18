

def veriChar(char):
   tepy = {'maiu':0,'minu':0}
   for i in char:
      if i.isupper():
         tepy['maiu'] += +1

      elif i.islower():
         tepy['minu'] +=1
   return tepy

print(veriChar('AsdfSDAfERASDfasdflkj'))


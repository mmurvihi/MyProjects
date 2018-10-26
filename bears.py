def bears(n):
   if n<0 or not type(n)==int:
       raise ValueError
   tensdigit = int(str(n)[-2]) if len(str(n))>1 else 0
   onesdigit = int(str(n)[-1])
   possible = False
   if n < 42:
       possible = False
   elif n == 42:
       return True
   elif n%2 == 0 and bears(n/2):
       possible = bears(n/2)
       if possible:
           return True
   elif n%4 == 0 or n%3 == 0 and bears(n-tensdigit*onesdigit):
       possible = bears(n-tensdigit*onesdigit)
       if possible:
           return True
   elif n%5 == 0 and bears(n-42):
       possible = bears(n-42)
       if possible:
           return True
   return possible


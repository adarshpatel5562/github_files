import random



uppercase1 = chr(random.randint(65,90))
uppercase2 = chr(random.randint(65,90))
lowercase1 = chr(random.randint(97,122))
lowercase2 = chr(random.randint(97,122))
digit1 = str(random.randint(0,9))
digit2 = str(random.randint(0,9))
punc1 = chr(random.randint(32,47))
punc2 = chr(random.randint(91,96))

password = uppercase1+uppercase2+lowercase2+lowercase1+digit2+digit1+punc2+punc1
password = ''.join(random.sample(password,len(password)))
print("The Suggested Password for you is "+password)

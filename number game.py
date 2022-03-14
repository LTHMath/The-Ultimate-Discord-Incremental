import math

print("Hello user! Here are commands: c(x): Count to x, b(x): Reset to base x, spn(): Get spn, enteracn(): Enter acn, completeacn(): Complete acn, exitacn(): Exit acn, iv(x): Count in iv to x, m(x): Reset to multi x, sp3set(x): Set your sp3 to x, incremental_sacrifice(): Incremental sacrifice, ib(x): Get ib x")


      
def reverse_base_conversion(number, base):
  result = 0
  digit = 0 
  midnumber = number
  while midnumber != 0:
    result += (midnumber % 10) * (base**digit)
    midnumber = (midnumber - midnumber % 10) / 10
    digit += 1
  return int(result)


def legalnumberinbase(number, base):
  midnumber = number
  result = True
  while midnumber != 0:
    result = result and (midnumber % 10 < base)
    midnumber = (midnumber - midnumber % 10) / 10
  return result


def base_conversion(number, base):
  result = 0
  digit = 0
  if base > 10:
    print('There is no support for this function yet until hexadecimal numbers are implemented, please give 3-5 business days.')
    #insert thingy thing here
  elif base < 2:
    print('An error has occurred in the code, check all features having to do with base if you are the developer.')
  elif isinstance(base, int):
    while int(number) > 0:
      result += (int(number) % (base)) * (10**digit)
      digit += 1
      number = (number - (int(number) % (base))) / base
    return result
  else:
    return result

number = 0
incremety = 0
incremetybase10 = 0
incremetybase = 10
base = 10
multi = 1
incremetymulti = multi//5 + 1
incrementalsacrifice = 1
numberbase10 = reverse_base_conversion(number, base)
starting_number = incremety*multi
sp1 = False
sp2 = False
sp3 = False
sp4 = False
sp3setting=0
inac1 = False
ac1complete = False
inac2 = False
ac2complete = False
inac3 = False
ac3complete = False

def sp1():
  global multi
  global sp1
  if multi>=5:
    sp1=True
    return "Success"
  else:
    return "Nope"

def sp2():
  global multi
  global sp2
  if multi>=10:
    sp2=True
    return "Success"
  else:
    return "Nope"

def sp3():
  global multi
  global sp3
  if multi>=30:
    sp3=True
    return "Success"
  else:
    return "Nope"

def sp4():
  global multi
  global sp4
  if multi>=60:
    sp4=True
    return "Success"
  else:
    return "Nope"

def sp3set(x):
  global sp3
  global sp3setting
  if sp3:
    sp3setting=x
  else:
    pass

def megascaling(x):
  if x<100:
    return 1
  else:
    y=(x-99)//5
    z=(x-99)%5
    result=1
    for i in range(0,y):
      result*=(1.01+.002*i)**5
    result*=(1.01+.002*y)**z
    return result

def scaling(x):
  ac3factor=1+.5*inac3
  if x<25:
    return 1
  elif x<50:
    return (1.1)**((x-20)//5)*ac3factor
  elif x<100:
    return (1.1)**((x-20)//5)*(1.5)**((x-40)//10)*ac3factor
  else:
    return (1.1)**((x-20)//5)*(1.5)**((x-40)//10)*megascaling(x)*ac3factor

def multi_formula(multii):
  global number
  global base
  global numberbase10
  global multi
  global sp1
  if multii==multi+1: 
    x=multii-2
    y=x%2
    z=x//2
    result=z*81+y*40+81
    ac3factor=1+2*inac3
    return base_conversion(result*scaling(x)*ac3factor,3)
  else:
    x=multii-2
    y=x%2
    z=x//2
    result=z*81+y*40+81
    w=multi_formula(multi+1)
    r = ac1complete or inac1 and (not inac2)
    r+=1
    return (w+(result-w)*2)/r


def valid_count(x):
  global number
  global base
  global numberbase10
  global multi
  global sp2
  if sp2:
    return x <= base_conversion(numberbase10 + multi, base) and x>number and isinstance(x,int) and legalnumberinbase(x,base)
  else:
    return x == base_conversion(numberbase10 + multi, base) and isinstance(x,int) and legalnumberinbase(x,base)

def valid_incremety(x):
  global number
  global base
  global numberbase10
  global multi
  global sp2
  global incremety
  global incremetymulti
  global incremetybase10
  global incremetybase
  global ac2complete
  global inac2
  global incrementalsacrifice
  if sp2:
    return x <= base_conversion(incremetybase10 + incremetymulti*incrementalsacrifice, incremetybase) and x>incremety and isinstance(x,int) and legalnumberinbase(x,incremetybase)
  else:
    return x == base_conversion(incremetybase10 + incremetymulti*incrementalsacrifice, incremetybase) and isinstance(x,int) and (ac2complete or inac2) and legalnumberinbase(x,incremetybase)

def digits(numbert):
  number=str(numbert)
  int_list = []
  for i in range(len(number)):
    int_list.append(int(number[i]))
  return int_list
  
def reverse_digits(digits):
  result=0
  for i in range(len(digits)):
    result+=10**(len(digits)-i-1)*int(digits[i])
  return result
  
def round_down(number,base):
  x=digits(number)
  y=[]
  for i in range(len(x)):
    if x[i]>=base:
      new_item=base-1
    else:
      new_item=x[i]
    y.append(new_item)
  return reverse_digits(y)

def base_formula(x):
  global number
  global base
  global numberbase10
  global multi
  global inac1
  global ac1complete
  values=[0,0,0,1000,400,300,250,200,150,100]
  r = (ac1complete or inac1) and (not inac2)
  r+=1
  return values[x]/r

def update():
  global number
  global base
  global numberbase10
  global multi
  global incremetymulti
  global incremety
  global incremetybase10
  global starting_number
  numberbase10=reverse_base_conversion(number,base)
  incremetymulti=multi//5+1
  incremetybase10=reverse_base_conversion(incremety,base)
  starting_number=multi*incremety

def incremental_sacrifice():
  global incrementalsacrifice
  global incremety
  global incremetybase
  global number
  global base
  global multi
  global inac3
  global ac3complete
  result = math.log(number,10)**1.5
  if sp4 and incrementalsacrifice<result:
    number=0
    incremety=0
    base=10
    multi=1
    update()
    incrementalsacrifice=result
    return result
  else:
    return "Nope"

    
def c(x):
  global number
  global base
  global numberbase10
  global multi
  global sp3setting
  if valid_count(x*10**sp3setting):
    number = x*10**sp3setting
    update()
    return x*10**sp3setting

def iv(x):
  global incremety
  global incremetybase
  if valid_incremety(x) and legalnumberinbase(x,incremetybase):
    incremety = x
    update()
    return x
    
def ib(x):
  global incremety
  global incremetybase
  global number
  global base
  global multi
  global inac3
  global ac3complete
  values=[0,5000,10000,15000,20000]
  if x>0 and incremety>values[x] and (inac3 or ac3complete):
    incremetybase=10-x
    number=0
    incremety=0
    base=10
    multi=1
    update()
    return "Success"
  else:
    return "Nope"
  

def b(x):
  global number
  global base
  global numberbase10
  global multi
  global starting_number
  if base-1==x and ((x>=3 and not inac1) or (x>3)):
    if number>=base_formula(x):
      base=x
      update()
      number=starting_number
      return "Success"
    else:
      return "Nope"
  else:
    return "Nope"

def m(x):
  global number
  global base
  global numberbase10
  global multi
  if isinstance(x,int):
    if number>=multi_formula(x) and ((x==multi+1) or (x>multi+1 and sp1)) and (base==3 or (inac1 and base==4)):
      multi=x
      base=10
      update()
      number=starting_number
      return "Success"
    else:
      return "Nope"
  else:
    return "Nope"

def enterac1():
  global number
  global base
  global numberbase10
  global multi
  global inac1
  global incremety
  if number>=100000 and not inac1 and not ac1complete and not inac2 and not inac3:
    number=0
    base=10
    multi=1
    incremety=0
    update()
    inac1 = True
    return "Success"
  else:
    return "Nope"

def exitac1():
  global number
  global base
  global numberbase10
  global multi
  global inac1
  global incremety
  if inac1:
    number=0
    base=10
    multi=1
    incremety=0
    update()
    inac1 = False
    return "Success"
  else:
    return "Nope"

def completeac1():
  global number
  global base
  global numberbase10
  global multi
  global inac1
  global ac1complete
  global incremety
  if number>=100000 and inac1:
    number=0
    base=10
    multi=1
    incremety=0
    update()
    inac1 = False
    ac1complete = True
    return "Success"
  else:
    return "Nope"

def enterac2():
  global number
  global base
  global numberbase10
  global multi
  global inac2
  global incremety
  if number>=1000000 and not inac2 and not ac2complete and not inac1 and not inac3:
    number=0
    base=10
    multi=1
    incremety=0
    update()
    inac2 = True
    return "Success"
  else:
    return "Nope"

def exitac2():
  global number
  global base
  global numberbase10
  global multi
  global inac2
  global incremety
  if inac2:
    number=0
    base=10
    multi=1
    incremety=0
    update()
    inac2 = False
    return "Success"
  else:
    return "Nope"

def completeac2():
  global number
  global base
  global numberbase10
  global multi
  global inac2
  global ac2complete
  global incremety
  if number>=1000000 and inac2:
    number=0
    base=10
    multi=1
    incremety=0
    update()
    inac2 = False
    ac2complete = True
    return "Success"
  else:
    return "Nope"


def enterac3():
  global number
  global base
  global numberbase10
  global multi
  global inac3
  global incremety
  if number>=100000000 and not inac3 and not ac3complete and not inac1 and not inac2:
    number=0
    base=10
    multi=1
    incremety=0
    update()
    inac3 = True
    return "Success"
  else:
    return "Nope"

def exitac3():
  global number
  global base
  global numberbase10
  global multi
  global inac3
  global incremety
  if inac3:
    number=0
    base=10
    multi=1
    incremety=0
    update()
    inac3 = False
    return "Success"
  else:
    return "Nope"

def completeac3():
  global number
  global base
  global numberbase10
  global multi
  global inac3
  global ac3complete
  global incremety
  if number>=100000000 and inac3:
    number=0
    base=10
    multi=1
    incremety=0
    update()
    inac3 = False
    ac3complete = True
    return "Success"
  else:
    return "Nope"
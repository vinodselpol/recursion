# recurssive approach

def getNthFib(n):
    if n ==2:
		return 1
	elif n==1:
		return 0
	else:
	
         return getNthFib(n-1)+getNthFib(n-2)
  
  # iterative approach
  def getNthFib(n):
	lastTwo=[0,1]
	counter=3
	
	while counter <=n:
		nextFib=lastTwo[0]+lastTwo[1]
		lastTwo[0]=lastTwo[1]
		lastTwo[1]=nextFib
		counter+=1
	return lastTwo[1] if n > 1 else lastTwo[0]

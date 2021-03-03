import sys
def luhns(cardNum):
	cardSum = 0
	alternate = False
	for i in range(len(cardNum) - 1, -1, -1):
		d = int(cardNum[i])
		if (alternate == True):
			d = d * 2
		cardSum += d // 10
		cardSum += d % 10
		alternate = not alternate
	if (cardSum % 10 == 0):
		return True
	else:
		return False
 
if __name__=="__main__":
	if len(sys.argv)!=2:
		print ("\nSyntax: python %s 'Card Number'" % (sys.argv[0]))
		exit()
	cardNum = sys.argv[1]
	if (luhns(cardNum)):
		print("This is a valid card")
	else:
		print("This is not a valid card")

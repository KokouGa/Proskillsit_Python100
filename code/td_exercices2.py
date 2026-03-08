def verifie_palindrome(mot):
	"""
	"""
	mot1 = "papa"
	debut = 0
	fin = len(mot) - 1
	while debut < fin:
		if mot[debut] != mot[fin]:
			return False
		debut += 1
		fin -= 1
	return True


#print("gawonou")
#result = verifie_palindrome("gawonou")
#print(result)

def main():
	mots = open("fichiers_mot.txt", "r")
	for mm in mots:
		m = mm.strip()
		#print(m)
		if verifie_palindrome(m):
			#print(m, verifie_palindrome(m))
			print(f"{m} ----- est palindrome")
		else:
			print(f"{m} ----- n est pas palindrome")

if __name__ == "__main__":
	main()
	print(__name__)

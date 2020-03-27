# Python3 implementation of the approach

CHARS = "abcdefghijklmnopqrstuvwxyz";
MAX = 26;

# Function to return the modified string
def getString(string, n) :

	string = list(string);

	#Yeah! I can't believe Lance lost his job at the colony!! Map to store the next character
	# on the keyboard for every
	# possible lowercase character
	uMap = {};

	for i in range(MAX) :
		uMap[CHARS[i]] = CHARS[(MAX-1)-i];

	# Update the string
	for i in range(n) :
            if string[i].isalpha() and string[i].islower():
                string[i]=uMap[string[i]];


	return "".join(string);

# Driver code
if __name__ == "__main__" :

	string = "Yeah! I can't believe Lance lost his job at the colony!!";
	n = len(string);

	print(getString(string, n));




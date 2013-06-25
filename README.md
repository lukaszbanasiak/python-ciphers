#python-ciphers
Simple ciphers implementation in Python.

## AtBash cipher ##
Atbash is a simple substitution cipher for the Hebrew alphabet.

### Functions ###

Different encoding:

- Diacritical marks conversion to the equivalent characters - if the ciphertext will contain Polish characters, program will convert them to the equivalent
- Based on the Polish alphabet - encryption with 32 characters, other characters ignored
- Based on the English alphabet - encryption using 26 characters, other characters ignored

Reading and writing ciphertext file.

### Examples ###

Encryption using Polish letters, switch `-l 2`

	 IN> gęślą jaźń
	OUT> rśęnź ożąk

Diacritical marks conversion to the equivalent characters (default mode)

	 IN> gęślą jaźń
	OUT> tvhoz qzam
	
	 IN> gesla jazn
	OUT> tvhoz qzam

Decrypt mode, switch `-d`

	 IN> tvhoz qzam
	OUT> gesla jaźń

Load a file to decrypt/encrypt, switch `-f`
	
	 IN> file.txt
	OUT> _file.txt

##Bacon cipher##
Method of steganography devised by Francis Bacon in 1605.

### Functions ###

1. Diacritical marks conversion to the equivalent characters - if the ciphertext will contain Polish characters, program will convert them to the equivalent.
2. Reading and writing ciphertext file.

### Examples ###

Diacritical marks conversion to the equivalent characters (default mode)

     IN> gęślą jaźń
	OUT> AABBAAABAABAABAABABBAAAAAABAABAAAAABBAABABBAB

	 IN> gesla jazn
	OUT> AABBAAABAABAABAABABBAAAAAABAABAAAAABBAABABBAB

Decrypt mode, switch `-d`

	 IN> AABBAAABAABAABAABABBAAAAAABAABAAAAABBAABABBAB
	OUT> GESLAJAZN

Load a file to decrypt/encrypt, switch `-f`
	
	 IN> file.txt
	OUT> _file.txt

##Bifid (aka Delastelle) cipher##
Bifid cipher is a cipher which combines the Polybius square with transposition, and uses fractionation to achieve diffusion.

### Functions ###

1. Diacritical marks conversion to the equivalent characters - if the ciphertext will contain Polish characters, program will convert them to the equivalent.
2. Reading and writing ciphertext file.
3. Ability to set own transformation key
4. Ability to set verbose mode showing intermediate states

### Examples ###

Diacritical marks conversion to the equivalent characters (default mode)

	 IN> gęślą jaźń
	OUT> HOBUCVKY
	
	 IN> gesla jazn
	OUT> HOBUCVKY

Decrypt mode, switch `-d`

	 IN> HOBUCVKY
	OUT> GESLAJAZN

Load a file to decrypt/encrypt, switch `-f`
	
	 IN> file.txt
	OUT> _file.txt

Transformation key, switch `-k klucz`

	      1   2   3   4   5
	 1 [  K   L   U   C   Z  ]
	 2 [  A   B   D   E   F  ]
	 3 [  G   H   I   M   N  ]
	 4 [  O   P   Q   R   S  ]
	 5 [  T   V   W   X   Y  ]
	
	 IN> gęślą jaźń
	OUT> HOBUCVKY

Verbose mode, switch `-v`

	 IN> gęślą jaźń
	  1: 31 24 45 12 21 21 15 35  # after determining coordinates 
	  2: 32 11 22 41 41 55 13 25  # after horizontal transformation
	OUT> HOBUCVKY

##Caeser cipher##
In cryptography a Caesar cipher is one of the simplest and most widely known encryption techniques.

### Functions ###

Different encoding:

- Diacritical marks conversion to the equivalent characters - if the ciphertext will contain Polish characters, program will convert them to the equivalent
- Based on the Polish alphabet - encryption with 32 characters, other characters ignored
- Based on the English alphabet - encryption using 26 characters, other characters ignored

Reading and writing ciphertext file.

Set number of shift relative to the first letter of the alphabet. 

### Examples ###

Set shift number, switch `-s 13`

	 IN> gęślą jaźń
	OUT> trfyn wnma
	
Diacritical marks conversion to the equivalent characters (default mode)

	 IN> gęślą jaźń
	OUT> trfyn wnma
	
	 IN> gesla jazn
	OUT> trfyn wnma

Based on the English alphabet, switch `-l 1`

	 IN> gęślą jaźń
	OUT> tęśyą wnźń

Decrypt mode, switch `-d`

	 IN> trfyn wnma
	OUT> GESLAJAZN

Load a file to decrypt/encrypt, switch `-f`
	
	 IN> file.txt
	OUT> _file.txt

##Polybius cipher##
In cryptography the Polybius square is a device for fractionating plaintext characters.

### Functions ###

1. Diacritical marks conversion to the equivalent characters - if the ciphertext will contain Polish characters, program will convert them to the equivalent.
2. Reading and writing ciphertext file.
3. Ability to set own transformation key
4. Representation of the ciphertext does not affect  at decryption, e.g. `42aaaa 41 1233 5124 14 32 35 331121ddddsss` is equivalent to `42 41 12 33 51 24 14 32 35 33 11 21`

### Examples ###

Diacritical marks conversion to the equivalent characters (default mode)

	 IN> gęślą jaźń
	OUT> 31 24 45 12 21 21 15 35
	
	 IN> gesla jazn
	OUT> 31 24 45 12 21 21 15 35

Decrypt mode, switch `-d`

	 IN> 31 24 45 12 21 21 15 35
	OUT> GESLAJAZN

Load a file to decrypt/encrypt, switch `-f`
	
	 IN> file.txt
	OUT> _file.txt

Transformation key, switch `-k klucz`

	      1   2   3   4   5
	 1 [  K   L   U   C   Z  ]
	 2 [  A   B   D   E   F  ]
	 3 [  G   H   I   M   N  ]
	 4 [  O   P   Q   R   S  ]
	 5 [  T   V   W   X   Y  ]
	
	 IN> gęślą jaźń
	OUT> 31 24 45 12 21 21 15 35

##CharFreq##
In cryptanalysis, frequency analysis is the study of the frequency of letters or groups of letters in a ciphertext.

### Functions ###
Counting:


- All characters or only letters
- Small and big letters.

Calculating percent

### Examples ###

Counting only letters and no case-sensitive (default mode)

	 IN> pan_tadeusz.txt
	  A: 14589  (8.96%)
	  I: 13997  (8.59%)
	  E: 11062  (6.79%)
	  O: 10995  (6.75%)
	  Z: 10485  (6.44%)
	  S: 8073  (4.96%)
	  N: 7711  (4.73%)
	  W: 7482  (4.59%)
	  R: 7227  (4.44%)
	  C: 6652  (4.08%)
	  Y: 6215  (3.82%)
	  K: 5933  (3.64%)
	  D: 5598  (3.44%)
	  T: 5313  (3.26%)
	  M: 4908  (3.01%)
	  Ł: 4773  (2.93%)
	  P: 4232  (2.60%)
	  U: 3733  (2.29%)
	  L: 3288  (2.02%)
	  J: 3154  (1.94%)
	  B: 2833  (1.74%)
	  Ę: 2410  (1.48%)
	  G: 2365  (1.45%)
	  Ą: 2143  (1.32%)
	  H: 1966  (1.21%)
	  Ż: 1533  (0.94%)
	  Ó: 1420  (0.87%)
	  Ś: 1245  (0.76%)
	  Ć: 844  (0.52%)
	  Ń: 283  (0.17%)
	  Ź: 212  (0.13%)
	  F: 175  (0.11%)
	  V: 6  (0.00%)
	  X: 6  (0.00%)
	  +: 162861


Case-sensitive `-c`

	 IN> hamlet.txt
	  e: 14657  (11.32%)
	  t: 11034  (8.52%)
	  o: 10790  (8.33%)
	  a: 9274  (7.16%)
	  s: 8085  (6.24%)
	  n: 8079  (6.24%)
	  h: 7828  (6.04%)
	  i: 7618  (5.88%)
	  r: 7580  (5.85%)
	  l: 5569  (4.30%)
	  d: 4876  (3.76%)
	  u: 4288  (3.31%)
	  m: 3987  (3.08%)
	  y: 3070  (2.37%)
	  w: 2642  (2.04%)
	  f: 2483  (1.92%)
	  c: 2413  (1.86%)
	  g: 2161  (1.67%)
	  p: 1775  (1.37%)
	  b: 1564  (1.21%)
	  v: 1187  (0.92%)
	  k: 1088  (0.84%)
	  H: 884  (0.68%)
	  I: 853  (0.66%)
	  T: 785  (0.61%)
	  A: 625  (0.48%)
	  W: 484  (0.37%)
	  O: 370  (0.29%)
	  B: 261  (0.20%)
	  S: 250  (0.19%)
	  M: 247  (0.19%)
	  G: 245  (0.19%)
	  L: 245  (0.19%)
	  E: 230  (0.18%)
	  P: 227  (0.18%)
	  F: 196  (0.15%)
	  x: 179  (0.14%)
	  K: 178  (0.14%)
	  N: 175  (0.14%)
	  C: 170  (0.13%)
	  R: 134  (0.10%)
	  Y: 129  (0.10%)
	  D: 126  (0.10%)
	  Q: 111  (0.09%)
	  q: 108  (0.08%)
	  j: 101  (0.08%)
	  z: 71  (0.05%)
	  U: 36  (0.03%)
	  V: 32  (0.02%)
	  J: 9  (0.01%)
	  +: 129509


Counting all the characters, not case-sensitive `-a`
	
	 IN> hamlet.txt
	   : 47747  (25.61%)
	  E: 14887  (7.98%)
	  T: 11819  (6.34%)
	  O: 11160  (5.99%)
	  A: 9899  (5.31%)
	  H: 8712  (4.67%)
	  I: 8471  (4.54%)
	  S: 8335  (4.47%)
	  N: 8254  (4.43%)
	  R: 7714  (4.14%)
	  L: 5814  (3.12%)
	  D: 5002  (2.68%)
	  U: 4324  (2.32%)
	  M: 4234  (2.27%)
	  Y: 3199  (1.72%)
	  W: 3126  (1.68%)
	  .: 3108  (1.67%)
	  ,: 2972  (1.59%)
	  F: 2679  (1.44%)
	  C: 2583  (1.39%)
	  G: 2406  (1.29%)
	  P: 2002  (1.07%)
	  B: 1825  (0.98%)
	  K: 1266  (0.68%)
	  V: 1219  (0.65%)
	  ': 1201  (0.64%)
	  ?: 452  (0.24%)
	  ;: 442  (0.24%)
	  !: 373  (0.20%)
	  -: 298  (0.16%)
	  Q: 219  (0.12%)
	  X: 179  (0.10%)
	  [: 116  (0.06%)
	  ]: 112  (0.06%)
	  J: 110  (0.06%)
	  Z: 71  (0.04%)
	  (: 44  (0.02%)
	  ): 43  (0.02%)
	  :: 32  (0.02%)
	  1: 6  (0.00%)
	  ": 1  (0.00%)
	  &: 1  (0.00%)
	  +: 186457

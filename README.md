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
- Percent of characters in the string
- Replace national characters to ASCII equivalents
- Calculating entropy
- Huffman coding

### Usage ###

    --version   show program's version number and exit
    -h, --help  show this help message and exit
    -a          count all chars
    -c          case-sensitivity
    -n          replace national characters to ASCII equivalents
    -f FILE     text file

### Examples ###

    CharFreq.py -f hamlet.txt
    Characters Frequency Analysis
    Author: Lukasz Banasiak
    Count all chars: True
    Case-sensitivity: True
    Replace national characters to ASCII equivalents: False
    
    >>> hamlet.txt
    Char    Count           Percent Hi      Fi      Huffman
    ----------------------------------------------------------------------
            47876           25.565% 1.968   0.511   10
    a       9317            4.975%  4.329   0.249   0010
    e       14722           7.861%  3.669   0.314   1101
    o       10842           5.789%  4.110   0.289   0101
    s       8126            4.339%  4.526   0.217   0000
    t       11073           5.913%  4.080   0.296   0110
    d       4893            2.613%  5.258   0.157   00111
    h       7839            4.186%  4.578   0.209   11110
    i       7657            4.089%  4.612   0.204   11101
    l       5598            2.989%  5.064   0.179   01110
    n       8117            4.334%  4.528   0.217   11111
    r       7638            4.079%  4.616   0.204   11100
    u       4307            2.300%  5.442   0.138   00011
    ,       3001            1.602%  5.964   0.096   011110
    .       3133            1.673%  5.901   0.100   110000
    c       2430            1.298%  6.268   0.091   010000
    f       2497            1.333%  6.229   0.093   010001
    g       2170            1.159%  6.431   0.081   000101
    m       4001            2.136%  5.549   0.128   110011
    w       2647            1.413%  6.145   0.099   010010
    y       3074            1.641%  5.929   0.098   011111
    '       1202            0.642%  7.284   0.051   0011011
    b       1568            0.837%  6.900   0.059   1100010
    k       1092            0.583%  7.422   0.047   0011000
    p       1780            0.950%  6.717   0.067   1100100
    v       1189            0.635%  7.299   0.051   0011010
    A       633             0.338%  8.209   0.030   01001100
    H       892             0.476%  7.714   0.038   11001010
    I       854             0.456%  7.777   0.036   11000111
    T       790             0.422%  7.889   0.034   01001111
    W       485             0.259%  8.593   0.023   00010001
    !       373             0.199%  8.972   0.018   010011100
    -       298             0.159%  9.296   0.016   001100110
    ;       442             0.236%  8.727   0.021   110001101
    ?       452             0.241%  8.695   0.022   110010110
    B       262             0.140%  9.481   0.014   001100100
    E       238             0.127%  9.620   0.013   000100000
    G       250             0.133%  9.549   0.013   000100101
    L       249             0.133%  9.555   0.013   000100100
    M       252             0.135%  9.537   0.013   000100110
    O       376             0.201%  8.960   0.018   010011101
    S       253             0.135%  9.532   0.014   000100111
    C       176             0.094%  10.055  0.010   0100110100
    D       132             0.070%  10.470  0.008   0011001011
    F       201             0.107%  9.864   0.011   1100011000
    K       180             0.096%  10.023  0.011   0100110110
    N       180             0.096%  10.023  0.011   0100110111
    P       236             0.126%  9.632   0.013   1100101111
    R       139             0.074%  10.396  0.008   0011001110
    Y       130             0.069%  10.492  0.008   0011001010
    [       116             0.062%  10.657  0.007   0001000010
    x       179             0.096%  10.031  0.011   0100110101
    Q       112             0.060%  10.707  0.007   11001011100
    ]       112             0.060%  10.707  0.007   11001011101
    j       101             0.054%  10.857  0.006   11000110010
    q       108             0.058%  10.760  0.006   11000110011
    z       72              0.038%  11.345  0.005   00110011110
    (       44              0.023%  12.055  0.003   001100111111
    )       43              0.023%  12.089  0.003   001100111110
    :       32              0.017%  12.515  0.002   000100001101
    U       36              0.019%  12.345  0.002   000100001111
    V       33              0.018%  12.470  0.002   000100001110
    J       9               0.005%  14.345  0.001   0001000011000
    1       7               0.004%  14.707  0.001   00010000110011
    0       1               0.001%  17.515  0.000   0001000011001000
    4       1               0.001%  17.515  0.000   0001000011001001
    6       1               0.001%  17.515  0.000   0001000011001010
    "       1               0.001%  17.515  0.000   00010000110010110
    &       1               0.001%  17.515  0.000   00010000110010111
    ----------------------------------------------------------------------
    +:      187271
    ======================================================================
    H: 4.3127286523
    L: 4.72424988386

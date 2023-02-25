# 50dust.py

# Write a better version of your 42dust.py program
# Your program must have the following properties

# 1. the entropy of each window is centered (N's in the middle of windows)
# 2. has option and default value for window size
# 3. has option and default value for entropy threshold
# 4. has a switch for N-based or lowercase (soft) masking
# 5. works with uppercase or lowercase input files
# 6. works as an executable

# Optional: make the algorithm faster (see 29gcwin.py for inspiration)
# Optional: benchmark your programs with different window sizes using time

# Hint: make a smaller file for testing (e.g. e.coli.fna in the CLI below)

import math, sys, mcb185, argparse

def entropy(probability):
	assert(math.isclose(1.0, sum(probability)))
	h = 0
	for p in probability:
		if p != 0 : h += (p * math.log2(1/p))
	return h

def seqentropy(seq):
	A = seq.count("A")/len(seq)
	C = seq.count("C")/len(seq)
	G = seq.count("G")/len(seq)
	T = seq.count("T")/len(seq)
	return entropy([A,C,G,T])

def seqen(seq):
	A = 0
	C = 0
	G = 0
	T = 0
	for base in seq:
		if base == "A": A += 1
		if base == "C": C += 1
		if base == "G": G += 1
		if base == "T": T += 1
	Ae = A/len(seq)
	Ce = C/len(seq)
	Ge = G/len(seq)
	Te = T/len(seq)
	return entropy([Ae,Ce,Ge,Te])

parser = argparse.ArgumentParser(description="Entropy filtering with inputs")
parser.add_argument('file', type=str, metavar='<path>',
		    help='Input file')
parser.add_argument('-w', required=False, type=int, default = 11,
		    metavar='<int>', help='Optional custom window size (default = 11)')
parser.add_argument('-t', required=False, type=float, default=1.4,
		    metavar='<float>', 
		    help='Optional entropy threshold (default = 1.4)')
parser.add_argument('-s', required=False, action='store_true',
		    help='Base masking for lower case (default = \'N\'')


arg = parser.parse_args()

for defline, seq in  mcb185.read_fasta(arg.file):
	print(defline)
	# seq = seq[:1000]
	startwin = seq[:arg.w]
	A,C,G,T, cc = 0,0,0,0,0
	for base in startwin:
		if base == "A": A += 1
		if base == "C": C += 1
		if base == "G": G += 1
		if base == "T": T += 1
	Ae = A/arg.w
	Ce = C/arg.w
	Ge = G/arg.w
	Te = T/arg.w
	print(seq[:arg.w//2], end="")
	cc += arg.w//2
	if entropy([Ae,Ce,Ge,Te]) < arg.t:
		if arg.s:
			print(seq[arg.w//2].lower(), end="")
			cc += 1
		else: 
			print("N", end="")
			cc += 1
		
	else:
		print(seq[arg.w//2], end="")
		cc += 1
	for i in range(0,len(seq)-arg.w+1):
		if i+arg.w > len(seq)-1: break
		if seq[i] == "A": A -= 1
		if seq[i] == "C": C -= 1
		if seq[i] == "G": G -= 1		
		if seq[i] == "T": T -= 1
		if seq[i+arg.w] == "A": A += 1
		if seq[i+arg.w] == "C": C += 1
		if seq[i+arg.w] == "G": G += 1
		if seq[i+arg.w] == "T": T += 1		
		Ae = A/arg.w
		Ce = C/arg.w
		Ge = G/arg.w
		Te = T/arg.w
		if entropy([Ae,Ce,Ge,Te]) < arg.t:
			if arg.s:
				print(seq[(i+arg.w)-arg.w//2].lower(), end="")
				cc += 1
			else: 
				print("N", end="")
				cc += 1
			
		else:
			print(seq[(i+arg.w)-arg.w//2], end = "")
			cc += 1
		if cc % 60 == 0:
			print("\n",end="")


"""
python3 50dust.py -w 11 -t 1.4 -s e.coli.fna  | head
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGCTTTTcATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTaaaaaaaGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAattaaaattttATTGACTTAGG
TCACTAAATacTTTAACCAATATAGGCATAGCGCACAGACAGAtAaaaaTTACAGAGTAC
ACAacATCCATGAAACGCATTAGCACCACCATTACCAccaccatCACCATTACCACAGGT
AACGGTGCgGGCTGACGCGTACAGGAAACacagaaaaAAGCCCGCACCTGACAGTGCGGG
CTttttttTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AGGCAGggGCaGGTGGCCACCGTCcTCtctgcccCcgcCAAAatcaccaacCACCTGGTG
GCGATGATTGaAAAAacCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA

Timings
win alg1 alg2
11  28.7 25.8
25  30.4 26.1
100 33.2 26.1
200 37.4 25.9
"""

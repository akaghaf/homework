# 41transmembrane.py

# Write a program that predicts which proteins in a proteome are transmembrane

# Transmembrane proteins are characterized by having
#    1. a hydrophobic signal peptide near the N-terminus
#    2. other hydrophobic regions to cross the plasma membrane

# Both the signal peptide and the transmembrane domains are alpha-helices
# Therefore, they do not contain Proline

# Hydrophobicity can be measured by Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot

# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

# Hint: copy mcb185.py to your homework repo and import that
# Hint: create a function for KD calculation
# Hint: create a function for hydrophobic alpha-helix
# Hint: use the same function for both signal peptide and transmembrane
import sys, mcb185

Scores = [["I",4.5],["V",4.2],["L",3.8],["F",2.8],["C",2.5],["M",1.9],
			 ["A",1.8],["G",-0.4],["T",-0.7],["S",-0.8],["W",-0.9],["Y",-1.3],
			 ["P",-10000.6],["H",-3.2],["E",-3.5],["Q",-3.5],["D",-3.5],
			 ["N",-3.5], ["K",-3.9],["R",-4.5]]

def kdcalc(subseq):
	kdtotal = 0
	for aa in subseq:
		for pair in Scores:
			if aa == pair[0]: kdtotal += pair[1]
	
		avg = kdtotal/len(subseq)
	yield avg

def hah(seq, window, threshold):
	alphahelix = False
	for i in range(0, len(seq) - window + 1):
		win = seq[i:i+window]
		for output in kdcalc(win):
			if output >= threshold: 
				alphahelix = True
	return alphahelix
			

for defline, seq in  mcb185.read_fasta(sys.argv[1]):
	if hah(seq[:30], 8, 2.5) == True and hah(seq[30:], 11, 2.0) == True:
		print(defline)



"""
python3 41transmembrane.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
NP_414560.1 Na(+):H(+) antiporter NhaA [Escherichia coli str. K-12 substr. MG1655]
NP_414568.1 lipoprotein signal peptidase [Escherichia coli str. K-12 substr. MG1655]
NP_414582.1 L-carnitine:gamma-butyrobetaine antiporter [Escherichia coli str. K-12 substr. MG1655]
NP_414607.1 DedA family protein YabI [Escherichia coli str. K-12 substr. MG1655]
NP_414609.1 thiamine ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414653.1 protein AmpE [Escherichia coli str. K-12 substr. MG1655]
NP_414666.1 quinoprotein glucose dehydrogenase [Escherichia coli str. K-12 substr. MG1655]
NP_414695.1 iron(III) hydroxamate ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414699.1 PF03458 family protein YadS [Escherichia coli str. K-12 substr. MG1655]
NP_414717.2 CDP-diglyceride synthetase [Escherichia coli str. K-12 substr. MG1655]
...
"""

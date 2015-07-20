# codon.py
# Ashkan Bigdeli
#
#Assignment 2: Question 2
#
# Match the input to a codon
# The function isStop will determine the stop codon
# The function isCodon will determine any codon

# Are we debugging?
DEBUG = True


# To save time I used this dictionary from day2.txt
# and will check for the codons presence in the list.
# Dictionary holding the code to life: Codon to Amino Acid map
code = {     'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
             'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
             'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': '*',
             'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
             'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
             'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
             'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
             'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
             'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
             'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
             'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
             'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R',
             'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
             'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
             'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
             'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'
         }
         
# This method will take the user's input and compare to each listing
# in the dictionary returning true if it is present.
def isCodon (bases):
    for i in xrange (0, len(code) ):
        if (bases in code ):
            return True
        return False

def isStop (bases):
    if bases in ("taa", "tag", "tga"):
        return True
    return False
    
    
def main(): 
    # I opted to do this using user input. convert to a standard lowercase
    # for string checking. 
    bases = raw_input ("Enter your 3 bases to perform the codon check: " )
    print (bases)
    bases = bases.lower()
    # execute function to test if this is a codon
    if (isCodon(bases)):
        print(bases + " is a codon!")
    else:
        print(bases + " is not a valid codon.")
    
    # execute the method to check if stop codon
    if (isStop(bases)):
        print(bases + " is a stop codon!")
    else:
        print(bases + " is not a stop codon")
        
main() 
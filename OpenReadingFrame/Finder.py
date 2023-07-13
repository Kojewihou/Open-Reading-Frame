from re import finditer

from utils import reverse_complement, ORF

def FindORF(sequence, minlength=50):

    """Takes a string DNA/RNA sequence and identifies all ORFs present above a set length.

    Yields:
        ORF: an open reading frame object containing all data of any identified open reading frame
    """

    DNA = "T" in sequence
    
    if ("ATG" if DNA else "AUG") in sequence:
        for start_codon in finditer("ATG" if DNA else "AUG",sequence):
            partial_read = sequence[start_codon.start():]
            for stop_codon in finditer("TAA|TAG|TGA" if DNA else "UAA|UAG|UGA",partial_read):
                read = partial_read[:stop_codon.end()]
                if len(read) % 3 == 0:
                    if len(read) >= minlength:
                        yield ORF(start_codon.start(), stop_codon.end()+start_codon.start(),seq= read ,reverse=False)
                    break
            

    sequence = reverse_complement(sequence)

    if ("ATG" if DNA else "AUG") in sequence:
        for start_codon in finditer("ATG" if DNA else "AUG",sequence):
            partial_read = sequence[start_codon.start():]
            for stop_codon in finditer("TAA|TAG|TGA" if DNA else "UAA|UAG|UGA",partial_read):
                read = partial_read[:stop_codon.end()]
                if len(read) % 3 == 0:
                    if len(read) >= minlength:
                        yield ORF(start_codon.start(), stop_codon.end()+start_codon.start(),seq= read ,reverse=True)
                    break
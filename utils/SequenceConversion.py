def complement(seq):
    DNA = False
    if "T" in seq:
        DNA = True
        
    mapping = str.maketrans(("ATGC" if DNA else "AUGC"),("TACG" if DNA else "UACG"))
    return seq.translate(mapping)

def reverse_complement(seq):
    DNA = False
    if "T" in seq:
        DNA = True
    seq = seq[::-1]
    mapping = str.maketrans(("ATGC" if DNA else "AUGC"),("TACG" if DNA else "UACG"))
    return seq.translate(mapping)

def transcription(seq):
    if "T" in seq:
        mapping = str.maketrans("T","U")
        return seq.translate(mapping)

def reverse_transcription(seq):
    if "U" in seq:
        mapping = str.maketrans("U","T")
        return seq.translate(mapping)



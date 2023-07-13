# No Global Imports

from test_sequence import test_DNA_sequence
from OpenReadingFrame import FindORF, PlotORFs

ORFs = FindORF(test_DNA_sequence)

PlotORFs(test_DNA_sequence, ORFs)
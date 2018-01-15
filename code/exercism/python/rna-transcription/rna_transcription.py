nucl_dict = {
 'G': 'C',
 'C': 'G',
 'T': 'A',
 'A': 'U'
}

def to_rna(dna_strand):
 result = []
 for n in dna_strand: 
  if n in nucl_dict:
   result.append(nucl_dict[n])
  else: 
   raise ValueError
 return ''.join(result)


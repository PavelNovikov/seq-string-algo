from seq_string_algo.edit_distance import edit_distance
from seq_string_algo.alphabet import Alphabet


seq1 = "elepant"
seq2 = "elephang"
alphabet = Alphabet(set(seq1).union(set(seq2)))



arr1 = alphabet.encode(seq1)
arr2 = alphabet.encode(seq2)
print edit_distance(arr1, arr2, insertion_cost = 0.1, deletion_cost = 0.1)

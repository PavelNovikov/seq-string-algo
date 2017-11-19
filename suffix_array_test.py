from seq_string_algo.suffix_array import build_order
from seq_string_algo.alphabet import Alphabet




seq = "broom_from_chrome"
alphabet = Alphabet(seq)



arr = alphabet.encode(seq)
order = build_order(arr)
for index in order:
	print "".join(alphabet.decode(arr[index:]))


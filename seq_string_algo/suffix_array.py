from ._suffix_array import lib, ffi
def build_order(sequence_of_longs):
	arr = ffi.new("long[%d]" % len(sequence_of_longs))
	order = ffi.new("long[%d]" % len(sequence_of_longs))
	for i in xrange(len(arr)):
		arr[i] = sequence_of_longs[i]
	
	lib.find_ordering(arr, len(sequence_of_longs), order)
	result = []
	for i in xrange(len(arr)):
		result.append(order[i])
	return result







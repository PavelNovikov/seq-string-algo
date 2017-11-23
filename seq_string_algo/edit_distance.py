from ._edit_distance import lib, ffi


def edit_distance(sequence_of_longs1, sequence_of_longs2, insertion_cost = 1.0, deletion_cost = 1.0, replacement_cost = 1.0):
	first = ffi.new("long[%d]" % len(sequence_of_longs1))
	second = ffi.new("long[%d]" % len(sequence_of_longs2))
	previous_costs = ffi.new("double[%d]" % (len(sequence_of_longs2) + 1))
	last_costs = ffi.new("double[%d]" % (len(sequence_of_longs2) + 1))
	for i in xrange(len(first)):
 		first[i] = sequence_of_longs1[i]
	for i in xrange(len(second)):
		second[i] = sequence_of_longs2[i]

        return lib.edit_distance(first,
        len(first),
        second,
        len(second),
        last_costs,
        previous_costs,
        insertion_cost,
        deletion_cost,
        replacement_cost)

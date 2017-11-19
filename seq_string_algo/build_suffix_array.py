import cffi
ffi = cffi.FFI()


#x = [1,2,3]

ffi.cdef("""
	struct arr_pos;
""")

ffi.cdef("""
	void find_ordering(long* sequence, long seq_length, long* order);
	int compare_remainders_lexicographically(const void * a, const void * b);
""")

ffi.set_source("seq_string_algo._suffix_array", """
	#include <stdlib.h>
	struct arr_pos
	{
		long* position; 
		long remainder_length;
	};
	int compare_remainders_lexicographically(const void * a, const void * b){
	 	struct arr_pos* s1 = (struct arr_pos*)(a);
		struct arr_pos* s2 = (struct arr_pos*)(b);
		long compared_length;
		if (s1->remainder_length < s2->remainder_length) {
			compared_length = s1->remainder_length;
		} else {
			compared_length = s2->remainder_length;
		}
		for (long i = 0; i < compared_length; i++) {
			if (s1->position[i] > s2->position[i]){
				return 1;
			} else if (s1->position[i] < s2->position[i]) {
				return -1;
			}
		}
		return s1->remainder_length - s2->remainder_length;
	}
	static void find_ordering(long* sequence, long seq_length, long* order){
		struct arr_pos positions[seq_length];
		for (long i = 0; i < seq_length; i++) {
			positions[i] = (struct arr_pos){.position = &(sequence[i]), .remainder_length = seq_length - i};
		}
		qsort(positions, seq_length, sizeof(struct arr_pos), compare_remainders_lexicographically);
		for (long i = 0; i < seq_length; i++) 
		{
			order[i]  = positions[i].position - sequence;
		}
		
	}
""")


ffi.compile(verbose=True)


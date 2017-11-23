import cffi
ffi = cffi.FFI()


#x = [1,2,3]


ffi.cdef("""
	double edit_distance(long* first,
        long first_length,
        long* second,
        long second_length,
        double* last_costs,
        double* previous_costs,
        double insertion_cost,
        double deletion_cost,
        double replacement_cost
        );
""")

ffi.set_source("seq_string_algo._edit_distance", """
	#include <limits.h>
	double edit_distance(long* first,
        long first_length,
        long* second,
        long second_length,
        double* last_costs,
        double* previous_costs,
        double insertion_cost,
        double deletion_cost,
        double replacement_cost
        ) {
            previous_costs[0] = 0;
            for (long i = 1; i <= second_length; i++) {
                previous_costs[i] = previous_costs[i - 1] + insertion_cost;
            }
            for (long i = 0; i < first_length; i++) {
                last_costs[0] = previous_costs[0] + deletion_cost;
                for (long j = 1; j <= second_length; j++) {
                    double cost = LONG_MAX;
                    if (last_costs[j - 1] + insertion_cost < cost) {
                        cost = last_costs[j - 1] + insertion_cost;
                    }
                    if (first[i] == second[j - 1]) {
                        if (previous_costs[j - 1] < cost) {
                            cost = previous_costs[j - 1];
                        }

                    } else {
                        if (previous_costs[j - 1] + replacement_cost < cost) {
                            cost = previous_costs[j - 1] + replacement_cost;
                        }
                    }
                    last_costs[j] = cost;
                }
                for (long j = 0; j < second_length; j++) {
                    previous_costs[j] = last_costs[j];
                }
            }

            return last_costs[second_length];

        }
""")


ffi.compile(verbose=True)

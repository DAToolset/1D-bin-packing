# import random
from binpackp import NumberBin, Fit


def print_result(fit_name, fit_result):
    print(fit_name + " Result: ", fit_result)
    for bin in fit_result.bins:
        print(bin)
    print()

# bin_size = random.randint(10,100)
# fit_these = [random.randint(1, bin_size) for _ in range(1000)]

# print(fit_these)

bin_size = 80
fit_these = [26, 57, 18, 8, 45, 16, 22, 29, 5, 11, 8, 27, 54, 13, 17, 21, 63, 14, 16, 45, 6, 32, 57, 24, 18, 27, 54, 35, 12, 43, 36, 72, 14, 28, 3, 11, 46, 27, 42, 59, 26, 41, 15, 41, 68]
# print(fit_these)

# generic_results = Fit.fit(NumberBin, bin_size, fit_these)
next_fit_results = Fit.nf(NumberBin, bin_size, fit_these)
first_fit_results = Fit.ff(NumberBin, bin_size, fit_these)
worst_fit_result = Fit.wf(NumberBin, bin_size, fit_these)
best_fit_result = Fit.bf(NumberBin, bin_size, fit_these)

# sorted_next_fit_results = Fit.nfd(NumberBin, bin_size, fit_these) # not implemented
sorted_first_fit_results = Fit.ffd(NumberBin, bin_size, fit_these)
sorted_worst_fit_result = Fit.wfd(NumberBin, bin_size, fit_these)
sorted_best_fit_result = Fit.bfd(NumberBin, bin_size, fit_these)

print_result("Next Fit", next_fit_results)
print_result("First Fit", first_fit_results)
print_result("Worst Fit", worst_fit_result)
print_result("Best Fit", best_fit_result)

# print_result("Next Fit With Sort", next_fit_results) # not implemented
print_result("First Fit With Sort", sorted_first_fit_results)
print_result("Worst Fit With Sort", sorted_worst_fit_result)
print_result("Best Fit With Sort", sorted_best_fit_result)



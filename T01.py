import math
import matplotlib.pyplot as plt

n = [x for x in range(1, 21)]

# Store functions and their labels
functions = [
    ([math.log(x) for x in n], r'$f_1(n) = \log n$'),
]

sorted_functions = sorted(functions, key=lambda x: x[0][-1] if x[0][-1] is not None else -math.inf, reverse=True)
for func, label in sorted_functions:
    plt.plot(n[:len(func)], func, label=label)

# Customize the plot
plt.yscale('log')  # Use logarithmic scale for better visualization
plt.xlabel('$n$')
plt.ylabel('$f(n)$ / log')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save as a borderless PDF
plt.savefig('functions-compared.pdf', format='pdf', bbox_inches='tight')
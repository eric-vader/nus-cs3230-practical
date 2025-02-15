def poly_mult_bruteforce(A, B):
    # A: Coefficients [a0, a1, ..., a_n] for A(x) = a0 + a1*x + ... + a_n*x^n.
    # B: Coefficients [b0, b1, ..., b_n] for B(x) = b0 + b1*x + ... + b_n*x^n.
    
    n = len(A) - 1  # Degree of the polynomials (assumed equal)
    result = [0] * (2 * n + 1)  # Result will have (2n + 1) coefficients
    
    for i in range(2 * n + 1):
        for j in range(max(0, i - n), min(i, n) + 1):
            result[i] += A[j] * B[i - j]
    return result

def poly_mult_dc(A, B):
    raise NotImplementedError

if __name__ == "__main__":
    # Test Case: Multiply
    #   A(10) = 352 = 3*10^2 + 5*10 + 2, i.e. A(x) = 3x^2 + 5x + 2, represented as [2, 5, 3]
    #   B(10) = 221 = 2*10^2 + 2*10 + 1, i.e. B(x) = 2x^2 + 2x + 1, represented as [1, 2, 2]
    A = [2, 5, 3]
    B = [1, 2, 2]
    
    # Using brute force:
    result_brute = poly_mult_bruteforce(A, B)
    assert result_brute == [2, 9, 17, 16, 6], f"Brute force expected [2, 9, 17, 16, 6], got {result_brute}"
    print("Brute force result:", result_brute)
    
    # Using divide and conquer:
    result_dc = poly_mult_dc(A, B)
    assert result_dc == [2, 9, 17, 16, 6], f"DC expected [2, 9, 17, 16, 6], got {result_dc}"
    print("Divide and Conquer result:", result_dc)

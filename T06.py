import numpy as np

def freivalds(A, B, C, k=10):
    raise NotImplementedError

# -----------------------
# Main function
# -----------------------
if __name__ == '__main__':
    np.random.seed(42)  # For reproducibility

    test_cases = [
        # Small correct multiplication
        {
            "A": np.array([[1, 2], [3, 4]]),
            "B": np.array([[2, 0], [1, 2]]),
            "C": np.dot(np.array([[1, 2], [3, 4]]), np.array([[2, 0], [1, 2]])),
            "expected": True
        },
        # Small incorrect multiplication
        {
            "A": np.array([[1, 2], [3, 4]]),
            "B": np.array([[2, 0], [1, 2]]),
            "C": np.array([[5, 5], [11, 13]]),  # Incorrect product
            "expected": False
        },
        # Large correct multiplication
        {
            "A": np.random.randint(0, 10, (5, 5)),
            "B": np.random.randint(0, 10, (5, 5)),
            "C": None,  # Will compute in the loop
            "expected": True
        },
        # Large incorrect multiplication (with slight modification)
        {
            "A": np.random.randint(0, 10, (5, 5)),
            "B": np.random.randint(0, 10, (5, 5)),
            "C": None,  # Will compute and modify in the loop
            "expected": False
        },
    ]
    
    for idx, case in enumerate(test_cases):
        A, B = case["A"], case["B"]
        C = np.dot(A, B) if case["C"] is None else case["C"]
        
        # Introduce an error for the incorrect large case
        if idx == 3:
            C[0, 0] += 1

        result = freivalds(A, B, C)
        print((f"Test {idx+1}", result == case["expected"]))

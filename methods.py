import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

TOLERANCE = 0.00001
MAX_ITERATIONS = 1000


def is_diagonally_dominant(matrix):
    n = len(matrix)
    for i in range(n):
        diagonal = abs(matrix[i][i])
        row_sum = sum(abs(matrix[i][j]) for j in range(n) if j != i)
        if diagonal <= row_sum:
            return False
    return True


def make_diagonally_dominant(matrix, vector):
    n = len(matrix)
    mat = [row[:] for row in matrix]
    vec = [row[:] for row in vector]

    for col in range(n):
        max_row = col
        max_val = abs(mat[col][col])

        for row in range(col + 1, n):
            if abs(mat[row][col]) > max_val:
                max_val = abs(mat[row][col])
                max_row = row

        if max_row != col:
            mat[col], mat[max_row] = mat[max_row], mat[col]
            vec[col], vec[max_row] = vec[max_row], vec[col]

    return mat, vec


def check_and_fix_dominance(matrix, vector):
    """
    Helper function shared by both methods.
    Returns: (mat, vec, is_dominant, was_fixed)
    """
    if is_diagonally_dominant(matrix):
        return matrix, vector, True, False

    mat, vec = make_diagonally_dominant(matrix, vector)

    if is_diagonally_dominant(mat):
        print("Row swapping (Pivoting) performed - matrix is now diagonally dominant.")
        return mat, vec, True, True
    else:
        print("Warning: Could not achieve diagonal dominance even after row swapping.")
        return mat, vec, False, True


def jacobi(matrix, vector):
    print("\nJacobi Method")

    mat, vec, dominant, _ = check_and_fix_dominance(matrix, vector)
    n = len(mat)

    x = [0.0] * n
    converged = False
    iteration = 0

    for iteration in range(1, MAX_ITERATIONS + 1):
        x_new = [0.0] * n

        for i in range(n):
            sigma = sum(mat[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (vec[i][0] - sigma) / mat[i][i]

        results_str = ", ".join(f"x{i+1}={x_new[i]:.6f}" for i in range(n))
        print(f"Iteration {iteration}: {results_str}")

        if max(abs(x_new[i] - x[i]) for i in range(n)) < TOLERANCE:
            converged = True
            x = x_new
            break

        x = x_new

    print(f"\nTotal iterations: {iteration}")

    if converged:
        if not dominant:
            print("Although there is no diagonal dominance, the results are:", end=" ")
        else:
            print("Solution:", end=" ")
        for i in range(n):
            print(f"x{i+1}={x[i]:.6f}", end="  ")
        print()
    else:
        print("The system does not converge.")


def gauss_seidel(matrix, vector):
    print("\nGauss-Seidel Method")

    mat, vec, dominant, _ = check_and_fix_dominance(matrix, vector)
    n = len(mat)

    x = [0.0] * n
    converged = False
    iteration = 0

    for iteration in range(1, MAX_ITERATIONS + 1):
        x_old = x[:]

        for i in range(n):
            sigma = sum(mat[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (vec[i][0] - sigma) / mat[i][i]

        results_str = ", ".join(f"x{i+1}={x[i]:.6f}" for i in range(n))
        print(f"Iteration {iteration}: {results_str}")

        if max(abs(x[i] - x_old[i]) for i in range(n)) < TOLERANCE:
            converged = True
            break

    print(f"\nTotal iterations: {iteration}")

    if converged:
        if not dominant:
            print("Although there is no diagonal dominance, the results are:", end=" ")
        else:
            print("Solution:", end=" ")
        for i in range(n):
            print(f"x{i+1}={x[i]:.6f}", end="  ")
        print()
    else:
        print("The system does not converge.")

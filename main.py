from methods import jacobi, gauss_seidel

matrixA = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
vectorB = [[2], [6], [5]]

print("Choose a method to solve the system of equations:")
print("1 - Jacobi")
print("2 - Gauss-Seidel")
print("3 - Both methods")

choice = input("Choice (1/2/3): ").strip()

if choice == "1":
    jacobi(matrixA, vectorB)
elif choice == "2":
    gauss_seidel(matrixA, vectorB)
elif choice == "3":
    jacobi(matrixA, vectorB)
    gauss_seidel(matrixA, vectorB)
else:
    print("Invalid choice.")

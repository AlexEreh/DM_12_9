def calc_det(matrix: [[int]]):
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if size == 3:
        return (
                matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
                matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
                matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
        )
    else:
        determinant = 0
        for j in range(size):
            sub_matrix = []
            for i in range(1, size):
                sub_matrix.append(matrix[i][:j] + matrix[i][j + 1:])
            sub_matrix_det = calc_det(sub_matrix)
            determinant += (-1) ** j * matrix[0][j] * sub_matrix_det
        return determinant


def main():
    matrix = []
    with open('input.txt', 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            matrix.append(row)
    determinant = calc_det(matrix)
    with open('output.txt', 'w') as file:
        file.write(str(determinant))


if __name__ == '__main__':
    main()

# импорт библиотеки для решения алгебраических линейных уравнений
import numpy as np

class LinearSystem:
    def __init__(self, A, B):
        """
        декларируем матрицу коэффициентов A и вектор свободных членов B
        A - это матрица с коэффициентами перед переменными в системе уравнений
        B - вектор результатов
        """
        self.A = np.array(A, dtype=float)
        self.B = np.array(B, dtype=float)

    def solve(self):
        """
        решаем систему уравнений A * X = B с использованием numpy
        возвращаем X, который содержит значения для переменных
        если решение не может быть найдено,
        выводим соответствующее сообщение
        """
        try:
            # с помощью numpy и linalg решаем и выводим X
            X = np.linalg.solve(self.A, self.B)
            return X
        except np.linalg.LinAlgError:
            # если нет решения, выводим ошибку
            return "нет решения/бесконечность"

    def gaussian_elimination(self):
        """
        решаем систему уравнений с использованием метода Гаусса
        возвращаем X, который содержит значения для переменных
        """
        n = len(self.B)
        # создаем расширенную матрицу
        augmented_matrix = np.hstack((self.A, self.B.reshape(-1, 1)))

        # прямой ход гаусса
        for i in range(n):
            # нормализуем строку
            augmented_matrix[i] = augmented_matrix[i] / augmented_matrix[i, i]
            for j in range(i + 1, n):
                augmented_matrix[j] -= augmented_matrix[j, i] * augmented_matrix[i]

        # обратный ход
        X = np.zeros(n)
        for i in range(n - 1, -1, -1):
            X[i] = augmented_matrix[i, -1] - np.sum(augmented_matrix[i, i + 1:n] * X[i + 1:n])

        return X

    def compare_solutions(self):
        """
        сравниваем решения, полученные с использованием numpy и методом Гаусса
        возвращаем оба решения
        """
        numpy_solution = self.solve()
        gaussian_solution = self.gaussian_elimination()

        return numpy_solution, gaussian_solution

    def display_solution(self, solution):
        """
        выводим решение системы если X - это массив,
        иначе выводим ошибку
        """
        if isinstance(solution, np.ndarray):
            print("| решение:", solution)
        else:
            print(f"⭕ ошибка! {solution}")

# здесь матрица систем
systems = [
    # 1
    ([
        [2, 3, -1, 0, 1],
        [0, 1, 0, -1, 1],
        [3, 0, 0, 10, -1],
        [0, 1, -5, -1, 0],
        [1, -1, 0, 0, 0]
    ], 
    [16, 12, 9, 15, 2]),

    # 2
    ([
        [2.32, 5.7, -0.8],
        [3.5, 2.7, -5.3],
        [1.7, 2.3, -1.8]
    ], 
    [6.49, 19.90, 5.09]),

    # 3
    ([
        [8.30, 2.62, 4.10, 1.90],
        [3.92, 8.45, 7.78, 2.46],
        [1.70, 7.12, 9.43, -2.15],
        [2.21, 3.65, 1.69, 6.99]
    ], 
    [10.65, -12.21, -15.45, 8.35]),

    # 4
    ([
        [0.30, 55.4, -6, 0],
        [5.09, -3.1, -7.2, 0],
        [5.11, 6.21, 5.43, -6.3],
        [2.21, 5.12, 2.69, 5.64]
    ], 
    [307.45, 22.753, 117.88, 18.781]),

    # 5
    ([
        [12, 5.4, -1.6],
        [9, -6.1, -5.3],
        [7.1, 2, -4.3]
    ], 
    [102.74, 117.88, 39.12]),

    # 6
    ([
        [7.8, 5.4, 19.74],
        [11.1, 6.61, 15.43],
        [6.21, 9.2, 5.43]
    ], 
    [0, 41.1, 57.09]),

    # 7
    ([
        [3, 4, -6],
        [59, 3, 45],
        [11, 21, 54]
    ], 
    [133, 184, 407]),

    # 8
    ([
        [17.8, 0.4, -51.78],
        [1, 6.1, -5.3],
        [6.21, -2.2, -106.23]
    ], 
    [0, 321.2, 1209]),

    # 9
    ([
        [7, -5.4, 0],
        [15, -32, -1.4],
        [7, 3, -3]
    ], 
    [685.12, 1462.72, 5605.8]),

    # 10
    ([
        [7.8, 5.4, 0],
        [14, 15, 0],
        [5.21, 56.2, 5]
    ], 
    [28.308, 128.6, 95.2019])
]

# цикл для решения уравнений
for i, (A, B) in enumerate(systems, 1):
    # передаем данные в класс
    system = LinearSystem(A, B)
    
    # сравниваем решения с numpy и гауссом
    numpy_solution, gaussian_solution = system.compare_solutions()
    
    # выводим результаты
    print(f"| система уравнений {i}:")
    print("решение с использованием numpy:")
    system.display_solution(numpy_solution)
    print("решение с использованием метода гаусса:")
    system.display_solution(gaussian_solution)
    print("-" * 70 + "|")
class Square:
    matrix = [['a', 'b', 'c', 'd'],
              ['e', 'f', 'g', 'h'],
              ['i', 'j', 'k', 'l'],
              ['m', 'n', 'p', 'r']]

    def show_matrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end=' ')
            print()


# def main():
#     s = Square()
#     s.show_matrix()
#
#
# main()

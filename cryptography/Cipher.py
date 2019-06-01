import data.Point as Point
import data.Square as Square


class Cipher:
    def __init__(self):
        self.square = Square.Square()

    def encode_v3(self, text):
        # 4. Jeśli ciąg znaków zawierać będzie nieparzystą liczbę znaków, należy uzupełnić go literą X.
        if len(text) % 2 == 1:
            text = text + "x"

        # 4. Jeśli litery p i q są identyczne, należy wstawić pomiędzy nie literę X
        new_text = text
        idx = 0
        for i, c in enumerate(text):
            if i != len(text) - 1 and c == text[i+1]:
                new_text = new_text[:i+1+idx] + "x" + new_text[i+1+idx:]
                idx += 1

        # 3. Jeśli p i q są w różnych wierszach i kolumnach, to tworzą narożniki prostokąta wewnątrz kwadratu szyfrującego.
        # Litery c i d należy odczytać z pozostałych dwóch narożników prostokąta, przy czym litera c powinna być w tej samej kolumnie co litera p.
        encode_text = self.transform_text(new_text)

        return encode_text

    def decode(self, text):

        decode_text = self.transform_text(text)

        return decode_text.replace("x", "")

    def find_element(self, el):
        for i in range(len(self.square.matrix)):
            for j in range(len(self.square.matrix[i])):
                if self.square.matrix[i][j] == el:
                    return Point.Point(i, j)

        return False

    def transform_text(self, new_text):
        encode_text = ""
        for i, c in enumerate(new_text):
            if i % 2 == 0 and i != len(new_text) - 1:
                if new_text[i+1] == " " or new_text[i] == " ":
                    encode_text = encode_text + new_text[i] + new_text[i+1]
                else:
                    if self.find_element(new_text[i]) != False and self.find_element(new_text[i + 1]) != False:
                        point_first = self.find_element(new_text[i])
                        point_second = self.find_element(new_text[i+1])
                        encode_text = encode_text + self.square.matrix[point_second.i][point_first.j]
                        encode_text = encode_text + self.square.matrix[point_first.i][point_second.j]
                    else:
                        encode_text = encode_text + new_text[i] + new_text[i+1]

        return encode_text

# def main():
#     c = Cipher()
#     s = c.encode("ala ma kota")
#     print(s)
#
#
# main()
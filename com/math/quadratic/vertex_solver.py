from com.math.fraction.Fraction import Fraction


class VertexSolver:
    def __init__(self, h: int, k: int, x: int, y: int):
        self.h = int(h)
        self.k = int(k)
        self.x = int(x)
        self.y = int(y)

    def solve(self):
        print("Vertex: " + "(" + str(self.h) + ", " + str(self.k) + ")")
        print("Point: " + "(" + str(self.x) + ", " + str(self.y) + ")" + "\n")

        steps = []
        # Write out vertex form
        equation = "y = a(x"
        if self.h < 0:
            equation += " + " + str(self.h * -1) + ")^2"
        else:
            equation += " - " + str(self.h) + ")^2"

        if self.k < 0:
            equation += " - " + str(self.k * -1)
        else:
            equation += " + " + str(self.k)
        steps.append(equation)

        # Sub in x and y
        equation = str(self.y) + " = a(" + str(self.x)
        if self.h < 0:
            equation += " + " + str(self.h * -1) + ")^2"
        else:
            equation += " - " + str(self.h) + ")^2"

        if self.k < 0:
            equation += " - " + str(self.k * -1)
        else:
            equation += " + " + str(self.k)
        steps.append(equation)

        # Isolate a
        equation = "0 ="
        if self.x - self.h == 0:
            steps.append("a is undefined")
            for step in steps:
                print(step)
        elif (self.x - self.h) ** 2 == 1:
            equation += " a"
            if self.k - self.y > 0:
                equation += " + " + str(self.k - self.y)
            else:
                equation += " - " + str((self.k - self.y) * -1)
            steps.append(equation)

            a = self.y - self.k
            equation = "a = " + Fraction(a, 1).simplify().to_str()
            steps.append(equation)
            for step in steps:
                print(step)
        else:
            equation += " " + str((self.x - self.h) ** 2) + "a"
            if self.k - self.y > 0:
                equation += " + " + str(self.k - self.y)
            else:
                equation += " - " + str((self.k - self.y) * -1)
            steps.append(equation)

            # a = (self.y - self.k) / (self.x - self.h) ** 2
            equation = "a = " + Fraction((self.y - self.k), (self.x - self.h) ** 2).simplify().to_str()
            steps.append(equation)
            for step in steps:
                print(step)

if __name__ == "__main__":
    # Test code
    v = VertexSolver(-2, 3, 4, 1)
    v.solve()

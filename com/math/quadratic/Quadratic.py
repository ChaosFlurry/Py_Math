

class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.vertex_x = b * -1 / 2 * a
        self.vertex_y = self.f(self.vertex_x)
        self.discriminant = b ** 2 - 4 * a * c
        self.y_intercept = c
        if self.discriminant == 0:
            self.x_intercepts = [0]
        elif self.discriminant > 0:
            pos_x = (-b + self.discriminant ** 0.5) / 2 * a
            neg_x = (-b - self.discriminant ** 0.5) / 2 * a
            self.x_intercepts = [pos_x, neg_x]
        else:
            self.x_intercepts = []

    @classmethod
    def from_user_input(cls):
        pass

    def to_str(self):
        quadratic = ""
        if self.a == 1:
            quadratic += "x^2"
        elif self.a == -1:
            quadratic += "-x^2"
        elif self.a != 0:
            quadratic += str(self.a) + "x^2"

        if self.b == 1:
            quadratic += "+" + str(self.b) + "x"
        elif self.b == -1:
            quadratic += "-" + str(self.b) + "x"
        elif self.b > 1:
            quadratic += "+" + str(self.b) + "x"
        elif self.b < 1:
            quadratic += str(self.b) + "x"

        if self.c == 1:
            quadratic += "+1"
        elif self.c == -1:
            quadratic += "-1"
        elif self.c > 1:
            quadratic += "+" + str(self.c)
        elif self.c < 0:
            quadratic += str(self.c)

        if quadratic[0] == "+":
            quadratic = quadratic[1:]

        if len(quadratic) == 0:
            quadratic = str(0)

        return quadratic

    def details(self):
        print(self.to_str())
        print("Vertex: " + "(" + str(self.vertex_x) + ", " + str(self.vertex_y) + ")")
        print("y-intercept: " + str(self.y_intercept))

        intercepts = ""
        for i in self.x_intercepts:
            intercepts += str(i) + ", "
        if intercepts[-2:] == ", ":
            intercepts = intercepts[0:-2]
        if len(intercepts) == 0:
            intercepts = "None"
        print("x-intercepts: " + intercepts)

    def f(self, x):
        return self.a * x ** 2 + self.b * x + self.c


if __name__ == "__main__":
    x = Quadratic(-1, 2, 3)
    x.details()

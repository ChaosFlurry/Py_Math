from math import atan, degrees, radians, sin, cos
from decimal import Decimal
import re


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = (x ** 2 + y ** 2) ** 0.5
        if x == 0 or y == 0:
            self.angle = 0
        else:
            self.angle = degrees(atan(y / x))
        # Correcting negative angles
        if x < 0 and y < 0:
            self.angle = degrees(atan(y / x)) + 180
        if x < 0 and y > 0:
            self.angle = degrees(atan(y / x)) + 180
        if x > 0 and y < 0:
            self.angle = 360 - degrees(atan(y / x)) * -1

        if self.angle >= 360:
            self.angle %= 360

    @classmethod
    def from_angle(cls, distance, angle):
        if angle < 0:
            angle = 360 - angle * -1
        return cls(distance * cos(radians(angle)), distance * sin(radians(angle)))

    @classmethod
    def from_user_input(cls, mode="angle"):
        # TODO handle user input (if user gives invalid value)
        if mode is "angle":
            distance = float(input("Distance: "))
            angle = input("Angle: ")
            absolute_angle = re.compile("^(-?\d+\.?\d*)$")
            relative_angle = re.compile("^(-?\d+\.?\d*)? ?((?:[NS] of [EW])|(?:[EW] of [NS])|(?:[NSEW]))$")

            if relative_angle.match(angle):
                cardinal_direction = relative_angle.match(angle).group(2)

                # if cardinal_direction is N, S, E, or W
                if len(cardinal_direction) == 1:
                    relative_angle_direction = 0
                else:
                    relative_angle_direction = Decimal(relative_angle.match(angle).group(1))
                angle = Vector.to_std_pos_angle(relative_angle_direction, cardinal_direction)
            elif absolute_angle.match(angle):
                angle = float(angle)
            else:
                # invalid input
                pass

            # formatting
            print("")
            return Vector.from_angle(distance, angle)
        if mode is "component":
            x = float(input("Horizontal component: "))
            y = float(input("Vertical component: "))

            # formatting
            print("")
            return Vector(x, y)

    def details(self):
        # Very minor calculation errors due to floating-point math, angle values may be differ
        print("x: " + str(round(Decimal(self.x), 2)))
        print("y: " + str(round(Decimal(self.y), 2)))
        print("distance: " + str(round(Decimal(self.distance), 2)))
        print("angle: " + str(round(Decimal(self.angle), 2)) + "°\n")

        print(str(round(Decimal(self.distance), 2)) + " " + Vector.to_relative_angle(round(Decimal(self.angle), 2)) + "\n")

    @staticmethod
    def add(v1, v2):
        return Vector(v1.x + v2.x, v1.y + v2.y)

    @staticmethod
    def subtract(v1, v2):
        return Vector(v1.x - v2.x, v1.y - v2.y)

    @staticmethod
    def to_std_pos_angle(angle, relative_of):
        angle %= 360
        if relative_of == "E":
            angle = 0
            return angle
        elif relative_of == "N":
            angle = 90
            return angle
        elif relative_of == "W":
            angle = 180
            return angle
        elif relative_of == "S":
            angle = 270
            return angle
        elif relative_of == "N of E":
            return angle
        elif relative_of == "E of N":
            return 90 - angle
        elif relative_of == "W of N":
            return 90 + angle
        elif relative_of == "N of W":
            return 180 - angle
        elif relative_of == "S of W":
            return 180 + angle
        elif relative_of == "W of S":
            return 270 - angle
        elif relative_of == "E of S":
            return 270 + angle
        elif relative_of == "S of E":
            return 360 - angle

    @staticmethod
    def to_relative_angle(angle):
        angle %= 360
        """
        Positive angles:
        0 to 45: N of E
        45 to 90: E of N
        90 to 135: W of N
        135 to 180: N of W
        180 to 225: S of W
        225 to 270: W of S
        270 to 315: E of S
        315 to 360: S of E

        Negative angles:
        0 to -45: S of E
        -45 to -90: E of S
        -90 to -135: W of S
        -135 to -180: S of W
        -180 to -225: N of W
        -225 to -270: W of N
        -270 to 315: E of N
        -315 to 360: N of E
        """

        if angle >= 0:
            if angle == 0:
                return "E"
            elif angle == 90:
                return "N"
            elif angle == 180:
                return "W"
            elif angle == 270:
                return "S"

            if 0 < angle <= 45:
                return str(angle) + "° N of E"
            elif 45 < angle < 90:
                return str(90 - angle) + "° E of N"
            elif 90 < angle < 135:
                return str(angle - 90) + "° W of N"
            elif 135 <= angle < 180:
                return str(180 - angle) + "° N of W"
            elif 180 < angle <= 225:
                return str(angle - 180) + "° S of W"
            elif 225 < angle < 270:
                return str(270 - angle) + "° W of S"
            elif 270 < angle < 315:
                return str(angle - 270) + "° E of S"
            elif 315 <= angle < 360:
                return str(360 - angle) + "° S of E"

        elif angle < 0:
            if angle == -90:
                return "S"
            elif angle == -180:
                return "W"
            elif angle == -270:
                return "N"

            if -360 < angle <= -315:
                return str(360 - angle * -1) + "° N of E"
            elif -315 < angle < -270:
                return str(angle * -1 - 270) + "° W of S"
            elif -270 < angle < -225:
                return str(270 - angle * -1) + "° W of N"
            elif -225 <= angle < -180:
                return str(angle * -1 - 180) + "° N of W"
            elif -180 < angle <= -135:
                return str(180 - angle * -1) + "° S of W"
            elif -135 < angle < -90:
                return str(angle * -1 - 90) + "° W of S"
            elif -90 < angle < -45:
                return str(90 - angle * -1) + "° E of S"
            elif -45 <= angle < 0:
                return str(angle * -1) + "° S of E"

    @staticmethod
    def to_bearing(angle):
        if angle >= 0:
            return str(angle + 90)
        else:
            return str(angle * -1 + 90)

# Test code
if __name__ == "__main__":
    """
    v1a = Vector.from_angle(13.1, 295.9)
    v1a.details()
    v1b = Vector.from_angle(6.24, 37.3)
    v1b.details()
    Vector.add(v1a, v1b).details()
    Vector.subtract(v1a, v1b).details()
    """

    while True:
        print("Vector 1:")
        v1 = Vector.from_user_input()
        v1.details()
        print("Vector 2:")
        v2 = Vector.from_user_input()
        v2.details()

        print("Combined Vectors: ")
        print("v1 + v2")
        Vector.add(v1, v2).details()
        print("v1 - v2")
        Vector.subtract(v1, v2).details()


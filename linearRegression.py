class linReg:

    inputCoordinateX = []
    inputCoordinateY = []

    ydif = []
    xdif = []

    xy = []
    xsqr = []

    def get_user_input():
        is_finished = 0
        i = 0
        while is_finished == 0:
            inputCoordinateX.append(float(input("Enter X value ")))
            inputCoordinateY.append(float(input("Enter Y value ")))

            if input("Finished Entering? y or n ") == "y":
                print(inputCoordinateX)
                print(inputCoordinateY)
                break
            else:
                i += 1
                continue


    def mean_x():
        sum = 0.0
        totalx = 0.0
        for x in range(len(inputCoordinateX)):
            sum += inputCoordinateX[x]
            totalx += 1
        return sum/totalx


    def mean_y():
        sum = 0.0
        totaly = 0
        for y in range(len(inputCoordinateY)):
            sum += inputCoordinateY[y]
            totaly += 1
        return sum/totaly


    def diff():
        for y in range(len(inputCoordinateY)):
            ydif.append(inputCoordinateY[y] - mean_y())
        for x in range(len(inputCoordinateX)):
            xdif.append(inputCoordinateX[x] - mean_x())


    def times_diff():
        total = 0
        for i in range(len(xdif)):
            xy.append(ydif[i]*xdif[i])
        for j in range(len(xy)):
            total += xy[j]
        return total


    def times_x():
        total = 0
        for i in range(len(inputCoordinateX)):
            xsqr.append(pow(inputCoordinateX[i] - mean_x(), 2))
        for j in range(len(xsqr)):
            total += xsqr[j]
        return total

    def slope():
        return times_diff()/times_x()


    def yint():
        return mean_y()-slope()*mean_x()

    def main():
        get_user_input()
        diff()
        print("m = " + str(slope()))
        print("b = " + str(yint()))
        print("R = " + str(slope()) + "x + " + str(yint()))

    main()

class expReg:

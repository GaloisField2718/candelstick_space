#@author: GaloisField
#@desc: Main file to run the program

import data
import distances


def main():
    # Load the data
    X = data.extract('BTC-EUR', '2024-08-01', '2024-08-31')

    # Print the data
#    data.print_data(X)

    # Compute the distance on each pair of following points
    for i in range(1, len(X)):
        t0, X0 = X[i-1]
        t1, X1 = X[i]
        d = distances.dist(X0, X1)
        d = round(d, 3)
        N0 = distances.norm2(X0)
        N1 = distances.norm2(X1)

        d3 = distances.dist3(X0, X1)
        d3 = round(d3, 3)

        t0 = t0.date()
        t1 = t1.date()
        print("Between : ", t0, " and ", t1, " the distance is: ", d)
        print("Between : ", t0, " and ", t1, " the distance3 is: ", d3)

        # Each value need to be called independently, otherwise it will print `np.float64(number)`
        print("(", X0[0],",", X0[1],",", X0[2],",", X0[3], ") ", "➡️  (", X1[0], ",",X1[1],",", X1[2],",", X1[3], ")")
        
        print("Norm2 of X0 is: ", N0)
        print("Norm2 of X1 is: ", N1)

        color1 = data.compute_color(X0)
        color2 = data.compute_color(X1)
        print(color1, "➡️ ", color2, "\n")

    d = distances.dist(X[len(X)-2][1], X[len(X)-1][1])
    
    print("Last Distance is: ", d)

if __name__ == '__main__':
    main()

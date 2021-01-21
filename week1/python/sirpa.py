# Import numpy package (imported with pip, Python's own package installer)
import numpy as np


def main():
    # Add data to the program
    data = [(1, 4), (9, 31), (40, 22.5)]
    # Decide an arbitrary number for an input variable 
    input = 5
    # Call the function
    sirpa(data, input)


def sirpa(perceptions, interesting_x):
    # Add coordinates to their own variables
    x = [perception[0] for perception in perceptions]
    y = [perception[1] for perception in perceptions]
    # Create a linear regression equation from perceptions and return coefficients
    model = np.polyfit(x, y, 1)
    # Construct a one-dimensional polynomial with the coefficients
    predict = np.poly1d(model)
    # Create a prediction with the constructed polynomial
    estimate = round(predict(interesting_x), 1)
    # Print the estimate
    print("Estime: " + str(estimate))
    # Return the estimate
    return estimate


main()

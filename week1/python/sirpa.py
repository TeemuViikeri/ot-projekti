# Import numpy package (imported with pip, Python's own package installer)
import numpy as np


def main():
    # Add data to the program
    tuples = [(1, 4), (9, 31), (40, 22.5)]

    # Initialize empty lists for x and y values 
    x, y = []
    # Iterate over tuples from data and add x and y values to their own lists
    for tuple in tuples:
        x.append(tuple[0])
        y.append(tuple[1])

    # Pack lists neatly to a dictionary
    data = { "x": x, "y": y}
    # Decide an arbitrary number for an input variable 
    input = 20

    # Call the function
    sirpa(data, input)


def sirpa(perceptions, interesting_x):
    # Create a linear regression model from perceptions
    model = np.polyfit(perceptions.get('x'), perceptions.get('y'), 1)
    # Construct a one-dimensional polynomial for predictions
    predict = np.poly1d(model)
    # Create a prediction of an output value from an input value
    estimate = round(predict(interesting_x), 1)
    # Print the estimate
    print("Estime: " + str(estimate))
    # Return the estimate
    return estimate


main()

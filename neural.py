import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    losses = pd.DataFrame(columns=["loss"])

    train_in = np.array(
        [[0, 2, 0], [0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
    train_sol = np.array([[0, 0, 0, 1, 1]]).T

    # initialize nn_weight
    np.random.seed(1)
    nn_weights = 2 * np.random.random((3, 1)) - 1
    learningRate = 10

    # train the networks
    for i in range(100000000):

        train_out = 1 / (1 + np.exp(-(np.dot(train_in, nn_weights))))

        # Run the nn adjustment
        nn_weights += learningRate * np.dot(train_in.T,  (train_sol-train_out)
                                            * train_out * (1-train_out))

        loss = np.average((train_sol - train_out) **
                          2 / (2 * train_sol.shape[1]))
        losses = losses.append({"loss": loss}, ignore_index=True)

        if i % 10000 == 0:
            print(i)
            print(loss)

    losses.plot()
    plt.show()

    test_in = np.array([1, 0, 0])
    print('\nThe final prediction is ', 1 /
          (1 + np.exp(-(np.dot(test_in, nn_weights)))))


if __name__ == "__main__":
    main()

    watermelon = np.array([[0.697, 0.46],
                           [0.774, 0.376],
                           [0.634, 0.264],
                           [0.608, 0.318],
                           [0.556, 0.215],
                           [0.403, 0.237],
                           [0.481, 0.149],
                           [0.437, 0.211],
                           [0.666, 0.091],
                           [0.243, 0.267],
                           [0.245, 0.057],
                           [0.343, 0.099],
                           [0.639, 0.161],
                           [0.657, 0.198],
                           [0.36, 0.37],
                           [0.593, 0.042],
                           [0.719, 0.103],
                           [0.359, 0.188],
                           [0.339, 0.241],
                           [0.282, 0.257],
                           [0.748, 0.232],
                           [0.714, 0.346],
                           [0.483, 0.312],
                           [0.478, 0.437],
                           [0.525, 0.369],
                           [0.751, 0.489],
                           [0.532, 0.472],
                           [0.473, 0.376],
                           [0.725, 0.445],
                           [0.446, 0.459]])
    kmeans = K_Means(watermelon, 3)
    mu, sample_label, iter = kmeans.k_means()
    # result
    type0 = watermelon[np.where(sample_label == 0)]
    type1 = watermelon[np.where(sample_label == 1)]
    type2 = watermelon[np.where(sample_label == 2)]
    plt.scatter(type0[:, 0], type0[:, 1], marker="x", c="b", label="Positive")
    plt.scatter(type1[:, 0], type1[:, 1], marker="x", c="r", label="Negative")
    plt.scatter(type2[:, 0], type2[:, 1], marker="x", c="k", label="Negative")
    plt.show()
# The-Netflix-prize-data
Analysis of the dataset that contains the evaluations attributed by Netflix users to a selection of films.

The goal will be to analyze the sparse matrix using some collaborative filtering methods. Implementation of methods such as: associative rules, more precisely through the Apriori algorithm, latent Factor models, paying attention to gradient descent and SVD.

To analize the dataset, a data sample was selected due to the large size of the dataset.

After creating the rating matrix, i.e. a sparse matrix with the user ID as row index, the movie ID as column index and as internal values the ratings for each pair {user_i, film_j}, this matrix has been reconstructed through some collaborative filtering methods.

The different methods mentioned above were developed in an iterative way, considering a number of latent factors equal to 5.

Among the different methods applied to the dataset, the traditional gradient descent algorithm turns out to be the most efficient in terms of time needed to reach convergence.

# Install required libraries
# !pip install pandas scikit-surprise

import pandas as pd
from surprise import Reader, Dataset
from surprise.model_selection import train_test_split
from surprise import SVD
from surprise import accuracy

# Load the MovieLens dataset
# Replace 'path/to/dataset' with the actual path to your dataset
# You can download the MovieLens dataset from: https://grouplens.org/datasets/movielens/
data = pd.read_csv('path/to/dataset/ml-latest-small/ratings.csv')

# Pre-process the dataset
# For simplicity, we won't handle duplicates or missing values in this example
reader = Reader(rating_scale=(1, 5))
dataset = Dataset.load_from_df(data[['userId', 'movieId', 'rating']], reader)

# Split the dataset into training and testing sets
trainset, testset = train_test_split(dataset, test_size=0.2, random_state=42)

# Build and train the collaborative filtering model (SVD)
model = SVD()
model.fit(trainset)

# Evaluate the model's performance on the testing set
predictions = model.test(testset)
mae = accuracy.mae(predictions)
rmse = accuracy.rmse(predictions)

print(f'Mean Absolute Error (MAE): {mae}')
print(f'Root Mean Squared Error (RMSE): {rmse}')

# Make movie recommendations for a user (for testing purposes)
user_id = 1  # Replace with the actual user ID
user_ratings = data[data['userId'] == user_id][['movieId', 'rating']]

# Create a list of unrated movies for the user
unrated_movies = data[~data['movieId'].isin(user_ratings['movieId'])]['movieId']

# Predict ratings for unrated movies
predictions = []
for movie_id in unrated_movies:
    predictions.append((movie_id, model.predict(user_id, movie_id).est))

# Sort predictions based on estimated ratings
sorted_predictions = sorted(predictions, key=lambda x: x[1], reverse=True)

# Display top N movie recommendations for the user
top_n = 5
top_movies = sorted_predictions[:top_n]
recommended_movies = data[data['movieId'].isin([movie[0] for movie in top_movies])]['title'].unique()

print(f'\nTop {top_n} recommended movies for user {user_id}:')
for i, movie in enumerate(recommended_movies, start=1):
    print(f'{i}. {movie}')

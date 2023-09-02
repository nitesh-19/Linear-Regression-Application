from linear_regression import LinearRegression, predict_with_model

data_path = r".\data\insurance.csv"
feature_columns = [0, 2, 3, 4]
target_column = 6
trainer = LinearRegression(DATA_PATH=data_path, feature_columns_index=feature_columns,
                           target_column_index=target_column, ALPHA=0.5, create_test_set=False, ITERATIONS_LIMIT=50)

parameters = [53, 33.25, 0, 0]
target_prediction = predict_with_model(parameters)
print(f"Prediction for the input features {parameters} is {target_prediction}")

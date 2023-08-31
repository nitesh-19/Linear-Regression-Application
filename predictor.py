import main

with open("models_log.txt") as model:
    lines = model.readlines()
    last_line = lines[-1]
    print(last_line)
    dict_of_parameters = eval(last_line)
    print(dict_of_parameters)

w = dict_of_parameters["Slope"]
b = dict_of_parameters["Y-Intercept"]
country = dict_of_parameters["Country"]
print(f"For the country {country},")
year = int(input("Type the year you want to predict the population for: "))
prediction = main.line_function(year * 10 ** -main.SCALING_FACTOR, w, b)
print(f"The population of {country} in the year {year} will be {round(prediction)} Thousand people.")

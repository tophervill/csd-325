# Christopher Villarreal
# November 22, 2025
# Module 7.2 - Test Cases
# Purpose:  Create a function that formats city and country information,
#           including optional parameters, such as population and language.

def main():
    COUNTER = 0
    
    while COUNTER < 3:
        # Gather user input
        city_input = input("Enter the city name: ")
        country_input = input("Enter the country that city is located in: ")
        population_input = input("Enter the population of the city (optional): ")
        language_input = input("Enter the primary language spoken in the city (optional): ")

        information = city_country(city_input, country_input, population_input, language_input)

        print("You entered:\n", information, "\n")

        COUNTER += 1
    
# Function to format city and country information
# Default parameters in the event optional information is not provided
def city_country(city, country, population="", language=""):
    if population and language:
        formatted_city_country = f"{city.title()}, {country.title()} - Population {population}, {language.title()}"
    elif population:
        formatted_city_country = f"{city.title()}, {country.title()} - Population {population}"
    else:
        formatted_city_country = f"{city.title()}, {country.title()}"
    
    return formatted_city_country

if __name__ == "__main__":
    main()
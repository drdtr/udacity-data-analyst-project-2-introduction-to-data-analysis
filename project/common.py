
resources_folder = "../resources/project"
output_folder = "../output/project"


the_year = 2018
"""We are going to analyze data sets for the year 2018."""


def get_declared_class_attributes(clazz):
    return dict(filter(lambda e: not e[0].startswith("__"), clazz.__dict__.items()))


def print_declared_class_attributes(clazz):
    print(f"class {clazz.__name__}:")
    for attr_name, attr_value in get_declared_class_attributes(clazz).items():
        print(f'\t{attr_name} = "{attr_value}"')


class ColGdp:
    """Column names for the GDP data sets"""
    country_code = "Country code"
    country = "Country"
    year = "Year"
    gdp_per_capita = "GDP per capita"
    gdp_per_capita_ppp = "GDP per capita (PPP dollars)"
    # Additional columns
    above_avg_gdp_per_capita = "Above-average GDP per capita"
    above_avg_gdp_per_capita_ppp = "Above-average GDP per capita (PPP dollars)"
    gdp_level = "GDP level"
    gdp_total = "GDP total"
    gdp_total_ppp = "GDP total (PPP dollars)"


class ColPop:
    """Column names for the population data set"""
    country_code = "Country code"
    country = "Country"
    population = "Population"


class ColFuel:
    """Column names for the fuel export data set"""
    country_code = "Country code"
    country = "Country"
    fuel_exports = "Fuel exports (% of merchandise exports)"


class ColDem:
    """Column names for the democracy index data set"""
    country_code = "Country code"
    country = "Country"
    year = "Year"
    democracy_index = "Democracy index"
    # Additional columns
    regime_type = "Regime type"


class RegimeType:
    """Regime types for the democracy data set"""
    democracy = "Democracy"
    hybrid = "Hybrid"
    authoritarian = "Authoritarian"
    values = [democracy, hybrid, authoritarian]


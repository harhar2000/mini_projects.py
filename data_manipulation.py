import os
# * A warning: the data you are using may not contain quite what you expect;
#   cleaning data (or changing your program) might be necessary to cope with
#   "imperfect" data

# == EXERCISES ==

# Purpose: return a boolean, False if the file doesn't exist, True if it does
# Example:
#   Call:    does_file_exist("nonsense")
#   Returns: False
#   Call:    does_file_exist("AirQuality.csv")
#   Returns: True

def does_file_exist(file_path):
    return os.path.exists(file_path)

print(does_file_exist("nonsense"))
print(does_file_exist("AirQuality.csv"))

# Purpose: get the contents of a given file and return them; if the file cannot be found, return a nice error message instead
# Example:
#   Call: get_file_contents("AirQuality.csv")
#   Returns:
#     Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);[...]
#     10/03/2004;18.00.00;2,6;1360;150;11,9;1046;166;1056;113;1692;1268;[...]
#     [...]
#   Call: get_file_contents("nonsense")
#   Returns: "This file cannot be found!"
# Notes:
# * Learn how to open file as read-only
# * Learn how to close files you have opened
# * Use readlines() to read the contents
# * Use should use does_file_exist()

def get_file_contents(filename):
    if does_file_exist(filename):
        with open(filename, "r") as file:
            return file.read()  # Return the entire file content as a string
    else:
        return "Not found"


# print(get_file_contents("AirQuality.csv"))
# print(get_file_contents("nonsense"))

# Fetch 25th December air quality data rows and if boolean argument "include_header_row" is True, return first header row (if False, omit)

def christmas_day_air_quality(filename, include_header_row):
    contents = get_file_contents(filename)
    if contents == "Not found":
        return "Not Found"
    
    lines = contents.splitlines()
    header = lines[0] if lines else ""
    christmas_rows = [line for line in lines if line.startswith("25/12")]

    if include_header_row and header:
        return f"{header}\n" + "\n".join(christmas_rows)
    else:
        return "\n".join(christmas_rows)


# print(christmas_day_air_quality("AirQuality.csv", True))
# print(christmas_day_air_quality("AirQuality.csv", False))


# Purpose: fetch Christmas Day average of "PT08.S1(CO)" values to 2 decimal places
# Example:
#   Call: christmas_day_average_air_quality("AirQuality.csv")
#   Returns: 1439.21

def christmas_day_average_air_quality(filename):
    data_rows = christmas_day_air_quality(filename, False)
    if data_rows == "Not Found":
        return "This file was not found"
    
    header_row = christmas_day_air_quality(filename, True).splitlines()[0]
    header_columns = header_row.split(";")

    try:
        pt08_index = header_columns.index("PT08.S1(CO)")
    except ValueError:
        return "Column 'PTO8.S1(CO)' not found in file"
    
    rows = data_rows.splitlines()
    pt08_values = []
    for row in rows:
        columns = row.split(";")
        try:
            value = float(columns[pt08_index].replace(",", "."))
            pt08_values.append(value)
        except (ValueError, IndexError):
            continue

    if pt08_values:
        average = sum(pt08_values) / len(pt08_values)
        return round(average, 2)
    else:
        return "No valid PT08.S1(CO) data has been found for Christmas"
print(christmas_day_average_air_quality("AirQuality.csv"))
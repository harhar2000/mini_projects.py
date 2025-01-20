import os
# Determine if a specific file exists in the relevant directory or path

def does_file_exist(file_path):
    return os.path.exists(file_path)

print(does_file_exist("nonsense"))
print(does_file_exist("AirQuality.csv"))


# Read the contents of a file and handle cases where the file doesn't exist

def get_file_contents(filename):
    if does_file_exist(filename):
        with open(filename, "r") as file:
            return file.read()  # Return the entire file content as a string
    else:
        return "Not found"

print(get_file_contents("AirQuality.csv"))
print(get_file_contents("nonsense"))


# Extract only the data rows for Christmas Day, with the option to include or exclude the header

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

print(christmas_day_air_quality("AirQuality.csv", True))
print(christmas_day_air_quality("AirQuality.csv", False))


# Calculate the average value of the PT08.S1(CO) column for Christmas Day, rounded to two decimal places

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
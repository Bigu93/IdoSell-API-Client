def parse_location(string):
    if string == "" or len(string) > 25 or not isinstance(string, str):
        return {"error": True, "message": "Invalid location string"}

    count = string.count("\\")
    strings_list = string.split("\\", count)

    num_location = strings_list[-1]
    level_location = strings_list[-3]

    data = {"level": level_location, "position": num_location}

    return data

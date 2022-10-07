def total(jeffs_list: list[float]) -> float:
    """return the sum of all floats in jeffs_list"""
    result: float = 0.0
    for float_item in jeffs_list:
        result += float_item
    return result


def join_things(list_of_numbers: list[int], delimiter: str = "") -> str:
    """Return an aggregated string containing both the integers and dimlimiter"""
    string_result: str = ""
    if len(list_of_numbers) == 0:
        return string_result

    for number in list_of_numbers:
        string_result += f"{number}{delimiter}"
    return string_result.strip(delimiter)


"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    "Return a list of wagons, given an arbitrary amount of wagon numbers."
    
    [*args_list] = args
    return args_list


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    "Fix the list of wagons."
    
    first, second, locomotive, *remaining = each_wagons_id
    modifications = locomotive, *missing_wagons, *remaining, first, second
    return list(modifications)


def add_missing_stops(journey, **route):
    "Add missing stops to route dict."
    
    journey['stops'] = [value for value in route.values()]
    return journey


def extend_route_information(route, more_route_information):
    "Extend route information with more_route_information."
    
    route.update(more_route_information)
    return route


def fix_wagon_depot(wagons_rows):
    "Fix the list of rows of wagons."

    row1, row2, row3 = wagons_rows
    fixed_rows = list(map(list, zip(row1, row2, row3)))
    return fixed_rows

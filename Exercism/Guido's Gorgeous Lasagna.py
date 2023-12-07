EXPECTED_BAKE_TIME = 40
def bake_time_remaining(elapsed_bake_time:int):
    """Calculate the bake time remaining.
 
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
 
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return 40 - elapsed_bake_time
def preparation_time_in_minutes(number_of_layers:int):
    """Calculate the time needed for preparing the layers.
 
    :param number_of_layers: int - the number of lasagna layers.
    :return: int - time that is needed for preparing each layer.
 
    Function that takes the number of layers and returns the time of their prepartion
    based on how many layers have been given as an argument!    
    """
    return 2 * number_of_layers
def elapsed_time_in_minutes(number_of_layers:int, elapsed_bake_time:int):
    """Calculating the time that has been elapsed to prepare the lasagna.
 
    :param number_of_layers: int - the number of lasagna layers.
    :param elapsed_bake_time: int - the time that has been elapsed for baking the lasagna.
    :return: int - time that is elapsed from the first step!
    
    """
    return (number_of_layers * 2) + elapsed_bake_time

def which_prize(points):
    if 0 <= points <= 50:
        message = "Congratulations! You have won a wooden rabbit!"
    elif points <= 150:
        message = "Oh dear, no prize this time."   
    elif points <= 180:
        message = "Congratulations! You have won a wafer-thin mint!"
    elif points <= 200:
        message = "Congratulations! You have won a penguin!"
    return print(message)
    
which_prize(12)
which_prize(72)
which_prize(162)
def convert(number):
    raindrop = ""
    if not number % 3: 
        raindrop += "Pling"
    if not number % 5: 
        raindrop += "Plang"
    if not number % 7: 
        raindrop += "Plong"
    return raindrop or str(number)

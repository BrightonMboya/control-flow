while (True):
    userInput = input("What isthe weather like today? (sunny/rainy/cold):")
    if userInput == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif userInput == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif userInput == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else: 
        print("Sorry, I don’t have recommendations for this weather.")
    break
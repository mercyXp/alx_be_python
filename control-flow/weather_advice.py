weatherCheck =str(input("What's the weather like today?(sunny/rainy/cold)")).lower()
print(weatherCheck)

if weatherCheck == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weatherCheck == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weatherCheck == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
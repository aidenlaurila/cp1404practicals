"""
CP1404 Practical
Program to show user hex codes of colours
"""

COLOUR_TO_CODE = {"amethyst": "#9966cc", "blackcoffee": "#3b2f2f", "blueviolet": "#8a2be2",
                "brickred": "#cb4154", "canary": "#ffff99", "cardinal": "#c41e3a",
                "celeste": "#b2ffff", "charcoal": "#36454f", "cobalt": "#0047ab",
                "corn": "#fbec5d"}

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    try:
        print(f"{colour_name} hex code is {COLOUR_TO_CODE[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()
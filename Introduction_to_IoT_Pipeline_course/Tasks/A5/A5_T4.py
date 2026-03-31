def askDimension(PPrompt: str) -> float:
    Feed = float(input(f"Insert {PPrompt}: "))
    return Feed

def calcRectangleArea(PWidth: float, PHeight: float) -> float:
    Area = PWidth * PHeight
    return Area

def main():
    print("Program starting.")

    PWidth = askDimension("width")
    PHeight = askDimension("height")
    Area = calcRectangleArea(PWidth, PHeight)

    print(f"\nArea is {Area}²")
    print("Program ending.")
    return None

main()
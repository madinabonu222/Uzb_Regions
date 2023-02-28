import turtle
import pandas

screen = turtle.Screen()
screen.title("Uzbekistan Regions Game")
image = "blank_regions_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("13_regions.csv")
all_regions = data.region.to_list()
guessed_regions = []

while len(guessed_regions) < 13:
    answer_region = screen.textinput(title=f"{len(guessed_regions)}/13 Regions Correct",
                                     prompt="What's another region's name?").title()
    # .title() method makes any string to capital letter.
    if answer_region == "Exit":
        missing_regions = []
        for region in all_regions:
            if region not in guessed_regions:
                missing_regions.append(region)
        data = pandas.DataFrame(missing_regions)
        data.to_csv("regions_to_learn.csv")
        break
    if answer_region in all_regions:
        guessed_regions.append(answer_region)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        region_data = data[data.region == answer_region]
        t.goto(int(region_data.x), int(region_data.y))
        t.write(answer_region)


screen.exitonclick()

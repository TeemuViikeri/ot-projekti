def main():
    temperature = 15
    func(temperature)


def func(temperature):
    while(True):
        answer = input(
            "Would you like your temperature in Celcius or Fahrenheit? Enter 'C' or 'F'.\n")
        if (answer == "C" or answer == "F"):
            break
    if (answer == "C"):
        print("Today's temperature is " + str(temperature) + "\u2103C")
    else:
        print("Today's temperature is " +
              str(convertToFahrenheit(temperature)) + "\u2109F")


def convertToFahrenheit(celciusTemp):
    f = round((celciusTemp * 9/5) + 32)
    return f


main()

# Koodin toiminta on rationaalista, sillä koodi toimii tarkoituksen mukaisesti ja loogisesti.
# Ohjelman etenee ohjelmaa käyttävän syötteen mukaisesti ja halutusti, ja ilmoittaa asianmukaisen vastauksen.
# Koodissa olevat silmukat ja ehtolausekkeet tuovat ohjelmaan ja func-funktioon rakennetta ja loogisuutta.
import pandas as pd
import datetime
import os


class Athlete:
    """a class to represent an athlete, seeks user input for name,
    pre and post workout weights, and then calculates hydration needs for
    each individual athlete."""

    def __init__(
        self,
        first_name,
        last_name,
        pre_practice_weight,
        post_practice_weight,
        weight_change_absolute,
        relative_weight_change,
        hydration_needs,
        date,
    ):
        if not first_name:
            raise ValueError("Missing Values, please fill out all fields.")
        if not last_name:
            raise ValueError("Missing Values, please fill out all fields.")
        if not pre_practice_weight:
            raise ValueError("Missing Values, please fill out all fields.")
        if not post_practice_weight:
            raise ValueError("Missing Values, please fill out all fields.")

        self.first_name = first_name
        self.last_name = last_name
        self.pre_practice_weight = pre_practice_weight
        self.post_practice_weight = post_practice_weight
        self.weight_change_absolute = weight_change_absolute
        self.relative_weight_change = relative_weight_change
        self.hydration_needs = hydration_needs
        self.date = date

    def __repr__(self):
        return f"Athlete({self.first_name!r}, {self.last_name!r}, {self.pre_practice_weight!r}, {self.post_practice_weight!r}, {self.weight_change_absolute!r}, {self.relative_weight_change!r}, {self.hydration_needs!r}, {self.date!r})"

    def __iter__(self):
        return iter(
            [
                self.first_name,
                self.last_name,
                self.pre_practice_weight,
                self.post_practice_weight,
                self.weight_change_absolute,
                self.relative_weight_change,
                self.hydration_needs,
                self.date,
            ]
        )


class bcolors:
    NAME = "\033[92m"
    BLINK = "\033[5m"
    RELATIVE = "\033[92m"
    LOST = "\033[93m"
    HYDRATE = "\033[96m"
    INPUT = "\033[31m"
    INPUT_OPP = "\033[97m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def main():
    """Repeatedly ask for athlete weight/info, printing out their change
    in weight pre vs post practice, and if they lost weight, the amount of fluid
    recommended to rehydrate. Repeat until force closed with ctrl+d so that
    many athletes can use the same computer to repeatedly enter their info after
    practice is complete. Store this information in a csv via pandas everytime
    the entire team finished completing new entries."""

    athletes = []
    trigger = True

    while trigger == True:
        try:
            # clear terminal at start of program and in-between try loops.
            os.system("cls||clear")

            # get individual athlete and then append them to an empty list
            athlete = get_athlete()
            athletes.append(athlete)

            # change colors of printed feedback based on hydration status
            if (
                athlete.relative_weight_change > 3
                and athlete.relative_weight_change < 5
            ):
                bcolors.RELATIVE = "\033[93m"
            elif athlete.relative_weight_change > 5:
                bcolors.RELATIVE = "\033[91m"
            else:
                bcolors.RELATIVE = "\033[92m"

            # change printed feedback on if they lost weight vs. gained weight
            if athlete.relative_weight_change >= 0:
                print(
                    f"\n{bcolors.NAME}{athlete.first_name}{bcolors.ENDC}, today at practice you lost {bcolors.LOST}{athlete.weight_change_absolute:.2f} pounds.{bcolors.ENDC}"
                )
                print(
                    f"That is {bcolors.RELATIVE}{abs(athlete.relative_weight_change):.2f}%{bcolors.ENDC} of your total body weight."
                )
                print(
                    f"It is recommended that you drink at least {bcolors.HYDRATE}{athlete.hydration_needs:.2f} ounces of fluid{bcolors.ENDC} today {bcolors.UNDERLINE}{bcolors.BOLD}in addition to what you would normally drink{bcolors.ENDC} in order to rehydrate the weight lost at practice.\n"
                )
            elif athlete.relative_weight_change < 0:
                print(
                    f"\n{bcolors.NAME}{athlete.first_name}{bcolors.ENDC}, today at practice you gained {bcolors.LOST}{abs(athlete.weight_change_absolute):.2f} pounds.{bcolors.ENDC}"
                )
                print(
                    f"That is {bcolors.RELATIVE}{abs(athlete.relative_weight_change):.2f}%{bcolors.ENDC} of your total body weight."
                )
                print(
                    f"{bcolors.HYDRATE}{bcolors.UNDERLINE}{bcolors.BOLD}You did a great job with hydration today while training. Nice Job!{bcolors.ENDC}\n"
                )

            # ask if more athlete's want to enter their info or end the program
            proceed = input(
                f"{bcolors.INPUT}Do you want to enter another athlete's information? {bcolors.ENDC}{bcolors.INPUT_OPP}Please enter {bcolors.BOLD}[yes or no]{bcolors.ENDC} "
            )
            # manual check via user input to break out of loop and end program
            if proceed == "no":
                trigger = False
            elif proceed == "yes":
                trigger == True
        finally:
            # save & append newly inputted information into CSV log
            df = pd.DataFrame(
                athletes,
                columns=[
                    "first_name",
                    "last_name",
                    "pre_practice_weight",
                    "post_practice_weight",
                    "weight_lost",
                    "percent_lost",
                    "hydration_demand",
                    "date",
                ],
            )
            df.to_csv("weight_chart.csv", mode="a", header=False, index=False)
            # clear terminal at end of program.
            os.system("cls||clear")


def get_athlete():
    """instantiate a specific athlete and retrieve their information."""
    while True:
        try:
            first_name = (
                input(f"{bcolors.INPUT}{bcolors.BOLD}First Name:{bcolors.ENDC} ")
                .strip()
                .capitalize()
            )
            if not first_name:
                raise ValueError
        except ValueError:
            print("Please enter a first name.")
        else:
            break
    while True:
        try:
            last_name = (
                input(f"{bcolors.INPUT_OPP}{bcolors.BOLD}Last Name:{bcolors.ENDC} ")
                .strip()
                .capitalize()
            )
            if not last_name:
                raise ValueError
        except ValueError:
            print("Please enter a last name.")
        else:
            break
    pre_practice_weight, post_practice_weight = get_weights()
    weight_change_absolute, relative_weight_change = get_weight_change(
        pre_practice_weight, post_practice_weight
    )
    # amount of water in oounces per lb of body weight lost due to sweat for rehydration
    fluid_ounces_per_pound = 16
    hydration_needs = weight_change_absolute * fluid_ounces_per_pound
    # create a timestamp of entry, allows for athletes to enter new info daily.
    date = datetime.datetime.now().date()
    return Athlete(
        first_name,
        last_name,
        pre_practice_weight,
        post_practice_weight,
        weight_change_absolute,
        relative_weight_change,
        hydration_needs,
        date,
    )


def get_weight_change(pre, post):
    """calculate absolute & relative intraday weight loss"""
    absolute = pre - post
    relative = round((1 - post / pre) * 100, ndigits=2)
    return absolute, relative


def get_weights():
    """Take user input for pre vs post workout weight. Validate input is
    numerical. If not repeatedly ask them to enter it until they get it right."""
    while True:
        try:
            x = float(
                input(
                    f"{bcolors.INPUT}{bcolors.BOLD}Before Practice Weight:{bcolors.ENDC} "
                )
            )
        except ValueError:
            print("Please enter a valid number")
        else:
            break
    while True:
        try:
            y = float(
                input(
                    f"{bcolors.INPUT_OPP}{bcolors.BOLD}After Practice Weight:{bcolors.ENDC} "
                )
            )
        except ValueError:
            print("Please enter a valid number")
        else:
            break
    return x, y


if __name__ == "__main__":
    main()

# Main file for the dates

from mechanics import Database, InputValidation
from time import sleep
from os import system


class Main:
    """The main class which handles interaction with the user
    
    Attrs:
        menu_
        
    Methods:
        main(): Contains the main loop for the program.
        menu(): Contains the menu for the user
        add_value(): Used to add a value to the database
        get_values(): stores a sorted list of returned dates in a file"""


    def __init__(self):
        self.db = Database()
        self.validate = InputValidation()

    def main(self):
        """Contains the main loop of the program"""
        while True:
            system("CLS")
            try:
                self.menu()
            except KeyboardInterrupt:
                print("Would you like to quit the program or return to the menu?")
                resp = self.validate.validateChoice({"0": "Quit", "1": "Return to menu"})
                if not int(resp):
                    print("Good bye.")
                    raise SystemExit
            print("\n")
            sleep(2)

    def menu(self):
        """Contains the main menu for the program."""
        choices = {"1": self.add_value, "2": self.get_values}
        menu_choices = {"1": "Add a new event and year", "2":"Get the sorted results"}
        print("How may we help you today?")
        choices[self.validate.validateChoice(menu_choices)]()

    def add_value(self) -> bool:
        """Used to add a new value to the database.
        
        Returns:
            False if user chooses to cancel"""
        while True:
            date_ = self.validate.validateInt("Press ctrl + c at any time to quit and return to menu\nEnter the year for the event")
            event_ = input("Enter the event that happened in that year.\n: ")
            print("Confirming that this information is correct:")
            print()
            print("On", date_, event_, "occurred.")
            result = int(self.validate.validateChoice({"0": "Confirmation", "1":"Canceling"}))
            if result:
                print("Cancelling")
                return False

            self.db.setEntry(date_, event_)

    def get_values(self):
        """Method used to get all of the values from the database, sort them, and store them in a txt file"""

        values = self.db.getAllEntries()
        if not values:
            print("Sorry, there aren't any entries in the database")
            return 
        
        values.sort(key=lambda x: x[1])
        with open("sorted.txt", "w") as fp:
            for tup in values:
                fp.write(f"{tup[1]}: {tup[2]}\n")

        print("Your result has been stored in the folder in the file sorted.txt")


if __name__ == "__main__":
    main = Main()
    main.main()

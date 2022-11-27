# My CS50 Hydration Log Project
### Video Demo:  <https://youtu.be/5ajvg_K1_Mg>
### Description:
##### This program was designed to be used by a sports medicine provider that is tasked with monitoring the hydration status of their athletes during the warm months of the year.
##### Traditionally, this is done with with the use of paper weight charts and is done by hand and requires hours and hours of work to record, calculate, and then parse for any drastic changes. A football team practicing in August may have 100-200 prospective players on the roster during the camp.
##### This python script serves to be run on a computer that can be filled out by the staff or the athletes as they finish practice. The program will prompt for the following user inputs.
1. First Name
2. Last Name
3. Pre workout bodyweight
4. Post workout bodyweight
##### This input is used to instantiate a custom Athlete class that represents each individual athlete that completes the weigh-in process, and ultimately appends them to a master list.
##### The pre vs. post bodyweight measurements are used to calculate:
+ ##### Absolute Change (Total intraday bodyweight loss)
+ ##### Relative Change (% change)
+ ##### Personalized Hydration Guideline
  - ##### This is based on the idea that for every 1lb of bodyweight lost through sweat, it takes ~16 fluid ounces of liquid to rehydrate.
+ ##### A date timestamp in the *YYYY-MM-DD* format
##### This information is provided back to the user after they have finished providing the necessary input. This is a personalized message using f-strings and conditional formatting.
 - ##### Conditional formatting is based on their relative or percent change in total body weight. This measure is more closely related to risk of heat illness, and performance decrements.
 - ##### If an athlete does not lose any weight or perhaps even gains weight while working out they are commended for their hydration efforts.
  - ##### If the athlete loses weight the color of the text within the terminal message changes from yellow to red, based on the magnitude of their % change.
##### After the personalized message the program prompts for a response on if it is desired to enter another athlete's weight record. This was done to allow for many athletes to be entered in rapid succession until were complete. The prompt is a simple yes or no input prompt that conditionally breaks out or continues an infinity loop based upon the user's response.
 - ##### If you answer yes, the terminal screen will clear the previous personalized message and begin to prompt for another athlete's information.
  - ##### If you answer no, the infinity loop breaks, the program saves the master list of athletes to a logfile by appending to a CSV file using the pandas library.
   - ##### The pandas library was used over the CSV library because of the common usage of this library in the sports science domain and I wanted to continue to familiarize myself with it.
   - ##### One other design idea was to have the personalized message be delivered via email and/or txt message but I didn't want the burden of dealing with email credentials or txt service tokens/passwords in this project. I didn't know if that level of design would make it hard for the CS50 grading and therefore I wanted the program to be entirely self-contained and able to be run without internet access.
 - ##### This log file is appended to and not overwritten because it allows for a master day-to-day log that can be used to watch athlete weights overtime. The CSV format was chosen because of how nicely it may plug into athlete monitoring software packages that already exist and due to the fact that coaches can easily be sent a file format like CSV and know how to open/read it.
   - ##### Future design ideas would consider using something like a SQL database that has complete CRUD functions.
   - ##### Implementing a complete CRUD function in the future would be nice to allow edits to any potential errors that were made during the input process despite the checks that were already implemented.

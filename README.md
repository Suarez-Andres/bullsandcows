# THIS IS BULLS AND COWS!

#### Description:
Hi! I am Andrés Suárez, the developer behind this project. Short presentation: I am 23 years old and come from Bogotá, Colombia.
So, my project is a web application of one of my favorites childhood games. bulls and cows! it was developed with flask, following the next structure:
- "app.py" file
- "requeriments.txt" file
- "numbers.db" file, a database involved in the operation of the app
- "static" folder, with all the images, icons, and the css file (all of them necesaries for the app)
- "templates" folder, with all the HTML files that are involved in the app (in this case are two, "index.html" and "game.html")

Allow me to list the operating order of mi app as follows:
1. Once you launch the server via `flask run`, the first thing that is loaded is the `index.html` page. Here, the rules of the game are explained along wit the operation of the principal page. At the bottom of the page there will be a button named `Lets play!` and once you click it, the principal page is going to be loaded.
> The `Lets play!` button works as a form because I wanted to use the POST method for change pages in my `app.py` file. the other elements used in the construcction of this page are unordered lists, headers and paragraphs, among others.
2. Now the `game.html` page is going to be loaded. Here is where the magic happens. You have to guess the number randomly generated by the computer using the bulls and cows hints! is so much fun. To check any number that you want to try, you have to write it in the "Number" text box and send it clicking the "check" button. (or pressing enter, both ways work)
3. While you keep trying to guess the number, the table below the button is going to show you this information:
- the number of your last attempt
- the number you entered in your attempt
- the bulls that you have in your number
- the cows that you have in your number
4. Once you guess the number, a flash message its going to tell you that you won, and the table its going to be cleaned. If you want a new number to play again, click the link below the table to go back to the instructions page and when you click `Lets play!` again, the game begins again with a new number and 0 attempts.
> In this page, the text box and the `check` button are part of a form. every time you send one number, its going to be added to a table in the "numbers.db" database for keeping track of the attempts and your bulls and cows. once you win, the table clean itself and you have to go to the first page to generate a new number.

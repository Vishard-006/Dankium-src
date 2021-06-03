# A Selenium Automated Discord Bot for Dank Memer
**Uses commands like pls beg, pls search etc for coin grinding**
### Purpose
For automating dank memer commands and grinding coins

### How is this better than other auto-typers ? 
- There are some other open-source autotypers available right eg https://github.com/iceteacandy/Dank-memer-discord-auto-typer or https://github.com/Swayx113/dank-memer-auto-typer ? Why should I use this script then ?
- Those scripts are good too , but the advantage of using Dankium is that it does not use your system keyboard . This means that you are free to type using your system keyboard while running Dankium , something you cannot do with the other scripts . Dankium launches a browser session through selenium , and so all the typing happens only in the browser window , which leaves your system keyboard for you to use .
- On the flip side , to be able to do this , Dankium needs to login to discord web , hence it requires you to type in your discord username and password . You will get a prompt to type in your username , password , server channel url and browser of choice (currently it supports chrome and firefox) .

### Whats the `data.json` file ?
- The first prompt you get after running the program is `Save login credentials ?` .  Where does it save them ?
- If you hit y for the prompt , your credentials will be saved in `src/data.json `
- but why does it need to save these credentials ?
- Simple , it saves you the time of typing the credentials manually every time . Basically feature can be called as 'autologin' .

## Compiling from Source

 

 - Unzip the Tarball/Zip
 - Navigate to the unzipped tar in the terminal
  `cd Downloads\Dankium\src\` \ `cd Downloads\Dankium\src\`
 - Now run `pip install -r requirements.txt` for getting all dependencies (Need Python added to PATH and pip)
 - For Mac/Linux
  `python3 -m dank_memer.py`
  - For Windows
` python -m dank_memer.py`

#### Full List of executed Commands
| Command | Item to be Purchased from Dank memer shop |
|---------|-------------------------------------------| 
| 1. pls beg | - |
| 2. pls hunt | Hunting Rifle |
| 3. pls fish | Fishing Rod
| 4. pls pm  | Laptop |
##### Income 
- An Average of anywhere between 5k to 40k coins per hour is expected 
> This totally depends on your luck !!
#### Note 
- For compiling from source an Installation of Python added to PATH is required
- You must have purchased required things for each command before running the bot . Otherwise Bot will not work
- This project was made for educational purposes and understanding selenium better . I am in no way responsible for any trouble that may be cause by using this tool , either for or  against you . Remember Dank Memer condemns people from using auto-typers and you may be banned for the same . Use the tool at your own risk .

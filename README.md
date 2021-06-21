# 🤖 Surveyor Bot
Surveryor is a selenium bot for answer bioprotocol surveys

## Requirements
- Python3
- Pip3
- Chrome Browser

## How run the bot?
1. Create a virtual enviroment called `.env`
2. Install requirements using pip `pip3 install -r requirements.txt`
3. Expose your bioprotocol credentials, Example: `export USER_MAIL="me@mail.com" && export USER_PWD="123456"`.
Also you can create a file called `credentials.sh`, it's only required if you want run the bot using the `surveyor.sh` shell script 
4. Download Chrome Driver for selenium, put this into search bar in chrome [chrome://settings/help](chrome://settings/help) check what is the chrome version and go to avobe link [Chrome Drivers](https://sites.google.com/a/chromium.org/chromedriver/downloads), Download the driver and unzip file called `chromedriver` into project path  
5. Run the bot, for do it you need run `python3 main.py`
6. Optional: You will add an alias surveyor into your `.bashrc` or `.zshrc`. The alias must look like something like that `alias surveyor="source <project_path>/surveyor.sh"`

Please, don't forget give me a star ⭐

```
Happy hacking!!!
```
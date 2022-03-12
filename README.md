# Propawhat


## WARNING - If lots of recipients report you, your WhatsApp account will be blocked. Best to use a throwaway simcard or virtual/e-sim from an online service

We the people of the world have a message to the Russian nation.
A nation that is to pay a huge price because of the shameful decision of the dictator Putin to attack an independent Ukraine by armed forces. The joint action of all the states of the free world, as a response to Russia’s aggression, will lead to the collapse of the entire country.

However, nearly 150 million Russians do not know the truth about the causes or course of the war in Ukraine. It is fed with the lies of the Kremlin propaganda. There is no free media in Russia and the internet is censored.

It is possible for each of us to convey a direct message to the inhabitants of this enslaved country.

This is a script that makes use of [squad303](https://twitter.com/squad3o3)'s api for retrieving randomly selected Russian phone numbers. 

It retrieves the phone numbers from squad303's api and then sends messages using Selenium and WhatsApp Web.
It also supports sending images.
t to open Whatsapp Web in the browser, automatically populate the recipient and message and then send the message


Let them know the truth. Let them know the power of the free world!

## Install on ubuntu
Python Version: 3.8

Not mandatory, but best to use a [Python Virtual Environment](https://docs.python.org/3.8/library/venv.html)

You need [tkinter](https://docs.python.org/3/library/tkinter.html)

`sudo apt-get install python3-tk python3-dev`

You need [Selenium Chromedriver](https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/). Only up to step 3 
(SeleniumServer not required)

### Setting up chrome profile
- Create a custom Chrome profile

- Log into Whatsapp Web in your chrome profile: [Whatsapp Web](https://web.whatsapp.com/)

NOTE: I had a lot of problems getting selenium to use a chrome profile. In order to make it happen I had to copy my user
dir from `/home/<usr name>/.config/google-chrome` to the project directory, then set the `user_data_dir` to the directory in
the project, and the `profile_directory` to the name of the profile that Chrome created for me. You will find this if you
open chrome with your new profile, navigate to `chrome://version` and look for the "Profile Path" value. Set `profile_directory`
to whatever is after the last forward slash. In my case it was `/home/<usr name>/.config/google-chrome/Profile 3` so I did as follows:
- copy `/home/<usr name>/.config/google-chrome` to a `google-chrome` in my project root
- set `user_data_path` in `config.json to `/google-chrome`
- set `profile_directory` in `config.json` to `Profile 3`

### Install Dependencies
`pip install -r requirements.txt`

### Run
`python main.py`

## Install on Windows
Untested - contributions welcomed

I think there may be some issues with the img sending because of different types of slashes between Windows and Linux but
I haven't tested

## Images
If you set `img_enabled` to `true` in `config.json`, the script will pick an image at random from the `/img` folder and send it with your message.
You can add as many images as you want to `/img` with any filenames - it will list the dir and then choose one at random.

## Current Limitations/Notes - 
- Your Whatsapp account may be banned after some hours of use, so best to use a virtual phone number/e sim or only work with small batches of varying message content

## Configuration
`config.json` allows you to configure the paramters of the script
- `user_data_path` and `profile_directory` point Selenium to your Chrome Profile (with Whatsapp already logged in)
see Setting Up Chrome profile section for more info
- `url` is the url from which to retrieve the phone numbers
- `messages` is a list of message content texts that are chosen at random for each message
- `img_enabled` is to enable/disable sending images, see Images section for more info
- `open_wait` is how long to wait before sending message after opening Whatsapp Web (random +- 2s)
- `click_wait` how long to wait between clicks when sending Whatsapp message

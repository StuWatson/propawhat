#Propawhat

We the people of the world have a message to the Russian nation.
A nation that is to pay a huge price because of the shameful decision of the dictator Putin to attack an independent Ukraine by armed forces. The joint action of all the states of the free world, as a response to Russia’s aggression, will lead to the collapse of the entire country.

However, nearly 150 million Russians do not know the truth about the causes or course of the war in Ukraine. It is fed with the lies of the Kremlin propaganda. There is no free media in Russia and the internet is censored.

It is possible for each of us to convey a direct message to the inhabitants of this enslaved country.

This is a script that makes use of [squad303](https://twitter.com/squad3o3)'s api for retrieving randomly selected Russian phone numbers. 
It uses pywhatkit to open Whatsapp Web in the browser, automatically populate the recipient and message and then send the message

Let them know the truth. Let them know the power of the free world!

## Install on ubuntu
Not mandatory, but best to use a [Python Virtual Environment](https://docs.python.org/3.8/library/venv.html)

You need [tkinter](https://docs.python.org/3/library/tkinter.html)

`sudo apt-get install python3-tk python3-dev`

`pip install -r requirements.txt`

Log into Whatsapp Web in your primary browser: [Whatsapp Web](https://web.whatsapp.com/)

`python main.py`

## Install on Windows
Untested

## Configuration
`config.json` allows you to configure the paramters of the script
- `api` is the url from which to retrieve the phone numbers
- `messages` is a list of message content texts that are chosen at random for each message
- `wait_time` is how long to wait before sending message after opening Whatsapp Web (random +- 2s)
- `tab_close` boolean, whether or not to close the tab after sending
- `close_time` how long to wait after sending before closing the tab (random +- 2s)


## Current Limitations - 
- Browser window must be full screen and can't be run in the background
- Would be better to have this packaged for non technical users


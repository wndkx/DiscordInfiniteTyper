<h1 style="text-align: center">DiscordInfiniteTyper</h1>
Make your type infinite

# Notice
The author is not responsible for your Discord account. These operations are breaking Discord ToS. This programme is written only for educational purposes

# Installation
* Install git

* Install [python](https://python.org)

* Clone this repository via: `git clone https://github.com/z3ven/DiscordInfiniteTyper/`

* Type: `pip3 install requests`

# Using
* Open the config.json file and change the settings
## Changing config
* In `token` you must put your user token which you can get in five steps:
* Open your browser
* Go to [discord.com](https://discord.com/app)
* Open the Developer menu, then the console
* And type this: 
```javascript
(
    webpackChunkdiscord_app.push(
        [
            [''],
            {},
            e => {
                m=[];
                for(let c in e.c)
                    m.push(e.c[c])
            }
        ]
    ),
    m
).find(
    m => m?.exports?.default?.getToken !== void 0
).exports.default.getToken()
```
* In `channel_id` you must put the id of a channel where you want to make infinite typing status
To get the channel id enable developer mode in your discord settings and right-click on the channel or DM, then click `Copy channel ID`.
* To enable debug mode set the `debug-mode` parameter to true. Debug mode prints useful information, if you want to contribute to the project.
## Running
* Now run `python main.py`
## Useful info
You will see useful information in a console if you enable debug mode.
If the request was successful you will see: `Received status code 204`
Error message:
`Error: ERROR_CODE RESPONSE_IN_JSON_FORMAT`
## Non-debug mode
If you disabled debug mode, you will see only error messages. 
Error message: `An error occurred

# Contributing
Please observe the code style of the project and describe the commits.

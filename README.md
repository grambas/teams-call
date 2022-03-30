# teams-call

Shell script to detect when you're on a Microsoft Teams Call.

## Bash script

When calling the script it will exit with 

* 0 if you're on a call
* 1 if you're not

## Teams Log file
!! Important !! Use Microsoft Teams **Preview** version and not Insider. Insider version doesn't generate log file.
Log file path depends on installation method. Possible custom place:
* /home/{USER}/snap/teams/6/.config/Microsoft/Microsoft Teams/logs.txt

## Python script

```python
import teams_call

isInCall = teams_call.isInCall()
```

If you know log file path call direct with argument:
```
python3 teams_call.py "/path/to/logs.txt"
```

## How?

You don't wanna know.

## Seriously... how?

When I connect to a call I see 
`eventData: s::;m::1;a::1` in ~/Library/Application\ Support/Microsoft/Teams/logs.txt and when I disconnect it writes `eventData: s::;m::1;a::3`.
Sad, but you asked for it.
Couldn't find any other way.
Specifically, the GraphQL API for checking the call presence is deprecated since v1.0 and I didn't want to scrape the network traffic or screengrab the status icon.

* eventData: s::;m::1;a::0 call in call + screen is shared
* eventData: s::;m::1;a::1 call started / joined
* eventData: s::;m::1;a::3 call left

## Why?

I couldn't find a script that does this.
Using it to indicate that I'm busy with a status LED outside the office.

![LED in front of my office](led.jpeg)

Using this script in combination with [ControlPlane](https://www.controlplaneapp.com/) to trigger the LED on status change.


## Limitations

Supports macOS and Linux. For Windows, see [this project](https://github.com/EBOOZ/TeamsStatus).

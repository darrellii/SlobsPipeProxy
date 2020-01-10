# SlobsPipeProxy
A python server that serves up the named pipe associated with Stream Labs OBS on your local network.
###### [See documentation on SLOBS named pipe](https://stream-labs.github.io/streamlabs-obs-api-docs/docs/index.html)

## Runing SlobsPipeProxy
* Download `SlobsPipeProxy.py` either by copying/dowloading the file, or forking this repo.
* Make sure you have [Python 3 downloaded](https://www.python.org/downloads/)
* open `Command Prompt` and run `python pathToFile/SlobsPipeProxy.py`


## Using SlobsPipeProxy
Once running you should see something like:
```
Started SLOBS server on port 8000 at 192.168.0.xx
```

Simply send `HTTP POST` or `GET` commands on to that `ip:port` like you would any other `JSONRPC` server.

If SLOBS is not currently running server will return a `404 NOT FOUND`, otherwise expect a `200` along with a body of whatever the pipe returned, reguardless of the pipe returning a `result` or an `error` response.

To close the server press `control + c` in the Command Prompt.
You should see: 
```
^C received, shutting down the SLOBS server
```

# NOTE FROM ME THE DEVELOPER
Thanks for using SlobsPipeProxy!
I'll have an app pushed up pretty soon showing how to use the server.
In the mean time if you have questions HMU on Twitter [@Darrellii](https://www.twitter.com/darrellii) or follow me on Twitch [@Darrellii](https://www.twitch.tv/darrellii)

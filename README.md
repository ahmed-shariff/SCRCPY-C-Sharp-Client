In addiion to what the original author had done, added a python version of the server.

*Note*: The csharp version does not work for me yet.

### To use:

- To run the csharp code:
  - Download the version 1.12.1 of scrcpy and extract in the same directory.
  - Execute the following.
```commands
    dotnet run
```

- To run the python version:
  - Run the `Program.py` script then run the `adb_stuff.cmd`.

CREATEAED IN RSPONSE OF DEBATE AT https://github.com/Genymobile/scrcpy/issues/1073

No jumbeled classes and files liabriries just a simple program.cs file.

# SCRCPY-C-Sharp-Client
https://github.com/qaisbayabani/SCRCPY-C-Sharp-Client


it covers.

multithreading

a single file program.cs converting smooth capture from scrcpy-server to c# client

adb commands using c#

server port opening

reading server received data and forwarding the stream to other port.

opencv capture from network stream and decode H264 stream from android screen capture.
cross plateform stuff.
enjoy

install nuget package opencv sharp and opencv runtime from visual studio 2019 cummunity at my side.

download scrcpy-server-v1.1.12 from https://github.com/Genymobile/scrcpy/releases and rename it as scrcpy-server put in your visual studio projects bin/debug

download android sdk plateform tools from https://developer.android.com/studio/releases/platform-tools and unzip or copy all files in visual studio projects bin/debug

copy program.cs file

change the name of namespace according to ur environment.

run

may have to change the adb commands according to your own environment.
100% smooth capture result.

# THIS REPO WILL BE CLOSED SOON.

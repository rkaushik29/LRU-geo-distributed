# Question C - Geo distributed LRU Cache

*Please read the instructions to run carefully.*

The entire distributed system is simulated on a local machine. The system consists of two programs: `clients.py` and `servers.py`. Click [here](#usage) to see how to run the system.

## Contents

- [Overview](#system-overview)
- [Usage](#usage)
- [Input File](#input-file)
- [Output](#output)


## System Overview
### servers.py
In this file, the servers are set up. There exists a *main server* which contains all the data at the beginning, think of it as a database. Apart from this, you have the choice to set up `M servers` along with their geographical co-ordinates (float type) in the input file. In the local machine, `ports 49152 to 49152 + M` are reserved for each server, which start listening on these ports through `TCP connections` that are set up `concurrently` using servers.py. Initially, the caches in these M servers are empty. After every request from a client, the servers.py file outputs the `cache state of the entire system` in `server_out.txt`. When a server is asked for data, if it does not have it, it will ask the nearest server (`Euclidean distance`) for the data, and so on until it finds the data. This data then gets caches in the server using LRU.

- One improvement to this can be limiting the number of hops in seeking data, as this would increase latency in case the data does not exist.
- A server can be made to keep a list of neighbors that it mostly gets data from, and prioritize exploratory requests to be sent to this one.
- The servers use TCP, this created latency because of the need for `acknowledgements`. Using UDP, depending on the use-case, could reduce latency. 

### clients.py
This script sets up `N clients` at pairs of co-ordinates, and reads the requests that they are making from the input file. These also occupy ports and are bound to them by sockets for TCP connections. The requests are then sent to the nearest server, calculated using `Euclidean distance`. The script outputs the response recieved from the server, along with the data and name of the server.

## Usage
Developed on Python3. This is recommended to run the project.

*Try to close all programs on the computer before running this, since it needs M+N free ports*

- In this directory, first fill out `rohit_kaushik_test.txt` with the server and client information, along with the sequence of requests.
- Run: `python3 servers.py` *first*
- Then, run `python3 clients.py`
- Look at `server_out.txt` for cache info and server status. Look at `client_out.txt` for client outputs including response from servers.
- Note: The servers.py `keeps running` after clients.py finishes running, and clients.py can be run again after changing the input file IFF the schema of the system stays the same.

## Input File
*Important*

Firstly, you can find the `input_format.txt` file which contains examples of the structure and its explanation in this directory.

- The first line of the file *always* has to be of the format `M N R`, where M,N,R are `integers`. M represents the number of servers. N represents number of clients. R represents number of requests. This helps read the file.
- The *next M lines* are of the format `ID x y` where ID is `integer`, x,y are `floats`. These represent `servers` with their ID and co-ordinates on Earth.
- The *next N lines* are of the format `ID x y` where ID is `integer`, x,y are `floats`. These represent `clients` with their ID and co-ordinates on Earth.
- The *next R lines* are of the format `ID S D` where ID is the client ID (`integer`), S is the request name (`string`) and D is the data.

* Note: The `data` used in this system is simply referenced by an id that has a range of `'A' to 'Z' in uppercase only`. These are the only values that can be requested by clients, for the sake of this demo.

## Output
There are two output files:

- `server_out` : This contains the cache state of all servers after each request completes. *Note:* due to code structure, this file has to be cleared manually on every server startup, not to run new requests.
- `client_out` : This contains the data returned by servers to clients, along with which server the response came from. *Note:* due to code structure, this file has to be cleared manually after each execution of clients.py.

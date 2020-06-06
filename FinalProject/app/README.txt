File Transfer App
Shinsaku Segawa

Usage:
1. start network
    ex.  python3 .\network.py -p .\network\ --clean

2. start client and server programs
    python3 client.py
    python3 server.py

    *by default, srever address is Z

3. follow the instruction on client's command line to log in

    ex.
        Type your own address: A
        Type a server address: Z
                :
        Type your login password: asdf

    * the default password is asdf for all client address

4. your file is stored on the sever at 

        server/client_data/(client address)/
    
    the client side files are stored at

        client/my_data/

5. you can use the following commands

    MKD - creating a folder on the server
    RMD - removing a folder from the server
    GWD - presenting the name of the current folder on the server
    CWD - changing the current working folder on the server
    LST  - listing the content of a folder on the server
    UPL - uploading a file to the server	(maximum file size to be determined later)
    DNL - downloading a file from the server (maximum file size to be determined later)
    RMF - removing a file from a folder on the server
    END - end the current session

    To use any of these, simply follow the instruction on the command line

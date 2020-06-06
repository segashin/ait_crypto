# filename: protocols.py
# author: Shinsaku Segawa
# last modified: 2020/4/30

class Protocols():

    def protocol2num(self, current_protocol):
        if current_protocol == "SEP":
            return 0
        if current_protocol == "FMP":
            return 1
        
        return None

    def sep_type2num(self, msg_type):
        if msg_type == "REQ_INIT":
            return 0
        if msg_type == "RES_INIT":
            return 1
        if msg_type == "REQ_LOGIN":
            return 2
        if msg_type == "RES_LOGIN":
            return 3

        return None

    def fmp_type2num(self, cmd_type):
        if cmd_type == "MKD":
            return 0
        elif cmd_type == "RMD":
            return 1
        elif cmd_type == "GWD":
            return 2
        elif cmd_type == "CWD":
            return 3
        elif cmd_type == "LST":
            return 4
        elif cmd_type == "UPL":
            return 5
        elif cmd_type == "DNL":
            return 6
        elif cmd_type == "RMF":
            return 7
        elif cmd_type == "END":
            return 8
        else:
            return -1
# p. 68 
# Grammar: 
# S -> 0 S 1 | 0 1


tokens = "010"
lookahead = tokens[0]


def S():
    if lookahead == "0":
        match("0")
        if lookahead == "1":
            match("1")
        else:
            S()
            match("1")
        
   
    
def match(t):
    global lookahead
    if lookahead == t:
        lookahead = next_element()    
    else:
        raise Exception("reject")
    
    
def next_element():
    global tokens 
    tokens = tokens[1:]
    if tokens:
        return tokens[0]
    
        

if __name__ == "__main__":
    try:
        S()
        if len(tokens) == 0:
            print("string accepted")
        else:
            print("string rejected")
    except Exception:
        print("string rejected")

# p. 68 
# Grammar: S -> +SS | -SS | a

tokens = "-+aaa"
lookahead = tokens[0]

def S():
    global lookahead

    if lookahead == "+":
        match("+")
        S()
        S()
        
    
    if lookahead == "-":
        match("-")
        S()
        S()
        
    
    if lookahead == "a":
        match("a")
    
    else:
        raise Exception("string rejected")
        
        
    
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
    
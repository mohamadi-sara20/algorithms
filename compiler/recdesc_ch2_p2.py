# p. 68 
# Grammar: 
# S -> S'
# S' -> ( S ) S S' | ε

tokens = "(((()))()((((((((((())))))))))))"
lookahead = tokens[0]


def Sp():
    global lookahead

    if lookahead == "(":
        match("(")
        S()
        match(")")
        Sp()
    
    if lookahead is None:
        pass
   

def S():
    Sp()
   
    
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
    
import math
a=10
def eval_loop():
    
    """Prompts from user and evaluates its expressions
       until the user enter done
       entering  values other than numerical operations would throw an error
       can use initialised variables like a"""
    
    while(True):
        decision=raw_input("enter some mathematical operations")
        if(decision=="done"):
            break
        print eval(decision)
        
eval_loop()



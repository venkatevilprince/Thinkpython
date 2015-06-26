prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    
    """changes suffix to uack for O and Q so that it spells correct
       Ouack and Quack"""
    
    if(letter == 'O' or letter ==  'Q'):
        suffix="uack"
    else:
        suffix="ack"    
    print letter + suffix






    

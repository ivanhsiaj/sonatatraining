def r_p_s(p1, p2):
    if(p1 == 'r' and p2 == 'p') or (p1 == 'p' and p2 == 's') or (p1 == 's' and p2 == 'r'):
        return p2
    elif(p1 == 'p' and p2 == 'r') or (p1 == 's' and p2 == 'p') or (p1 == 'r' and p2 == 's'):
        return p1
    else:
        return 'nothing wins,match was tie'

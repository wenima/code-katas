def deadAntCount(ants):
    dead_ants = ants.replace('ant','.')
    return (max(dead_ants.count('a'), dead_ants.count('n'), dead_ants.count('t')))

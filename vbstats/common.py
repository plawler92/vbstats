from types import SimpleNamespace

def get_stats():
    stats = []
    #general
    stats.append(SimpleNamespace(name="dumb errors", tag="dumberrors"))
    stats.append(SimpleNamespace(name="first of second over", tag="firstorsecondover"))
    #attacking
    stats.append(SimpleNamespace(name="kills", tag="kills"))
    stats.append(SimpleNamespace(name="attack errors", tag="attackerrors"))
    stats.append(SimpleNamespace(name="total attacks", tag="totalattacks"))
    #setting
    stats.append(SimpleNamespace(name="assists", tag="assists"))
    stats.append(SimpleNamespace(name="assisterrors", tag="settingerrors"))
    #aces
    stats.append(SimpleNamespace(name="aces", tag="aces"))
    stats.append(SimpleNamespace(name="service attempts", tag="serveattempts"))
    stats.append(SimpleNamespace(name="service errors", tag="serveerrors"))
    #passing
    stats.append(SimpleNamespace(name="reception attempts", tag="receiveattempts"))
    stats.append(SimpleNamespace(name="reception errors", tag="receiveerrors"))
    #defense
    stats.append(SimpleNamespace(name="digs", tag="digs"))
    stats.append(SimpleNamespace(name="dig errors", tag="digerrors")) #issue in db
    #blocks
    stats.append(SimpleNamespace(name="blocks", tag="blocks"))
    stats.append(SimpleNamespace(name="block assists", tag="blockassists")) #issue in db
    stats.append(SimpleNamespace(name="block errors", tag="blockerrors"))
    
    return stats




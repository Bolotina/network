string_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."
def create_data_structure(string_input):
    network = {}
    content = string_input.split('.')
    for line in content:
        if len(line) < 3:
            continue
        if line.find('is connected to') !=-1:
            connections_index = line.find('is connected to')
            connections_length = len('is connected to')
            connections = line[(connections_index + connections_length) : len(line)]
            connections = connections.split(',' ' ')
            updated_connections = []
            for name in connections:
                updated_connections.append(name.strip())
            line = line.split(' ')
            user = line[0]
            if user not in network:
                network[user] = {}
            network[user]['connections'] = updated_connections
        else:
            games_index = line.find('likes to play')
            games_length = len('likes to play')
            games = line[(games_index + games_length) : len(line)]
            games = games.split(',' ' ')
            updated_games = []
            for game in games:
                updated_games.append(game.strip())
            line = line.split(' ')
            user = line[0]
            if user not in network:
                network[user] = {}
            network[user]['games'] = updated_games
    return network

#print create_data_structure(string_input)

def get_connections(network, user):
    if user not in network:
        return None
    else:
        return network[user]['connections']

#print get_connections(create_data_structure(string_input), 'Bryant')

def get_games_liked(network, user):
    if user not in network:
        return None
    else:
        return network[user]['games']

#print get_games_liked(create_data_structure(string_input), 'Bryant')

def add_connection(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    if user_B not in network[user_A]['connections']:
        network[user_A]['connections'].append(user_B)
    return network

#print add_connection(create_data_structure(string_input), 'Walter', 'Jennie')

def add_new_user(network, user, games):
    if user not in network:
        network[user] = {'connections': [], 'games': games}
    return network
#print add_new_user(create_data_structure(string_input), 'Adam', ['Call of Arms', 'Super Mushroom Man'])

def get_secondary_connections(network, user):
    if user not in network:
        return None
    new_secondary_connections=[]
    for connection in get_connections(network, user):
        secondary_connections = get_connections(network, connection)
        if secondary_connections is not None:
            for secondary_connection in secondary_connections:
                if secondary_connection not in new_secondary_connections:
                    new_secondary_connections.append(secondary_connection)
    return new_secondary_connections

#print get_secondary_connections(create_data_structure(string_input), 'John')

def count_common_connections(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    else:
        connections_user_A = get_connections(network, user_A)
        #print connections_user_A
        connections_user_B = get_connections(network, user_B)
        #print connections_user_B
        count = 0
        for connection in connections_user_A:
            if connection in connections_user_B:
                count += 1
        return count

#print count_common_connections(create_data_structure(string_input), 'Bryant', 'Olive')

def find_path_to_friend(network, user_A, user_B, path=[]):
    path = path + [user_A]
    if user_A == user_B:
        return path
    if user_A not in network or user_B not in network:
        return None
    for friend in get_connections(network, user_A):
        if friend not in path:
            newpath = find_path_to_friend(network, friend, user_B, path)
            if newpath: return newpath
    return None
#print find_path_to_friend(create_data_structure(string_input), "John", "Ollie")

def gamers_list(network, game):
    users_list=[]
    for user in network:
        if game in network[user]['games']:
            users_list.append(user)
    return users_list
#print gamers_list(create_data_structure(string_input), 'Dinosaur Diner')


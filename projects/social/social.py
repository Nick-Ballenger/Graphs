import random


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        """
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        for i in range(num_users):
            self.add_user(f'User {i + 1}')
        target_friendships = (num_users * avg_friendships)
        total_friendships = 0
        collisions = 0
        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            if self.add_friendship(user_id, friend_id):
                total_friendships += 2
            else:
                collisions += 1

        print(f'COLLISIONS: {collisions}')

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """

        queue = Queue()
        been_there = {} 
        queue.enqueue([user_id])
        while queue.size() > 0:
            path = queue.dequeue()
            active_friend = path[-1]
            if active_friend not in been_there:
                been_there[active_friend] = path
                for friend_id in self.friendships[active_friend]:
                    new_path = path.copy()
                    new_path.append(friend_id)
                    queue.enqueue(new_path)
        return been_there


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(500, 2)
    print('-----Users-----')
    print(sg.users)
    print('-----Friendships-----')
    print(sg.friendships)
    print('----Social Paths------')
    connections = sg.get_all_social_paths(1)
    print(connections)

    connection_lens = [len(v) for v in connections.values()]

    print('Lengths of all Social Paths')
    print(connection_lens)
    print('Average Lengths of Social Paths')
    print(sum(connection_lens) // len(connection_lens))
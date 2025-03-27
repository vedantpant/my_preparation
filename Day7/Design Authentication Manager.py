class AuthenticatingManager:

    def __init__(self, sessionTimeout):
        self.sessionTimeout = sessionTimeout
        self.users = {}
        self.sessions = {}

    def addUser(self, username, password):
        if username not in self.users:
            self.users[username] = password

    def login(self, username, password, currentTime):
        if username in self.users and self.users[username] == password:
            self.sessions[username] = currentTime + self.sessionTimeout
            return True
        return False

    def logout(self, username):
        if username in self.sessions:
            del self.sessions[username]

    def is_authenticated(self, username, currentTime):
        if username in self.sessions and self.sessions[username] > currentTime:
            return True
        return False

    def remove_expired_sessions(self, currentTime):
        expired_users = [user for user, expiry in self.sessions.items() if expiry <= currentTime]
        for user in expired_users:
            del self.sessions[user]

auth = AuthenticatingManager(10)
auth.addUser('john', 'password123')
print(auth.login('john', 'password123', 1))
print(auth.is_authenticated('john', 5))
print(auth.is_authenticated("john", 12))
auth.remove_expired_sessions(12)

            
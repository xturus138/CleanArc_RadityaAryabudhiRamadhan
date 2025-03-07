class UserUsecase:
    def __init__(self, user_repository):
        self.user_repository = user_repository
    def get_all_users(self):
        return self.user_repository.get_all()
    def create_user(self, user):
        return self.user_repository.create(user)
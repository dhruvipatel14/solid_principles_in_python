# Single Responsibility: A class should have a single responsibility

class UserManager:
    # violation of Single responsibility
    def authentic_user(self, username, password):
        pass

    def update_user_profile(self, user_id, profile_data):
        pass

    def send_email_notifications(self, email, message):
        pass


# separate classes into three different classes based on responsibility: authentication,
# update profile and email notifier

class UserAuthentication:
    def authentic_user(self, username, password):
        pass


class UserProfileManager:
    def update_user_profile(self, user_id, profile_data):
        pass


class EmailNotifier:
    def send_email_notifications(self, email, message):
        pass

from typing import Any


class NotificationCRUD:
    def __init__(self, db:Any) -> None:
        self.db = db

    def add_notification(self, user_id: int, message:str) -> None:
        data = self.db.load_data()
        notifications = data.get("notifications", {})
        if str(user_id) not in notifications:
            notifications[str(user_id)] = []
        
        notifications[str(user_id)].append(message)
        data['notifications'] = notifications
        self.db.save_data(data)

    def get_notifications(self, user_id: int) -> list:
        data = self.db.load_data()
        return data.get("notifications", {}).get(str(user_id), [])
    
    def clear_notifications(self, user_id:int) -> None:
        data = self.db.load_data()
        if str(user_id) in data["notifications"]:
            del data['notifications'][str(user_id)]
            self.db.save_data(data)

    def display_pending_notification(self, user_id : int) -> None:
        notifications = self.get_notifications(user_id)
        if notifications:
            print("\n== MASZ POWIADOMIENIE: ==")
            for message in notifications:
                print(message)
            self.clear_notifications(user_id)
        
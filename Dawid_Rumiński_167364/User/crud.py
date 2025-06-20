from typing import Any 

class UserCRUD: 
    def __init__(self, db:Any) -> None:
        self.db = db

    def find_user_by_id(self, id:int) -> dict | None:
        data = self.db.load_data()
        for user in data['users']:
            if user['id'] == id:
                return user
        return None

    def edit_user(self, updated_user:Any) -> None: 
        data=self.db.load_data()
        for i, user in enumerate(data['users']):
            if user['id'] == updated_user['id']:
                data['users'][i] = updated_user
                break
        self.db.save_data(data)
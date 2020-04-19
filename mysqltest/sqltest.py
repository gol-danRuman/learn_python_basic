from .dbHandler import CodeHubMySqlConnector

if __name__ == "__main__":
    db = CodeHubMySqlConnector().getDB()
    # print(db.delete_instructor_made_assignment(123))

import os
import json

class DatabaseManager:
    def __init__(self, db_path="database"):
        self.db_path = db_path
        os.makedirs(self.db_path, exist_ok=True)

    def create_table(self, table_name):
        table_path = os.path.join(self.db_path, table_name)
        os.makedirs(table_path, exist_ok=True)

    def insert(self, table_name, data):
        self.create_table(table_name)
        record_id = len(os.listdir(os.path.join(self.db_path, table_name))) + 1
        record_path = os.path.join(self.db_path, table_name, f"{record_id}.txt")
        
        if os.path.exists(record_path):
            raise ValueError(f"Registro com ID {record_id} já existe na tabela {table_name}")

        with open(record_path, "w") as f:
            f.write(json.dumps(data, indent=4))
            
        return record_id

    def get(self, table_name, record_id):
        record_path = os.path.join(self.db_path, table_name, f"{record_id}.txt")
        
        if not os.path.exists(record_path):
            return None

        with open(record_path, "r") as f:
            return json.loads(f.read())

    def list_all(self, table_name):
        table_path = os.path.join(self.db_path, table_name)
        
        if not os.path.exists(table_path):
            return []

        records = []
        for file_name in os.listdir(table_path):
            record_id = file_name.replace(".txt", "")
            records.append({"id": record_id, "data": self.get(table_name, record_id)})

        return records

    def delete(self, table_name, record_id):
        record_path = os.path.join(self.db_path, table_name, f"{record_id}.txt")
        
        if os.path.exists(record_path):
            os.remove(record_path)
            return True
        return False
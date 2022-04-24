import mysql.connector

class UseDatabase:
	def __init__(self, config : dict) -> None:
		self.conn = config

	def __enter__(self) -> :
		

	def __exit__(self):
		self.conn.commit()
    	self.cursor.close()
    	self.conn.close()



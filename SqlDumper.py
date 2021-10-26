import pymssql  
import json
from pathlib import Path
import logging

class SqlDumper:
    def __init__(self,env):
        self.env = env
        self.config = {}
        self.context= None
        self.tableNames = [{}]
        self.logger = logging.basicConfig(level = logging.INFO)

    def _LoadConfig(self):
        with open("config.json","r") as f:
            data = json.load(f)
            self.config = data[self.env]
        
    def Connect(self):
        self._LoadConfig();
        x = pymssql.connect(server=self.config["IP"],database=self.config["Database"],user=self.config["User"],password=self.config["Password"])
        self.context = x.cursor(as_dict=True)

    def DumpDb(self,folder,names = None,default = str,ensure_ascii = True):

        names = names  if names != None else self.tableNames

        for name in names:
            value =  name["TABLE_NAME"]

            self.logger.info(f""" Dumping -> {value} table\n""")

            try:
                self.context.execute(f"SELECT * FROM {value}")

                table = self.context.fetchall()
                
                Path(folder).mkdir(parents=True, exist_ok=True)

                with open( f"{folder}/{value}.json","w+") as db:
                    json.dump(table,db,default=default,ensure_ascii= ensure_ascii,)

            except Exception as e:
                self.logger.error(f""" Dumping -> {value} table Failed\n""")

            finally:
                continue
    def GetTablesName(self):
        self.context.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES")
        self.tableNames = self.context.fetchall()
        data = self.tableNames
        return data

        


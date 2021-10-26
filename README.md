# Python SqlDumper:
A Simple python script to dump all your Sql database data

#Configluration: 
A simple config.json where provide connection data:

```json
{
    "Connection" : {
        "IP":"127.0.0.1",
        "Database" : "MyDb",
        "User":"MyUser",
        "Password":"Mypassword!"
    }
}
```

#Usage:

```python

import SqlDumper as Dumper

dumper = Dumper("path/to/config/Connection")

dumper.Connect()

names = dumper.GetTablesName()

dumper.DumpDb(names=names,folder="path/to/folder")

```

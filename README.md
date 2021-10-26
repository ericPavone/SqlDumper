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

from SqlDumper import SqlDumper as Dumper
import helpers


dumper = Dumper("path/to/config/Connection")

dumper.Connect()

_context = dumper.context

names = dumper.GetTablesName(_context)

dumper.DumpDb(names=names,folder="path/to/folder")

```

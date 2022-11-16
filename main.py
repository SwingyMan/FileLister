import csv
import fabric
import re
from tabulate import tabulate
if __name__ == '__main__':
    connection = fabric.Connection("hostname", user="user", port=22, connect_kwargs={"password": "password"})
    result = str(connection.run("ls -la"))
    result = result.splitlines()
    newResult = []
    for x in result[3:-2]:
        newResult.append(re.split("\s+",x))
    head = ["Chmod","PID","User","Owner","Size","Month","Day","Hour","Filename"]
    f = open("export.csv","w")
    csv.writer(f).writerows(newResult)
    print(tabulate(newResult,headers=head))
# config/__init__.py

import pymysql

# Le dice a Django que use PyMySQL en lugar de mysqlclient
pymysql.install_as_MySQLdb()
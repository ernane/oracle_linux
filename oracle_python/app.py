import cx_Oracle

dsn_tns = cx_Oracle.makedsn('127.0.0.1', 1521, service_name='HR')
con = cx_Oracle.connect(user='HR', password='password', dsn=dsn_tns)

print(con.version)
con.close()


import configparser
import hashlib
import pyodbc
import time

import veflat


def connect():
    try:
        init_conf = configparser.ConfigParser()
        init_conf.read('./config.ini')

        config = configparser.ConfigParser()
        config.read(init_conf.get("DB_FILE", "path"))

        host = config.get('server', 'host')
        user = config.get('server', 'user')
        password = config.get('server', 'password')
        port = config.get('server', 'port')
        driver = config.get('server', 'driver')
        database = config.get('server', 'database')

        conn = pyodbc.connect("Driver="+driver+"; "
                          "Server="+host+";Port="+port+";"
                          "Database="+database+";"
                          "uid="+user+";pwd="+password+"")
        return conn
    except Exception as e:
        print("ERROR AL CONECTAR.")
        print(e)
        return None


def login(user, passw, type):
    print("LOGIN ON MODEL.")
    if len(user) > 0:
        conn = connect()
        try:
            passw = hashlib.md5(passw.encode()).hexdigest()

            qry = """SELECT * FROM users WHERE email = '%s' AND password = '%s' """ % (user, passw)
            print(qry)
            cursor = conn.cursor()
            cursor.execute(qry)
            columns = [column[0] for column in cursor.description]
            results = []
            for row in cursor.fetchall():
                results.append(dict(zip(columns, row)))
            if len(results) > 0:

                if "password" in results[0]:
                    del results[0]["password"]
                print(results)
                return {"message": "Usuario correcto", "data": results}
            else:
                return {"message": "Usuario incorrecta"}

        except Exception as e:
            print(e)
            print("EXCEPTION MODEL.")
            if conn is not None:
                conn.close()
            return {}
    else:
        return {}


def register_basic(name, last_name, nickname, email, passw, ip):
    print("REGISTER BASIC .")

    if len(email) > 0 and len(last_name) > 0 and len(passw) > 0 and check_email(email) is None:
        conn = connect()
        try:
            passw = hashlib.md5(passw.encode()).hexdigest()
            cursor = conn.cursor()
            rdate = time.strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute("insert into users("
                           "name, lastname, nickname, email, password, source_ip, email_status, status, create_at, "
                           "email_confirmation_sent_on)"
                           " VALUES "
                           "(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                           name, last_name, nickname.split("@")[0][:16], email, passw, ip, 0, 1, rdate, veflat.random_string(30))

            conn.commit()

        except pyodbc.DatabaseError as err:
            print(err)
            conn.rollback()
            return False
        else:
            conn.commit()
        finally:
            conn.autocommit = True
        return True
    return False


def register_social(name, last_name, nickname, email, ip, social_id):
    print("REGISTER WITH SOCIAL.")
    user_reg = check_social(social_id)
    if user_reg is None:
        if len(email) > 0 and len(last_name) > 0 and len(social_id) > 0:
            conn = connect()
            try:
                #passw = hashlib.md5(passw.encode()).hexdigest()
                cursor = conn.cursor()
                rdate = time.strftime('%Y-%m-%d %H:%M:%S')
                cursor.execute("insert into users("
                               "name, lastname, nickname, email, other_id, source_ip, email_status, status, create_at, "
                               "email_confirmation_sent_on)"
                               " VALUES "
                               "(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                               name, last_name, nickname.split("@")[0][:16], email, social_id, ip, 0, 1, rdate, veflat.random_string(30))

                conn.commit()

                user_reg = check_social(social_id)

            except pyodbc.DatabaseError as err:
                print(err)
                conn.rollback()
                return False
            else:
                conn.commit()
                cursor.close()
                conn.close()
            finally:
                conn.autocommit = True

            return user_reg
        return False
    else:
        return user_reg


def check_social(social_id):
    if len(social_id) > 0:
        conn = connect()
        try:
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM users WHERE other_id = '%s' """ % social_id)

            columns = [column[0] for column in cursor.description]
            results = []
            for row in cursor.fetchall():
                results.append(dict(zip(columns, row)))

            cursor.close()
            conn.close()

            if len(results) > 0:
                return results
            return None
        except:
            if conn is not None:
                conn.close()
            return None


def check_email(email):
    if len(email) > 0:
        conn = connect()
        try:
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM users WHERE email = '%s' """ % email)

            columns = [column[0] for column in cursor.description]
            results = []
            for row in cursor.fetchall():
                results.append(dict(zip(columns, row)))

            if len(results) > 0:
                result = results[0]
            else:
                return None

            cursor.close()
            conn.close()
            return result

        except:

            if conn is not None:
                conn.close()
            return None


def get_user_id(id):
    if len(id) > 0:
        conn = connect()
        try:
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM users WHERE id = '%s' """ % id)

            columns = [column[0] for column in cursor.description]
            results = []
            for row in cursor.fetchall():
                results.append(dict(zip(columns, row)))

            if len(results) > 0:
                result = results[0]
            else:
                return None
            cursor.close()
            conn.close()
            return result

        except:

            if conn is not None:
                conn.close()
            return None

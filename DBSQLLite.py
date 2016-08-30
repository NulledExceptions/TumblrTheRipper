import sqlite3



class DBSQLLite(object):
    def __init__(self):
        self.table_name='tumblr_accounts'
        self.file_name='TumblrDataBase.sqlite'
        self.prim_id='account'



    def createTable(self):
        sqlite_file = self.file_name  # name of the sqlite database file
        table_name2 = self.table_name  # name of the table to be created
        primary_key = self.prim_id  # name of the column
        field_type = 'TEXT'  # column data type

        # Connecting to the database file
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()


        # Creating a second table with 1 column and set it as PRIMARY KEY
        # note that PRIMARY KEY column must consist of unique values!
        c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)' \
                  .format(tn=table_name2, nf=primary_key, ft=field_type))

        # Committing changes and closing the connection to the database file
        conn.commit()
        conn.close()

        return 1


    def addColumnTable(self):
        sqlite_file = self.file_name  # name of the sqlite database file
        table_name = self.table_name  # name of the table to be created
        id_column = 'account'  # name of the PRIMARY KEY column
        id_field = 'account'
        new_column0 = 'date'
        new_column1 = 'current'  # name of the new column
        new_column2 = 'total'  # name of the new column
        column_type = 'INTEGER'  # E.g., INTEGER, TEXT, NULL, REAL, BLOB
        column_type = 'TEXT'
        default_val = '0'  # a default value for the new column rows




        # Connecting to the database file
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()



        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}DEFAULT '{df}'" \
                  .format(tn=table_name, cn=new_column1, ct=column_type,df=default_val))


        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}" \
                  .format(tn=table_name, cn=new_column2, ct=column_type))

        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'" \
                  .format(tn=table_name, cn=new_column0))

        # Committing changes and closing the connection to the database file
        conn.commit()
        conn.close()



    def updateTable(self, name, total, current=0):
        sqlite_file = self.file_name
        table_name = self.table_name
        id_column = 'account'
        column_name = 'total'
        current_column='current'
        date_column='date'


        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        # A) Inserts an ID with a specific value in a second column

        try:
            c.execute("INSERT INTO {tn} ({idf}, {cn},{cn1},{cn2}) VALUES({name}, {total},{current}, DATE('now'))" \
                  .format(tn=table_name, idf=id_column, cn=column_name, cn1=current_column, cn2=date_column))

        except sqlite3.IntegrityError:
            print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))
        else:
            print('success')

        '''
        try:
            c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')". \
                      format(tn=table_name, idf=id_column, cn=column_name))
        except sqlite3.IntegrityError:
            print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))

        # B) Tries to insert an ID (if it does not exist yet)
        # with a specific value in a second column
        c.execute("INSERT OR IGNORE INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')". \
                  format(tn=table_name, idf=id_column, cn=column_name))

        # C) Updates the newly inserted or pre-existing entry
        c.execute("UPDATE {tn} SET {cn}=('Hi World') WHERE {idf}=(123456)". \
                  format(tn=table_name, cn=column_name, idf=id_column))
        '''
        conn.commit()
        conn.close()




    def queryTable(self):
        sqlite_file = self.file_name  # name of the sqlite database file
        table_name = self.table_name  # name of the table to be queried
        id_column = 'account'
        some_id = 123456
        column_2 = 'my_2nd_column'
        column_3 = 'my_3rd_column'

        # Connecting to the database file
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()

        # 1) Contents of all columns for row that match a certain value in 1 column
        c.execute('SELECT * FROM {tn} WHERE {cn}="Hi World"'. \
                  format(tn=table_name, cn=column_2))
        all_rows = c.fetchall()
        print('1):', all_rows)

        # 2) Value of a particular column for rows that match a certain value in column_1
        c.execute('SELECT ({coi}) FROM {tn} WHERE {cn}="Hi World"'. \
                  format(coi=column_2, tn=table_name, cn=column_2))
        all_rows = c.fetchall()
        print('2):', all_rows)

        # 3) Value of 2 particular columns for rows that match a certain value in 1 column
        c.execute('SELECT {coi1},{coi2} FROM {tn} WHERE {coi1}="Hi World"'. \
                  format(coi1=column_2, coi2=column_3, tn=table_name, cn=column_2))
        all_rows = c.fetchall()
        print('3):', all_rows)

        # 4) Selecting only up to 10 rows that match a certain value in 1 column
        c.execute('SELECT * FROM {tn} WHERE {cn}="Hi World" LIMIT 10'. \
                  format(tn=table_name, cn=column_2))
        ten_rows = c.fetchall()
        print('4):', ten_rows)

        # 5) Check if a certain ID exists and print its column contents
        c.execute("SELECT * FROM {tn} WHERE {idf}={my_id}". \
                  format(tn=table_name, cn=column_2, idf=id_column, my_id=some_id))
        id_exists = c.fetchone()
        if id_exists:
            print('5): {}'.format(id_exists))
        else:
            print('5): {} does not exist'.format(some_id))

        # Closing the connection to the database file
        conn.close()


    def dateTime(self):
        sqlite_file = 'my_first_db.sqlite'  # name of the sqlite database file
        table_name = 'my_table_3'  # name of the table to be created
        id_field = 'id'  # name of the ID column
        date_col = 'date'  # name of the date column
        time_col = 'time'  # name of the time column
        date_time_col = 'date_time'  # name of the date & time column
        field_type = 'TEXT'  # column data type

        # Connecting to the database file
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()

        # Creating a new SQLite table with 1 column
        c.execute('CREATE TABLE {tn} ({fn} {ft} PRIMARY KEY)' \
                  .format(tn=table_name, fn=id_field, ft=field_type))

        # A) Adding a new column to save date insert a row with the current date
        # in the following format: YYYY-MM-DD
        # e.g., 2014-03-06
        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'" \
                  .format(tn=table_name, cn=date_col))
        # insert a new row with the current date and time, e.g., 2014-03-06
        c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES('some_id1', DATE('now'))" \
                  .format(tn=table_name, idf=id_field, cn=date_col))

        # B) Adding a new column to save date and time and update with the current time
        # in the following format: HH:MM:SS
        # e.g., 16:26:37
        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'" \
                  .format(tn=table_name, cn=time_col))
        # update row for the new current date and time column, e.g., 2014-03-06 16:26:37
        c.execute("UPDATE {tn} SET {cn}=TIME('now') WHERE {idf}='some_id1'" \
                  .format(tn=table_name, idf=id_field, cn=time_col))

        # C) Adding a new column to save date and time and update with current date-time
        # in the following format: YYYY-MM-DD HH:MM:SS
        # e.g., 2014-03-06 16:26:37
        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'" \
                  .format(tn=table_name, cn=date_time_col))
        # update row for the new current date and time column, e.g., 2014-03-06 16:26:37
        c.execute("UPDATE {tn} SET {cn}=(CURRENT_TIMESTAMP) WHERE {idf}='some_id1'" \
                  .format(tn=table_name, idf=id_field, cn=date_time_col))

        # The database should now look like this:
        # id         date           time        date_time
        # "some_id1" "2014-03-06"   "16:42:30"  "2014-03-06 16:42:30"

        # 4) Retrieve all IDs of entries between 2 date_times
        c.execute("SELECT {idf} FROM {tn} WHERE {cn} BETWEEN '2013-03-06 10:10:10' AND '2015-03-06 10:10:10'". \
                  format(idf=id_field, tn=table_name, cn=date_time_col))
        all_date_times = c.fetchall()
        print('4) all entries between ~2013 - 2015:', all_date_times)

        # 5) Retrieve all IDs of entries between that are older than 1 day and 12 hrs
        c.execute("SELECT {idf} FROM {tn} WHERE DATE('now') - {dc} >= 1 AND DATE('now') - {tc} >= 12". \
                  format(idf=id_field, tn=table_name, dc=date_col, tc=time_col))
        all_1day12hrs_entries = c.fetchall()
        print('5) entries older than 1 day:', all_1day12hrs_entries)

        # Committing changes and closing the connection to the database file
        conn.commit()
        conn.close()

    def infoTable(self):
        import sqlite3

        sqlite_file = self.file_name
        table_name = self.table_name

        # Connecting to the database file
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()

        # Retrieve column information
        # Every column will be represented by a tuple with the following attributes:
        # (id, name, type, notnull, default_value, primary_key)
        c.execute('PRAGMA TABLE_INFO({})'.format(table_name))

        # collect names in a list
        names = [tup[1] for tup in c.fetchall()]
        print(names)
        # e.g., ['id', 'date', 'time', 'date_time']

        # Closing the connection to the database file
        conn.close()



    '''




    Here is a quick overview of all data types that are supported by SQLite 3:

    INTEGER: A signed integer up to 8 bytes depending on the magnitude of the value.
    REAL: An 8-byte floating point value.
    TEXT: A text string, typically UTF-8 encoded (depending on the database encoding).
    BLOB: A blob of data (binary large object) for storing binary data.
    NULL: A NULL value, represents missing data or an empty cell.






    # Creating a new SQLite table with 1 column
        c.execute('CREATE TABLE {tn} ({nf} {ft})' \
                  .format(tn=table_name1, nf=new_field, ft=field_type))




    # A) Adding a new column without a row value
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
            .format(tn=table_name, cn=new_column1, ct=column_type))

    # B) Adding a new column with a default row value
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} DEFAULT '{df}'"\
            .format(tn=table_name, cn=new_column2, ct=column_type, df=default_val))












    def connect(sqlite_file):
        """ Make connection to an SQLite database file """
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        return conn, c

    def close(conn):
        """ Commit changes and close connection to the database """
        # conn.commit()
        conn.close()

    def total_rows(cursor, table_name, print_out=False):
        """ Returns the total number of rows in the database """
        c.execute('SELECT COUNT(*) FROM {}'.format(table_name))
        count = c.fetchall()
        if print_out:
            print('\nTotal rows: {}'.format(count[0][0]))
        return count[0][0]

    def table_col_info(cursor, table_name, print_out=False):
        """ Returns a list of tuples with column informations:
            (id, name, type, notnull, default_value, primary_key)
        """
        c.execute('PRAGMA TABLE_INFO({})'.format(table_name))
        info = c.fetchall()

        if print_out:
            print("\nColumn Info:\nID, Name, Type, NotNull, DefaultVal, PrimaryKey")
            for col in info:
                print(col)
        return info

    def values_in_col(cursor, table_name, print_out=True):
        """ Returns a dictionary with columns as keys and the number of not-null
            entries as associated values.
        """
        c.execute('PRAGMA TABLE_INFO({})'.format(table_name))
        info = c.fetchall()
        col_dict = dict()
        for col in info:
            col_dict[col[1]] = 0
        for col in col_dict:
            c.execute('SELECT ({0}) FROM {1} WHERE {0} IS NOT NULL'.format(col, table_name))
            # In my case this approach resulted in a better performance than using COUNT
            number_rows = len(c.fetchall())
            col_dict[col] = number_rows
        if print_out:
            print("\nNumber of entries per column:")
            for i in col_dict.items():
                print('{}: {}'.format(i[0], i[1]))
        return col_dict


    if __name__ == '__main__':

        sqlite_file = 'my_first_db.sqlite'
        table_name = 'my_table_3'

        conn, c = connect(sqlite_file)
        total_rows(c, table_name, print_out=True)
        table_col_info(c, table_name, print_out=True)
        values_in_col(c, table_name, print_out=True) # slow on large data bases

        close(conn)




Default tutorial

Copy Pasted from / http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html#unique_indexes
'''
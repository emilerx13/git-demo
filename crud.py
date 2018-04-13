import sqlite3
conn = sqlite3.connect('test.db')

c = conn.cursor()
try:
    c.execute("CREATE TABLE customerTable (id, name, email, address, 
city)")
    print("Could'n find the table making a new table")
except:
    print('Table allready exist')

def main():

    print ('1. Create')
    print ('2. Read')
    print ('3. Update')
    print ('4. Delete')
    print ('5. exit')

    user = int (input ('Choose a number: '))

    if user == 1:
        create()
        # Save (commit) the changes
        conn.commit()
    elif user == 2:
        read()
    elif user == 3:
        update()
        conn.commit()
    elif user == 4:
        delete()
        conn.commit()
    elif user == 5:
        # We can also close the connection if we are done with it.
        conn.close()
        exit()
    main()

def create():
    # Insert a row of data
    user_id = int (input ('id: '))
    name = input ('name: ')
    email = input ('email: ')
    address = input ('address: ')
    city = input ('city: ')
    c.execute("INSERT INTO customerTable values (?, ?, ?, ?, ?)", (user_id, name, email, address, city))

def read():
    where = input ('What do you want to select?: ')
    result = c.execute("Select %s from customerTable" % (where))
    rows = c.fetchall()

    for row in rows:
        print(row)

def update():
    with conn:
        change = int (input ('What id do you want to change: '))
        new = int (input ('new id: '))
        name = input ('new name: ')
        email = input ('new email: ')
        address = input ('new address: ')
        city = input ('new city: ')
        c.execute("""UPDATE customerTable SET id = %s, name = '%s', email = '%s', address = '%s', city = '%s' WHERE id = %s """ %(new ,name, email, address, city, change))

def delete():
    delete = int (input ('What id do you want to delete: '))
    c.execute("DELETE FROM customerTable WHERE id = %s" %(delete))
    
main()

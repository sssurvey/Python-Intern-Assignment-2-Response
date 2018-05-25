# Haomin Shi
# 05/25/2018
# Response to the assignment 2, task 2

import mysql.connector
from intercom.client import Client
# intercom = https://github.com/intercom/python-intercom
import requests
from requests.auth import HTTPBasicAuth
"""
 MySQL table overview

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `email` varchar(120) NOT NULL
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
def solution_by_client(): # for this function, using the python intercom module
    # since I cannot test this, please look at this as pseudo code
    # 1. connect to the mySQL DB of Monument Labs
    cnx = mysql.connector.connect(user='Admin', password='password',
                                  host='localhost',
                                  database='MonumentLabsDB')
    # 2. query the db
    cursor = cnx.cursor()
    query = ("SELECT id, name, email FROM user ")
    cursor.execute(query)
    rows = cursor.fetchall()
    # 3. load the table to construct list of user element
    rowarray_list = []
    for row in rows:
        t = (row.id, row.name, row.email)
        rowarray_list.append(t)

    '''
    rowarray_list
    [
        [
            1123,
            "John Doh",
            "jd102201@mail.com"
        ],
        ...
    '''
    cnx.close() # disconnect from db, everything about user recorded in a list of list

    # 5. connect to intercom via python-intercom module...
    intercom = Client(personal_access_token='my_personal_access_token')
    # for access token, reference: https://developers.intercom.com/docs/personal-access-tokens

    # 6. looping through the list based on the Monument labs "user" table
    # e.g: owarray_list[1][0] = id, rowarray_list[1][1] = name, rowarray_list[1][2] = email
    for element in rowarray_list:
        intercom.users.create(id = element[0], name = element[1], email = element[2])
    # since table already specify not NULL, I dont need to worry about null value
    # ref: https://developers.intercom.com/reference#user-model
    return True

def solution_without_client(): #for this function, without the python intercom module
    # for connect to the intercom
    users_url = 'https://api.intercom.io/users'
    app_id = 'YOUR_APP_ID'
    api_key = 'YOUR_API_KEY'
    # since I cannot test this, please look at this as pseudo code
    # 1. connect to the mySQL DB of Monument Labs
    cnx = mysql.connector.connect(user='Admin', password='password',
                                  host='localhost',
                                  database='MonumentLabsDB')
    # 2. query the db
    cursor = cnx.cursor()
    query = ("SELECT id, name, email FROM user ")
    cursor.execute(query)
    rows = cursor.fetchall()
    # 3. load the table to construct list of list, each sublist is a user
    rowarray_list = []
    for row in rows:
        t = (row.id, row.name, row.email)
        rowarray_list.append(t)
    cnx.close()

    # 4. loop through the rowarray_list to create user on intercom
    for element in rowarray_list:
        data = {'id': element[0],
                'name': element[1], 'email': element[2]}
        requests.post(users_url, data=data, auth=HTTPBasicAuth(api_id, api_key))
    
def main():
    solution_by_client() # with python intercom module
    solution_without_client() # without python intercom module

if __name__ == "__main__":
    main()
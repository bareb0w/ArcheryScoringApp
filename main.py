import sqlite3

# define connection and cursor


def setup():
    with sqlite3.connect('Scoring.db') as connection:

        cursor = connection.cursor()


        # Creating the table for the scores
        command = '''CREATE TABLE IF NOT EXISTS
        scores(id INTERGER PRIMARY KEY, round TEXT, score INTERGER, notes TEXT, status TEXT,
        arrow_values TEXT)'''

        cursor.execute(command)


        # Creating the table for the default rounds
        command = '''CREATE TABLE IF NOT EXISTS
        defaultRounds(id INTERGER PRIMARY KEY, round TEXT, distances TEXT, arrowPerEnd INT, targetFace STR)'''

        cursor.execute(command)


        # Creating the table for the user added rounds
        command = '''CREATE TABLE IF NOT EXISTS
        userRounds(id INTERGER PRIMARY KEY, round TEXT, distances TEXT, arrowPerEnd INT, targetFace STR)'''

        cursor.execute(command)

        # Creating the table for the user metrics
        command = '''CREATE TABLE IF NOT EXISTS
        weekMetrics(id INTERGER PRIMARY KEY, week_begining TEXT, arrow_count INT, sessions INT)'''

        cursor.execute(command)

setup()

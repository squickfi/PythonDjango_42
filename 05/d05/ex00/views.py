import psycopg2
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


def init(request):
    try:
        connection = psycopg2.connect(
            dbname='djangotraining',
            user='djangouser',
            password='secret',
            host='127.0.0.1',
            port='5432',
        )
        try:
            curs = connection.cursor()
            curs.execute("""
                CREATE TABLE IF NOT EXISTS ex00_movies(
                    title VARCHAR(64) UNIQUE NOT NULL,
                    episode_nb INT PRIMARY KEY,
                    opening_crawl TEXT,
                    director VARCHAR(32) NOT NULL,
                    producer VARCHAR(128) NOT NULL,
                    release_date DATE NOT NULL
                    );
                """)
            curs.execute('commit')
            curs.close()
        except Exception as e:
            connection.close()
            return e
        connection.close()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)

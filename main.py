import requests
from typing import Text
import mysql.connector
import mysql
import time
import psycopg2
from flask import jsonify

from api_temp_request import GetTemperatureFromApi, requests, json, jsonpickle
from os import system

from power_stove_calculate import Calculation
from pgadmin_configuration import PgDatabase


class StoveControl:
    print(
        "Witaj w aplikacji sterującej piecem, pamiętaj że aplikacja wymaga dostępu do sieci!!!\n"
    )
    clear = lambda: system("clear")  # terminal clear
    clear()

    # /// *** create objects *** \\\

    try:  # internet fault connection

        api_info = GetTemperatureFromApi(  # create object and assignment values for GetTempFromApi
            # response info
            json.loads(
                requests.get(
                    "http://api.weatherapi.com/v1/current.json?key=6135b0d4cfec4f9c8eb195114210305&q=Katowice&aqi=no"
                ).text
            ),
            # data1, Value in database table 'water_temp'
            json.loads(
                requests.get(
                    "http://api.weatherapi.com/v1/current.json?key=6135b0d4cfec4f9c8eb195114210305&q=Katowice&aqi=no"
                ).text
            )["current"]["temp_c"],
            # data2, day in database table 'water_temp'
            json.loads(
                requests.get(
                    "http://api.weatherapi.com/v1/current.json?key=6135b0d4cfec4f9c8eb195114210305&q=Katowice&aqi=no"
                ).text
            )["location"]["localtime"],
        )

        api_data = str(api_info.data2)
        api_value = str(api_info.data1)

        conf_connect_to_pgadmin = PgDatabase(
            "qpnlppia",
            "qpnlppia",
            "3cnRcv179qn8ON6arJ6TzPfImB2UsMtX",
            "batyr.db.elephantsql.com",
            "5432",
            "id",
            api_info.data2,
            api_info.data2,
        )

        # temperature power stove calcution create object
        power_calc = Calculation(0)
        temp_celcius = api_info.data1

        # /// *** define main app functions *** \\\

        try:  # to correct, not working when database not start

            @staticmethod
            def get_connection_wth_database(
                connect_to_database,
            ):  # connect database function

                connection = mysql.connector.connect(
                    user=connect_to_database.user,
                    password=connect_to_database.password,
                    host=connect_to_database.host,
                    database=connect_to_database.database,
                    auth_plugin=connect_to_database.auth_plugin,
                )

                if connection.is_connected():
                    return connection, print(
                        "!pomyślnie połączono z bazą danych!|\n".upper()
                    )
                else:
                    return connection

                connection.close()

        except mysql.connector.errors.DatabaseError:
            print("\nbłąd połączenia z bazą danych\n".upper())

        @staticmethod
        def connect_to_pgadmin(api_data, api_value):

            DB_NAME = "qpnlppia"
            DB_USER = "qpnlppia"
            DB_PASS = "3cnRcv179qn8ON6arJ6TzPfImB2UsMtX"
            DB_HOST = "batyr.db.elephantsql.com"
            DB_PORT = "5432"

            try:
                conn = psycopg2.connect(
                    database=DB_NAME,
                    user=DB_USER,
                    password=DB_PASS,
                    host=DB_HOST,
                    port=DB_PORT,
                )

                print("Pomyślnie połączono z bazą danych")

            except:
                print("Błąd połączenia z bazą danych")

            return conn

        @staticmethod
        def put_values_to_db(api_data, api_value):

            DB_NAME = "qpnlppia"
            DB_USER = "qpnlppia"
            DB_PASS = "3cnRcv179qn8ON6arJ6TzPfImB2UsMtX"
            DB_HOST = "batyr.db.elephantsql.com"
            DB_PORT = "5432"

            try:
                conn = psycopg2.connect(
                    database=DB_NAME,
                    user=DB_USER,
                    password=DB_PASS,
                    host=DB_HOST,
                    port=DB_PORT,
                )

                print("Pomyślnie połączono z bazą danych")

            except:
                print("Błąd połączenia z bazą danych")

            cur = conn.cursor()

            insert_query = (
                """INSERT INTO archive_temp(temp_data, temp_value) VALUES (%s,%s)"""
            )
            insert_values = (api_data, api_value)

            cur.execute(insert_query, insert_values)
            conn.commit()

            print("Archiwizowanie temperetury w DB zakończone sukcesem")
            conn.close()

        @staticmethod
        def return_temp_from_json(day_data, day_value):

            print(
                "\ntemperatura w Katowicach w dniu".upper(),
                day_value,
                "to",
                day_data,
                "°C\n",
            )

        def power_stove_calcution(self, calc_power, api_t):

            if api_t >= 20.0:
                calc_power = 10
            elif api_t < 20.0 and api_t > 15.0:
                calc_power = 25
            elif api_t <= 15.0 and api_t > 10.0:
                calc_power = 38
            elif api_t <= -10.0 and api_t > 5.0:
                calc_power = 50
            elif api_t <= 5.0 and api_t > 0.0:
                calc_power = 60
            elif api_t <= 0.0 and api_t > -10.0:
                calc_power = 75
            elif api_t <= -10.0 and api_t > -20.0:
                calc_power = 88
            elif api_t <= -20.0:
                calc_power = 100

            self.power_calc.temp_calc = calc_power
            print(
                "\ntemperatura na zewnątrz to: ".upper(),
                self.api_info.data1,
                "°C\n",
                "\npraca pieca w trybie automatycznym aktywna, ustawiono moc pieca na:".upper(),
                int(self.power_calc.temp_calc),
                "%\n".upper(),
            )

        def stove_manual_control(self, calc_power):
            print("test")
            self.power_calc.temp_calc = calc_power
            print("Praca w trybie manual na:", str(calc_power))

        @staticmethod
        def return_json_info(json_information):
            print(json_information)

    except requests.exceptions.ConnectionError:
        print("\n|!Błąd połączenia z internetem, sprawdź połączanie sieciowe!|".upper())

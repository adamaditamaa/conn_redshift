
import os
import redshift_connector as rnn
from datetime import datetime, timedelta
import pandas as pd
from sqlalchemy import create_engine
import warnings
warnings.filterwarnings("ignore")

from dotenv import load_dotenv



# Load environment variables from the .env file
load_dotenv()


def connect_redshift():
    host_redshift = os.getenv('ip_redshift')
    database_redshift = os.getenv('db_redshift')
    port_redshift = os.getenv('port')
    user_redshift = os.getenv('username_redshift')
    password_redshift = os.getenv('pwd_redshift')

    conn_redshift = rnn.connect(
        host=host_redshift,
        database=database_redshift,
        port=int(port_redshift),
        user=user_redshift,
        password=password_redshift
    )
    return conn_redshift






















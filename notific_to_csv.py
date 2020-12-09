import os
import settings

from sqlalchemy import create_engine
import pandas as pd




engine = create_engine(
    "postgresql://{}:{}@{}:{}/{}".format(
        settings.PSQL_USER,
        settings.PSQL_PASSWORD,
        settings.PSQL_HOST,
        settings.PSQL_PORT,
        settings.PSQL_DB,
    )
)

def main():
    """
    """

    sql = (
        '''
        SELECT dt_notific,dt_sin_pri,dt_digita, cid10_codigo FROM "Municipio"."Notificacao" 
        WHERE municipio_geocodigo = 3304557 AND ano_notif > 2017;
        '''
        )

    df = pd.read_sql(sql, con=engine)

    return df.to_csv('notific_to_csv2.csv')


if __name__ == "__main__":
    main()
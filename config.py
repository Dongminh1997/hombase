import clickhouse_connect

user = 'minhquanghaidong'
password = 'qdstyPOz65xD'
host = 'ep-holy-leaf-714342.ap-southeast-1.aws.neon.tech'
port = 5432

ch_host = 'cypr4zyjjk.us-east-1.aws.clickhouse.cloud'
ch_username='default'
ch_password = 'fOl8uGQ~F4yOD'
ch_port = 8443

create_table_sql = ('''
    CREATE TABLE "winequality_red" (
        "volatile_acidity" FLOAT,
        "citric_acid" FLOAT,
        "chlorides" FLOAT,
        "total_sulfur_dioxide" INT,
        "density" FLOAT,
        "sulphates" FLOAT,
        "alcohol" FLOAT,
        "quality" VARCHAR
    ) 
''')

insert_table_sql = ("INSERT INTO winequality_red (volatile_acidity, citric_acid, chlorides, total_sulfur_dioxide, density, sulphates, alcohol, quality) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)")

def get_connection(user, password, host, port, database='postgres'):
    connection = "postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database)
    return connection
    
def get_client(ch_host, ch_port, ch_username, ch_password):
    client = clickhouse_connect.get_client(host=ch_host, port=ch_port, username=ch_username, password=ch_password)
    return client
from config import *

client = get_client(ch_host, ch_port, ch_username, ch_password)

#1. Count distinct unique value in column total_sulfur_dioxide
sql1 = '''SELECT COUNT(DISTINCT total_sulfur_dioxide) FROM winequality_red;'''
result1 = client.command(sql1)
print(result1)

#2. Average citric_acid by quality 
sql2 = '''SELECT quality, AVG(citric_acid) FROM winequality_red GROUP BY quality'''
result2 = client.command(sql2)
print(result2)
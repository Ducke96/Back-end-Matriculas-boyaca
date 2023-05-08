from flask import Flask, render_template, request, redirect, url_for, flash ,jsonify
from flask_mysqldb import MySQL
import json
from flask_cors import CORS

# initializations
app = Flask(__name__)
  
CORS(app)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'datosmatricula'
mysql = MySQL(app)
# settings
app.secret_key = "mysecretkey"


# routes
@app.route('/')

def Index():

    cur = mysql.connection.cursor()
    cur.execute('SELECT NOMBRE_ESTABLECIMIENTO , sum(TOTAL_MATRICULA) as TOTAL_MATRICULA_C FROM dataframe GROUP BY NOMBRE_ESTABLECIMIENTO ORDER BY TOTAL_MATRICULA_C desc;')
   
    data = cur.fetchall()
    row_headers=[x[0] for x in cur.description]
    print(row_headers)
    
    cur.close() 
    
    json_data=[]

    for result in data:
        print(result)
        data_dit = {}
        for i in range(len(row_headers)):
            data_dit[row_headers[i]] = result[i]
        
        json_data.append(data_dit)

    s = json.dumps(json_data)
    s = s.replace('\\"', '')

    return  jsonify(s)




@app.route('/api/first_question/' , methods = ['GET'])
def get_json():
    cur = mysql.connection.cursor()
    cur.execute('SELECT NOMBRE_ESTABLECIMIENTO , sum(TOTAL_MATRICULA) as TOTAL_MATRICULA_C FROM dataframe GROUP BY NOMBRE_ESTABLECIMIENTO ORDER BY TOTAL_MATRICULA_C desc;')
   
    
    row_headers=[x[0] for x in cur.description]
    print(row_headers)
    data = cur.fetchall()
    cur.close() 
    
    json_data=[]

    for result in data:
        json_data.append(dict(zip(row_headers,result)))

    
    response = json_data
   

    return response








@app.route('/api/second_question/' , methods = ['GET'])
def second_question():
    cur = mysql.connection.cursor()
    cur.execute('SELECT ZONA , sum(TOTAL_MATRICULA) as TOTAL_MATRICULA FROM dataframe GROUP BY ZONA ORDER BY TOTAL_MATRICULA desc;')
   
    
    row_headers=[x[0] for x in cur.description]
    print(row_headers)
    data = cur.fetchall()
    cur.close() 
    
    json_data=[]

    for result in data:
      
        json_data.append(dict(zip(row_headers,[result[0],int(result[1])])))

    
    response = json_data
   

    return response





@app.route('/api/third_question/' , methods = ['GET'])
def third_question():
    cur = mysql.connection.cursor()
    cur.execute('SELECT ANNO_INF AS anio , GRADO AS nivel_formacion , SUM(TOTAL_MATRICULA) as graduados FROM dataframe GROUP BY GRADO,ANNO_INF ORDER BY graduados,GRADO ASC;')
   
    
    row_headers=[x[0] for x in cur.description]
    print(row_headers)
    data = cur.fetchall()
    cur.close() 
    
    json_data=[]

    for result in data:
        json_data.append(dict(zip(row_headers,result)))

    
    response = json_data
   

    return response






@app.route('/api/fourth_question/' , methods = ['GET'])
def fourth_question():
    cur = mysql.connection.cursor()
    cur.execute('SELECT  GRADO as programa_academico , SUM(TOTAL_MATRICULA) as graduados FROM dataframe GROUP BY GRADO ORDER BY graduados desc;')
   
    
    row_headers=[x[0] for x in cur.description]
    print(row_headers)
    data = cur.fetchall()
    cur.close() 
    
    json_data=[]

    for result in data:
        json_data.append(dict(zip(row_headers,result)))

    
    response = json_data
   

    return response






@app.route('/api/fifth_question/' , methods = ['GET'])
def fifth_question():
    cur = mysql.connection.cursor()
    cur.execute('SELECT  MUNICIPIO as departamento_domicilio_ies , SUM(TOTAL_MATRICULA) as graduados FROM dataframe GROUP BY MUNICIPIO ORDER BY graduados DESC;')
   
    
    row_headers=[x[0] for x in cur.description]
    print(row_headers)
    data = cur.fetchall()
    cur.close() 
    
    json_data=[]

    for result in data:
         json_data.append(dict(zip(row_headers,[result[0],int(result[1])])))

    
    response = json_data
   

    return response







@app.route('/api/sixth_question/' , methods = ['GET'])
def sixth_question():
    cur = mysql.connection.cursor()
    cur.execute('SELECT  ANNO_INF as anio ,  TIPO_JORNADA as metodologia ,COUNT(TOTAL_MATRICULA) as cantidad_ies FROM dataframe GROUP BY TIPO_JORNADA,anio ;')
   
    
    row_headers=[x[0] for x in cur.description]
    print(row_headers)
    data = cur.fetchall()
    cur.close() 
    
    json_data=[]

    for result in data:
        json_data.append(dict(zip(row_headers,[result[0], result[1],int(result[2])])))

    
    response = json_data
   

    return response









@app.route('/api/seventh_question/' , methods = ['GET'])
def seventh_question():
    cur = mysql.connection.cursor()
    cur.execute('SELECT  NOMBRE_ESTABLECIMIENTO	 as departamento_domicilio_ies , SUM(TOTAL_MATRICULA) as graduados FROM dataframe GROUP BY NOMBRE_ESTABLECIMIENTO ORDER BY graduados DESC;')
   
    
    row_headers=[x[0] for x in cur.description]
    print(row_headers)
    data = cur.fetchall()
    cur.close() 
    
    json_data=[]

    for result in data:
        json_data.append(dict(zip(row_headers,result)))

    
    response = json_data
   

    return response





# starting the app
if __name__ == "__main__":
    app.run(port=8000, debug=True)

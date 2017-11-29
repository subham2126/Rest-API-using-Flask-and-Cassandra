from flask import Blueprint,Flask,request
import json
from cassandra.cluster import Cluster
cluster = Cluster(["127.0.0.1"])

api = Blueprint('api', __name__,url_prefix='/module');


class myClass:
    @api.route('/login')
    def login_in():
        session = cluster.connect('tutorialspoint')
        rows = session.execute('SELECT emp_id, emp_city, emp_name FROM emp')
        rows_as_dict = []
        for row in rows:
            temp = {
                'id' : row.emp_id,
                'city' : row.emp_city,
                'name' : row.emp_name}
            rows_as_dict.append(temp)
            #print (row.emp_id, row.emp_city, row.emp_name)
        return ((json.dumps(rows_as_dict)));
    @api.route('/signup')
    def sign_up():
        return 'signup!'

    @api.route("/sumNumber",methods=['POST'])
    def doSum():
        a = int(json.loads(request.data)['a'])
        b = int(json.loads(request.data)['b'])
        
        return str(a+b)
    
    @api.route("/insertData",methods=['post'])
    def doInsert():
        id = int(json.loads(request.data)['id'])
        city= json.loads(request.data)['city']
        name = json.loads(request.data)['name']
        session = cluster.connect('tutorialspoint')
        session.execute(
        """
        INSERT INTO emp (emp_id, emp_city, emp_name)
        VALUES (%s, %s, %s)
        """,
        (id, city, name)
        )
        return "SUCCESS"
    @api.route('/search')
    def search():
        id_search = (request.args['x'])
        session = cluster.connect('tutorialspoint')
        rows = session.execute("SELECT emp_id, emp_city, emp_name FROM emp WHERE emp_id=" + id_search)
        rows_as_dict = []
       
        
        for row in rows:

            temp = {
                'id' : row.emp_id,
                'city' : row.emp_city,
                'name' : row.emp_name}
            
            rows_as_dict.append(temp)
            
            #print (row.emp_id, row.emp_city, row.emp_name)
        return ((json.dumps(rows_as_dict)))
    
    




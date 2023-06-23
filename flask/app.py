from flask import Flask, render_template, request, session, redirect, url_for, Response, jsonify,flash
import cv2
from PIL import Image
import mysql.connector
import numpy as np
import os
import time
from datetime import date
from config import config
from flask_mysqldb import MySQL
from models.ModelUser import ModelUser
from models.entities.User import User  
from datetime import datetime, timedelta
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from datetime import datetime, timedelta
from flask_cors import CORS
import glob

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret'
db= MySQL(app)
CORS(app)

cnt = 0
pause_cnt = 0
justscanned = False

login_manager_app = LoginManager(app)
jwt = JWTManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user  = User(0, request.form['email'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                access_token = create_access_token({'id': logged_user.id,
                    'email': logged_user.email,
                    'fullname': logged_user.fullname,
                    'exp': str(datetime.utcnow() + timedelta(days=7))})
                return jsonify({
                    'token': access_token,}) 
            else:
                return jsonify({"error": "Sai mat khau"}), 401 
        else:
            return jsonify({"error": "Khong tim thay tai khoan"}), 401
    else:
        return jsonify({"error": ""}), 401

@app.route('/class', methods = ['GET'])
def list_class():
    try:
        l_class = db.connection.cursor()
        sql = "SELECT id, name_class, course FROM class"
        l_class.execute(sql)
        datos = l_class.fetchall()
        l_class = []
        for i in datos:
            classes = {'id': i[0], 'class': i[1], 'coursre': i[2]}
            l_class.append(classes)
        return jsonify(l_class)
    except Exception as ex:
        return jsonify({'mess': "Error"})
    
@app.route('/classdetails/<id>', methods = ['GET'])  
def classdetails(id):
    try:
        l_class = db.connection.cursor()
        sql = "SELECT name_class, course FROM class WHERE id = {}".format(id)
        l_class.execute(sql)
        datos = l_class.fetchall()
        l_class = {}
        for i in datos:
            l_class = {'class': i[0], 'coursre': i[1]}
        return jsonify(l_class)
    except Exception as ex:
        return jsonify({'mess': "Error"}) 
    
@app.route('/addclass', methods = ['GET','POST'])
def  addclass():
    if request.method == 'POST':
        nameclass = request.form['nameclass']
        course = request.form['course']   
        con = db.connection.cursor()
        sql = "insert into class (name_class, course) value (%s,%s)"
        con.execute(sql,[nameclass, course])
        db.connection.commit()
        con.close()
        return jsonify({'mess': "Thanh cong"})
    return jsonify({'mess': "That bai"}) 
    
@app.route("/deleteClass/<id>", methods = ['GET', 'POST'])
def deleteClass(id):
    con = db.connection.cursor()
    sql = "DELETE FROM class WHERE id = (%s)"     
    con.execute(sql, (id,))
    db.connection.commit()
    con.close()
    return jsonify({'mess': "Thanh cong"}) 

@app.route('/studentclass/<id>', methods = ['GET', 'POST'])
def studentclass(id):
    try:
        con = db.connection.cursor()
        sql = ("select  a.mssv, a.idclass, b.sv_name, b.sv_class, b.email, a.id"
                     " from studentclass a"
                     " left join qlsv b on b.mssv = a.mssv"
                     " left join class c on a.idclass = c.id"
                     " where c.id = (%s)")
        con.execute(sql, (id,))
        data = con.fetchall()
        student_class = []
        for i in data:
            student_classes = {'mssv': i[0], 'idclass': i[1], 'name': i[2], 'class': i[3], 'email': i[4], 'id':i[5]}
            student_class.append(student_classes)
        return jsonify(student_class)
    except Exception as ex:
        return jsonify({'mess': "Error"})

@app.route('/addstudentclass/<id>', methods = ['GET','POST'])
def  addstudentclass(id):
    if request.method == 'POST':
        idclass = id
        mssv = request.form.get('mssv') 
        con = db.connection.cursor()
        sql = "insert into studentclass (mssv, idclass) value (%s,%s)"
        con.execute(sql,[mssv, idclass])
        db.connection.commit()
        con.close()
        return jsonify({'mess': "Thanh cong"})
    return jsonify({'mess': "That bai"}) 

@app.route("/deleteStdClass/<id>", methods = ['GET', 'POST'])
def deleteStdClass(id):
    con = db.connection.cursor()
    sql = "DELETE FROM studentclass WHERE id = (%s)"     
    con.execute(sql, (id,))
    db.connection.commit()
    con.close()
    return jsonify({'mess': "Thanh cong"}) 

@app.route('/loadDataClass/<id>', methods = ['GET', 'POST'])
def loadDataClass(id):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="datn"
    )
    mycursor = mydb.cursor()
    sql = ("select a.accs_id, a.accs_prsn, b.sv_name, b.sv_class, date_format(a.accs_added, '%Y-%m-%d'), date_format(a.accs_added, '%H:%i') "
                     " from accs_hist a "
                     " left join qlsv b on a.accs_prsn = b.mssv "
                     " left join studentclass c on b.mssv = c.mssv"
                     " left join class d on c.idclass = d.id"
                     " where a.accs_date = curdate() and d.id = (%s)"
                     " order by 1 desc")
    mycursor.execute(sql, (id,))
    data = mycursor.fetchall()
    statistic = []
    for i in data:
            statistics = {'mssv': i[1], 'name': i[2], 'class': i[3], 'date': i[4],'time': i[5]}
            statistic.append(statistics)
    return jsonify(statistic)
#Face>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="datn"
)
mycursor = mydb.cursor() 
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Generate dataset >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def generate_dataset(nbr):
    face_classifier = cv2.CascadeClassifier("./resources/haarcascade_frontalface_default.xml")
    def face_cropped(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        # scaling factor=1.3
        # Minimum neighbor = 5
        if faces is ():
            return None
        for (x, y, w, h) in faces:
            cropped_face = img[y:y + h, x:x + w]
        return cropped_face
 
    cap = cv2.VideoCapture(0)
 
    mycursor.execute("select ifnull(max(img_id), 0) from img_dataset")
    row = mycursor.fetchone()
    lastid = row[0]
 
    img_id = lastid
    max_imgid = img_id + 50 
    count_img = 0
 
    while True:
        ret, img = cap.read()
        if face_cropped(img) is not None:
            count_img += 1
            img_id += 1
            face = cv2.resize(face_cropped(img), (200, 200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
 
            file_name_path = "dataset/"+nbr+"."+ str(img_id) + ".jpg"
            cv2.imwrite(file_name_path, face)
            cv2.putText(face, str(count_img), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
 
            mycursor.execute("""INSERT INTO `img_dataset` (`img_id`, `img_sv`) VALUES
                                ('{}', '{}')""".format(img_id, nbr))
            mydb.commit()
 
            frame = cv2.imencode('.jpg', face)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
 
            if cv2.waitKey(1) == 13 or int(img_id) == int(max_imgid):
                break
                cap.release()
                cv2.destroyAllWindows()


def generate_dataset_img(nbr):
    face_classifier = cv2.CascadeClassifier("D:/DATN/DiemDanhSV/flask/resources/haarcascade_frontalface_default.xml")
 
    def face_cropped(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        # scaling factor=1.3
        # Minimum neighbor = 5
 
        if faces is ():
            return None
        for (x, y, w, h) in faces:
            cropped_face = img[y:y + h, x:x + w]
        return cropped_face
 
    mycursor.execute("select ifnull(max(img_id), 0) from img_dataset")
    row = mycursor.fetchone()
    lastid = row[0]
 
    img_id = lastid
    max_imgid = img_id + 20 
    count_img = 0
    
    var = 2
    folder = glob.glob("D:/DATN/Data_Face/Dinh Trong Hieu_212129_assignsubmission_file_/2115207/*.jpg")
    while True:
        for file in folder:
            imgg = cv2.imread(file , cv2.IMREAD_UNCHANGED)
            img = cv2.resize(imgg,  (550, 600))
            print(file)  
            cv2.waitKey(1000)
            cv2.destroyAllWindows() 
            if face_cropped(img) is not None:
                count_img += 1
                img_id += 1
                
                face = cv2.resize(face_cropped(img), (200, 200))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
 
                file_name_path = "dataset/"+nbr+"."+ str(img_id) + ".jpg"
                cv2.imwrite(file_name_path, face)
                cv2.putText(face, str(count_img), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                mycursor.execute("""INSERT INTO `img_dataset` (`img_id`, `img_sv`) VALUES
                            ('{}', '{}')""".format(img_id, nbr))
                mydb.commit()
 
                frame = cv2.imencode('.jpg', face)[1].tobytes()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        print(img_id)
        print(max_imgid)
        if cv2.waitKey(1) == 13 or int(img_id) >= int(max_imgid):
            break
            cv2.destroyAllWindows()
            
 
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Train Classifier >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/train_classifier/<nbr>')
def train_classifier(nbr):
    dataset_dir = "./dataset"
    path = [os.path.join(dataset_dir, f) for f in os.listdir(dataset_dir)]
    faces = []
    ids = []
    for image in path:
        img = Image.open(image).convert('L')
        imageNp = np.array(img, 'uint8')
        id = int(os.path.split(image)[1].split(".")[1])
 
        faces.append(imageNp)
        ids.append(id)
    ids = np.array(ids)
    # Train the classifier and save
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces, ids)
    clf.write("classifier.xml")
 
    return redirect('/')
 
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Face Recognition >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def face_recognition():  # generate frame by frame from camera
    def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
        global justscanned
        global pause_cnt
        pause_cnt += 1
        coords = []
        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            id, pred = clf.predict(gray_image[y:y + h, x:x + w])
            confidence = int(100 * (1 - pred / 300))
            if confidence > 70 and not justscanned:
                global cnt
                cnt += 1
                n = (100 / 30) * cnt
                # w_filled = (n / 100) * w
                w_filled = (cnt / 30) * w
                cv2.putText(img, str(int(n))+' %', (x + 20, y + h + 28), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (153, 255, 255), 2, cv2.LINE_AA)
                cv2.rectangle(img, (x, y + h + 40), (x + w, y + h + 50), color, 2)
                cv2.rectangle(img, (x, y + h + 40), (x + int(w_filled), y + h + 50), (153, 255, 255), cv2.FILLED)
                mycursor.execute("select a.img_sv, b.sv_name, b.sv_class "
                                 " from img_dataset a "
                                 " left join qlsv b on a.img_sv = b.mssv "
                                 " where img_id = " + str(id))
                row = mycursor.fetchone()
                pnbr = row[0]
                pname = row[1]
                pskill = row[2]
                if int(cnt) == 30:
                    cnt = 0
                    mycursor.execute("insert into accs_hist (accs_date, accs_prsn) values('"+str(date.today())+"', '" + pnbr + "')")
                    mydb.commit()
                    cv2.putText(img, pname + ' | ' + pskill, (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (153, 255, 255), 2, cv2.LINE_AA)
                    time.sleep(1)
 
                    justscanned = True
                    pause_cnt = 0
            else:
                if not justscanned:
                    cv2.putText(img, 'UNKNOWN', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2, cv2.LINE_AA)
                else:
                    cv2.putText(img, ' ', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2,cv2.LINE_AA)
 
                if pause_cnt > 80:
                    justscanned = False
 
            coords = [x, y, w, h]
        return coords
    def recognize(img, clf, faceCascade):
        coords = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 0), "Face", clf)
        return img
 
    faceCascade = cv2.CascadeClassifier("./resources/haarcascade_frontalface_default.xml")
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.read("classifier.xml")
 
    wCam, hCam = 400, 400
 
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
 
    while True:
        ret, img = cap.read()
        img = recognize(img, clf, faceCascade)
        frame = cv2.imencode('.jpg', img)[1].tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        key = cv2.waitKey(1)
        if key == 27:
            break
 
 
 
@app.route('/')
def home():
    mycursor.execute("select mssv, sv_name, sv_class bh from qlsv")
    data = mycursor.fetchall()
 
    return render_template('index.html', data=data)


@app.route('/sv', methods = ['GET'])
def sv():
    mycursor.execute("select mssv, sv_name,email, sv_class from qlsv")
    data = mycursor.fetchall()
    listsinhvien = []
    for i in data:
        list = {'mssv': i[0], 'name': i[1], 'email': i[2], 'class': i[3] }
        listsinhvien.append(list)
    return jsonify(listsinhvien)


@app.route('/addprsn')
def addprsn():
    mycursor.execute("select ifnull(max(mssv) + 0, 0)  from qlsv")
    row = mycursor.fetchone()
    nbr = row[0]
    # print(int(nbr))
 
    return render_template('addprsn.html', newnbr=int(nbr))
 
@app.route('/addprsn_submit', methods=['POST'])
def addprsn_submit():
    mssv = request.form.get('mssv')
    namesv = request.form.get('txtname')
    emailsv = request.form.get('txtemail')
    classsv = request.form.get('class')
 
    mycursor.execute("""INSERT INTO `qlsv` (`mssv`, `sv_name`, `email`, `sv_class`) VALUES
                    ('{}', '{}', '{}', '{}')""".format(mssv, namesv, emailsv, classsv))
    mydb.commit()
 
    # return redirect(url_for('home'))
    return redirect(url_for('vfdataset_page', prs=mssv))
 
@app.route('/vfdataset_page/<prs>')
def vfdataset_page(prs):
    return render_template('gendataset.html', prs=prs)
 
@app.route('/vidfeed_dataset/<nbr>')
def vidfeed_dataset(nbr):
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(generate_dataset(nbr), mimetype='multipart/x-mixed-replace; boundary=frame')
 
@app.route('/video_feed')
def video_feed():
    # Video streaming route. Put this in the src attribute of an img tag
    return Response(face_recognition(), mimetype='multipart/x-mixed-replace; boundary=frame')
 
@app.route('/fr_page')
def fr_page():
    """Video streaming home page."""
    mycursor.execute("select a.accs_id, a.accs_prsn, b.sv_name, b.sv_class, a.accs_added "
                     "  from accs_hist a "
                     "  left join qlsv b on a.accs_prsn = b.mssv "
                     " where a.accs_date = curdate() "
                     " order by 1 desc")
    data = mycursor.fetchall()
 
    return render_template('fr_page.html', data=data)
 
 
@app.route('/countTodayScan')
def countTodayScan():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="datn"
    )
    mycursor = mydb.cursor()
 
    mycursor.execute("select count(*) "
                     "  from accs_hist "
                     " where accs_date = curdate() ")
    row = mycursor.fetchone()
    rowcount = row[0]
 
    return jsonify({'rowcount': rowcount})
 
 
@app.route('/loadData', methods = ['GET', 'POST'])
def loadData():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="datn"
    )
    mycursor = mydb.cursor()
 
    mycursor.execute("select a.accs_id, a.accs_prsn, b.sv_name, b.sv_class, date_format(a.accs_added, '%H:%i:%s') "
                     " from accs_hist a "
                     " left join qlsv b on a.accs_prsn = b.mssv "
                     " where a.accs_date = curdate() "
                     " order by 1 desc")
    data = mycursor.fetchall()
 
    return jsonify(response = data)
  
if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()
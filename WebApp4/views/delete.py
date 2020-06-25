from flask import Blueprint, render_template, redirect
import pymysql as db

delete_blueprint = Blueprint('delete', __name__)

@delete_blueprint.route('/list')

def delete():
    # 데이터 베이스 접속
    conn = db.connect(host='192.168.44.46',
                      user='kdw',
                      password='1234',
                      db='kdw',
                      charset='utf8')

    # 쿼리문 실행 객체 생성
    cur = conn.cursor()

    # 쿼리문 실행
    sql = "DELETE FROM `USER3` WHERE `uid`= '%s'"
    cur.execute(sql)
    conn.commit()

    # 데이터 베이스 종료
    conn.close()

    return redirect('/list')
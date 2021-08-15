import psycopg2
import mysql.connector

class Db_value_get():
    def __init__(self):
        self.maxdb = psycopg2.connect(
            host="",
            port=,
            user="",
            password="",
            database="",
        )

    def db_scan_task_get_limit_10(self):
        cur = self.maxdb.cursor()
        cur.execute("select job_id, plan_id, resource_id, task_state FROM scan_task ORDER BY job_id desc limit 10")
        rows = cur.fetchall()
        for result in rows:
            print("job_id: ", result[0])
            print("plan_id: ", result[1])
            print("resource_id: ", result[2])
            print("task_state: ", result[3])

        self.maxdb.close()

    def db_scan_task_get_last1(self):
        cur = self.maxdb.cursor()
        cur.execute("select job_id, plan_id, resource_id, task_state FROM scan_task ORDER BY job_id desc limit 1")
        rows = cur.fetchall()
        for result in rows:
            result_list = ["job_id: ", result[0], "plan_id: ", result[1], "resource_id: ", result[2],
                           "task_state: ", result[3]]
            print(result_list)

            result_dic = {"job_id" : result[0], "plan_id" : result[1], "resource_id" : result[2],
                           "task_state" : result[3]}
            print(result_dic['job_id'])

        self.maxdb.close()

if __name__ == "__main__":
    db = Db_value_get()
    db.db_scan_task_get_last1()


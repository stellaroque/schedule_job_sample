import time
import schedule

def task():
    print("Tarefa executada!")

schedule.every(5).seconds.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)

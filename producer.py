from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')


def main():
    result = app.send_task("xworker.run_chord", args=[], kwargs={"x":2,"y":2,"x1":2,"y1":2})
    print("Chord task initiated. Waiting for results...")
    print("Result:", result)
    

if __name__ == '__main__':
    main()

from celery import Celery, chord, signature

app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

@app.task(bind=True, name='xworker.add')
def add(self, x, y):
    return x + y

@app.task(bind=True, name='xworker.multiply')
def multiply(self, x, y):
    return x * y

@app.task(bind=True, name='xworker.chord_callback')
def chord_callback(self, results):
    total = sum(results)
    return f"Chord callback executed. Total: {total}" 



@app.task(bind=True, name='xworker.run_chord')
def run_chord(self, *args, **kwargs):
    x = kwargs.get("x"); y = kwargs.get("y")
    x1 = kwargs.get("x1"); y1 = kwargs.get("y1")

    tasks = [ signature('xworker.add', args=[x, y]), 
              signature('xworker.multiply', args=[x1, y1])]
      
    result = chord(tasks)(chord_callback.s())
    return result




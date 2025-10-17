from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configurar CORS para permitir conexión con el frontend (puerto 5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tasks = [
    {"id": 1, "title": "Diseñar interfaz", "status": "pendiente"},
    {"id": 2, "title": "Definir API", "status": "pendiente"},
    {"id": 3, "title": "Conectar backend", "status": "progreso"},
    {"id": 4, "title": "Configurar Vite", "status": "completado"}
]

@app.get("/")
def home():
    return {"message": "Servidor Kanban activo y funcionando correctamente"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def add_task(task: dict):
    task["id"] = len(tasks) + 1
    tasks.append(task)
    return {"message": "Tarea agregada correctamente", "task": task}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: dict):
    for task in tasks:
        if task["id"] == task_id:
            task.update(updated_task)
            return {"message": "Tarea actualizada", "task": task}
    return {"error": "Tarea no encontrada"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return {"message": "Tarea eliminada"}

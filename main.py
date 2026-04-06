from fastapi import FastAPI
 
app = FastAPI()
 
users = []
 
@app.get('/hello')
def add_user(name ,password):
    users.append({
        'username': name,
        'age': password
    })
    return users
 
 
@app.get('/delete')

def del_user(name):
    for user in users:
        if user['username'] == name:
            users.remove(user)
            return {"message": " User deleted Successfully"}
        return {"message": "User not Found"}
 
@app.get('/all')
def get_all():
    return users
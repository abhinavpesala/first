from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

# 1. This endpoint serves a visual HTML Form to the user
@app.get("/", response_class=HTMLResponse)
async def get_form():
    return """
    <html>
        <body>
            <h2>Enter Your Details</h2>
            <form action="/submit" method="post">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    """

# 2. This endpoint handles the submitted Form data
@app.post("/submit")
async def handle_form(name: str = Form(...)): # <-- Form(...) tells FastAPI to read form data
    return {"message": f"Successfully received form input name: {name}"}

if __name__ == "__main__":
    uvicorn.run("application:app", host="127.0.0.1", port=7780, reload=True)

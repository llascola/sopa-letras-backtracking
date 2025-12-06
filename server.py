from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sopa_letras 

app = FastAPI()

class PuzzleRequest(BaseModel):
    words: list[str]
    size: int = 15  
    complexity: int = 0

@app.post("/generate-puzzle")
async def generate(request: PuzzleRequest):
    try:
        grid = sopa_letras.create_grid(request.words, request.size, request.complexity)

        if grid == []: 
            raise HTTPException(status_code=400, detail="No se pudo generar la sopa de letras") 
        
        return {
            "status": "success",
            "grid": grid,
            "words_placed": request.words
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"message": "Word Search API is running!"}
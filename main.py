
# Commit 1 — Basic API Setup

# This commit should include:

# - A working FastAPI application
# - At least one GET endpoint
# - Proper project structure
# - Use of:

#   - Asynchronous route functions
#   - Query parameters OR path parameters
#   - Basic response handling

# The API should return a meaningful JSON response and should be runnable locally.



# from fastapi import FastAPI,HTTPException , Query
# import uvicorn

# app = FastAPI()


# @app.get('/users',status_code=201)
# async def get(Name:str , ID:int =Query(...,gt=0) ):
#     try:
#         if len(Name) < 2:
#             raise HTTPException(status_code= 404 , detail= 'Nayal Is Awesome')
#         return {'Name':Name , 'ID':ID}
#     except HTTPException:
#         raise
#     except Exception as e:
#         raise HTTPException(status_code= 500 , detail=str(e))
 
 
# @app.get('/')
# async def get():
#     return {'Message':'Hello World'}

       
# if __name__ == "__main__":
#     uvicorn.run(app = 'main:app',host = '0.0.0.0' , port = 8000 , reload =True )




# Commit 2 — API Expansion & Structure

# In this commit, you must extend the API by adding:

# - Additional endpoints (GET and/or POST)
# - Request and response models using Pydantic
# - Proper distinction between:

#   - Path parameters
#   - Query parameters
#   - Request body
# - Custom error handling using appropriate HTTP status codes
# - At least one example of dependency injection

# You should also organize routes using routers to keep the code modular and readable.



from fastapi import FastAPI
import uvicorn
from api.routes.user import router as user_route
from api.routes.items  import router as items_route
from api.routes.joke import router as joke_route
app = FastAPI()

app.include_router(user_route)
app.include_router(items_route)
app.include_router(joke_route)
   
if __name__ == "__main__":
    uvicorn.run(app = 'main:app',host = '0.0.0.0' , port = 8000 , reload =True )




# Commit 3 — External API Integration & Refinement

# In the final commit, you must:

# - Integrate one external public API (read-only usage is sufficient)
# - Consume the external API asynchronously
# - Process and return a clean, structured response to the client
# - Handle possible failure cases (e.g., external API failure, invalid input)

# This commit should demonstrate:

# - Proper async handling
# - Robust error handling
# - Clean separation of logic

# Important Notes
# - Do not use a database.
# - Do not use any AI or code generation tools.
# - Focus on clarity, correctness, and incremental improvement.

# Note: This task is meant to assess how you think and build, not just whether the API runs.
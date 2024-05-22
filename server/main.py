import time
from fastapi import FastAPI, Request, Response
import uvicorn
from routers import router

app = FastAPI(dependencies=[])


@app.middleware("http")
async def logging_middleware(request: Request, call_next) -> Response:
    start_time = time.perf_counter_ns()
    response = await call_next(request)
    end_time = time.perf_counter_ns()
    duration = (end_time - start_time) / 1000000
    print(
        "request recieved",
        {
          "request":{
            "method": request.method,
            "path": request.url.path,
            "headers": dict(request.headers),
            "query_params": dict(request.query_params),
            "ip": request.client.host,
          }
        },
        {
          "response":{
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "ms": duration,
            "lol":"lololo------"
          }
        }
    )
    return response


app.include_router(router, prefix="/api", tags=["frankenstein"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

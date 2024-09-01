import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.function_name(name='HttpTrigger')
@app.route('api/HttpTrigger')
def main(req: func.HttpRequest) ->str:
    return 'Hello, World!'
import json
def no_auth_handler(event,context):
  return{    "statusCode":200,    "body":json.dumps({      "message":"hello world",    }),  }
def auth_handler(event,context):
  return{    "statusCode":200,    "body":json.dumps({      "message":"hello world with auth",    }),  }

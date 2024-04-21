#!C:/Users/91934/AppData/Local/Programs/Python/Python311-32/python.exe
import os.path

print("content-type: text/html \r\n\r\n")
import pymysql, cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="restaraunt")
cur = con.cursor()
print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard|Admin</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.2/css/fontawesome.min.css">
</head>
<style>

   .navbar-nav1{
            position: absolute;
            right: 90px;
            top:10px;
            list-style: none;
        }
        .navbar-nav1 li img{
          position:relative;
          right:70px;
          bottom:40px;
        }

    .list-group a:hover {
        color: crimson;
    }   
    .mail-wrapper{
       display:flex;
       justify-content:center;
       align-items:center;
       height:100vh;
    }
    .form-log{
    border: 2px solid black;
            border-radius: 10px;
            width: 500px;
            padding: 20px;
            height: 570px;
            box-shadow: 2px 2px 6px black;
    }
</style>

<body>
    <section id="nav">
        <div class="d-flex" id="dash">
            <nav class="navbar navbar-collapse navbar-dark bg-success fixed-top">
                <div class="container-fluid">
                    <a href="#" class="navbar-brand fs-3 mt-0 fw-bold">
                        <span
                            class="bi bi-grid-1x2-fill d-inline-block fs-3 me-2 align-top text-danger"></span>Dash<span
                            class="text-danger">Board</span>
                    </a>

                    <button class="navbar-toggler me-0 mt-0" type="button" data-bs-toggle="offcanvas"
                        data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar"
                        aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <ul class="navbar-nav1 ml-auto justify-content-end flex-grow-1 pe-1">
                        <li class="nav-item dropdown">
                            <a href="#" class="nav-link dropdown-toggle second-text text-white fw-bold fs-5 mt-2"
                                id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                <i class="bi bi-person fs-4 me-2"></i>Admin
                            </a>
                            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                                <li><a href="#" class="dropdown-item">Profile</a></li>
                                <li><a href="#" class="dropdown-item">Settings</a></li>
                                <li><a href="Homepage.py" class="dropdown-item" onclick="lgout()">Logout</a></li>
                            </ul>
                        </li>
                         <li><img src="./images/profile.jpg" width="50px" height="50px" class="rounded-circle" alt="..."></li>
                    </ul>


                    <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasNavbar"
                        aria-labelledby="offcanvasNavbarLabel">
                        <div class="offcanvas-header">
                            <h5 class="offcanvas-title mt-1 fs-4" id="offcanvasNavbarLabel"> <span
                                    class="bi bi-person d-inline-block fs-4 mt-0 align-top"></span>Hi Admin</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="offcanvas"
                                aria-label="Close"></button>
                        </div>

                        <div class="offcanvas-body navbar-collapse" id="offcanvasNavbar">
                            <ul class="navbar-nav ml-auto justify-content-end flex-grow-1 pe-1">
                                <div class="list-group list-group-flush my-3">
                                    <a href="admindashboard.py"
                                        class="list-group-item list-group-item-action bg-hover second-text text hover fs-5"
                                        id="dashboard">
                                        <i class="bi bi-journals me-2"></i>Branches
                                    </a>
                                    <a href="admincustomers.py"
                                        target="_self" class="list-group-item list-group-item-action bg-hover second-text fs-5">
                                        <i class="bi bi-person me-2"></i>Customers
                                    </a>
                                    <a href="adminmenus.py"
                                        class="list-group-item list-group-item-action bg-hover second-text fs-5">
                                        <i class="bi bi-menu-button me-2"></i>Menus
                                    </a>
                                    <a href="#"
                                        class="list-group-item list-group-item-action active bg-hover second-text fs-5">
                                        <i class="bi bi-menu-button me-2"></i>Delivery Mail Message
                                    </a>
                                    <a href="Homepage.py"
                                        class="list-group-item list-group-item-action bg-hover text-danger fw-bold fs-5 mt-5" onclick="lgout()">
                                        <i class="bi bi-box-arrow-right me-2" ></i>Logout
                                    </a>
                                </div>
                            </ul>
                        </div>
                    </div>
                </div>
            </nav>
        </div>
    </section>
    <section id="mails">
        <div class="container">
         <div class="mail-wrapper">
             <div class="form-log">
              <form action="#" class="was-validated" id="demo" method="post" name="login1">
                   <h2 class="text-center">Mail <i class="bi bi-envelope text-danger"></i> </h2>
                    <div class="input-box" class="form-group">
                        <label for="Username">Customer Name <i class="bi bi-person"></i></label>
                        <input type="username" id="user" value="" name="name" placeholder="Enter the name"
                            autocomplete="off" class="form-control" required>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                    </div>
                    <div class="input-box" class="form-group">
                          <label for="email">To Email <i class="bi bi-envelope"></i></label>
                          <input type="email" id="emn" name="em" placeholder="To email"
                            class="form-control" required>
                          <div class="valid-feedback">Valid.</div>
                          <div class="invalid-feedback">Please fill out this field.</div>
                        </div>
                    <div class="input-box" class="form-group">
                       <label for="text"> Body of MailBox <i class="bi bi-envelope"></i></label>
                      <textarea name="textarea1" id="text1" cols="50" rows="10" autofocus
                            placeholder="Drop your comments in mailbox!"></textarea>
                    </div>
                       
                     <button type="submit" value="submit" name="sub" class="btn btn-success w-100">Mail Send</button>
                </form>
             </div>
          </div>
        </div>


    
<script>
    function lgout(){
      alert("Logging out!!")
    }
</script>
</body>

</html>
""")
import pymysql, cgi, cgitb, smtplib

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="restaraunt")
cur = con.cursor()

form = cgi.FieldStorage()
Name = form.getvalue("name")
Email = form.getvalue("em")
mailbox =form.getvalue("textarea1")
Submit = form.getvalue("sub")
if Submit != None:
    p = """ insert into msend(name,mailid,mailbox) values('%s','%s','%s')""" % (Name,Email,mailbox)
    cur.execute(p)
    con.commit()
    fromadd = 'harishbalaji016@gmail.com'
    password = 'vvkw rfzc tbfg bhpk'
    toadd = Email
    subject = mailbox
    body = "Hello{}".format(Name)
    msg = """subject: {} \n\n{}""".format(subject, body)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(fromadd, password)
    server.sendmail(fromadd, toadd, msg)
    server.quit()
    print("""
       <script>
          alert("Mail send successfully")
       </script>
    """)


p = """select * from msend"""
cur.execute(p)
res = cur.fetchall()
print("""
<div class="container">
 <table border="2px"class="table table-striped" style="width:100%;position:relative; top: 50px;">
  <tr>
    <th>S.no</th>
    <th>Name</th>
    <th>Email id</th>
    <th>Mail box</th>
    <th>Regdate</th>
</div>
""")

for i in res:
         print("""
            <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            </tr>
            """ % (i[0], i[1], i[2], i[3], i[4]))
con.close()
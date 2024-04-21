#!C:/Users/91934/AppData/Local/Programs/Python/Python311-32/python.exe
import os.path

print("content-type: text/html \r\n\r\n")
import pymysql, cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="restaraunt")
cur = con.cursor()
form=cgi.FieldStorage()
idd=form.getvalue("id")
s="""select * from userlogin where id=%s """%(idd)
cur.execute(s)
v=cur.fetchall()
for i in v:
    print("""
    <!DOCTYPE html>
    <html lang="en">

    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User|Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css">
    <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.2/css/fontawesome.min.css">
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

        #userlg {
            display: flex;
            justify-content: center;
            align-items: center;
            height:120vh;
        }

        .orderdetails {
            padding: 20px;
            border: 2px solid black;
            border-radius: 20px;
        }
    </style>

    </head>
    
    <body>
    <section id="nav">
        <div class="d-flex" id="dash">
            <nav class="navbar navbar-collapse navbar-dark bg-success fixed-top">
                <div class="container-fluid">
                    <a href="#" class="navbar-brand fs-3 mt-0 fw-bold">
                        <span
                            class="bi bi-grid-1x2-fill d-inline-block fs-3 me-2  align-top text-danger"></span>Dash<span
                            class="text-danger">Board</span>
                    </a>

                    <button class="navbar-toggler me-0 mt-0" type="button" data-bs-toggle="offcanvas"
                        data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar"
                        aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <ul class="navbar-nav1 ml-auto justify-content-end flex-grow-1 pe-1">
                        <li class="nav-item dropdown">
                            <a href="#" class="nav-link dropdown-toggle second-text text-white fw-bold fs-5 mt-0"
                                id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                <i class="bi bi-person fs-4 me-2"></i>User
                            </a>
                            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                                <li><a href="user_profile.py?id=%s" class="dropdown-item">Profile</a></li>
                                <li><a href="#" class="dropdown-item">Settings</a></li>
                                <li><a href="./user_login.py" class="dropdown-item" onclick="lgout()">Logout</a></li>
                            </ul>   
                        </li>
                       <li><img src="./images/profile.jpg" width="50px" height="50px" class="rounded-circle" alt="..."></li>
                    </ul>
    """%(idd))
    print("""
     <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasNavbar"
                        aria-labelledby="offcanvasNavbarLabel">
                        <div class="offcanvas-header">
                            <h5 class="offcanvas-title mt-1 fs-4" id="offcanvasNavbarLabel"> <span
                                    class="bi bi-person d-inline-block fs-4 mt-0 align-top"></span>Hi <span class="text-success">User</span></h5>
                            <button type="button" class="btn-close" data-bs-dismiss="offcanvas"
                                aria-label="Close"></button>
                        </div>

                        <div class="offcanvas-body navbar-collapse" id="offcanvasNavbar">
                            <ul class="navbar-nav ml-auto justify-content-end flex-grow-1 pe-1">
                                <div class="list-group list-group-flush my-3">
                                    <a href="user_branch.py?id=%s"
                                        class="list-group-item list-group-item-action bg-hover second-text text hover fs-5"
                                        id="dashboard">
                                        <i class="bi bi-journals me-2"></i>Branches
                                    </a>
                                    <a href="#"
                                        class="list-group-item list-group-item-action active bg-hover bg-default second-text text hover fs-5"
                                        id="dashboard">
                                        <i class="bi bi-cart me-2"></i>Food Order
                                    </a>
                                    <a href="usermenu.py?id=%s"
                                        class="list-group-item list-group-item-action bg-hover second-text fs-5">
                                        <i class="bi bi-menu-button me-2"></i>Menus
                                    </a>
                                    <a href="user_login.py"
                                        class="logout list-group-item list-group-item-action bg-hover text-danger fw-bold fs-5 mt-5"
                                        onclick="lgout()">
                                        <i class="bi bi-box-arrow-right me-2"></i>Logout
                                    </a>
                                </div>
                            </ul>"""%(idd,idd))
    print("""
                        </div>
                    </div>
                </div>
            </nav>
        </div>
    </section>

    <section id="userlg" class="bg-secondary">
        <div class="order">
            <div class="orderdetails">
                <h2 class="text-center text-white">Menu <span class="text-danger">Orders</span></h2>
                <form action="#" class="was-validated" id="demo" method="post" name="order">
                    <div class="input-box" class="form-group">
                        <label for="emn">Name <i class="bi bi-person"></i></label>
                        <input type="username" name="text" id="txt" value="" placeholder="Enter your name"
                            autocomplete="off" class="form-control" required>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                    </div>
                    <div class="input-box" class="form-group">
                        <label for="text">Choose your food Orders <i class="bi bi-card-checklist"></i></label>
                           <select name="food" id="cars" class="w-100" class="form-control">
                               <option value="chicken65">Chicken65</option>
                               <option value="mbriyani">Mutton briyani</option>
                               <option value="cbriyani">Chicken briyani</option>
                                <option value="fried rice">Veg Fried rice</option>
                            </select>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                       
                    </div>
                    <div class="input-box" class="form-group">
                        <label for="email">Email <i class="bi bi-envelope"></i></label>
                        <input type="email" name="email2" id="email2" value="" placeholder="Enter your email"
                            class="form-control" required>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                    </div>
                    <div class="input-box" class="form-group">
                        <label for="datetime">Delivered Date <i class="bi bi-calendar"></i></label> <br>
                        <input type="datetime-local" name="date" id="date">
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                    </div>

                    <div class="input-box" class="textarea form-group">
                        <label for="text">Comments please <i class="bi bi-card-checklist"></i></label> <br>
                        <textarea name="textarea1" id="text1" cols="50" rows="10" autofocus
                            placeholder="Drop your comments!"></textarea>
                    </div>
                    <button type="submit" value="submit" name="submit" class="btn btn-success w-100">Order</button>
                </form>
            </div>
        </div>
    </section>


    <script>
        function lgout() {
           confirm("Do you want to logout?")
            alert("Logging out!!")
        }
    </script>
    </body>
    
    </html>
    """)
val=cgi.FieldStorage()
submit=val.getvalue("submit")
usern=val.getvalue("text")
food=val.getvalue("food")
email=val.getvalue("email2")
date=val.getvalue("date")
comment=val.getvalue("textarea1")

if submit!=None:
    p="""insert into customerdetails(name1,forder,email,deliverdate,comments) values('%s','%s','%s','%s','%s')"""%(
        usern,food,email,date,comment)
    cur.execute(p)
    con.commit()
    print("""
    <script>
      alert("Thanks for your order!!,Your order is deliver on time!")
    </script>
    """)


form=cgi.FieldStorage()
name = form.getvalue("name")
email = form.getvalue("email")
c="""select id from userlogin where usern='%s' and email='%s'"""%(name,email)
cur.execute(c)
f=cur.fetchone()
if f != None:
    print("""
    <script>
    alert("Login successfully!")
    location.href="user_profile.py?id=%s"
    </script>
    """ % f[0])
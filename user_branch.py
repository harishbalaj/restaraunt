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

    #branch {
        position: absolute;
        top: 100px;
    }
    .card img{
           transition: all 0.4s
    }
    .card img:hover{
        transform: scale(1.15)
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
                                <i class="bi bi-person fs-4 me-2"></i>User
                            </a>
                            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                                <li><a href="user_profile.py?id=%s" class="dropdown-item">Profile</a></li>
                                <li><a href="#" class="dropdown-item">Settings</a></li>
                                <li><a href="Homepage.py" class="dropdown-item" onclick="lgout()">Logout</a></li>
                            </ul>
                        </li>
                        <li><img src="./images/profile.jpg" width="50px" height="50px" class="rounded-circle" alt="..."></li>
                    </ul>
    """ %(idd))
    print("""


                    <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasNavbar"
                        aria-labelledby="offcanvasNavbarLabel">
                        <div class="offcanvas-header">
                            <h5 class="offcanvas-title mt-1 fs-4" id="offcanvasNavbarLabel"> <span
                                    class="bi bi-person d-inline-block fs-4 mt-0 align-top"></span>Hi User</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="offcanvas"
                                aria-label="Close"></button>
                        </div>

                        <div class="offcanvas-body navbar-collapse" id="offcanvasNavbar">
                            <ul class="navbar-nav ml-auto justify-content-end flex-grow-1 pe-1">
                                <div class="list-group list-group-flush my-3">
                                    <a href="#"
                                        class="list-group-item list-group-item-action active bg-hover second-text text hover fs-5"
                                        id="dashboard">
                                        <i class="bi bi-journals me-2"></i>Branches
                                    </a>
                                   <a href="userdash.py?id=%s"
                                        class="list-group-item list-group-item-action  bg-hover bg-default second-text text hover fs-5"
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
                                </div>""" %(idd,idd))
    print("""
                            </ul>
                        </div>
                    </div>
                </div>
            </nav>
        </div>
    </section>


    <section id="branch">
        <div class="row">
            <div class="card mb-3 ms-2" style="max-width: 540px;">
                <div class="row g-0">
                    <div class="col-md-4">
                        <img src="./images/branch.jpg" class="img-fluid rounded-start" alt="...">
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <h5 class="card-title">Avinashi</h5>
                            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to
                                additional content. This content is a little bit longer.</p>
                            <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
                        </div>
                    </div>
                </div>
            </div>


            <div class="card mb-3 ms-2" style="max-width: 540px;">
                <div class="row g-0">
                    <div class="col-md-4">
                        <img src="./images/branch2.jpg" class="img-fluid rounded-start" alt="...">
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <h5 class="card-title">Peelamedu</h5>
                            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to
                                additional content. This content is a little bit longer.</p>
                            <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="card mb-3 ms-2" style="max-width: 540px;">
                <div class="row g-0">
                    <div class="col-md-4">
                        <img src="./images/branch.jpg" class="img-fluid rounded-start" alt="...">
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <h5 class="card-title">RTO Office</h5>
                            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to
                                additional content. This content is a little bit longer.</p>
                            <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    <div class="row">
        <div class="card mb-3 ms-2" style="max-width: 540px;">
            <div class="row g-0">
                <div class="col-md-4">
                    <img src="./images/branch2.jpg" class="img-fluid rounded-start" alt="...">
                </div>
                <div class="col-md-8">
                    <div class="card-body">
                        <h5 class="card-title">Prozone</h5>
                        <p class="card-text">This is a wider card with supporting text below as a natural lead-in to
                            additional content. This content is a little bit longer.</p>
                        <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
                    </div>
                </div>
            </div>
        </div>

        <div class="card mb-3 ms-2" style="max-width: 540px;">
            <div class="row g-0">
                <div class="col-md-4">
                    <img src="./images/branch.jpg" class="img-fluid rounded-start" alt="...">
                </div>
                <div class="col-md-8">
                    <div class="card-body">
                        <h5 class="card-title">Sitra</h5>
                        <p class="card-text">This is a wider card with supporting text below as a natural lead-in to
                            additional content. This content is a little bit longer.</p>
                        <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
                    </div>
                </div>
            </div>
        </div>

        <div class="card mb-3 ms-2" style="max-width: 540px;">
            <div class="row g-0">
                <div class="col-md-4">
                    <img src="./images/branch2.jpg" class="img-fluid rounded-start" alt="...">
                </div>
                <div class="col-md-8">
                    <div class="card-body">
                        <h5 class="card-title">Town Hall</h5>
                        <p class="card-text">This is a wider card with supporting text below as a natural lead-in to
                            additional content. This content is a little bit longer.</p>
                        <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    </section>
    <script>
        function lgout(){
          alert("Logging out!!")
        }
    </script>
    </body>
    
    </html>
         """)
#!C:/Users/91934/AppData/Local/Programs/Python/Python311-32/python.exe
import os.path

print("content-type: text/html \r\n\r\n")
import pymysql, cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="restaraunt")
cur = con.cursor()

# p = """ select * from profile where Id='%s' """ % (1)
# cur.execute(p)
# pri = cur.fetchall()
#
# for i in pri:
#     fn = "images/" + i[4]
#     print("""
#     <img src="%s" width="50px" height="50px" class="rounded-circle" alt="..."><a href="#exampleModal" data-bs-toggle="modal"><span class="icon"><i class="bi bi-pencil-square text-danger fs-4"></i></span></a>
#    """ % (fn))

print("""
<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form method="post" enctype="multipart/form-data">
          <input type="file" name="image"> <br>
          <input type="submit" name="upd" value="Update">
        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>

""")


form = cgi.FieldStorage()
update = form.getvalue("upd")
if update != None:
    if len(form) != 0:
        pro = form['image']
        if pro.filename:
            fl = os.path.basename(pro.filename)
            open("images/" + fl, "wb").write(pro.file.read())
            ql = """update profile set image='%s' where Id='%s' """ % (fl, 1)
            cur.execute(ql)
            con.commit()
            print("""
            <html>
            <body>
            <script>
            alert("profile updated")
            </script>
            </body>
            </html>
            """)
con.close()


print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Menus|Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css">
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
        .icon{
         position:relative;
         right:80px;
         bottom:20px;
         cursor:pointer;
        }

        .list-group a:hover {
            color: crimson;
        }
        #menus{
            position: relative;
            top: 20px;
            display: flex;
            height: 90.6vh;
           
        }
        .card img {
      transition: all 0.4s;
    }

    .card:hover img {
      transform: scale(1.15);
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
                        <li><img src="./images/profile.jpg" width="50px" height="50px" class="rounded-circle" alt="..."><a href="#exampleModal" data-bs-toggle="modal"><span class="icon"><i class="bi bi-pencil-square text-danger fs-4"></i></span></a></li>
                         
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
                                            class="list-group-item list-group-item-action bg-hover second-text fs-5">
                                            <i class="bi bi-person me-2"></i>Customers
                                        </a>
                                    <a href="#"
                                        class="list-group-item list-group-item-action active bg-hover second-text fs-5">
                                        <i class="bi bi-menu-button me-2"></i>Menus
                                    </a>
                                     <a href="adminmailsend.py"
                                        class="list-group-item list-group-item-action bg-hover second-text fs-5">
                                        <i class="bi bi-menu-button me-2"></i>Delivery Mail Message
                                    </a>
                                    <a href="./Homepage.py"
                                        class="logout list-group-item list-group-item-action bg-hover text-danger fw-bold fs-5 mt-5"
                                        onclick="lgout()">
                                        <i class="bi bi-box-arrow-right me-2"></i>Logout
                                    </a>
                                </div>
                            </ul>
                        </div>
                    </div>
                </div>
            </nav>
        </div>
    </section>


    <section id="menus" class="bg-dark mt-5">
        <div class="container">
          <div class="menu-text">
            <h1 style="text-align: center; color: wheat;">All <span class="text-success">Menus</span></h1>
            <div class="row">
              <div class="col-sm-12 col-lg-4 col-xs-12 col-md-6">
                <div class="card" style="width: 20rem;">
                  <a href="userdash.py"> <img src="./images/menu1.jpg" class="card-img-top" alt="..."></a>
                </div>
              </div>
              <div class="col-sm-12 col-lg-4 col-xs-12">
                <div class="card" style="width: 20rem;">
                  <a href="userdash.py"> <img src="./images/menu2.jpg" class="card-img-top" alt="..."></a>
                </div>
              </div>
    
              <div class="col-sm-12 col-lg-4 col-xs-12">
                <div class="card" style="width: 20rem;">
                  <a href="userdash.py"> <img src="./images/menu3.jpg" class="card-img-top" alt="..."></a>
                </div>
              </div>
            </div>
    
            <div class="row">
              <div class="col-sm-12 col-lg-4 col-xs-12 rounded-img">
                <div class="card" style="width: 20rem;margin-top: 10px;">
                  <a href="userdash.py"><img src="./images/menu4.jpg" class="card-img-top" alt="..."></a>
                </div>
              </div>
    
              <div class="col-sm-12 col-lg-4 col-xs-12 rounded-img">
                <div class="card" style="width: 20rem; margin-top: 10px;">
                  <a href="userdash.py"> <img src="./images/menu5.jpg" class="card-img-top" alt="..."></a>
                </div>
              </div>
    
              <div class="col-sm-12 col-lg-4 col-xs-12 rounded-img">
                <div class="card" style="width: 20rem; margin-top: 10px;">
                  <a href="userdash.py"> <img src="./images/menu6.jpg" class="card-img-top" alt="..."></a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    

      <section id="menus1" class="bg-secondary mt-3 ">
        <div class="container">
          <div class="menu-text">
            <h1 style="text-align: center; color: wheat;">Veg <span class="text-danger">Menus</span></h1>
            <div class="row">
              <div class="col-sm-12 col-lg-4 col-xs-12 col-md-6">
                <div class="card" style="width: 20rem;">
                  <a href="userdash.py"> <img src="./images/tiffen.jpg" class="card-img-top" alt="..."></a>
                </div>
              </div>
              <div class="col-sm-12 col-lg-4 col-xs-12">
                <div class="card" style="width: 20rem;">
                  <a href="userdash.py"> <img src="./images/veggravy.jpg" class="card-img-top" alt="..."></a>
                </div>
              </div>
    
              <div class="col-sm-12 col-lg-4 col-xs-12">
                <div class="card" style="width: 20rem;">
                  <a href="userdash.py"> <img src="./images/menu3.jpg" class="card-img-top" alt="..."></a>
                </div>
              </div>
            </div>
    
            <div class="row">
              <div class="col-sm-12 col-lg-4 col-xs-12 rounded-img">
                <div class="card" style="width: 20rem;margin-top: 10px;">
                  <a href="userdash.py"><img src="./images/menu4.jpg" class="card-img-top" alt="..."></a>
                </div>
              </div>
    
              <div class="col-sm-12 col-lg-4 col-xs-12 rounded-img">
                <div class="card" style="width: 20rem; margin-top: 10px;">
                  <a href="userdash.py"> <img src="./images/vegnonveg-noodles.jpg" class="card-img-top" alt="..."></a>
                </div>
              </div>
    
              <div class="col-sm-12 col-lg-4 col-xs-12 rounded-img">
                <div class="card" style="width: 20rem; margin-top: 10px;">
                  <a href="userdash.py"> <img src="./images/menu6.jpg" class="card-img-top" alt="..."></a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="menus2" class="bg-danger mt-0 mb-0">
        <div class="container">
          <div class="menu-text">
            <h1 style="text-align: center; color: wheat;">Non-Veg <span class="text-dark">Menus</span></h1>
            <div class="row">
              <div class="col-sm-12 col-lg-4 col-xs-12 col-md-6">
                <div class="card" style="width: 20rem;">
                  <a href="userdash.py"> <img src="./images/sea foods.jpg" class="card-img-top" alt="..."></a>
                </div>
              </div>
              <div class="col-sm-12 col-lg-4 col-xs-12">
                <div class="card" style="width: 20rem;">
                  <a href="userdash.py"> <img src="./images/menu1.jpg" class="card-img-top" alt="..."></a>
                </div>
              </div>
    
              <div class="col-sm-12 col-lg-4 col-xs-12">
                <div class="card" style="width: 20rem;">
                  <a href="userdash.py"> <img src="./images/menu2.jpg" class="card-img-top" alt="..."></a>
                </div>
              </div>
            </div>
    
            <div class="row">
              <div class="col-sm-12 col-lg-4 col-xs-12 rounded-img">
                <div class="card" style="width: 20rem;margin-top: 10px;">
                  <a href="userdash.py"><img src="./images/menu5.jpg" class="card-img-top" alt="..."></a>
                </div>
              </div>
    
              <div class="col-sm-12 col-lg-4 col-xs-12 rounded-img">
                <div class="card" style="width: 20rem; margin-top: 10px;">
                  <a href="userdash.py"> <img src="./images/vegnonveg-noodles.jpg" class="card-img-top" alt="..."></a>
                </div>
              </div>
    
              <div class="col-sm-12 col-lg-4 col-xs-12 rounded-img">
                <div class="card" style="width: 20rem; margin-top: 10px;">
                  <a href="userdash.py"> <img src="./images/menu6.jpg" class="card-img-top" alt="..."></a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    
    <script>
        function lgout() {
            alert("Logging out!!")
        }
    </script>
</body>
</html>
""")
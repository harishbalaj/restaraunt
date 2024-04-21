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
  <title>haribhavanam|Restaurant</title>
  <!-- Latest compiled and minified CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css">
  <link rel="icon" href="./images/haribhavanam-hotel-restaurant.jpg">

  <style>
    html {
      scroll-behavior: smooth;
    }

    .nav-link {
      font-weight: bold;
      font-family: Georgia, 'Times New Roman', Times, serif;
    }

    .dropdown-item {
      font-weight: bold;
      font-family: Georgia, 'Times New Roman', Times, serif;
    }

    #about h1 {
      text-align: center;
      color: #d63d3d;
    }

    .about-text p {
      font-family: 'Times New Roman', Times, serif;
      font-size: 18px;
      font-weight: bold;
    }

    .carousel-caption {
      bottom: 400px;
      z-index: 2;
    }

    .carousel-caption h5 {
      font-size: 30px;
      font-weight: bold;
      font-family: 'Times New Roman', Times, serif;
      text-transform: capitalize;
      letter-spacing: 3px;
      color: wheat;
    }

    .about-img {
      display: flex;
      justify-content: center;
    }

    .contact-text h1 {
      font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
      text-align: center;
      color: rgb(211, 85, 40);
    }

    .contact-text img {
      transition: all 0.4s;
    }

    .contact-text img:hover {
      transform: scale(1.15);
    }

    .icon {
      font-size: 20px;
      display: flex;
      justify-content: space-evenly;
    }

    .icon i:hover {
      color: orangered;
    }

    .order{
      display: flex;
      justify-content: center;
      align-items: center;
      
    }
    .orderdetails {
      padding: 20px;
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
    <nav class="navbar navbar-black navbar-expand-lg bg-white fixed-top ">
      <div class="container-fluid">
        <a class="navbar-brand" href="#"><img width="200" height="50" src="./images/bhav.png" class="sticky-logo"
            alt="Haribhavanam | Traditional Taste"> </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasDarkNavbar"
          aria-controls="offcanvasDarkNavbar" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="offcanvas offcanvas-end text-bg-white" tabindex="-1" id="offcanvasDarkNavbar"
          aria-labelledby="offcanvasDarkNavbarLabel">
          <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="offcanvasDarkNavbarLabel"><img src="./images/bhav.png" width="150px"
                height="50px" alt="hb"><img width="100px" height="50px" src="./images/50-Years-Logo-New-01-01.png"
                alt="logo"></h5>
            <button type="button" class="btn-close btn-close-dark " data-bs-dismiss="offcanvas"
              aria-label="Close"></button>
          </div>
          <div class="offcanvas-body">
            <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#about">About</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#menus">Menu orders</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#Contact">Contact</a>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
                  aria-expanded="false">
                  Login
                </a>
                <ul class="dropdown-menu dropdown-menu-dark">
                  <li><a href="user_login.py" target="_self"><button type="button" class="btn btn-success">User Sign
                        in</button></a></li>
                  <li><a href="user_reg.py" target="_self"><button type="button" class="btn btn-secondary"
                        data-bs-toggle="modal" data-bs-target="#myModal1">User Sign up</button></a></li>
                </ul>
              </li>
              <li>
                <a class="btn btn-success" data-bs-toggle="modal" href="#myModal2" role="button">Admin</a>
              </li>
            </ul>

          </div>
        </div>
      </div>
    </nav>
  </section>

  <section id="carouselpg">
    <div id="carouselAbout" class="carousel carousel-dark slide" data-bs-ride="carousel">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselAbout" data-bs-slide-to="0" class="active" aria-current="true"
          aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselAbout" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselAbout" data-bs-slide-to="2" aria-label="Slide 3"></button>
      </div>
      <div class="carousel-inner" id="carousel-inner1">
        <div class="carousel-item active">
          <img src="./images/s1.jpg" class="d-block w-100" alt="food">
        </div>
        <div class="carousel-item">
          <img src="./images/classy-restaurant.jpg" class="d-block w-100" alt="new">
        </div>
        <div class="carousel-item">
          <img src="./images/slide3.jpg" class="d-block w-100" alt="img">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselAbout" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselAbout" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </section>
  <section id="about">
    <div class="container">
      <div class="row">
        <div class="col-lg-12 col-sm-12">
          <h1>Our Journey</h1>
          <div class="about-img">
            <img src="./images/founder.jpg" alt="founder" width="200px" height="200px">
          </div>
          <div class="about-text col-lg-12">
            <h2>We provide Best Quality Services ever</h2>
            <p>Haribhavanam Hotels, steeped in history and tradition, has long been a revered name in the culinary
              landscape of Coimbatore. Our journey began with a humble yet innovative idea that transformed into an
              enduring legacy. It all started with Mr. Raju, who managed Haribhavanam Lodge, nestled in the heart of
              Gandhipuram's 4th Street. The patrons of the lodge yearned for more than just a place to stay; they longed
              for the comfort and warmth of home-cooked food. <br>
            </p>
            <a href="#" class="btn btn-warning w-25 col-xs-12" style="margin-bottom: 10px;">Know More</a>



            <div class="modal fade" id="myModal2" aria-hidden="true" aria-labelledby="myModal2" tabindex="-1">
              <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                  <!-- Modal header -->
                  <div class="modal-header">
                    <h1 class="modal-title fs-5" id="myModal2">Admin Sign in</h1>
                    <!-- <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button> -->
                  </div>
                  <!--Modal body-->
                  <div class="modal-body">
                    <div class="wrapper">
                      <div class="form-box login">
                        <h2>Login</h2>
                        <form action="#" class="was-validated" id="demo" method="get"
                          name="login1">
                          <div class="input-box" class="form-group">
                            <label for="username">Username <i class="bi bi-person"></i></label>
                            <input type="username" name="uname" id="uname" value="" placeholder="Enter your username"
                              autocomplete="off" class="form-control" required>
                            <div class="valid-feedback">Valid.</div>
                            <div class="invalid-feedback">Please fill out this field.</div>
                          </div>
                          <div class="input-box" class="form-group">
                            <label for="password">Password <i class="bi bi-lock"></i></label>
                            <input type="password" id="psn" value="" name="password" placeholder="Enter your password"
                              class="form-control" required>
                            <div class="valid-feedback">Valid.</div>
                            <div class="invalid-feedback">Please fill out this field.</div>
                          </div>
                          <div class="checkbox-btn form-check">
                            <label class="form-check-label"><input type="checkbox" class="form-check-input"
                                name="checkbox" required>
                              Remember me</label>
                            <div class="valid-feedback">Valid.</div>
                            <div class="invalid-feedback">Check this checkbox to continue.</div>
                            <a href="#">Forgot Password?</a>
                          </div>
                           <button type="submit" name="sub" value="submit" class="btn btn-success w-100">Login</button>
                        </form>
                      </div>
                    </div>
                  </div>

                  <!-- Modal footer -->
                  <div class="modal-footer">
                    <button class="btn btn-primary" data-bs-target="#myModal3" data-bs-toggle="modal">Admin Sign
                      up</button>
                    <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
                  </div>
                </div>
              </div>
            </div>
            <div class="modal fade" id="myModal3" aria-hidden="true" aria-labelledby="myModal3" tabindex="-1">
              <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                  <div class="modal-header">
                    <h1 class="modal-title fs-5" id="myModal3">Admin Sign up</h1>
                    <!-- <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button> -->
                  </div>
                  <div class="modal-body">
                    <div class="form-box register">
                      <h2>Registration</h2>
                      <form action="#" id="demo" class="was-validated" method="post"
                        name="login2">
                        <div class="input-box" class="form-group">
                          <label for="Username">Username <i class="bi bi-person"></i></label>
                          <input type="username" id="usn" value="" name="text" placeholder="Enter your username"
                            autocomplete="off" class="form-control" required>
                          <div class="valid-feedback">Valid.</div>
                          <div class="invalid-feedback">Please fill out this field.</div>
                        </div>
                        <div class="input-box" class="form-group">
                          <label for="email">Create Email <i class="bi bi-envelope"></i></label>
                          <input type="email" id="emn" value="" name="email" placeholder="Create new email"
                            class="form-control" required>
                          <div class="valid-feedback">Valid.</div>
                          <div class="invalid-feedback">Please fill out this field.</div>
                        </div>
                        <div class="input-box" class="form-group">
                          <label for="password">Create Password <i class="bi bi-lock"></i></label>
                          <input type="password" id="psn" value="" name="password" placeholder="Create a password"
                            class="form-control" required>
                          <div class="valid-feedback">Valid.</div>
                          <div class="invalid-feedback">Please fill out this field.</div>
                        </div>
                        <div class="input-box" class="form-group">
                          <label for="tel" id="phone">Phone <i class="bi bi-phone"></i></label>
                          <input type="tel" id="phone" value="" name="phone" placeholder="Enter your phone no"
                            class="form-control" required>
                          <div class="valid-feedback">Valid.</div>
                          <div class="invalid-feedback">Please fill out this field.</div>
                        </div>
                        <div class="input-box" class="form-group">
                          <label for="addr" id="addr">Address <i class="bi bi-house"></i></label>
                          <input type="text" id="addr" value="" name="addr" placeholder="Enter your address"
                            class="form-control" required>
                          <div class="valid-feedback">Valid.</div>
                          <div class="invalid-feedback">Please fill out this field.</div>
                        </div>
                        <div class="input-box" class="form-group">
                          <label for="pin" id="pin">Pincode <i class="bi bi-geo-alt-fill"></i></label>
                          <input type="text" id="pin" value="" name="pin" placeholder="Enter your pincode"
                            class="form-control" required>
                          <div class="valid-feedback">Valid.</div>
                          <div class="invalid-feedback">Please fill out this field.</div>
                        </div>
                        <div class="checkbox-btn">
                          <label class="form-check-label"><input type="checkbox" class="form-check-input"
                              name="checkbox" required>
                            I accept all terms and conditions</label>
                          <div class="valid-feedback">Valid.</div>
                          <div class="invalid-feedback">Check this checkbox to continue.</div>
                        </div>
                        <button type="submit" value="submit" name="submit"
                          class="btn btn-success w-100">Register</button>
                        <div class="register-btn">
                          <p>Already have an account? <a href="https://mail.google.com" class="login-link">Login</a></p>
                        </div>
                      </form>
                    </div>

                  </div>
                  <div class="modal-footer">
                    <button class="btn btn-primary" data-bs-target="#myModal2" data-bs-toggle="modal">Admin Sign
                      in</button>
                    <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
                  </div>
                </div>
              </div>
            </div>




          </div>
        </div>
      </div>
    </div>
  </section>

  <section id="menus" class="bg-dark">
    <div class="container">
      <div class="menu-text">
        <h1 style="text-align: center; color: wheat;">Menus</h1>
        <div class="row">
          <div class="col-sm-12 col-lg-4 col-xs-12 col-md-6">
            <div class="card" style="width: 20rem;">
              <a href="#"> <img src="./images/menu1.jpg" class="card-img-top" alt="..."></a>
            </div>
          </div>
          <div class="col-sm-12 col-lg-4 col-xs-12">
            <div class="card" style="width: 20rem;">
              <a href="#"> <img src="./images/menu2.jpg" class="card-img-top" alt="..."></a>
            </div>
          </div>

          <div class="col-sm-12 col-lg-4 col-xs-12">
            <div class="card" style="width: 20rem;">
              <a href="#"> <img src="./images/menu3.jpg" class="card-img-top" alt="..."></a>
            </div>
          </div>
        </div>

        <div class="row">
          <div class="col-sm-12 col-lg-4 col-xs-12 rounded-img">
            <div class="card" style="width: 20rem;margin-top: 10px;">
              <a href="#"><img src="./images/menu4.jpg" class="card-img-top" alt="..."></a>
            </div>
          </div>

          <div class="col-sm-12 col-lg-4 col-xs-12 rounded-img">
            <div class="card" style="width: 20rem; margin-top: 10px;">
              <a href="#"> <img src="./images/menu5.jpg" class="card-img-top" alt="..."></a>
            </div>
          </div>

          <div class="col-sm-12 col-lg-4 col-xs-12 rounded-img">
            <div class="card" style="width: 20rem; margin-top: 10px;">
              <a href="#"> <img src="./images/menu6.jpg" class="card-img-top" alt="..."></a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>


  <section id="Contact">
    <div class="container">
      <div class="row">
        <div class="contact-text">
          <h1>Get our delicious food delivered at your doorstep with</h1>
          <!-- <img src="./images/swiggy.jpg" width="50px" height="50px" alt="swiggy">
             <img src="./images/Zomato_logo.png" width="50px" height="50px" alt="swiggy">-->
          <img src="./images/Zomato-Swiggy.jpg" width="200px" height="100px" class="col-sm-4 col-lg-2 col-xs-3"
            alt="zomata"> <br>
          <p class="col-xs-4">
            RTO Office Road |
            Peelamedu |
            Goldwins |
            Brookefields |
            Prozone |
            Avinashi |
            Sitra |
            Pothys
          </p>

          <div class="col-lg-4 col-xs-4">
            <img src="./images/bhav.png" width="300px" height="100px" alt="">
          </div>
          <div class="col-lg-4 col-xs-4">
            <h5 style="color: orangered;">Opening hours</h5>
            <li style="font-weight: bold;">Restaurant and Take Away</li>
            <li style="font-weight: bold;">11.30AM-10.30PM</li>
          </div>
          <div class="col-lg-4 col-xs-4">
            <address style="font-weight: bold;">
              <h5 style="color: orangered;">Address</h5>
              NO-193-195,HARIBHAVANAM,<br>
              4TH STREET,COIMBATORE,<br>
              TAMILNADU,641012 <br>
              +91 90801 80000
            </address>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section id="social-media" class="bg-dark text-white">
    <div class="container">
      <div class="social-media">
        <div class="row">
          <p>&copy; 2024 All rights reserved.Haribhavanam | Created by Harishbalaji.B</p>
          <span class="icon col-lg-12 col-xs-3">
            <a href="https://www.linkedin.com/in/harishbalaji016/"> <i class="bi bi-linkedin"></i></a>
            <i class="bi bi-twitter"></i>
            <a href="https://www.instagram.com/hari_manmax?igsh=YzAwZjE1ZTI0Zg=="><i class="bi bi-instagram"></i></a>
            <i class="bi bi-youtube"></i>
          </span>
        </div>
      </div>
    </div>
  </section>




  <!-- <script>

      function login() {
        user = document.forms["login2"]["user"];
        pass = document.forms["login2"]["passw"];
        email = document.forms["login2"]["email"];
        phone = document.forms["login2"]["phone"]
        address = document.forms["login2"]["addr1"]
        pincode = document.forms["login2"]["pin"]

        if (user.value == "") {
          alert("Enter the username");
          user.focus();
          return false;
        }
        // else if (pass.value == "") {
        //   alert("Enter your password");
        //   pass.focus();
        //   return false;
        // }
        // else if (email.value == "") {
        //   alert("Enter your email address");
        //   email.focus();
        //   return false;
        // }

        // else if (address.value == "") {
        //   alert("Enter your address");
        //   address.focus();
        //   return false;
        // }
        // else if (pincode.value == "") {
        //   alert("Enter the pincode");
        //   pincode.focus();
        //   return false;
        // }

        else if (email.value != "" && pass.value != "" && user.value != "" && phone.value != "" && address.value != "" && pincode.value != "") {
          alert("Register successfully!!");
          return true;
        }
        else {
          alert("Please fill the details completly!!");
          return false;
        }

      }


      function lg() {
        email = document.forms["login1"]["emn"];
        pass = document.forms["login1"]["psn"];

        if (email.value == "") {
          alert("Enter your email");
          email.focus();
          return false;
        }
        else if (pass.value == "") {
          alert("Enter your password");
          pass.focus();
          return false;
        }
        else if (email.value == "harishbalaji@gmail.com" && pass.value == "12345") {
          alert("Login successfully!!");
          return true;
        }
        else {
          alert("User not found!!");
          return false;
        }

      }

    </script> -->
</body>

</html>
""")

v = cgi.FieldStorage()
if len(v) != 0:
    submit = v.getvalue("submit")

    if submit != None:
        name = v.getvalue("text")
        email = v.getvalue("email")
        psw = v.getvalue("password")
        phone = v.getvalue("phone")
        address = v.getvalue("addr")
        pincode = v.getvalue("pin")
        n = """insert into reg_form(uname,cemail,cpsw,phone,addr,pin) values('%s','%s','%s','%s','%s','%s')""" % (
            name, email, psw, phone, address, pincode)
        cur.execute(n)
        con.commit()
        print("""
        <script>
           alert("Hello Admin!,Register successfully in your database!!")
        </script>
        """)

form = cgi.FieldStorage()
username = form.getvalue("uname")
passw = form.getvalue("password")
submit = form.getvalue("sub")

if submit != None:
    p = """select id from reg_form where uname='%s' and cpsw='%s'""" % (username, passw)
    cur.execute(p)
    rec = cur.fetchone()
    if rec != None:
        print("""
        <script>
        alert("Login successfully!")
        location.href="admindashboard.py?id=%s"
        </script>
        """ % rec[0])
    else:
        print("""
            <script>
              alert("user not found!)"
            </script>
             """)



#!C:/Users/91934/AppData/Local/Programs/Python/Python311-32/python.exe
import os.path

print("content-type: text/html \r\n\r\n")
import pymysql, cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="restaraunt")
cur = con.cursor()

print("""
    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title text-black" id="exampleModalLabel">Change Password</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
          <form action="#" class="was-validated" id="demo" method="get" name="login1">
             <div class="input-box" class="form-group">
           
                            <label for="text" class="text-dark">Username <i class="bi bi-lock"></i></label>
                            <input type="username" id="name" value="" name="name" placeholder="Enter your username"
                                autocomplete="off" class="form-control" required>
                            <div class="valid-feedback">Valid.</div>
                            <div class="invalid-feedback">Please fill out this field.</div>
            </div>
             <div class="input-box" class="form-group">
           
                            <label for="email" class="text-dark">Email<i class="bi bi-envelope"></i></label>
                            <input type="email" id="em" value="" name="em" placeholder="Enter To email"
                                autocomplete="off" class="form-control" required>
                            <div class="valid-feedback">Valid.</div>
                            <div class="invalid-feedback">Please fill out this field.</div>
            </div>
            <div class="input-box" class="form-group">
                            <label for="password" class="text-dark">Change Password <i class="bi bi-lock"></i></label>
                            <input type="password" id="pass" value="" name="pass1" placeholder="Enter the password"
                                autocomplete="off" class="form-control" required>
                            <div class="valid-feedback">Valid.</div>
                            <div class="invalid-feedback">Please fill out this field.</div>
            </div> <br> <br>
            <input type="submit" value="submit" name="sub1" class="btn btn-success w-100" value="Submit">
        </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
        </section>
    </body>
    
    </html>
    """)



print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UserLogin|Restaurant</title>
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
        .wrapper{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .login{
            border: 2px solid black;
            border-radius: 10px;
            width: 400px;
            padding: 20px;
            height: 350px;
            box-shadow: 2px 2px 6px black;
        }
        /* #login{
            background-image: url("images/124569.jpg");
            background-size: cover;
            background-repeat: no-repeat;

        } */
        
    </style>
</head>

<body>
    <section id="nav">
        <nav class="navbar navbar-black navbar-expand-lg bg-white fixed-top ">
            <div class="container-fluid">
                <a class="navbar-brand" href="#"><img width="200" height="50" src="./images/bhav.png"
                        class="sticky-logo" alt="Haribhavanam | Traditional Taste"> </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas"
                    data-bs-target="#offcanvasDarkNavbar" aria-controls="offcanvasDarkNavbar"
                    aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="offcanvas offcanvas-end text-bg-white" tabindex="-1" id="offcanvasDarkNavbar"
                    aria-labelledby="offcanvasDarkNavbarLabel">
                    <div class="offcanvas-header">
                        <h5 class="offcanvas-title" id="offcanvasDarkNavbarLabel"><img src="./images/bhav.png"
                                width="150px" height="50px" alt="hb"><img width="100px" height="50px"
                                src="./images/50-Years-Logo-New-01-01.png" alt="logo"></h5>
                        <button type="button" class="btn-close btn-close-dark " data-bs-dismiss="offcanvas"
                            aria-label="Close"></button>
                    </div>
                    <div class="offcanvas-body">
                        <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
                            <li class="nav-item">
                                <a class="nav-link active" aria-current="page" href="Homepage.py" target="_parent">Home</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#Contact">Contact</a>
                            </li>
                            <li class="nav-item">
                                <a class="btn btn-success" href="user_reg.py" target="_self">User Sign up</a>
                            </li>
                        </ul>

                    </div>
                </div>
            </div>
        </nav>
    </section>

    <section id="login" class="bg-secondary"> 
        <div class="wrapper">
            <div class="form-box login">
                <h2 class="text-center">User Login</h2>
                <form action="#" class="was-validated" id="demo" method="post" name="login1">
                    <div class="input-box" class="form-group">
                        <label for="Username">Username <i class="bi bi-person"></i></label>
                        <input type="username" id="user" value="" name="uname" placeholder="Enter your username"
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
                        <label class="form-check-label"><input type="checkbox" class="form-check-input" name="checkbox"
                                required>
                            Remember me</label>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Check this checkbox to continue.</div>
                        <a href="#exampleModal" data-bs-toggle="modal" data-bs-target="#exampleModal">Forgot Password?</a>
                    </div>
                     <button type="submit" value="submit" name="sub"  class="btn btn-success w-100">Login</button>
                    <!-- <div class="register-btn">
                  <p>Don't have a account? <a href="myModal1" class="register-link">Register</a></p>
                </div> -->
                </form>""")
print("""
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
                     <img src="./images/Zomato-Swiggy.jpg" width="200px" height="100px" class="col-sm-4 col-lg-2 col-xs-3" alt="zomata"> <br>
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
                        <a href="https://www.instagram.com/hari_manmax?igsh=YzAwZjE1ZTI0Zg=="><i
                                class="bi bi-instagram"></i></a>
                        <i class="bi bi-youtube"></i>
                    </span>
                </div>
            </div>
        </div>
""")


form = cgi.FieldStorage()
username = form.getvalue("uname")
passw = form.getvalue("password")
submit = form.getvalue("sub")

if submit != None:
    p = """select id from userlogin where usern='%s' and passw='%s'""" % (username, passw)
    cur.execute(p)
    rec = cur.fetchone()
    if rec != None:
        print("""
        <script>
        alert("Login successfully!")
        location.href="userdash.py?id=%s"
        </script>
        """ % rec[0])


# cpass = form.getvalue("pass1")
# submit = form.getvalue("sub1")
#
# if submit != None:
#         n = """update userlogin set passw='%s' where id='%s' """ % (cpass,r[0])
#         cur.execute(n)
#         con.commit()
#         print("""
#         <script>
#          alert("Your password has been change & updated!!")
#         </script>
#         """)
con.close()
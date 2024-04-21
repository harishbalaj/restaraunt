#!C:/Users/91934/AppData/Local/Programs/Python/Python311-32/python.exe
import os.path

print("content-type: text/html \r\n\r\n")
import pymysql, cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="restaraunt")
cur = con.cursor()
print("""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UserRegister|Restaurant</title>
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

        .wrapper {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 120vh;
        }

        .register {
            border: 2px solid black;
            border-radius: 10px;
            width: 22%;
            padding: 20px;
            height: 760px;
            width: 500px;
           
        }
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
                                <a class="btn btn-success" href="user_login.py">User Sign in</a>
                            </li>
                            
                        </ul>

                    </div>
                </div>
            </div>
        </nav>
    </section>
    <section id="register" class="bg-success">
        <div class="wrapper">
            <div class="form-box register">
                <h2 class="text-center">User Registration</h2>
                <form action="#" id="demo1" class="was-validated" method="post" name="login2">
                    <div class="input-box" class="form-group">
                        <label for="Username">Username <i class="bi bi-person"></i></label>
                        <input type="username" id="user" value="" name="text" placeholder="Enter your username"
                            autocomplete="off" class="form-control" required>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                    </div>
                    <div class="input-box" class="form-group">
                        <label for="email">Create Email <i class="bi bi-envelope"></i></label>
                        <input type="email" id="email" value="" name="email" placeholder="Create new email"
                            class="form-control" required>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                    </div>
                    <div class="input-box" class="form-group">
                        <label for="password">Create Password <i class="bi bi-lock"></i></label>
                        <input type="password" id="passw" value="" name="password" placeholder="Create a password"
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
                        <input type="text" id="addr1" value="" name="addr" placeholder="Enter your address"
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
                        <label class="form-check-label"><input type="checkbox" class="form-check-input" name="checkbox"
                                required>
                            I accept all terms and conditions</label>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Check this checkbox to continue.</div>
                    </div>
                    <button type="submit" value="submit" name="sub" class="btn btn-danger w-100">Register</button>
                    <div class="register-btn">
                        <p>Already have an account? <a href="https://mail.google.com" class="login-link">Login</a></p>
                    </div>
                </form>
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
    </section>
</body>

</html>
""")

h = cgi.FieldStorage()
if len(h) != 0:
    submit = h.getvalue("sub")

    if submit != None:
        user = h.getvalue("text")
        email = h.getvalue("email")
        psw = h.getvalue("password")
        phone = h.getvalue("phone")
        addr = h.getvalue("addr")
        pincode = h.getvalue("pin")
        b = """insert into userlogin(usern,email,passw,phn,address,pincode) values('%s','%s','%s','%s','%s','%s')""" % (
                user, email, psw, phone, addr, pincode)
        cur.execute(b)
        con.commit()
        print("""
            <script>
               alert("Hello User!,Your registration is successfully done!");
               location.href="user_login.py?id=%s"
            </script>
            """)

#!C:/Users/91934/AppData/Local/Programs/Python/Python311-32/python.exe

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
</head>
<body>
          <div class="wrapper">
            <div class="form-box login">
              <h2>Login</h2>
              <form action="#" class="was-validated" onsubmit="return lg()" id="demo" method="post" name="login1">
                <div class="input-box" class="form-group">
                  <label for="emn">Username <i class="bi bi-person"></i></label>
                  <input type="text" name="uname" id="emn" value="" placeholder="Enter the username" autocomplete="off"
                    class="form-control" required>
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
                  <a href="https://accounts.google.com/v3/signin/challenge/pwd?TL=AEzbmxx6wtu_U2p2DXJJmcGiByYKCH8M5Jh7
                    3cdgcQqLh4qYNpIfpIS2tLmGCaHy&cid=1&continue=https%3A%2F%2Fmyaccount.google.com%2Fsigninoptions%2Fpassword%3Fcontinue%3Dhttps%3A%2F%2Fmyaccount.google.com%2Fsecurity%3Fhl%253Den_GB&flowName=GlifWebSignIn&hl=en-
                    GB&ifkv=ARZ0qKIhXF7ZYTu1CBTRhaYG-7mBiadoiaWePkIt1DXlQ658LyxyHqsjh8pc17-YNbH_98pP4_k8Ug&kdi=CAM&rart=ANgoxceT4MI8U61NgBalxbIuEWsEPlc4_aIAoySY4PV6b3VyeJ
                    eOFFH6bdeoO15B3tynOWjaqyJ37OOWQJ6P1BNzdpNF3TX4A38EKMwAknCD7Oyq7XmZuHk&rpbg=1&sarp=1&scc=1&service=accountsettings&theme=mn">Forgot Password?</a>
                </div>
                <input type="submit" value="submit" name="sub" onclick="lg()" class="btn btn-success w-10">
                <!-- <div class="register-btn">
                  <p>Don't have a account? <a href="myModal1" class="register-link">Register</a></p>
                </div> -->
              </form>
            </div>
          </div>
        </div>
</body>
</html>
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
        location.href="Homepage.py?id=%s"
        </script>
        """ % rec[0])
    else:
        print("""
     <script>
     alert("user not found!)"
     </script>
     """)

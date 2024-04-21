#!C:/Users/91934/AppData/Local/Programs/Python/Python311-32/python.exe
import os.path

print("content-type: text/html \r\n\r\n")
import pymysql, cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="restaraunt")
cur = con.cursor()

p = """ select * from profile where Id='%s' """ % (1)
cur.execute(p)
pri = cur.fetchall()

for i in pri:
    fn = "images/" + i[4]
    print("""
    <img src="%s" width="200px" height="200px" class="rounded-circle" alt="...">""" % (fn))

print("""
<!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
  Launch demo modal
</button>

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
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
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
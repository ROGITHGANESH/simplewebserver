from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
    
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Signup Form</title>
   input
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color:blue;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: whitesmoke;
        }
        
        .container {
            background-color:yellow(0, 0, 255, 0);
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 0 20px rgba(255, 255, 255, 0.5);
            width: 400px;
            text-align: center;
        }
        
        h1 {
            margin-bottom: 20px;
            color: violet; 
            
        }
        
        input[type="text"],
        input[type="number"],
        input[type="password"],
        input[type="email"],
        select {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            display: inline-block;
            border: 1px solid #0f0;
            border-radius: 4px;
            box-sizing: border-box;
            background-color: #111;
            color: #0f0;
        }

        label {
            color:paleturquoise;
            margin-right: 10px;
        }

        input[type="checkbox"],
        input[type="radio"] {
            margin-right: 5px;
        }

        input[type="submit"],
        input[type="reset"] {
            background-color:whitesmoke;
            color:black;
            padding: 14px 20px;
            margin: 8px 0;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
        
        }
        
        input[type="submit"]:hover,
        input[type="reset"]:hover {
            background-color:violet;
        }
        
       
        
        
        input[type="submit"], input[type="reset"] 
        {
            background-color: #000;
            color: whitesmoke; 
        }

        input[type="date"]::placeholder {
            color: #0f0;
        }

        select {
            font-size: 16px;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Signup Form</h1>
    <form method="post">
        <input
        type="text"
        name="search"
        placeholder="Book search"
        style="
        width: 400px;
        height: 50;
        border-radius: 25px;
        background-image: url(rogith), url(search);
        background-size: 30px;
        background-repeat: no repeat;
        background-position: 2%, 95%;
        text-aligen: center;
        font-size: 30px;">
        <!--Row 1- Column 2-->
        <div style="width: 70%">
        <a href="">Home</a>
        <a href=" ">About Us</a>
        <a href="">Department</a>
        <a href="">Life at sec</a>
        <a href="">Admissions</a>
        <a href="">Placements</a>
        </div>
        
        <input type="text" minlength="3" maxlength="20" required name="fname" placeholder="First Name"><br/>
        <input type="text" name="lname" required name="lname" placeholder="last Name"><br/>
        <input type="number" min="6000000000" max="9999999999" name="phone number" placeholder="Phone Number"><br>
        <div style="position: relative;">
            <input type="password" name="password" id="password" pattern="(?=.\d)(?=.[a-z])(?=.*[A-Z]).{8,}" placeholder="Password">
            <i class="toggle-password fas fa-eye-slash" onclick="togglePassword()"></i>
        </div>
        <input type="email" name="mail id" placeholder="Email Address" pattern="[a-z0-9._]+@[a-z0-9.\-]+\.[a-z]{2,4}$"><br>
        <label for="dob">Date of Birth:</label><br>
        <input type="date" id="dob" name="Date of birth" value="dob"><br>
        <label>Gender:</label><br>
        <input type="radio" name="gender" value="male">Male
        <input type="radio" name="gender" value="female">Female<br>
        <label>Electives:</label><br>
        <input type="checkbox" name="Electives" value="soft skills  2credits">Soft Skills
        <input type="checkbox" name="Electives" value="web application  5credits">Web Application<br>
        <label>Course:</label><br>
        <select name="courses">
            <option value="">---- Select any course ----</option>
            <option value="python">Python</option>
            <option value="c programming">C Programming</option>
            <option value="java">Java</option>
            <option value="django">Django</option>
        </select><br>
        <input type="submit" name="submit" value="Submit">
        <input type="reset" name="clear all" value="Clear All">
    
    </form>
</div>



</body>
</html
"""

class myhandler(BaseHTTPRequestHandler):
    def do_Get(self):
        print("request recieved")
        self.send_response(200)
        self.send_header('content-type','text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
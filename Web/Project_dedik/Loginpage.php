<!DOCTYPE html>

<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8" />
    <title>Log In</title>
    <link rel="stylesheet" href="loginpage.css" />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"
    />
  </head>
  <body>
    <div class="header-bottom fade">
      <div class="in-bottom">
        <h2>GoldenLuxe</h2>
        <p>Home</p>
        <p>Rooms</p>
        <p>Facilities</p>
        <p>Contact Us</p>
        <p>About</p>
        <div class="login-bottom">
          <button>Login</button>
          <button>Register</button>
        </div>
        <div class="bars">
          <i class="fas fa-bars"></i>
        </div>
      </div>
    </div>

    <div class="bg-img">
      <div class="content">
        <header>Wellcome Back!</header>
        <form action="#">
          <div class="form-content">
            <span class="fa fa-user"></span>
            <input type="text" required placeholder="Email or Phone" />
          </div>
          <div class="form-content">
            <span class="fa fa-lock"></span>
            <input
              type="password"
              class="keyword"
              required
              placeholder="Password"
            />
          
          </div>
          <div class="password-input">
            <a href="#">Forgot Password?</a>
          </div>
          <div class="form-content">
            <input
              type="submit"
              value="LOGIN"
              onclick="location.href='index.html';"
            />
          </div>
        </form>
        <div class="login">Or login with</div>
        <div class="icon">
          <div class="Apple">
            <i class="fab fa-apple"><span>Apple</span></i>
          </div>
          <div class="facebook">
            <i class="fab fa-facebook-f"><span>Facebook</span></i>
          </div>
        </div>
        <div class="register">
          Don't have account?
          <a href="register.html">Register Now</a>
        </div>
      </div>
    </div>
    <script>
      const pass_field = document.querySelector(".keyword");
      const showBtn = document.querySelector(".pass");
      showBtn.addEventListener("click", function () {
        if (pass_field.type === "password") {
          pass_field.type = "text";
          showBtn.textContent = "HIDE";
          showBtn.style.color = "#3498db";
        } else {
          pass_field.type = "password";
          showBtn.textContent = "SHOW";
          showBtn.style.color = "#222";
        }
      });
    </script>
  </body>
</html>

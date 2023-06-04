# n11_loginPage_tests
Functional, UI and security automated test cases examples for https://www.n11.com/ login page.

Test Cases

-test case 1 - Login with an invalid username and a valid password

 Go to https://www.n11.com/
 
 Click "Giriş Yap" button
 
 Enter an invalid username and a valid password
 
 Verify that it gives an incorrect login message 

-test case 2 - Login with an valid username and an invalid password

 Go to https://www.n11.com/
 
 Click "Giriş Yap" button
 
 Enter a valid username and an invalid password
 
 Verify that it gives an incorrect login message
 
-test case 3 - Login with an valid username and an valid password

 Go to https://www.n11.com/
 
 Click "Giriş Yap" button
 
 Enter a valid username and a valid password
 
 Verify that succesfully login
 
-test case 4 - Scroll menu and log out

 Scroll My Account dropdown menu
 
 Click "Çıkış Yap" button
 
 Click "Giriş Yap" button

-test case 5 - verify 'Şifremi Unuttum' button on login page

 Click "Şifremi Unuttum" button
 
 Verify "Şifre Yenileme" popup screen

-test case 6 - verify 'Beni Unutma' button on login page

-test case 7 - verify other login buttons

-test case 8 - Verify presence of label texts

-test case 9 - Verify presence of text boxes

-test case 10 - Verify presence of buttons


-test case 11 - Verify HTTPS

-test case 12 - Verify SSL certificate

-test case 13 - Verify login success

-test case 14 - Verify session timeout


The tests are written with the ios operating system and run by Pycharm CE (PyCharm 2022.3.3)
Chrome Version 114.0.5735.90

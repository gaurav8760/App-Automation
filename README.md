## Python unittest automation Lambdatest

Python selenium automation sample test for [LambdaTest](https://www.lambdatest.com/) cloud-based Selenium Grid.


## Install Python
 - Download the latest python build from https://www.python.org/downloads/
 - Make sure pip should installed. you can check using `pip --version`


### Configuring Test
- Replace {username}  with your username 
- Replace {accessToken}  with your username 
- List of supported platfrom, browser, version can be found at https://www.lambdatest.com/capabilities-generator/


### Installating Dependencies
```bash
pip install selenium
export PYTHONWARNINGS="ignore:Unverified HTTPS request"   //Disable ssl warning
```

### Executing Test
```bash
python google-serach-lambdatest.py
python android.py
```
## About LambdaTest
[LambdaTest](https://www.lambdatest.com/) is a cloud based selenium grid infrastructure that can help you run automated cross browser compatibility tests on 2000+ different browser and operating system environments. LambdaTest supports all programming languages and frameworks that are supported with Selenium, and have easy integrations with all popular CI/CD platforms. It's a perfect solution to bring your [selenium automation testing](https://www.lambdatest.com/selenium-automation) to cloud based infrastructure that not only helps you increase your test coverage over multiple desktop and mobile browsers, but also allows you to cut down your test execution time by running tests on parallel.

/////////////////////////////////////////////////////////////////////////////////////

App Automation Set-up Steps:

App Automation Steps:

1. Create access token from https://mixedanalytics.com/knowledge-base/api-connector-encode-credentials-to-base-64/ by entering username:accsess_key.
2. Copy The Curl and add the generated access token and import it on postman.
3. In postman, open form-data and add the below key value pairs:
	a). appFile = Your .apk file
	b). name = Any Name

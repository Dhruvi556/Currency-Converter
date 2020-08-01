# Currency-Converter
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![cc](https://user-images.githubusercontent.com/68439180/89105418-ced85400-d3d5-11ea-90b7-28f8184632fc.gif)


## About 
A currency converter that converts the amount input by the user from a given currency to another.It works on the fundamentals of speech recognition and web-scraping. <br>
Programming Language: **Python 3.8.5**

## Requirements 

### System Requirements
To install a requirement, you can download from the link mentioned.
- **Python 3 and above.**            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Download Python](https://www.python.org/downloads/)
- **Chrome Webdriver**               &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Chrome Webdriver Installation](https://chromedriver.chromium.org/downloads) 
- **PIP for Python in Windows**      &nbsp;&nbsp;&nbsp;&nbsp;[PIP Installation Guide](https://phoenixnap.com/kb/install-pip-windows) <br> <br>

### Python Module Requirements

- Modules required: **selenium, speech_recognition, pyttsx3. <br>
- These can be installed by typing the following command in CMD: ```pip3 install -r requirements.txt```
     
         
## Implementation 

- Open CMD, navigate to the working directory. Type in:  ```python Currency_Converter.py``` 
- If you encounter an error, check if the Python version is 3 and above and the modules are installed correctly.
- On program execution, input necessary details: amount to be converted, currency from which amount is to be converted, currency to which amount is to be converted.  
- The speech recognizer recognizes the speech input and an online website (xe.com) is opened to convert and retrieve the amount.
- The converted amount is then read aloud by the system.

## Notes 
- This bot **only works in _Windows_** (due to directory address configurations which differ in other OS'es.)
- It is important to **_replace the chrome Webdriver address in line number 27_ with the address of your Webdriver's location address.** 
- After changing the address, **if you receive an error**, convert all the single back-slashes into double back-slashes in the address. **Eg: "\\" becomes "\\\\"**. 


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

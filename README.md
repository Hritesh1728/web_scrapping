
## Automation of the electricity Bill Fetch.

This project uses the automation tool "PlayWright" and the programming language "Python" to get information about the consumer's most recent eletricity bill.

## Acknowledgements

 - [Playwright tutorial in Python](https://playwright.dev/python/)


## Documentation

1. Input your k-number data in the csv file **"source.csv"** located in the directory **"data"** followed by their respective **"Board directories"**.

    The CSV file looks like this: -
    | SR | kno | Amount |
    | -------- | -------- | -------- |
    | 1| 13012XXXXXXX| 21XX|
    | 2| 13012XXXXXXX| 31XX|

    **Note:** - The most and only important column here is the **"kno"**

2. Run the Script by the command: -
    ```bash
      py test_playwright.py
    ```

3. Choose the electricity board by entering 1 or 2 or 3 in the command prompt which looks like as below:-
    ![Input image for playwright](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

4. Wait for the task to complete and finally, you will get the output CSV file in the same directory where the **"source.csv"** lies with the name **"result.csv"**
The data provided by the output files are: -

    |  ___________  |    _______________       |    _________  |      ___________   |
    |-------------------|-------------------|-------------------|-------------------|
    | k_number           | account_number    | billing_month     | issue_date        |
    | name               | bill_number       | payment_mode      | issue_bank        |
    | address            | receipt_number    | reference_number  | bill_amount_(rs)  |
    | receipt_date         |                   |       |                   |



## 🚀 About Me
  **Name:** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Hritesh_
    
  **Graduation:**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; BTech from the _Indian Institute of Technology, Kanpur_
    
  **Email:** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hriteshalw1728@gmail.com
    
  **GitHub:** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Hritesh1728](https://github.com/Hritesh1728)
    
  **Profession:**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "_Enthusiastic Fresher Software Developer Eager to Innovate and Learn_"


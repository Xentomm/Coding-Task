# Backend oriented task

## Descritpion
Coding task for internship. Local Python server using Flask that query data from Narodowy Bank Polski and returns relevant information.

## Required operations

Provide a separate endpoint for each operation:
1. Given a date (formatted YYYY-MM-DD) and a currency code (list: https://nbp.pl/en/statistic-and-financial-reporting/rates/table-a/), provide its average exchange rate.
2. Given a currency code and the number of last quotations N (N <= 255), provide the max and min average value (every day has a different average).
3. Given a currency code and the number of last quotations N (N <= 255), provide the major difference between the buy and ask rate (every day has different rates).

## Instructions
- To start the server, run this command and visit browser on localhost(http://127.0.0.1:5000/ or other port):
```
flask run
```
- Example 1 - to query operation 1, go to this url(returns 4.2006):
```
http://127.0.0.1:5000/average/usd/2023-04-21
```
- Example 2 - to query operation 1, go to this url(returns 5.2086):
```
http://127.0.0.1:5000/average/gbp/2023-04-21
```
- Example 3 - to query operation 2, go to this url(returns 4.2932 and 42006):
```
http://127.0.0.1:5000/minmax/usd/10
```
- Example 4 - to query operation 2, go to this url(returns 5.4638 and 5.2086):
```
http://127.0.0.1:5000/minmax/gbp/100
```
- Example 5 - to query operation 3, go to this url(returns 0.087200):
```
http://127.0.0.1:5000/buyask/usd/20
```
- Example 6 - to query operation 3, go to this url(returns 0.114400):
```
http://127.0.0.1:5000/buyask/gbp/200
```

# Shopping Cart Project
 
[Project Description](https://github.com/prof-rossetti/intro-to-python/blob/main/projects/shopping-cart/challenges.md)

## Installation 

Clone or download from [Github source](https://github.com/annava28/shoppingcart), then navigate into the project repository:

```sh
cd shoppingcart
```

## Environment Set Up

Creating the virtual environment:

```sh
conda create -n rps-env python=3.8
```

Activating the virtual environment:

```sh
conda activate rps-env
```

Installing package dependencies:
```sh
pip install -r requirements.txt
```

## Customizing the Sales Tax Rate according to a specific state
Different states have different sales tax rates. To specify your state-specific tax rate, open the repo in VS Code and create an .env file. Within the .env file type "TAX_RATE =" and specify your tax rate (12% should be formatted as 0.12, see below): 

```
TAX_RATE = 0.12
```

## Emailing receipts to yourself
Add to the .env file "SENDGRID_API_KEY = " and "SENDER_ADDRESS = ". To send yourself receipts, you must set up a SendGrid account. Once set up, generate an API key and paste into the .env file, linking it to the API Key variable. Add your desired email address to the Sender Address variable. See below for an example:

```
SENDGRID_API_KEY = (((PASTE YOUR API KEY HERE)))
SENDER_ADDRESS = janedoe@gmail.com
```

## Usage

Run the program:

```sh
python shopping_cart.py
```



from enum import Enum
from fastapi import FastAPI, Path

app = FastAPI()

class AccountType(str, Enum):
    FREE = "free"
    PRO = "pro"

# The three dots mean that the value is required and that no default value has been provided,
#  ge=3 means that the value can be greater or equal to 3, while le=12 means that it can be smaller or equal to 12.


@app.get("/account/{acc_type}/{months}")
async def account( acc_type: AccountType, months:int = Path(...,ge=3, le=12)):
    return {
        "message": "Account_created",
        "account_type":acc_type,
        "months":months
    }
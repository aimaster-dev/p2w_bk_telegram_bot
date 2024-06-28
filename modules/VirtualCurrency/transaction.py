import grequests
import requests
from datetime import datetime

ERC20_API_KEY = "CKPRKVPZ4VPDCG5CHA77MVK9HABDTRE9I7"
TRC20_API_KEY = "c963a2c6-1e36-45f1-80a5-12e83159d5d0"
BEP20_API_KEY = "X4F8NZ47564ZRRMC48FDS1ARQEIXU8TVPQ"


# Get current balance from an address
def get_current_balance(type, address):
    try:
        if type == "erc20":
            api_key = ERC20_API_KEY
            url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={api_key}"
        elif type == "bep20":
            api_key = BEP20_API_KEY
            url = f"https://api.bscscan.com/api?module=account&action=balance&address={address}&tag=latest&apikey={api_key}"
        elif type == "trc20":
            api_key = TRC20_API_KEY
            url = f"https://apilist.tronscanapi.com/api/accountv2?address={address}"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if type == "trc20":
                return float(data["balance"]) / int(1e6)
            else:
                return float(data["result"]) / int(1e18)
    except Exception as err:
        print(err)
    return 0


# Get transaction history from an address
def get_transactions(type, address, fromDate, toDate, rows):
    if rows == None:
        rows = 20

    if type == "erc20":
        api_key = ERC20_API_KEY
        hostUrl = "https://api.etherscan.io/api"
    elif type == "bep20":
        api_key = BEP20_API_KEY
        hostUrl = "https://api.bscscan.com/api"
    elif type == "trc20":
        api_key = TRC20_API_KEY
        hostUrl = "https://apilist.tronscanapi.com/api"

    start_ts = int(datetime.strptime(fromDate, "%Y-%m-%d").timestamp())
    end_ts = int(datetime.strptime(toDate + " 23:59:59", "%Y-%m-%d %H:%M:%S").timestamp())
    startBlockNumber = ''
    endBlockNumber = ''

    if fromDate != None and toDate != None and type != "trc20":
        startReq = grequests.get(
            f"{hostUrl}?module=block&action=getblocknobytime&timestamp={start_ts}&closest=after&apikey={api_key}")
        endReq = grequests.get(
            f"{hostUrl}?module=block&action=getblocknobytime&timestamp={end_ts}&closest=before&apikey={api_key}")
        res = grequests.map([startReq, endReq])

        startData = res[0].json()
        endData = res[1].json()

        startBlockNumber = startData["result"]
        endBlockNumber = endData["result"]

    try:
        if type == "erc20":
            url = f"{hostUrl}?module=account&action=txlist&address={address}&startblock={startBlockNumber}&endblock={endBlockNumber}&sort=asc&page=1&offset={rows}&apikey={api_key}"
        elif type == "bep20":
            url = f"{hostUrl}?module=account&action=txlist&address={address}&startblock={startBlockNumber}&endblock={endBlockNumber}&sort=asc&page=1&offset={rows}&apikey={api_key}"
        elif type == "trc20":
            url = f"{hostUrl}/new/token_trc20/transfers?relatedAddress={address}&start_timestamp={start_ts * 1000}&end_timestamp={end_ts * 1000}&limit={rows}&filterTokenValue=1"

        response = requests.get(url)
        if response.status_code == 200:
            resData = []
            data = response.json()

            if "result" in data:
                for record in data["result"]:
                    timestamp = datetime.fromtimestamp(int(record["timeStamp"])).strftime("%Y-%m-%d %H:%M:%S")
                    resData.append({
                        "time": timestamp,
                        "value": float(record["value"]) / int(1e18),
                        "transfer": "in" if record["to"] == address else "out"
                    })
            elif "token_transfers" in data:
                for record in data["token_transfers"]:
                    timestamp = datetime.fromtimestamp(int(record["block_ts"]) / 1000).strftime("%Y-%m-%d %H:%M:%S")
                    resData.append({
                        "time": timestamp,
                        "value": float(record["quant"]) / int(1e6),
                        "transfer": "in" if record["to_address"] == address else "out"
                    })
            return resData
    except Exception as err:
        print(err)
    return []


# Create your views here.
def erc20(address, startDate, endDate, rows):
    return {
        "current_balance": get_current_balance("erc20", address),
        "transactions": get_transactions("erc20", address, startDate, endDate, rows)
    }


def bep20(address, startDate, endDate, rows):
    return {
        "current_balance": get_current_balance("bep20", address),
        "transactions": get_transactions("bep20", address, startDate, endDate, rows)
    }


def trc20(address, startDate, endDate, rows):
    return {
        "current_balance": get_current_balance("trc20", address),
        "transactions": get_transactions("trc20", address, startDate, endDate, rows)
    }


def showData(data):
    print(f"Current balance: {data['current_balance']}")
    print("Transactions:")
    for transaction in data['transactions']:
        print("-------------")
        print(f"Time: {transaction['time']}")
        print(f"value: {transaction['value']}")
        print(f"transter: {transaction['transfer']}")


erc20_address = "0xCAFb065e343c174a8623494d4A54Ba29AA990D74"
bep20_address = "0xCAFb065e343c174a8623494d4A54Ba29AA990D74"
trc20_address = "TMJRykMuw7WwmxWDcSiWMuefj2xqZPKGTA"

erc20_data = erc20(erc20_address, "2023-03-01", "2023-11-01", 2)
bep20_data = bep20(bep20_address, "2023-05-01", "2023-10-01", 3)
trc20_data = trc20(trc20_address, "2023-11-01", "2023-12-30", 5)

print("\n**************** erc20 ****************\n")
showData(erc20_data)
print("\n**************** bep20 ****************\n")
showData(bep20_data)
print("\n**************** trc20 ****************\n")
showData(trc20_data)

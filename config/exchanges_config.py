import time

exchanges = { 
    "gateio": {
        "ws": "wss://api.gateio.ws/ws/v4/",
        "currencies": "https://api.gateio.ws/api/v4/spot/currencies",
        "request": {
            "time": int(time.time()),
            "channel": "spot.book_ticker",
            "event": "subscribe", # "unsubscribe" for unsubscription
            "payload": ""
        },
        "auth": "",
        "isAuth": False
    },
    "indodax": {
        "ws": "wss://ws3.indodax.com/ws",
        "currencies": "https://indodax.com/api/pairs",
        "request" : {
            "method": 1,
            "params": {
                "channel": "market:order-book-"
            },
            "id":3
        },
        "auth": {
            "url": "",
            "method": '',
            "request": {
                "params": {
                    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE5NDY2MTg0MTV9.UR1lBM6Eqh0yWz-PVirw1uPCxe60FdchR8eNVdsskeo"
                },
                "id": 1
            }    
        },
        "isAuth": True
    },
    "bitmart": {
        "ws": "wss://ws-manager-compress.bitmart.com/api?protocol=1.1",
        "currencies": "https://api-cloud.bitmart.com/spot/v1/currencies",
        "request": {
            'op': 'subscribe',
            'args': 'spot/depth5:BTC_USDT'
        },
        "auth": {},
        "isAuth": False
    },
    "binance": {
        "ws": "wss://stream.binance.com:9443/ws",
        "currencies" : "https://api.binance.com/api/v3/exchangeInfo",
        "request": {
            "method": "SUBSCRIBE",
            "params":[
                "<>@depth"
            ],
            "id": 1
        },
        "auth": {},
        "isAuth": False
    },
    "kukoin": {
        "ws": "wss://ws-api-spot.kucoin.com/?token=<token>&connectId=123",
        "currencies": "https://api.kucoin.com/api/v3/currencies",
        "request": {
            "id": 1545910660739,
            "type": "subscribe",
            "topic": "/spotMarket/level2Depth5:BTC-USDT",
            "response": True
        },
        "auth": {
            "url":"https://api.kucoin.com/api/v1/bullet-public",
            "method": 'post',
            "request":{}
        },
        "isAuth": True
    }
}
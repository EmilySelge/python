revenue = {
    "Johnver": {
        "tea": 190,
        "coffee": 325,
        "water": 682,
        "milk": 829
    },

    "Vanston": {
        "tea": 140,
        "coffee": 19,
        "water": 14,
        "milk": 140
    },

     "Danbree": {
        "tea": 1926,
        "coffee": 293,
        "water": 852,
        "milk": 609
    },

     "Vansey": {
        "tea": 14,
        "coffee": 1491,
        "water": 56,
        "milk": 120
    },

     "Mundyke": {
        "tea": 143,
        "coffee": 162,
        "water": 659,
        "milk": 87
    }
}

expenses = {
    "Johnver": {
        "tea": 120,
        "coffee": 300,
        "water": 50,
        "milk": 67
    },

    "Vanston": {
        "tea": 65,
        "coffee": 10,
        "water": 299,
        "milk": 254
    },

     "Danbree": {
        "tea": 890,
        "coffee": 23,
        "water": 1290,
        "milk": 89
    },

     "Vansey": {
        "tea": 54,
        "coffee": 802,
        "water": 12,
        "milk": 129
    },

     "Mundyke": {
        "tea": 430,
        "coffee": 235,
        "water": 145,
        "milk": 76
    }
}

for key in revenue:
    total_profit = 0
    for drink in revenue[key]:
        profit = revenue[key][drink] - expenses[key][drink]
        if profit > 0:
            total_profit += profit
    
    print(key, round(total_profit * 0.062))
import gurobipy as gp
from gurobipy import GRB

def solve_min_cost_flow(nodes, arcs):
    # Create a new model
    m = gp.Model("min_cost_flow")

    # Create variables
    flows = {}
    for arc in arcs:
        flows[(arc['from'], arc['to'])] = m.addVar(lb=arc['lower_bound'], ub=arc['upper_bound'], vtype=gp.GRB.CONTINUOUS,
                                                   name=f"flow_{arc['from']}_{arc['to']}")

    # Set objective
    m.setObjective(gp.quicksum(arc['cost'] * flows[(arc['from'], arc['to'])] for arc in arcs), sense=gp.GRB.MINIMIZE)

    # Add flow conservation constraints
    for node, data in nodes.items():
        inflow = gp.quicksum(flows[(arc['from'], arc['to'])] for arc in arcs if arc['to'] == node)
        outflow = gp.quicksum(flows[(arc['from'], arc['to'])] for arc in arcs if arc['from'] == node)
        m.addConstr(inflow - outflow == data['demand'], name=f"balance_{node}")

    # Optimize model
    m.optimize()

    # Extract solution
    if m.status == gp.GRB.OPTIMAL:
        solution_flows = {arc: var.x for arc, var in flows.items()}
        total_cost = sum(arc['cost'] * solution_flows[(arc['from'], arc['to'])] for arc in arcs)
        return solution_flows, total_cost
    else:
        print("No optimal solution found.")
        return None, None


nodes = {
        "1": {
            "demand": -1137
        },
        "2": {
            "demand": -1000
        },
        "3": {
            "demand": -1194
        },
        "4": {
            "demand": -535
        },
        "5": {
            "demand": -1094
        },
        "6": {
            "demand": -414
        },
        "7": {
            "demand": -686
        },
        "8": {
            "demand": -1055
        },
        "9": {
            "demand": -372
        },
        "10": {
            "demand": -2273
        },
        "11": {
            "demand": -92
        },
        "12": {
            "demand": -590
        },
        "13": {
            "demand": -503
        },
        "14": {
            "demand": -1905
        },
        "15": {
            "demand": -800
        },
        "16": {
            "demand": -2350
        },
        "17": {
            "demand": 0
        },
        "18": {
            "demand": 0
        },
        "19": {
            "demand": 0
        },
        "20": {
            "demand": 0
        },
        "21": {
            "demand": 0
        },
        "22": {
            "demand": 0
        },
        "23": {
            "demand": 0
        },
        "24": {
            "demand": 0
        },
        "25": {
            "demand": 0
        },
        "26": {
            "demand": 0
        },
        "27": {
            "demand": 0
        },
        "28": {
            "demand": 0
        },
        "29": {
            "demand": 0
        },
        "30": {
            "demand": 0
        },
        "31": {
            "demand": 0
        },
        "32": {
            "demand": 0
        },
        "33": {
            "demand": 0
        },
        "34": {
            "demand": 0
        },
        "35": {
            "demand": 0
        },
        "36": {
            "demand": 0
        },
        "37": {
            "demand": 0
        },
        "38": {
            "demand": 0
        },
        "39": {
            "demand": 0
        },
        "40": {
            "demand": 0
        },
        "41": {
            "demand": 0
        },
        "42": {
            "demand": 0
        },
        "43": {
            "demand": 0
        },
        "44": {
            "demand": 0
        },
        "45": {
            "demand": 0
        },
        "46": {
            "demand": 0
        },
        "47": {
            "demand": 0
        },
        "48": {
            "demand": 0
        },
        "49": {
            "demand": 0
        },
        "50": {
            "demand": 0
        },
        "51": {
            "demand": 0
        },
        "52": {
            "demand": 0
        },
        "53": {
            "demand": 0
        },
        "54": {
            "demand": 0
        },
        "55": {
            "demand": 0
        },
        "56": {
            "demand": 0
        },
        "57": {
            "demand": 0
        },
        "58": {
            "demand": 0
        },
        "59": {
            "demand": 0
        },
        "60": {
            "demand": 0
        },
        "61": {
            "demand": 0
        },
        "62": {
            "demand": 0
        },
        "63": {
            "demand": 0
        },
        "64": {
            "demand": 0
        },
        "65": {
            "demand": 0
        },
        "66": {
            "demand": 0
        },
        "67": {
            "demand": 0
        },
        "68": {
            "demand": 0
        },
        "69": {
            "demand": 0
        },
        "70": {
            "demand": 0
        },
        "71": {
            "demand": 0
        },
        "72": {
            "demand": 0
        },
        "73": {
            "demand": 0
        },
        "74": {
            "demand": 0
        },
        "75": {
            "demand": 0
        },
        "76": {
            "demand": 0
        },
        "77": {
            "demand": 0
        },
        "78": {
            "demand": 0
        },
        "79": {
            "demand": 0
        },
        "80": {
            "demand": 0
        },
        "81": {
            "demand": 0
        },
        "82": {
            "demand": 0
        },
        "83": {
            "demand": 0
        },
        "84": {
            "demand": 0
        },
        "85": {
            "demand": 0
        },
        "86": {
            "demand": 0
        },
        "87": {
            "demand": 0
        },
        "88": {
            "demand": 0
        },
        "89": {
            "demand": 0
        },
        "90": {
            "demand": 0
        },
        "91": {
            "demand": 0
        },
        "92": {
            "demand": 0
        },
        "93": {
            "demand": 0
        },
        "94": {
            "demand": 0
        },
        "95": {
            "demand": 0
        },
        "96": {
            "demand": 0
        },
        "97": {
            "demand": 0
        },
        "98": {
            "demand": 0
        },
        "99": {
            "demand": 0
        },
        "100": {
            "demand": 0
        },
        "101": {
            "demand": 0
        },
        "102": {
            "demand": 0
        },
        "103": {
            "demand": 0
        },
        "104": {
            "demand": 0
        },
        "105": {
            "demand": 0
        },
        "106": {
            "demand": 0
        },
        "107": {
            "demand": 0
        },
        "108": {
            "demand": 0
        },
        "109": {
            "demand": 0
        },
        "110": {
            "demand": 0
        },
        "111": {
            "demand": 0
        },
        "112": {
            "demand": 0
        },
        "113": {
            "demand": 0
        },
        "114": {
            "demand": 0
        },
        "115": {
            "demand": 0
        },
        "116": {
            "demand": 0
        },
        "117": {
            "demand": 0
        },
        "118": {
            "demand": 0
        },
        "119": {
            "demand": 0
        },
        "120": {
            "demand": 0
        },
        "121": {
            "demand": 0
        },
        "122": {
            "demand": 0
        },
        "123": {
            "demand": 0
        },
        "124": {
            "demand": 0
        },
        "125": {
            "demand": 0
        },
        "126": {
            "demand": 0
        },
        "127": {
            "demand": 0
        },
        "128": {
            "demand": 0
        },
        "129": {
            "demand": 0
        },
        "130": {
            "demand": 0
        },
        "131": {
            "demand": 0
        },
        "132": {
            "demand": 0
        },
        "133": {
            "demand": 0
        },
        "134": {
            "demand": 0
        },
        "135": {
            "demand": 0
        },
        "136": {
            "demand": 0
        },
        "137": {
            "demand": 0
        },
        "138": {
            "demand": 0
        },
        "139": {
            "demand": 0
        },
        "140": {
            "demand": 0
        },
        "141": {
            "demand": 0
        },
        "142": {
            "demand": 0
        },
        "143": {
            "demand": 0
        },
        "144": {
            "demand": 0
        },
        "145": {
            "demand": 0
        },
        "146": {
            "demand": 0
        },
        "147": {
            "demand": 0
        },
        "148": {
            "demand": 0
        },
        "149": {
            "demand": 0
        },
        "150": {
            "demand": 0
        },
        "151": {
            "demand": 0
        },
        "152": {
            "demand": 0
        },
        "153": {
            "demand": 0
        },
        "154": {
            "demand": 0
        },
        "155": {
            "demand": 0
        },
        "156": {
            "demand": 0
        },
        "157": {
            "demand": 0
        },
        "158": {
            "demand": 0
        },
        "159": {
            "demand": 0
        },
        "160": {
            "demand": 0
        },
        "161": {
            "demand": 0
        },
        "162": {
            "demand": 0
        },
        "163": {
            "demand": 0
        },
        "164": {
            "demand": 0
        },
        "165": {
            "demand": 0
        },
        "166": {
            "demand": 0
        },
        "167": {
            "demand": 0
        },
        "168": {
            "demand": 0
        },
        "169": {
            "demand": 0
        },
        "170": {
            "demand": 0
        },
        "171": {
            "demand": 0
        },
        "172": {
            "demand": 0
        },
        "173": {
            "demand": 0
        },
        "174": {
            "demand": 0
        },
        "175": {
            "demand": 0
        },
        "176": {
            "demand": 0
        },
        "177": {
            "demand": 0
        },
        "178": {
            "demand": 0
        },
        "179": {
            "demand": 0
        },
        "180": {
            "demand": 0
        },
        "181": {
            "demand": 0
        },
        "182": {
            "demand": 0
        },
        "183": {
            "demand": 0
        },
        "184": {
            "demand": 0
        },
        "185": {
            "demand": 0
        },
        "186": {
            "demand": 0
        },
        "187": {
            "demand": 0
        },
        "188": {
            "demand": 0
        },
        "189": {
            "demand": 0
        },
        "190": {
            "demand": 0
        },
        "191": {
            "demand": 0
        },
        "192": {
            "demand": 0
        },
        "193": {
            "demand": 0
        },
        "194": {
            "demand": 0
        },
        "195": {
            "demand": 0
        },
        "196": {
            "demand": 0
        },
        "197": {
            "demand": 0
        },
        "198": {
            "demand": 0
        },
        "199": {
            "demand": 0
        },
        "200": {
            "demand": 0
        },
        "201": {
            "demand": 0
        },
        "202": {
            "demand": 0
        },
        "203": {
            "demand": 0
        },
        "204": {
            "demand": 0
        },
        "205": {
            "demand": 0
        },
        "206": {
            "demand": 0
        },
        "207": {
            "demand": 0
        },
        "208": {
            "demand": 0
        },
        "209": {
            "demand": 0
        },
        "210": {
            "demand": 0
        },
        "211": {
            "demand": 0
        },
        "212": {
            "demand": 0
        },
        "213": {
            "demand": 0
        },
        "214": {
            "demand": 0
        },
        "215": {
            "demand": 0
        },
        "216": {
            "demand": 0
        },
        "217": {
            "demand": 0
        },
        "218": {
            "demand": 0
        },
        "219": {
            "demand": 0
        },
        "220": {
            "demand": 0
        },
        "221": {
            "demand": 0
        },
        "222": {
            "demand": 0
        },
        "223": {
            "demand": 0
        },
        "224": {
            "demand": 0
        },
        "225": {
            "demand": 0
        },
        "226": {
            "demand": 0
        },
        "227": {
            "demand": 0
        },
        "228": {
            "demand": 0
        },
        "229": {
            "demand": 0
        },
        "230": {
            "demand": 0
        },
        "231": {
            "demand": 0
        },
        "232": {
            "demand": 0
        },
        "233": {
            "demand": 0
        },
        "234": {
            "demand": 0
        },
        "235": {
            "demand": 0
        },
        "236": {
            "demand": 0
        },
        "237": {
            "demand": 0
        },
        "238": {
            "demand": 0
        },
        "239": {
            "demand": 0
        },
        "240": {
            "demand": 0
        },
        "241": {
            "demand": 956
        },
        "242": {
            "demand": 262
        },
        "243": {
            "demand": 102
        },
        "244": {
            "demand": 3396
        },
        "245": {
            "demand": 2398
        },
        "246": {
            "demand": 461
        },
        "247": {
            "demand": 585
        },
        "248": {
            "demand": 155
        },
        "249": {
            "demand": 854
        },
        "250": {
            "demand": 1530
        },
        "251": {
            "demand": 1102
        },
        "252": {
            "demand": 509
        },
        "253": {
            "demand": 595
        },
        "254": {
            "demand": 315
        },
        "255": {
            "demand": 2280
        },
        "256": {
            "demand": 500
        }
}

arcs = [
        {
            "from": "1",
            "to": "156",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1137
        },
        {
            "from": "1",
            "to": "146",
            "cost": 4678,
            "lower_bound": 0,
            "upper_bound": 967
        },
        {
            "from": "1",
            "to": "139",
            "cost": 1127,
            "lower_bound": 0,
            "upper_bound": 752
        },
        {
            "from": "1",
            "to": "183",
            "cost": 660,
            "lower_bound": 0,
            "upper_bound": 613
        },
        {
            "from": "1",
            "to": "199",
            "cost": 53,
            "lower_bound": 0,
            "upper_bound": 15
        },
        {
            "from": "1",
            "to": "251",
            "cost": 5430,
            "lower_bound": 0,
            "upper_bound": 549
        },
        {
            "from": "1",
            "to": "202",
            "cost": 168,
            "lower_bound": 0,
            "upper_bound": 236
        },
        {
            "from": "1",
            "to": "227",
            "cost": 1875,
            "lower_bound": 0,
            "upper_bound": 609
        },
        {
            "from": "1",
            "to": "62",
            "cost": 3365,
            "lower_bound": 0,
            "upper_bound": 236
        },
        {
            "from": "1",
            "to": "21",
            "cost": 7645,
            "lower_bound": 0,
            "upper_bound": 841
        },
        {
            "from": "1",
            "to": "119",
            "cost": 8673,
            "lower_bound": 0,
            "upper_bound": 309
        },
        {
            "from": "1",
            "to": "132",
            "cost": 5331,
            "lower_bound": 0,
            "upper_bound": 649
        },
        {
            "from": "27",
            "to": "195",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1137
        },
        {
            "from": "27",
            "to": "93",
            "cost": 5228,
            "lower_bound": 0,
            "upper_bound": 536
        },
        {
            "from": "28",
            "to": "155",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1137
        },
        {
            "from": "28",
            "to": "211",
            "cost": 8388,
            "lower_bound": 0,
            "upper_bound": 737
        },
        {
            "from": "28",
            "to": "82",
            "cost": 5778,
            "lower_bound": 0,
            "upper_bound": 231
        },
        {
            "from": "28",
            "to": "195",
            "cost": 1080,
            "lower_bound": 0,
            "upper_bound": 91
        },
        {
            "from": "28",
            "to": "49",
            "cost": 7388,
            "lower_bound": 0,
            "upper_bound": 606
        },
        {
            "from": "28",
            "to": "150",
            "cost": 8089,
            "lower_bound": 0,
            "upper_bound": 896
        },
        {
            "from": "29",
            "to": "31",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1137
        },
        {
            "from": "29",
            "to": "224",
            "cost": 5428,
            "lower_bound": 0,
            "upper_bound": 944
        },
        {
            "from": "29",
            "to": "202",
            "cost": 5696,
            "lower_bound": 0,
            "upper_bound": 461
        },
        {
            "from": "29",
            "to": "63",
            "cost": 8376,
            "lower_bound": 0,
            "upper_bound": 833
        },
        {
            "from": "29",
            "to": "108",
            "cost": 1298,
            "lower_bound": 0,
            "upper_bound": 426
        },
        {
            "from": "29",
            "to": "225",
            "cost": 6226,
            "lower_bound": 0,
            "upper_bound": 824
        },
        {
            "from": "29",
            "to": "171",
            "cost": 454,
            "lower_bound": 0,
            "upper_bound": 105
        },
        {
            "from": "29",
            "to": "200",
            "cost": 6396,
            "lower_bound": 0,
            "upper_bound": 864
        },
        {
            "from": "29",
            "to": "91",
            "cost": 7574,
            "lower_bound": 0,
            "upper_bound": 780
        },
        {
            "from": "31",
            "to": "125",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1137
        },
        {
            "from": "31",
            "to": "71",
            "cost": 9326,
            "lower_bound": 0,
            "upper_bound": 439
        },
        {
            "from": "31",
            "to": "160",
            "cost": 4039,
            "lower_bound": 0,
            "upper_bound": 174
        },
        {
            "from": "31",
            "to": "133",
            "cost": 7345,
            "lower_bound": 0,
            "upper_bound": 965
        },
        {
            "from": "31",
            "to": "45",
            "cost": 8782,
            "lower_bound": 0,
            "upper_bound": 235
        },
        {
            "from": "31",
            "to": "224",
            "cost": 2244,
            "lower_bound": 0,
            "upper_bound": 386
        },
        {
            "from": "31",
            "to": "32",
            "cost": 9253,
            "lower_bound": 0,
            "upper_bound": 398
        },
        {
            "from": "31",
            "to": "228",
            "cost": 2003,
            "lower_bound": 0,
            "upper_bound": 232
        },
        {
            "from": "31",
            "to": "194",
            "cost": 3814,
            "lower_bound": 0,
            "upper_bound": 282
        },
        {
            "from": "31",
            "to": "129",
            "cost": 6098,
            "lower_bound": 0,
            "upper_bound": 367
        },
        {
            "from": "31",
            "to": "222",
            "cost": 5021,
            "lower_bound": 0,
            "upper_bound": 215
        },
        {
            "from": "31",
            "to": "232",
            "cost": 980,
            "lower_bound": 0,
            "upper_bound": 752
        },
        {
            "from": "52",
            "to": "104",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1137
        },
        {
            "from": "52",
            "to": "141",
            "cost": 5179,
            "lower_bound": 0,
            "upper_bound": 539
        },
        {
            "from": "52",
            "to": "247",
            "cost": 4335,
            "lower_bound": 0,
            "upper_bound": 271
        },
        {
            "from": "52",
            "to": "253",
            "cost": 4571,
            "lower_bound": 0,
            "upper_bound": 759
        },
        {
            "from": "86",
            "to": "147",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1137
        },
        {
            "from": "86",
            "to": "226",
            "cost": 6110,
            "lower_bound": 0,
            "upper_bound": 606
        },
        {
            "from": "86",
            "to": "96",
            "cost": 4729,
            "lower_bound": 0,
            "upper_bound": 116
        },
        {
            "from": "86",
            "to": "57",
            "cost": 8476,
            "lower_bound": 0,
            "upper_bound": 999
        },
        {
            "from": "86",
            "to": "70",
            "cost": 8757,
            "lower_bound": 0,
            "upper_bound": 10
        },
        {
            "from": "86",
            "to": "112",
            "cost": 2594,
            "lower_bound": 0,
            "upper_bound": 5
        },
        {
            "from": "104",
            "to": "198",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1137
        },
        {
            "from": "104",
            "to": "50",
            "cost": 9337,
            "lower_bound": 0,
            "upper_bound": 589
        },
        {
            "from": "104",
            "to": "254",
            "cost": 1784,
            "lower_bound": 0,
            "upper_bound": 525
        },
        {
            "from": "104",
            "to": "187",
            "cost": 7713,
            "lower_bound": 0,
            "upper_bound": 266
        },
        {
            "from": "104",
            "to": "179",
            "cost": 3765,
            "lower_bound": 0,
            "upper_bound": 194
        },
        {
            "from": "104",
            "to": "240",
            "cost": 8750,
            "lower_bound": 0,
            "upper_bound": 577
        },
        {
            "from": "104",
            "to": "214",
            "cost": 2421,
            "lower_bound": 0,
            "upper_bound": 669
        },
        {
            "from": "104",
            "to": "219",
            "cost": 7226,
            "lower_bound": 0,
            "upper_bound": 863
        },
        {
            "from": "123",
            "to": "161",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1137
        },
        {
            "from": "123",
            "to": "247",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1137
        },
        {
            "from": "123",
            "to": "57",
            "cost": 5677,
            "lower_bound": 0,
            "upper_bound": 286
        },
        {
            "from": "123",
            "to": "197",
            "cost": 2534,
            "lower_bound": 0,
            "upper_bound": 773
        },
        {
            "from": "123",
            "to": "192",
            "cost": 9915,
            "lower_bound": 0,
            "upper_bound": 204
        },
        {
            "from": "123",
            "to": "187",
            "cost": 2533,
            "lower_bound": 0,
            "upper_bound": 24
        },
        {
            "from": "123",
            "to": "207",
            "cost": 2667,
            "lower_bound": 0,
            "upper_bound": 212
        },
        {
            "from": "123",
            "to": "100",
            "cost": 5826,
            "lower_bound": 0,
            "upper_bound": 478
        },
        {
            "from": "125",
            "to": "251",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1137
        },
        {
            "from": "125",
            "to": "75",
            "cost": 3097,
            "lower_bound": 0,
            "upper_bound": 703
        },
        {
            "from": "125",
            "to": "169",
            "cost": 2747,
            "lower_bound": 0,
            "upper_bound": 374
        },
        {
            "from": "125",
            "to": "190",
            "cost": 4535,
            "lower_bound": 0,
            "upper_bound": 434
        },
        {
            "from": "125",
            "to": "209",
            "cost": 3146,
            "lower_bound": 0,
            "upper_bound": 226
        },
        {
            "from": "125",
            "to": "235",
            "cost": 777,
            "lower_bound": 0,
            "upper_bound": 602
        },
        {
            "from": "125",
            "to": "176",
            "cost": 1609,
            "lower_bound": 0,
            "upper_bound": 229
        },
        {
            "from": "125",
            "to": "252",
            "cost": 1221,
            "lower_bound": 0,
            "upper_bound": 862
        },
        {
            "from": "125",
            "to": "46",
            "cost": 378,
            "lower_bound": 0,
            "upper_bound": 22
        },
        {
            "from": "125",
            "to": "141",
            "cost": 9166,
            "lower_bound": 0,
            "upper_bound": 40
        },
        {
            "from": "125",
            "to": "45",
            "cost": 7837,
            "lower_bound": 0,
            "upper_bound": 846
        },
        {
            "from": "125",
            "to": "88",
            "cost": 4844,
            "lower_bound": 0,
            "upper_bound": 460
        },
        {
            "from": "147",
            "to": "210",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1137
        },
        {
            "from": "147",
            "to": "129",
            "cost": 377,
            "lower_bound": 0,
            "upper_bound": 538
        },
        {
            "from": "147",
            "to": "209",
            "cost": 3662,
            "lower_bound": 0,
            "upper_bound": 534
        },
        {
            "from": "147",
            "to": "237",
            "cost": 683,
            "lower_bound": 0,
            "upper_bound": 487
        },
        {
            "from": "147",
            "to": "223",
            "cost": 4842,
            "lower_bound": 0,
            "upper_bound": 692
        },
        {
            "from": "147",
            "to": "144",
            "cost": 6372,
            "lower_bound": 0,
            "upper_bound": 609
        },
        {
            "from": "147",
            "to": "42",
            "cost": 9661,
            "lower_bound": 0,
            "upper_bound": 763
        },
        {
            "from": "147",
            "to": "83",
            "cost": 9467,
            "lower_bound": 0,
            "upper_bound": 217
        },
        {
            "from": "147",
            "to": "249",
            "cost": 5949,
            "lower_bound": 0,
            "upper_bound": 894
        },
        {
            "from": "147",
            "to": "188",
            "cost": 759,
            "lower_bound": 0,
            "upper_bound": 30
        },
        {
            "from": "147",
            "to": "40",
            "cost": 889,
            "lower_bound": 0,
            "upper_bound": 301
        },
        {
            "from": "147",
            "to": "161",
            "cost": 3783,
            "lower_bound": 0,
            "upper_bound": 202
        },
        {
            "from": "147",
            "to": "69",
            "cost": 8334,
            "lower_bound": 0,
            "upper_bound": 231
        },
        {
            "from": "147",
            "to": "136",
            "cost": 9058,
            "lower_bound": 0,
            "upper_bound": 588
        },
        {
            "from": "147",
            "to": "66",
            "cost": 1803,
            "lower_bound": 0,
            "upper_bound": 582
        },
        {
            "from": "155",
            "to": "27",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1137
        },
        {
            "from": "155",
            "to": "233",
            "cost": 5560,
            "lower_bound": 0,
            "upper_bound": 737
        },
        {
            "from": "155",
            "to": "189",
            "cost": 6105,
            "lower_bound": 0,
            "upper_bound": 299
        },
        {
            "from": "155",
            "to": "145",
            "cost": 8543,
            "lower_bound": 0,
            "upper_bound": 323
        },
        {
            "from": "155",
            "to": "110",
            "cost": 9122,
            "lower_bound": 0,
            "upper_bound": 823
        },
        {
            "from": "155",
            "to": "93",
            "cost": 8382,
            "lower_bound": 0,
            "upper_bound": 135
        },
        {
            "from": "155",
            "to": "106",
            "cost": 9717,
            "lower_bound": 0,
            "upper_bound": 503
        },
        {
            "from": "155",
            "to": "192",
            "cost": 7042,
            "lower_bound": 0,
            "upper_bound": 92
        },
        {
            "from": "155",
            "to": "35",
            "cost": 2220,
            "lower_bound": 0,
            "upper_bound": 682
        },
        {
            "from": "155",
            "to": "23",
            "cost": 6609,
            "lower_bound": 0,
            "upper_bound": 681
        },
        {
            "from": "156",
            "to": "123",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1137
        },
        {
            "from": "156",
            "to": "248",
            "cost": 9284,
            "lower_bound": 0,
            "upper_bound": 973
        },
        {
            "from": "156",
            "to": "118",
            "cost": 9998,
            "lower_bound": 0,
            "upper_bound": 762
        },
        {
            "from": "156",
            "to": "176",
            "cost": 9648,
            "lower_bound": 0,
            "upper_bound": 881
        },
        {
            "from": "156",
            "to": "47",
            "cost": 4350,
            "lower_bound": 0,
            "upper_bound": 405
        },
        {
            "from": "156",
            "to": "135",
            "cost": 4762,
            "lower_bound": 0,
            "upper_bound": 150
        },
        {
            "from": "156",
            "to": "207",
            "cost": 5061,
            "lower_bound": 0,
            "upper_bound": 794
        },
        {
            "from": "156",
            "to": "141",
            "cost": 2299,
            "lower_bound": 0,
            "upper_bound": 359
        },
        {
            "from": "156",
            "to": "184",
            "cost": 1124,
            "lower_bound": 0,
            "upper_bound": 888
        },
        {
            "from": "156",
            "to": "73",
            "cost": 928,
            "lower_bound": 0,
            "upper_bound": 140
        },
        {
            "from": "156",
            "to": "161",
            "cost": 6045,
            "lower_bound": 0,
            "upper_bound": 763
        },
        {
            "from": "156",
            "to": "227",
            "cost": 4802,
            "lower_bound": 0,
            "upper_bound": 90
        },
        {
            "from": "156",
            "to": "67",
            "cost": 8993,
            "lower_bound": 0,
            "upper_bound": 802
        },
        {
            "from": "156",
            "to": "171",
            "cost": 3211,
            "lower_bound": 0,
            "upper_bound": 32
        },
        {
            "from": "156",
            "to": "20",
            "cost": 5557,
            "lower_bound": 0,
            "upper_bound": 616
        },
        {
            "from": "161",
            "to": "52",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1137
        },
        {
            "from": "161",
            "to": "61",
            "cost": 3819,
            "lower_bound": 0,
            "upper_bound": 351
        },
        {
            "from": "161",
            "to": "31",
            "cost": 8627,
            "lower_bound": 0,
            "upper_bound": 209
        },
        {
            "from": "161",
            "to": "137",
            "cost": 1858,
            "lower_bound": 0,
            "upper_bound": 617
        },
        {
            "from": "161",
            "to": "186",
            "cost": 1536,
            "lower_bound": 0,
            "upper_bound": 148
        },
        {
            "from": "161",
            "to": "33",
            "cost": 5006,
            "lower_bound": 0,
            "upper_bound": 718
        },
        {
            "from": "161",
            "to": "57",
            "cost": 7491,
            "lower_bound": 0,
            "upper_bound": 207
        },
        {
            "from": "195",
            "to": "86",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1137
        },
        {
            "from": "195",
            "to": "109",
            "cost": 9548,
            "lower_bound": 0,
            "upper_bound": 269
        },
        {
            "from": "195",
            "to": "149",
            "cost": 7746,
            "lower_bound": 0,
            "upper_bound": 211
        },
        {
            "from": "195",
            "to": "156",
            "cost": 3970,
            "lower_bound": 0,
            "upper_bound": 668
        },
        {
            "from": "195",
            "to": "138",
            "cost": 5414,
            "lower_bound": 0,
            "upper_bound": 146
        },
        {
            "from": "195",
            "to": "78",
            "cost": 6446,
            "lower_bound": 0,
            "upper_bound": 128
        },
        {
            "from": "195",
            "to": "98",
            "cost": 2177,
            "lower_bound": 0,
            "upper_bound": 279
        },
        {
            "from": "195",
            "to": "74",
            "cost": 5890,
            "lower_bound": 0,
            "upper_bound": 688
        },
        {
            "from": "195",
            "to": "71",
            "cost": 3192,
            "lower_bound": 0,
            "upper_bound": 947
        },
        {
            "from": "195",
            "to": "124",
            "cost": 552,
            "lower_bound": 0,
            "upper_bound": 355
        },
        {
            "from": "195",
            "to": "112",
            "cost": 5309,
            "lower_bound": 0,
            "upper_bound": 60
        },
        {
            "from": "195",
            "to": "211",
            "cost": 2410,
            "lower_bound": 0,
            "upper_bound": 246
        },
        {
            "from": "198",
            "to": "28",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1137
        },
        {
            "from": "198",
            "to": "47",
            "cost": 6005,
            "lower_bound": 0,
            "upper_bound": 416
        },
        {
            "from": "198",
            "to": "164",
            "cost": 6423,
            "lower_bound": 0,
            "upper_bound": 245
        },
        {
            "from": "198",
            "to": "70",
            "cost": 2678,
            "lower_bound": 0,
            "upper_bound": 517
        },
        {
            "from": "198",
            "to": "150",
            "cost": 142,
            "lower_bound": 0,
            "upper_bound": 998
        },
        {
            "from": "198",
            "to": "134",
            "cost": 7584,
            "lower_bound": 0,
            "upper_bound": 420
        },
        {
            "from": "198",
            "to": "51",
            "cost": 170,
            "lower_bound": 0,
            "upper_bound": 84
        },
        {
            "from": "198",
            "to": "168",
            "cost": 5736,
            "lower_bound": 0,
            "upper_bound": 220
        },
        {
            "from": "198",
            "to": "76",
            "cost": 9991,
            "lower_bound": 0,
            "upper_bound": 672
        },
        {
            "from": "198",
            "to": "130",
            "cost": 6813,
            "lower_bound": 0,
            "upper_bound": 546
        },
        {
            "from": "198",
            "to": "186",
            "cost": 523,
            "lower_bound": 0,
            "upper_bound": 114
        },
        {
            "from": "198",
            "to": "42",
            "cost": 9255,
            "lower_bound": 0,
            "upper_bound": 262
        },
        {
            "from": "198",
            "to": "158",
            "cost": 3073,
            "lower_bound": 0,
            "upper_bound": 34
        },
        {
            "from": "198",
            "to": "137",
            "cost": 4604,
            "lower_bound": 0,
            "upper_bound": 222
        },
        {
            "from": "210",
            "to": "29",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1137
        },
        {
            "from": "210",
            "to": "73",
            "cost": 884,
            "lower_bound": 0,
            "upper_bound": 903
        },
        {
            "from": "210",
            "to": "45",
            "cost": 7999,
            "lower_bound": 0,
            "upper_bound": 950
        },
        {
            "from": "210",
            "to": "219",
            "cost": 5914,
            "lower_bound": 0,
            "upper_bound": 601
        },
        {
            "from": "210",
            "to": "109",
            "cost": 9491,
            "lower_bound": 0,
            "upper_bound": 669
        },
        {
            "from": "210",
            "to": "167",
            "cost": 4077,
            "lower_bound": 0,
            "upper_bound": 930
        },
        {
            "from": "2",
            "to": "76",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1000
        },
        {
            "from": "2",
            "to": "108",
            "cost": 2667,
            "lower_bound": 0,
            "upper_bound": 873
        },
        {
            "from": "2",
            "to": "133",
            "cost": 9129,
            "lower_bound": 0,
            "upper_bound": 592
        },
        {
            "from": "47",
            "to": "256",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1000
        },
        {
            "from": "47",
            "to": "116",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1000
        },
        {
            "from": "47",
            "to": "119",
            "cost": 1965,
            "lower_bound": 0,
            "upper_bound": 212
        },
        {
            "from": "76",
            "to": "158",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1000
        },
        {
            "from": "76",
            "to": "155",
            "cost": 5220,
            "lower_bound": 0,
            "upper_bound": 171
        },
        {
            "from": "76",
            "to": "62",
            "cost": 6743,
            "lower_bound": 0,
            "upper_bound": 546
        },
        {
            "from": "76",
            "to": "169",
            "cost": 9793,
            "lower_bound": 0,
            "upper_bound": 525
        },
        {
            "from": "76",
            "to": "165",
            "cost": 2182,
            "lower_bound": 0,
            "upper_bound": 16
        },
        {
            "from": "76",
            "to": "208",
            "cost": 9423,
            "lower_bound": 0,
            "upper_bound": 293
        },
        {
            "from": "76",
            "to": "201",
            "cost": 2673,
            "lower_bound": 0,
            "upper_bound": 156
        },
        {
            "from": "76",
            "to": "166",
            "cost": 920,
            "lower_bound": 0,
            "upper_bound": 918
        },
        {
            "from": "76",
            "to": "202",
            "cost": 9565,
            "lower_bound": 0,
            "upper_bound": 979
        },
        {
            "from": "76",
            "to": "229",
            "cost": 4253,
            "lower_bound": 0,
            "upper_bound": 244
        },
        {
            "from": "80",
            "to": "87",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1000
        },
        {
            "from": "80",
            "to": "235",
            "cost": 4689,
            "lower_bound": 0,
            "upper_bound": 735
        },
        {
            "from": "80",
            "to": "150",
            "cost": 4925,
            "lower_bound": 0,
            "upper_bound": 125
        },
        {
            "from": "80",
            "to": "61",
            "cost": 2554,
            "lower_bound": 0,
            "upper_bound": 433
        },
        {
            "from": "80",
            "to": "135",
            "cost": 9992,
            "lower_bound": 0,
            "upper_bound": 64
        },
        {
            "from": "80",
            "to": "186",
            "cost": 9534,
            "lower_bound": 0,
            "upper_bound": 50
        },
        {
            "from": "80",
            "to": "173",
            "cost": 1842,
            "lower_bound": 0,
            "upper_bound": 335
        },
        {
            "from": "80",
            "to": "213",
            "cost": 5495,
            "lower_bound": 0,
            "upper_bound": 362
        },
        {
            "from": "80",
            "to": "176",
            "cost": 5076,
            "lower_bound": 0,
            "upper_bound": 147
        },
        {
            "from": "80",
            "to": "253",
            "cost": 1251,
            "lower_bound": 0,
            "upper_bound": 866
        },
        {
            "from": "80",
            "to": "18",
            "cost": 2771,
            "lower_bound": 0,
            "upper_bound": 258
        },
        {
            "from": "80",
            "to": "142",
            "cost": 6457,
            "lower_bound": 0,
            "upper_bound": 892
        },
        {
            "from": "87",
            "to": "145",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1000
        },
        {
            "from": "87",
            "to": "196",
            "cost": 7750,
            "lower_bound": 0,
            "upper_bound": 843
        },
        {
            "from": "87",
            "to": "77",
            "cost": 7089,
            "lower_bound": 0,
            "upper_bound": 963
        },
        {
            "from": "87",
            "to": "107",
            "cost": 6629,
            "lower_bound": 0,
            "upper_bound": 991
        },
        {
            "from": "87",
            "to": "182",
            "cost": 9891,
            "lower_bound": 0,
            "upper_bound": 165
        },
        {
            "from": "87",
            "to": "64",
            "cost": 5813,
            "lower_bound": 0,
            "upper_bound": 35
        },
        {
            "from": "87",
            "to": "109",
            "cost": 2905,
            "lower_bound": 0,
            "upper_bound": 41
        },
        {
            "from": "87",
            "to": "92",
            "cost": 3991,
            "lower_bound": 0,
            "upper_bound": 68
        },
        {
            "from": "87",
            "to": "96",
            "cost": 5733,
            "lower_bound": 0,
            "upper_bound": 108
        },
        {
            "from": "87",
            "to": "112",
            "cost": 140,
            "lower_bound": 0,
            "upper_bound": 259
        },
        {
            "from": "87",
            "to": "19",
            "cost": 6,
            "lower_bound": 0,
            "upper_bound": 498
        },
        {
            "from": "87",
            "to": "209",
            "cost": 8562,
            "lower_bound": 0,
            "upper_bound": 172
        },
        {
            "from": "87",
            "to": "124",
            "cost": 535,
            "lower_bound": 0,
            "upper_bound": 792
        },
        {
            "from": "87",
            "to": "190",
            "cost": 9177,
            "lower_bound": 0,
            "upper_bound": 407
        },
        {
            "from": "90",
            "to": "181",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1000
        },
        {
            "from": "90",
            "to": "38",
            "cost": 4329,
            "lower_bound": 0,
            "upper_bound": 990
        },
        {
            "from": "90",
            "to": "86",
            "cost": 8468,
            "lower_bound": 0,
            "upper_bound": 687
        },
        {
            "from": "90",
            "to": "205",
            "cost": 4673,
            "lower_bound": 0,
            "upper_bound": 557
        },
        {
            "from": "90",
            "to": "170",
            "cost": 3156,
            "lower_bound": 0,
            "upper_bound": 121
        },
        {
            "from": "90",
            "to": "163",
            "cost": 4535,
            "lower_bound": 0,
            "upper_bound": 540
        },
        {
            "from": "116",
            "to": "230",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1000
        },
        {
            "from": "116",
            "to": "154",
            "cost": 6884,
            "lower_bound": 0,
            "upper_bound": 182
        },
        {
            "from": "141",
            "to": "219",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1000
        },
        {
            "from": "141",
            "to": "158",
            "cost": 9565,
            "lower_bound": 0,
            "upper_bound": 15
        },
        {
            "from": "145",
            "to": "141",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1000
        },
        {
            "from": "145",
            "to": "110",
            "cost": 3870,
            "lower_bound": 0,
            "upper_bound": 815
        },
        {
            "from": "158",
            "to": "237",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1000
        },
        {
            "from": "158",
            "to": "99",
            "cost": 633,
            "lower_bound": 0,
            "upper_bound": 194
        },
        {
            "from": "158",
            "to": "182",
            "cost": 9123,
            "lower_bound": 0,
            "upper_bound": 255
        },
        {
            "from": "158",
            "to": "141",
            "cost": 9561,
            "lower_bound": 0,
            "upper_bound": 11
        },
        {
            "from": "158",
            "to": "124",
            "cost": 1551,
            "lower_bound": 0,
            "upper_bound": 549
        },
        {
            "from": "158",
            "to": "83",
            "cost": 7043,
            "lower_bound": 0,
            "upper_bound": 449
        },
        {
            "from": "158",
            "to": "79",
            "cost": 4720,
            "lower_bound": 0,
            "upper_bound": 535
        },
        {
            "from": "158",
            "to": "118",
            "cost": 8749,
            "lower_bound": 0,
            "upper_bound": 814
        },
        {
            "from": "158",
            "to": "163",
            "cost": 3646,
            "lower_bound": 0,
            "upper_bound": 714
        },
        {
            "from": "158",
            "to": "33",
            "cost": 5925,
            "lower_bound": 0,
            "upper_bound": 49
        },
        {
            "from": "158",
            "to": "65",
            "cost": 9771,
            "lower_bound": 0,
            "upper_bound": 852
        },
        {
            "from": "158",
            "to": "209",
            "cost": 3175,
            "lower_bound": 0,
            "upper_bound": 472
        },
        {
            "from": "158",
            "to": "52",
            "cost": 2588,
            "lower_bound": 0,
            "upper_bound": 992
        },
        {
            "from": "158",
            "to": "238",
            "cost": 4952,
            "lower_bound": 0,
            "upper_bound": 603
        },
        {
            "from": "181",
            "to": "80",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1000
        },
        {
            "from": "181",
            "to": "176",
            "cost": 6085,
            "lower_bound": 0,
            "upper_bound": 954
        },
        {
            "from": "181",
            "to": "215",
            "cost": 3887,
            "lower_bound": 0,
            "upper_bound": 668
        },
        {
            "from": "181",
            "to": "36",
            "cost": 578,
            "lower_bound": 0,
            "upper_bound": 762
        },
        {
            "from": "181",
            "to": "64",
            "cost": 8552,
            "lower_bound": 0,
            "upper_bound": 459
        },
        {
            "from": "181",
            "to": "244",
            "cost": 6014,
            "lower_bound": 0,
            "upper_bound": 494
        },
        {
            "from": "181",
            "to": "117",
            "cost": 1333,
            "lower_bound": 0,
            "upper_bound": 612
        },
        {
            "from": "181",
            "to": "196",
            "cost": 4984,
            "lower_bound": 0,
            "upper_bound": 642
        },
        {
            "from": "181",
            "to": "103",
            "cost": 8477,
            "lower_bound": 0,
            "upper_bound": 165
        },
        {
            "from": "181",
            "to": "44",
            "cost": 2513,
            "lower_bound": 0,
            "upper_bound": 754
        },
        {
            "from": "181",
            "to": "57",
            "cost": 1557,
            "lower_bound": 0,
            "upper_bound": 332
        },
        {
            "from": "197",
            "to": "251",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1000
        },
        {
            "from": "197",
            "to": "72",
            "cost": 6680,
            "lower_bound": 0,
            "upper_bound": 402
        },
        {
            "from": "219",
            "to": "197",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1000
        },
        {
            "from": "219",
            "to": "70",
            "cost": 4585,
            "lower_bound": 0,
            "upper_bound": 232
        },
        {
            "from": "219",
            "to": "199",
            "cost": 2460,
            "lower_bound": 0,
            "upper_bound": 616
        },
        {
            "from": "219",
            "to": "108",
            "cost": 4504,
            "lower_bound": 0,
            "upper_bound": 568
        },
        {
            "from": "219",
            "to": "132",
            "cost": 2130,
            "lower_bound": 0,
            "upper_bound": 482
        },
        {
            "from": "219",
            "to": "114",
            "cost": 6921,
            "lower_bound": 0,
            "upper_bound": 907
        },
        {
            "from": "219",
            "to": "61",
            "cost": 7025,
            "lower_bound": 0,
            "upper_bound": 54
        },
        {
            "from": "230",
            "to": "90",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1000
        },
        {
            "from": "230",
            "to": "126",
            "cost": 5073,
            "lower_bound": 0,
            "upper_bound": 517
        },
        {
            "from": "230",
            "to": "139",
            "cost": 4360,
            "lower_bound": 0,
            "upper_bound": 821
        },
        {
            "from": "237",
            "to": "47",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1000
        },
        {
            "from": "237",
            "to": "32",
            "cost": 6974,
            "lower_bound": 0,
            "upper_bound": 288
        },
        {
            "from": "237",
            "to": "97",
            "cost": 3948,
            "lower_bound": 0,
            "upper_bound": 379
        },
        {
            "from": "237",
            "to": "167",
            "cost": 6527,
            "lower_bound": 0,
            "upper_bound": 522
        },
        {
            "from": "237",
            "to": "238",
            "cost": 6898,
            "lower_bound": 0,
            "upper_bound": 11
        },
        {
            "from": "237",
            "to": "229",
            "cost": 5329,
            "lower_bound": 0,
            "upper_bound": 561
        },
        {
            "from": "237",
            "to": "201",
            "cost": 9405,
            "lower_bound": 0,
            "upper_bound": 364
        },
        {
            "from": "237",
            "to": "102",
            "cost": 6793,
            "lower_bound": 0,
            "upper_bound": 203
        },
        {
            "from": "237",
            "to": "100",
            "cost": 8369,
            "lower_bound": 0,
            "upper_bound": 85
        },
        {
            "from": "3",
            "to": "93",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1194
        },
        {
            "from": "3",
            "to": "160",
            "cost": 4976,
            "lower_bound": 0,
            "upper_bound": 369
        },
        {
            "from": "3",
            "to": "23",
            "cost": 6443,
            "lower_bound": 0,
            "upper_bound": 71
        },
        {
            "from": "3",
            "to": "219",
            "cost": 6592,
            "lower_bound": 0,
            "upper_bound": 880
        },
        {
            "from": "3",
            "to": "211",
            "cost": 3037,
            "lower_bound": 0,
            "upper_bound": 975
        },
        {
            "from": "3",
            "to": "136",
            "cost": 5728,
            "lower_bound": 0,
            "upper_bound": 758
        },
        {
            "from": "3",
            "to": "35",
            "cost": 2364,
            "lower_bound": 0,
            "upper_bound": 752
        },
        {
            "from": "3",
            "to": "162",
            "cost": 2514,
            "lower_bound": 0,
            "upper_bound": 234
        },
        {
            "from": "3",
            "to": "169",
            "cost": 9396,
            "lower_bound": 0,
            "upper_bound": 271
        },
        {
            "from": "19",
            "to": "109",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1194
        },
        {
            "from": "19",
            "to": "95",
            "cost": 8046,
            "lower_bound": 0,
            "upper_bound": 354
        },
        {
            "from": "19",
            "to": "50",
            "cost": 8309,
            "lower_bound": 0,
            "upper_bound": 738
        },
        {
            "from": "19",
            "to": "45",
            "cost": 8735,
            "lower_bound": 0,
            "upper_bound": 131
        },
        {
            "from": "19",
            "to": "86",
            "cost": 672,
            "lower_bound": 0,
            "upper_bound": 575
        },
        {
            "from": "19",
            "to": "58",
            "cost": 5820,
            "lower_bound": 0,
            "upper_bound": 62
        },
        {
            "from": "19",
            "to": "161",
            "cost": 4209,
            "lower_bound": 0,
            "upper_bound": 85
        },
        {
            "from": "19",
            "to": "177",
            "cost": 9693,
            "lower_bound": 0,
            "upper_bound": 352
        },
        {
            "from": "55",
            "to": "117",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1194
        },
        {
            "from": "55",
            "to": "87",
            "cost": 5099,
            "lower_bound": 0,
            "upper_bound": 155
        },
        {
            "from": "55",
            "to": "86",
            "cost": 8622,
            "lower_bound": 0,
            "upper_bound": 779
        },
        {
            "from": "55",
            "to": "249",
            "cost": 3562,
            "lower_bound": 0,
            "upper_bound": 881
        },
        {
            "from": "55",
            "to": "20",
            "cost": 3220,
            "lower_bound": 0,
            "upper_bound": 360
        },
        {
            "from": "55",
            "to": "136",
            "cost": 8807,
            "lower_bound": 0,
            "upper_bound": 562
        },
        {
            "from": "55",
            "to": "164",
            "cost": 3701,
            "lower_bound": 0,
            "upper_bound": 59
        },
        {
            "from": "55",
            "to": "156",
            "cost": 5730,
            "lower_bound": 0,
            "upper_bound": 824
        },
        {
            "from": "55",
            "to": "166",
            "cost": 8761,
            "lower_bound": 0,
            "upper_bound": 717
        },
        {
            "from": "65",
            "to": "224",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1194
        },
        {
            "from": "65",
            "to": "108",
            "cost": 6329,
            "lower_bound": 0,
            "upper_bound": 316
        },
        {
            "from": "65",
            "to": "38",
            "cost": 3369,
            "lower_bound": 0,
            "upper_bound": 586
        },
        {
            "from": "65",
            "to": "131",
            "cost": 8627,
            "lower_bound": 0,
            "upper_bound": 660
        },
        {
            "from": "65",
            "to": "105",
            "cost": 3532,
            "lower_bound": 0,
            "upper_bound": 995
        },
        {
            "from": "65",
            "to": "216",
            "cost": 9779,
            "lower_bound": 0,
            "upper_bound": 642
        },
        {
            "from": "65",
            "to": "84",
            "cost": 2139,
            "lower_bound": 0,
            "upper_bound": 489
        },
        {
            "from": "65",
            "to": "210",
            "cost": 222,
            "lower_bound": 0,
            "upper_bound": 760
        },
        {
            "from": "65",
            "to": "171",
            "cost": 3328,
            "lower_bound": 0,
            "upper_bound": 203
        },
        {
            "from": "65",
            "to": "123",
            "cost": 729,
            "lower_bound": 0,
            "upper_bound": 374
        },
        {
            "from": "65",
            "to": "78",
            "cost": 1549,
            "lower_bound": 0,
            "upper_bound": 111
        },
        {
            "from": "65",
            "to": "95",
            "cost": 7671,
            "lower_bound": 0,
            "upper_bound": 136
        },
        {
            "from": "65",
            "to": "235",
            "cost": 6210,
            "lower_bound": 0,
            "upper_bound": 178
        },
        {
            "from": "65",
            "to": "21",
            "cost": 5372,
            "lower_bound": 0,
            "upper_bound": 931
        },
        {
            "from": "65",
            "to": "120",
            "cost": 7505,
            "lower_bound": 0,
            "upper_bound": 30
        },
        {
            "from": "78",
            "to": "55",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1194
        },
        {
            "from": "78",
            "to": "190",
            "cost": 8353,
            "lower_bound": 0,
            "upper_bound": 457
        },
        {
            "from": "78",
            "to": "233",
            "cost": 423,
            "lower_bound": 0,
            "upper_bound": 872
        },
        {
            "from": "78",
            "to": "54",
            "cost": 1884,
            "lower_bound": 0,
            "upper_bound": 685
        },
        {
            "from": "78",
            "to": "57",
            "cost": 4460,
            "lower_bound": 0,
            "upper_bound": 991
        },
        {
            "from": "78",
            "to": "59",
            "cost": 8753,
            "lower_bound": 0,
            "upper_bound": 309
        },
        {
            "from": "78",
            "to": "210",
            "cost": 7896,
            "lower_bound": 0,
            "upper_bound": 865
        },
        {
            "from": "78",
            "to": "220",
            "cost": 1124,
            "lower_bound": 0,
            "upper_bound": 690
        },
        {
            "from": "78",
            "to": "182",
            "cost": 5690,
            "lower_bound": 0,
            "upper_bound": 926
        },
        {
            "from": "78",
            "to": "242",
            "cost": 2689,
            "lower_bound": 0,
            "upper_bound": 190
        },
        {
            "from": "78",
            "to": "147",
            "cost": 2507,
            "lower_bound": 0,
            "upper_bound": 825
        },
        {
            "from": "78",
            "to": "52",
            "cost": 6090,
            "lower_bound": 0,
            "upper_bound": 52
        },
        {
            "from": "78",
            "to": "169",
            "cost": 2706,
            "lower_bound": 0,
            "upper_bound": 418
        },
        {
            "from": "78",
            "to": "27",
            "cost": 3484,
            "lower_bound": 0,
            "upper_bound": 263
        },
        {
            "from": "89",
            "to": "228",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1194
        },
        {
            "from": "89",
            "to": "203",
            "cost": 7585,
            "lower_bound": 0,
            "upper_bound": 629
        },
        {
            "from": "89",
            "to": "127",
            "cost": 8008,
            "lower_bound": 0,
            "upper_bound": 499
        },
        {
            "from": "89",
            "to": "236",
            "cost": 9901,
            "lower_bound": 0,
            "upper_bound": 879
        },
        {
            "from": "89",
            "to": "133",
            "cost": 9765,
            "lower_bound": 0,
            "upper_bound": 372
        },
        {
            "from": "89",
            "to": "82",
            "cost": 1268,
            "lower_bound": 0,
            "upper_bound": 788
        },
        {
            "from": "93",
            "to": "110",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1194
        },
        {
            "from": "93",
            "to": "49",
            "cost": 3749,
            "lower_bound": 0,
            "upper_bound": 622
        },
        {
            "from": "93",
            "to": "186",
            "cost": 1049,
            "lower_bound": 0,
            "upper_bound": 771
        },
        {
            "from": "93",
            "to": "201",
            "cost": 5274,
            "lower_bound": 0,
            "upper_bound": 217
        },
        {
            "from": "109",
            "to": "175",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1194
        },
        {
            "from": "109",
            "to": "25",
            "cost": 9416,
            "lower_bound": 0,
            "upper_bound": 707
        },
        {
            "from": "109",
            "to": "210",
            "cost": 8319,
            "lower_bound": 0,
            "upper_bound": 467
        },
        {
            "from": "109",
            "to": "94",
            "cost": 7437,
            "lower_bound": 0,
            "upper_bound": 911
        },
        {
            "from": "109",
            "to": "240",
            "cost": 1118,
            "lower_bound": 0,
            "upper_bound": 960
        },
        {
            "from": "109",
            "to": "247",
            "cost": 6133,
            "lower_bound": 0,
            "upper_bound": 395
        },
        {
            "from": "109",
            "to": "42",
            "cost": 2568,
            "lower_bound": 0,
            "upper_bound": 104
        },
        {
            "from": "109",
            "to": "78",
            "cost": 4625,
            "lower_bound": 0,
            "upper_bound": 219
        },
        {
            "from": "109",
            "to": "84",
            "cost": 8699,
            "lower_bound": 0,
            "upper_bound": 553
        },
        {
            "from": "109",
            "to": "189",
            "cost": 7245,
            "lower_bound": 0,
            "upper_bound": 560
        },
        {
            "from": "109",
            "to": "168",
            "cost": 5112,
            "lower_bound": 0,
            "upper_bound": 548
        },
        {
            "from": "109",
            "to": "83",
            "cost": 477,
            "lower_bound": 0,
            "upper_bound": 285
        },
        {
            "from": "110",
            "to": "163",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1194
        },
        {
            "from": "110",
            "to": "77",
            "cost": 4958,
            "lower_bound": 0,
            "upper_bound": 407
        },
        {
            "from": "110",
            "to": "178",
            "cost": 6755,
            "lower_bound": 0,
            "upper_bound": 796
        },
        {
            "from": "110",
            "to": "172",
            "cost": 1597,
            "lower_bound": 0,
            "upper_bound": 376
        },
        {
            "from": "110",
            "to": "80",
            "cost": 1670,
            "lower_bound": 0,
            "upper_bound": 320
        },
        {
            "from": "110",
            "to": "108",
            "cost": 2204,
            "lower_bound": 0,
            "upper_bound": 765
        },
        {
            "from": "110",
            "to": "153",
            "cost": 7778,
            "lower_bound": 0,
            "upper_bound": 505
        },
        {
            "from": "110",
            "to": "149",
            "cost": 3573,
            "lower_bound": 0,
            "upper_bound": 967
        },
        {
            "from": "110",
            "to": "134",
            "cost": 4361,
            "lower_bound": 0,
            "upper_bound": 541
        },
        {
            "from": "114",
            "to": "226",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1194
        },
        {
            "from": "114",
            "to": "197",
            "cost": 4278,
            "lower_bound": 0,
            "upper_bound": 918
        },
        {
            "from": "114",
            "to": "202",
            "cost": 9717,
            "lower_bound": 0,
            "upper_bound": 713
        },
        {
            "from": "114",
            "to": "82",
            "cost": 6300,
            "lower_bound": 0,
            "upper_bound": 325
        },
        {
            "from": "114",
            "to": "110",
            "cost": 3717,
            "lower_bound": 0,
            "upper_bound": 663
        },
        {
            "from": "114",
            "to": "163",
            "cost": 9168,
            "lower_bound": 0,
            "upper_bound": 671
        },
        {
            "from": "114",
            "to": "65",
            "cost": 459,
            "lower_bound": 0,
            "upper_bound": 356
        },
        {
            "from": "114",
            "to": "233",
            "cost": 5597,
            "lower_bound": 0,
            "upper_bound": 802
        },
        {
            "from": "114",
            "to": "148",
            "cost": 1886,
            "lower_bound": 0,
            "upper_bound": 250
        },
        {
            "from": "114",
            "to": "66",
            "cost": 4269,
            "lower_bound": 0,
            "upper_bound": 326
        },
        {
            "from": "114",
            "to": "86",
            "cost": 9767,
            "lower_bound": 0,
            "upper_bound": 573
        },
        {
            "from": "114",
            "to": "100",
            "cost": 4494,
            "lower_bound": 0,
            "upper_bound": 363
        },
        {
            "from": "114",
            "to": "180",
            "cost": 7460,
            "lower_bound": 0,
            "upper_bound": 959
        },
        {
            "from": "114",
            "to": "235",
            "cost": 1839,
            "lower_bound": 0,
            "upper_bound": 680
        },
        {
            "from": "114",
            "to": "23",
            "cost": 3758,
            "lower_bound": 0,
            "upper_bound": 516
        },
        {
            "from": "117",
            "to": "168",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1194
        },
        {
            "from": "117",
            "to": "115",
            "cost": 685,
            "lower_bound": 0,
            "upper_bound": 817
        },
        {
            "from": "163",
            "to": "177",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1194
        },
        {
            "from": "163",
            "to": "161",
            "cost": 8605,
            "lower_bound": 0,
            "upper_bound": 647
        },
        {
            "from": "163",
            "to": "56",
            "cost": 1074,
            "lower_bound": 0,
            "upper_bound": 586
        },
        {
            "from": "168",
            "to": "185",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1194
        },
        {
            "from": "168",
            "to": "68",
            "cost": 7265,
            "lower_bound": 0,
            "upper_bound": 416
        },
        {
            "from": "168",
            "to": "187",
            "cost": 7233,
            "lower_bound": 0,
            "upper_bound": 471
        },
        {
            "from": "168",
            "to": "183",
            "cost": 9476,
            "lower_bound": 0,
            "upper_bound": 684
        },
        {
            "from": "168",
            "to": "209",
            "cost": 9873,
            "lower_bound": 0,
            "upper_bound": 402
        },
        {
            "from": "168",
            "to": "254",
            "cost": 1973,
            "lower_bound": 0,
            "upper_bound": 337
        },
        {
            "from": "168",
            "to": "179",
            "cost": 9551,
            "lower_bound": 0,
            "upper_bound": 292
        },
        {
            "from": "175",
            "to": "78",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1194
        },
        {
            "from": "175",
            "to": "100",
            "cost": 1808,
            "lower_bound": 0,
            "upper_bound": 930
        },
        {
            "from": "175",
            "to": "24",
            "cost": 6625,
            "lower_bound": 0,
            "upper_bound": 303
        },
        {
            "from": "175",
            "to": "113",
            "cost": 4263,
            "lower_bound": 0,
            "upper_bound": 763
        },
        {
            "from": "175",
            "to": "51",
            "cost": 8431,
            "lower_bound": 0,
            "upper_bound": 765
        },
        {
            "from": "175",
            "to": "33",
            "cost": 946,
            "lower_bound": 0,
            "upper_bound": 286
        },
        {
            "from": "175",
            "to": "193",
            "cost": 9371,
            "lower_bound": 0,
            "upper_bound": 702
        },
        {
            "from": "175",
            "to": "167",
            "cost": 3892,
            "lower_bound": 0,
            "upper_bound": 75
        },
        {
            "from": "175",
            "to": "228",
            "cost": 2152,
            "lower_bound": 0,
            "upper_bound": 762
        },
        {
            "from": "175",
            "to": "187",
            "cost": 6915,
            "lower_bound": 0,
            "upper_bound": 47
        },
        {
            "from": "175",
            "to": "22",
            "cost": 6328,
            "lower_bound": 0,
            "upper_bound": 577
        },
        {
            "from": "175",
            "to": "126",
            "cost": 8832,
            "lower_bound": 0,
            "upper_bound": 239
        },
        {
            "from": "175",
            "to": "180",
            "cost": 3885,
            "lower_bound": 0,
            "upper_bound": 810
        },
        {
            "from": "175",
            "to": "85",
            "cost": 4629,
            "lower_bound": 0,
            "upper_bound": 736
        },
        {
            "from": "177",
            "to": "19",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1194
        },
        {
            "from": "177",
            "to": "52",
            "cost": 5806,
            "lower_bound": 0,
            "upper_bound": 342
        },
        {
            "from": "177",
            "to": "222",
            "cost": 2993,
            "lower_bound": 0,
            "upper_bound": 394
        },
        {
            "from": "177",
            "to": "74",
            "cost": 5425,
            "lower_bound": 0,
            "upper_bound": 45
        },
        {
            "from": "177",
            "to": "189",
            "cost": 4556,
            "lower_bound": 0,
            "upper_bound": 464
        },
        {
            "from": "177",
            "to": "242",
            "cost": 5449,
            "lower_bound": 0,
            "upper_bound": 80
        },
        {
            "from": "177",
            "to": "196",
            "cost": 4929,
            "lower_bound": 0,
            "upper_bound": 226
        },
        {
            "from": "185",
            "to": "114",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1194
        },
        {
            "from": "185",
            "to": "109",
            "cost": 8835,
            "lower_bound": 0,
            "upper_bound": 13
        },
        {
            "from": "185",
            "to": "141",
            "cost": 1530,
            "lower_bound": 0,
            "upper_bound": 743
        },
        {
            "from": "185",
            "to": "217",
            "cost": 1112,
            "lower_bound": 0,
            "upper_bound": 288
        },
        {
            "from": "185",
            "to": "162",
            "cost": 9698,
            "lower_bound": 0,
            "upper_bound": 210
        },
        {
            "from": "185",
            "to": "69",
            "cost": 2210,
            "lower_bound": 0,
            "upper_bound": 329
        },
        {
            "from": "185",
            "to": "192",
            "cost": 5343,
            "lower_bound": 0,
            "upper_bound": 979
        },
        {
            "from": "185",
            "to": "68",
            "cost": 38,
            "lower_bound": 0,
            "upper_bound": 872
        },
        {
            "from": "185",
            "to": "111",
            "cost": 4418,
            "lower_bound": 0,
            "upper_bound": 959
        },
        {
            "from": "185",
            "to": "89",
            "cost": 9032,
            "lower_bound": 0,
            "upper_bound": 703
        },
        {
            "from": "185",
            "to": "251",
            "cost": 8167,
            "lower_bound": 0,
            "upper_bound": 453
        },
        {
            "from": "208",
            "to": "244",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1194
        },
        {
            "from": "208",
            "to": "238",
            "cost": 4052,
            "lower_bound": 0,
            "upper_bound": 240
        },
        {
            "from": "224",
            "to": "208",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1194
        },
        {
            "from": "224",
            "to": "220",
            "cost": 8517,
            "lower_bound": 0,
            "upper_bound": 237
        },
        {
            "from": "224",
            "to": "104",
            "cost": 9552,
            "lower_bound": 0,
            "upper_bound": 8
        },
        {
            "from": "224",
            "to": "174",
            "cost": 7061,
            "lower_bound": 0,
            "upper_bound": 684
        },
        {
            "from": "226",
            "to": "229",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1194
        },
        {
            "from": "226",
            "to": "209",
            "cost": 4098,
            "lower_bound": 0,
            "upper_bound": 51
        },
        {
            "from": "226",
            "to": "202",
            "cost": 5370,
            "lower_bound": 0,
            "upper_bound": 396
        },
        {
            "from": "226",
            "to": "171",
            "cost": 2089,
            "lower_bound": 0,
            "upper_bound": 43
        },
        {
            "from": "226",
            "to": "30",
            "cost": 7827,
            "lower_bound": 0,
            "upper_bound": 794
        },
        {
            "from": "226",
            "to": "231",
            "cost": 1820,
            "lower_bound": 0,
            "upper_bound": 112
        },
        {
            "from": "226",
            "to": "51",
            "cost": 1932,
            "lower_bound": 0,
            "upper_bound": 834
        },
        {
            "from": "226",
            "to": "244",
            "cost": 8330,
            "lower_bound": 0,
            "upper_bound": 477
        },
        {
            "from": "226",
            "to": "104",
            "cost": 4431,
            "lower_bound": 0,
            "upper_bound": 870
        },
        {
            "from": "226",
            "to": "239",
            "cost": 7937,
            "lower_bound": 0,
            "upper_bound": 830
        },
        {
            "from": "226",
            "to": "36",
            "cost": 5606,
            "lower_bound": 0,
            "upper_bound": 912
        },
        {
            "from": "228",
            "to": "65",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1194
        },
        {
            "from": "228",
            "to": "102",
            "cost": 6797,
            "lower_bound": 0,
            "upper_bound": 838
        },
        {
            "from": "228",
            "to": "190",
            "cost": 8999,
            "lower_bound": 0,
            "upper_bound": 273
        },
        {
            "from": "228",
            "to": "28",
            "cost": 2391,
            "lower_bound": 0,
            "upper_bound": 996
        },
        {
            "from": "228",
            "to": "139",
            "cost": 658,
            "lower_bound": 0,
            "upper_bound": 238
        },
        {
            "from": "228",
            "to": "144",
            "cost": 3326,
            "lower_bound": 0,
            "upper_bound": 255
        },
        {
            "from": "228",
            "to": "162",
            "cost": 5848,
            "lower_bound": 0,
            "upper_bound": 374
        },
        {
            "from": "228",
            "to": "69",
            "cost": 7620,
            "lower_bound": 0,
            "upper_bound": 10
        },
        {
            "from": "228",
            "to": "138",
            "cost": 9431,
            "lower_bound": 0,
            "upper_bound": 125
        },
        {
            "from": "228",
            "to": "230",
            "cost": 149,
            "lower_bound": 0,
            "upper_bound": 824
        },
        {
            "from": "228",
            "to": "18",
            "cost": 5550,
            "lower_bound": 0,
            "upper_bound": 408
        },
        {
            "from": "228",
            "to": "123",
            "cost": 2998,
            "lower_bound": 0,
            "upper_bound": 274
        },
        {
            "from": "229",
            "to": "89",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1194
        },
        {
            "from": "229",
            "to": "249",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1194
        },
        {
            "from": "229",
            "to": "156",
            "cost": 506,
            "lower_bound": 0,
            "upper_bound": 392
        },
        {
            "from": "229",
            "to": "18",
            "cost": 3174,
            "lower_bound": 0,
            "upper_bound": 592
        },
        {
            "from": "229",
            "to": "130",
            "cost": 6068,
            "lower_bound": 0,
            "upper_bound": 27
        },
        {
            "from": "229",
            "to": "153",
            "cost": 4240,
            "lower_bound": 0,
            "upper_bound": 295
        },
        {
            "from": "229",
            "to": "157",
            "cost": 5472,
            "lower_bound": 0,
            "upper_bound": 234
        },
        {
            "from": "229",
            "to": "103",
            "cost": 611,
            "lower_bound": 0,
            "upper_bound": 361
        },
        {
            "from": "229",
            "to": "235",
            "cost": 6360,
            "lower_bound": 0,
            "upper_bound": 994
        },
        {
            "from": "229",
            "to": "82",
            "cost": 6242,
            "lower_bound": 0,
            "upper_bound": 348
        },
        {
            "from": "229",
            "to": "244",
            "cost": 6428,
            "lower_bound": 0,
            "upper_bound": 5
        },
        {
            "from": "229",
            "to": "119",
            "cost": 6161,
            "lower_bound": 0,
            "upper_bound": 928
        },
        {
            "from": "229",
            "to": "109",
            "cost": 4870,
            "lower_bound": 0,
            "upper_bound": 195
        },
        {
            "from": "4",
            "to": "96",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 535
        },
        {
            "from": "4",
            "to": "177",
            "cost": 6467,
            "lower_bound": 0,
            "upper_bound": 875
        },
        {
            "from": "4",
            "to": "203",
            "cost": 1013,
            "lower_bound": 0,
            "upper_bound": 549
        },
        {
            "from": "4",
            "to": "45",
            "cost": 9555,
            "lower_bound": 0,
            "upper_bound": 26
        },
        {
            "from": "4",
            "to": "85",
            "cost": 3511,
            "lower_bound": 0,
            "upper_bound": 844
        },
        {
            "from": "4",
            "to": "243",
            "cost": 5286,
            "lower_bound": 0,
            "upper_bound": 815
        },
        {
            "from": "4",
            "to": "131",
            "cost": 7621,
            "lower_bound": 0,
            "upper_bound": 13
        },
        {
            "from": "4",
            "to": "136",
            "cost": 5603,
            "lower_bound": 0,
            "upper_bound": 322
        },
        {
            "from": "4",
            "to": "80",
            "cost": 6072,
            "lower_bound": 0,
            "upper_bound": 994
        },
        {
            "from": "4",
            "to": "135",
            "cost": 4462,
            "lower_bound": 0,
            "upper_bound": 145
        },
        {
            "from": "4",
            "to": "123",
            "cost": 9675,
            "lower_bound": 0,
            "upper_bound": 174
        },
        {
            "from": "4",
            "to": "231",
            "cost": 4240,
            "lower_bound": 0,
            "upper_bound": 583
        },
        {
            "from": "46",
            "to": "190",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 535
        },
        {
            "from": "46",
            "to": "87",
            "cost": 7865,
            "lower_bound": 0,
            "upper_bound": 100
        },
        {
            "from": "46",
            "to": "122",
            "cost": 3149,
            "lower_bound": 0,
            "upper_bound": 248
        },
        {
            "from": "46",
            "to": "195",
            "cost": 513,
            "lower_bound": 0,
            "upper_bound": 778
        },
        {
            "from": "46",
            "to": "227",
            "cost": 2817,
            "lower_bound": 0,
            "upper_bound": 223
        },
        {
            "from": "46",
            "to": "255",
            "cost": 8070,
            "lower_bound": 0,
            "upper_bound": 887
        },
        {
            "from": "46",
            "to": "71",
            "cost": 8327,
            "lower_bound": 0,
            "upper_bound": 442
        },
        {
            "from": "56",
            "to": "121",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 535
        },
        {
            "from": "56",
            "to": "232",
            "cost": 6761,
            "lower_bound": 0,
            "upper_bound": 514
        },
        {
            "from": "56",
            "to": "222",
            "cost": 2757,
            "lower_bound": 0,
            "upper_bound": 130
        },
        {
            "from": "56",
            "to": "147",
            "cost": 4428,
            "lower_bound": 0,
            "upper_bound": 499
        },
        {
            "from": "56",
            "to": "148",
            "cost": 790,
            "lower_bound": 0,
            "upper_bound": 462
        },
        {
            "from": "56",
            "to": "59",
            "cost": 1796,
            "lower_bound": 0,
            "upper_bound": 211
        },
        {
            "from": "56",
            "to": "140",
            "cost": 1498,
            "lower_bound": 0,
            "upper_bound": 577
        },
        {
            "from": "56",
            "to": "231",
            "cost": 8831,
            "lower_bound": 0,
            "upper_bound": 786
        },
        {
            "from": "56",
            "to": "81",
            "cost": 7268,
            "lower_bound": 0,
            "upper_bound": 242
        },
        {
            "from": "58",
            "to": "46",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 535
        },
        {
            "from": "58",
            "to": "244",
            "cost": 2053,
            "lower_bound": 0,
            "upper_bound": 262
        },
        {
            "from": "58",
            "to": "40",
            "cost": 7287,
            "lower_bound": 0,
            "upper_bound": 466
        },
        {
            "from": "58",
            "to": "64",
            "cost": 607,
            "lower_bound": 0,
            "upper_bound": 920
        },
        {
            "from": "58",
            "to": "104",
            "cost": 3337,
            "lower_bound": 0,
            "upper_bound": 723
        },
        {
            "from": "58",
            "to": "145",
            "cost": 5209,
            "lower_bound": 0,
            "upper_bound": 300
        },
        {
            "from": "58",
            "to": "219",
            "cost": 1156,
            "lower_bound": 0,
            "upper_bound": 749
        },
        {
            "from": "58",
            "to": "169",
            "cost": 2276,
            "lower_bound": 0,
            "upper_bound": 953
        },
        {
            "from": "58",
            "to": "80",
            "cost": 3325,
            "lower_bound": 0,
            "upper_bound": 771
        },
        {
            "from": "58",
            "to": "98",
            "cost": 5942,
            "lower_bound": 0,
            "upper_bound": 74
        },
        {
            "from": "58",
            "to": "163",
            "cost": 8471,
            "lower_bound": 0,
            "upper_bound": 290
        },
        {
            "from": "58",
            "to": "18",
            "cost": 8993,
            "lower_bound": 0,
            "upper_bound": 476
        },
        {
            "from": "58",
            "to": "235",
            "cost": 4376,
            "lower_bound": 0,
            "upper_bound": 561
        },
        {
            "from": "58",
            "to": "201",
            "cost": 7769,
            "lower_bound": 0,
            "upper_bound": 450
        },
        {
            "from": "73",
            "to": "153",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 535
        },
        {
            "from": "73",
            "to": "48",
            "cost": 3030,
            "lower_bound": 0,
            "upper_bound": 693
        },
        {
            "from": "73",
            "to": "123",
            "cost": 8449,
            "lower_bound": 0,
            "upper_bound": 218
        },
        {
            "from": "73",
            "to": "230",
            "cost": 4474,
            "lower_bound": 0,
            "upper_bound": 763
        },
        {
            "from": "73",
            "to": "249",
            "cost": 612,
            "lower_bound": 0,
            "upper_bound": 958
        },
        {
            "from": "73",
            "to": "216",
            "cost": 1958,
            "lower_bound": 0,
            "upper_bound": 836
        },
        {
            "from": "73",
            "to": "167",
            "cost": 2843,
            "lower_bound": 0,
            "upper_bound": 939
        },
        {
            "from": "73",
            "to": "125",
            "cost": 4081,
            "lower_bound": 0,
            "upper_bound": 38
        },
        {
            "from": "73",
            "to": "231",
            "cost": 3133,
            "lower_bound": 0,
            "upper_bound": 970
        },
        {
            "from": "73",
            "to": "154",
            "cost": 3873,
            "lower_bound": 0,
            "upper_bound": 708
        },
        {
            "from": "73",
            "to": "112",
            "cost": 641,
            "lower_bound": 0,
            "upper_bound": 463
        },
        {
            "from": "73",
            "to": "195",
            "cost": 4775,
            "lower_bound": 0,
            "upper_bound": 426
        },
        {
            "from": "73",
            "to": "241",
            "cost": 2397,
            "lower_bound": 0,
            "upper_bound": 650
        },
        {
            "from": "73",
            "to": "34",
            "cost": 4061,
            "lower_bound": 0,
            "upper_bound": 572
        },
        {
            "from": "73",
            "to": "190",
            "cost": 5010,
            "lower_bound": 0,
            "upper_bound": 125
        },
        {
            "from": "74",
            "to": "215",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 535
        },
        {
            "from": "74",
            "to": "134",
            "cost": 6810,
            "lower_bound": 0,
            "upper_bound": 952
        },
        {
            "from": "74",
            "to": "51",
            "cost": 5812,
            "lower_bound": 0,
            "upper_bound": 838
        },
        {
            "from": "74",
            "to": "110",
            "cost": 5274,
            "lower_bound": 0,
            "upper_bound": 153
        },
        {
            "from": "74",
            "to": "197",
            "cost": 6925,
            "lower_bound": 0,
            "upper_bound": 23
        },
        {
            "from": "74",
            "to": "103",
            "cost": 4414,
            "lower_bound": 0,
            "upper_bound": 517
        },
        {
            "from": "74",
            "to": "168",
            "cost": 2177,
            "lower_bound": 0,
            "upper_bound": 672
        },
        {
            "from": "74",
            "to": "107",
            "cost": 6833,
            "lower_bound": 0,
            "upper_bound": 247
        },
        {
            "from": "74",
            "to": "68",
            "cost": 1010,
            "lower_bound": 0,
            "upper_bound": 988
        },
        {
            "from": "96",
            "to": "201",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 535
        },
        {
            "from": "96",
            "to": "242",
            "cost": 7159,
            "lower_bound": 0,
            "upper_bound": 511
        },
        {
            "from": "96",
            "to": "136",
            "cost": 638,
            "lower_bound": 0,
            "upper_bound": 373
        },
        {
            "from": "96",
            "to": "28",
            "cost": 2915,
            "lower_bound": 0,
            "upper_bound": 78
        },
        {
            "from": "96",
            "to": "135",
            "cost": 9162,
            "lower_bound": 0,
            "upper_bound": 237
        },
        {
            "from": "96",
            "to": "107",
            "cost": 7059,
            "lower_bound": 0,
            "upper_bound": 647
        },
        {
            "from": "96",
            "to": "103",
            "cost": 5703,
            "lower_bound": 0,
            "upper_bound": 542
        },
        {
            "from": "96",
            "to": "105",
            "cost": 4795,
            "lower_bound": 0,
            "upper_bound": 300
        },
        {
            "from": "96",
            "to": "221",
            "cost": 1924,
            "lower_bound": 0,
            "upper_bound": 292
        },
        {
            "from": "96",
            "to": "168",
            "cost": 47,
            "lower_bound": 0,
            "upper_bound": 202
        },
        {
            "from": "96",
            "to": "223",
            "cost": 2727,
            "lower_bound": 0,
            "upper_bound": 879
        },
        {
            "from": "96",
            "to": "128",
            "cost": 5133,
            "lower_bound": 0,
            "upper_bound": 25
        },
        {
            "from": "96",
            "to": "92",
            "cost": 5062,
            "lower_bound": 0,
            "upper_bound": 94
        },
        {
            "from": "121",
            "to": "192",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 535
        },
        {
            "from": "121",
            "to": "217",
            "cost": 5687,
            "lower_bound": 0,
            "upper_bound": 699
        },
        {
            "from": "121",
            "to": "86",
            "cost": 8900,
            "lower_bound": 0,
            "upper_bound": 536
        },
        {
            "from": "121",
            "to": "202",
            "cost": 9160,
            "lower_bound": 0,
            "upper_bound": 51
        },
        {
            "from": "121",
            "to": "205",
            "cost": 3558,
            "lower_bound": 0,
            "upper_bound": 820
        },
        {
            "from": "121",
            "to": "113",
            "cost": 2697,
            "lower_bound": 0,
            "upper_bound": 127
        },
        {
            "from": "121",
            "to": "152",
            "cost": 5418,
            "lower_bound": 0,
            "upper_bound": 171
        },
        {
            "from": "121",
            "to": "129",
            "cost": 3507,
            "lower_bound": 0,
            "upper_bound": 398
        },
        {
            "from": "153",
            "to": "238",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 535
        },
        {
            "from": "153",
            "to": "162",
            "cost": 6782,
            "lower_bound": 0,
            "upper_bound": 74
        },
        {
            "from": "153",
            "to": "29",
            "cost": 6228,
            "lower_bound": 0,
            "upper_bound": 212
        },
        {
            "from": "153",
            "to": "138",
            "cost": 6188,
            "lower_bound": 0,
            "upper_bound": 334
        },
        {
            "from": "153",
            "to": "154",
            "cost": 7356,
            "lower_bound": 0,
            "upper_bound": 361
        },
        {
            "from": "153",
            "to": "220",
            "cost": 6518,
            "lower_bound": 0,
            "upper_bound": 269
        },
        {
            "from": "153",
            "to": "50",
            "cost": 4133,
            "lower_bound": 0,
            "upper_bound": 252
        },
        {
            "from": "153",
            "to": "140",
            "cost": 5110,
            "lower_bound": 0,
            "upper_bound": 179
        },
        {
            "from": "153",
            "to": "203",
            "cost": 2138,
            "lower_bound": 0,
            "upper_bound": 383
        },
        {
            "from": "164",
            "to": "73",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 535
        },
        {
            "from": "164",
            "to": "237",
            "cost": 9384,
            "lower_bound": 0,
            "upper_bound": 992
        },
        {
            "from": "164",
            "to": "158",
            "cost": 6533,
            "lower_bound": 0,
            "upper_bound": 690
        },
        {
            "from": "164",
            "to": "222",
            "cost": 3401,
            "lower_bound": 0,
            "upper_bound": 621
        },
        {
            "from": "164",
            "to": "60",
            "cost": 7121,
            "lower_bound": 0,
            "upper_bound": 512
        },
        {
            "from": "164",
            "to": "157",
            "cost": 787,
            "lower_bound": 0,
            "upper_bound": 943
        },
        {
            "from": "164",
            "to": "30",
            "cost": 3125,
            "lower_bound": 0,
            "upper_bound": 813
        },
        {
            "from": "164",
            "to": "219",
            "cost": 5894,
            "lower_bound": 0,
            "upper_bound": 40
        },
        {
            "from": "164",
            "to": "248",
            "cost": 7959,
            "lower_bound": 0,
            "upper_bound": 12
        },
        {
            "from": "164",
            "to": "33",
            "cost": 5795,
            "lower_bound": 0,
            "upper_bound": 59
        },
        {
            "from": "164",
            "to": "226",
            "cost": 5351,
            "lower_bound": 0,
            "upper_bound": 49
        },
        {
            "from": "164",
            "to": "159",
            "cost": 6630,
            "lower_bound": 0,
            "upper_bound": 58
        },
        {
            "from": "180",
            "to": "164",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 535
        },
        {
            "from": "180",
            "to": "197",
            "cost": 4933,
            "lower_bound": 0,
            "upper_bound": 309
        },
        {
            "from": "190",
            "to": "254",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 535
        },
        {
            "from": "190",
            "to": "242",
            "cost": 8621,
            "lower_bound": 0,
            "upper_bound": 501
        },
        {
            "from": "190",
            "to": "39",
            "cost": 8413,
            "lower_bound": 0,
            "upper_bound": 753
        },
        {
            "from": "190",
            "to": "251",
            "cost": 9436,
            "lower_bound": 0,
            "upper_bound": 727
        },
        {
            "from": "190",
            "to": "44",
            "cost": 6816,
            "lower_bound": 0,
            "upper_bound": 330
        },
        {
            "from": "190",
            "to": "67",
            "cost": 9075,
            "lower_bound": 0,
            "upper_bound": 992
        },
        {
            "from": "190",
            "to": "120",
            "cost": 1868,
            "lower_bound": 0,
            "upper_bound": 676
        },
        {
            "from": "190",
            "to": "27",
            "cost": 1606,
            "lower_bound": 0,
            "upper_bound": 61
        },
        {
            "from": "192",
            "to": "180",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 535
        },
        {
            "from": "192",
            "to": "186",
            "cost": 2793,
            "lower_bound": 0,
            "upper_bound": 610
        },
        {
            "from": "192",
            "to": "153",
            "cost": 1797,
            "lower_bound": 0,
            "upper_bound": 902
        },
        {
            "from": "192",
            "to": "160",
            "cost": 4272,
            "lower_bound": 0,
            "upper_bound": 602
        },
        {
            "from": "192",
            "to": "205",
            "cost": 7829,
            "lower_bound": 0,
            "upper_bound": 383
        },
        {
            "from": "192",
            "to": "23",
            "cost": 3425,
            "lower_bound": 0,
            "upper_bound": 782
        },
        {
            "from": "192",
            "to": "188",
            "cost": 8610,
            "lower_bound": 0,
            "upper_bound": 603
        },
        {
            "from": "192",
            "to": "227",
            "cost": 6570,
            "lower_bound": 0,
            "upper_bound": 974
        },
        {
            "from": "192",
            "to": "155",
            "cost": 4893,
            "lower_bound": 0,
            "upper_bound": 809
        },
        {
            "from": "192",
            "to": "244",
            "cost": 8120,
            "lower_bound": 0,
            "upper_bound": 941
        },
        {
            "from": "192",
            "to": "138",
            "cost": 9788,
            "lower_bound": 0,
            "upper_bound": 128
        },
        {
            "from": "192",
            "to": "182",
            "cost": 9010,
            "lower_bound": 0,
            "upper_bound": 772
        },
        {
            "from": "201",
            "to": "56",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 535
        },
        {
            "from": "201",
            "to": "242",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 535
        },
        {
            "from": "201",
            "to": "154",
            "cost": 3388,
            "lower_bound": 0,
            "upper_bound": 146
        },
        {
            "from": "201",
            "to": "185",
            "cost": 6452,
            "lower_bound": 0,
            "upper_bound": 257
        },
        {
            "from": "201",
            "to": "170",
            "cost": 7216,
            "lower_bound": 0,
            "upper_bound": 319
        },
        {
            "from": "215",
            "to": "58",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 535
        },
        {
            "from": "215",
            "to": "120",
            "cost": 7646,
            "lower_bound": 0,
            "upper_bound": 553
        },
        {
            "from": "238",
            "to": "74",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 535
        },
        {
            "from": "238",
            "to": "78",
            "cost": 1418,
            "lower_bound": 0,
            "upper_bound": 618
        },
        {
            "from": "238",
            "to": "53",
            "cost": 2303,
            "lower_bound": 0,
            "upper_bound": 59
        },
        {
            "from": "238",
            "to": "188",
            "cost": 5084,
            "lower_bound": 0,
            "upper_bound": 735
        },
        {
            "from": "5",
            "to": "106",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1094
        },
        {
            "from": "5",
            "to": "97",
            "cost": 5,
            "lower_bound": 0,
            "upper_bound": 403
        },
        {
            "from": "5",
            "to": "120",
            "cost": 5863,
            "lower_bound": 0,
            "upper_bound": 129
        },
        {
            "from": "5",
            "to": "195",
            "cost": 7197,
            "lower_bound": 0,
            "upper_bound": 600
        },
        {
            "from": "5",
            "to": "95",
            "cost": 4449,
            "lower_bound": 0,
            "upper_bound": 691
        },
        {
            "from": "5",
            "to": "82",
            "cost": 1880,
            "lower_bound": 0,
            "upper_bound": 787
        },
        {
            "from": "18",
            "to": "44",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1094
        },
        {
            "from": "18",
            "to": "253",
            "cost": 1900,
            "lower_bound": 0,
            "upper_bound": 471
        },
        {
            "from": "18",
            "to": "31",
            "cost": 233,
            "lower_bound": 0,
            "upper_bound": 884
        },
        {
            "from": "18",
            "to": "99",
            "cost": 2271,
            "lower_bound": 0,
            "upper_bound": 296
        },
        {
            "from": "18",
            "to": "61",
            "cost": 1599,
            "lower_bound": 0,
            "upper_bound": 625
        },
        {
            "from": "18",
            "to": "192",
            "cost": 7950,
            "lower_bound": 0,
            "upper_bound": 386
        },
        {
            "from": "18",
            "to": "87",
            "cost": 6293,
            "lower_bound": 0,
            "upper_bound": 913
        },
        {
            "from": "23",
            "to": "70",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1094
        },
        {
            "from": "23",
            "to": "250",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1094
        },
        {
            "from": "23",
            "to": "71",
            "cost": 5822,
            "lower_bound": 0,
            "upper_bound": 972
        },
        {
            "from": "23",
            "to": "153",
            "cost": 9512,
            "lower_bound": 0,
            "upper_bound": 22
        },
        {
            "from": "23",
            "to": "194",
            "cost": 1427,
            "lower_bound": 0,
            "upper_bound": 780
        },
        {
            "from": "23",
            "to": "83",
            "cost": 9184,
            "lower_bound": 0,
            "upper_bound": 861
        },
        {
            "from": "23",
            "to": "183",
            "cost": 9979,
            "lower_bound": 0,
            "upper_bound": 322
        },
        {
            "from": "23",
            "to": "139",
            "cost": 1390,
            "lower_bound": 0,
            "upper_bound": 163
        },
        {
            "from": "23",
            "to": "135",
            "cost": 8688,
            "lower_bound": 0,
            "upper_bound": 230
        },
        {
            "from": "23",
            "to": "50",
            "cost": 3684,
            "lower_bound": 0,
            "upper_bound": 278
        },
        {
            "from": "23",
            "to": "60",
            "cost": 8900,
            "lower_bound": 0,
            "upper_bound": 787
        },
        {
            "from": "23",
            "to": "76",
            "cost": 4285,
            "lower_bound": 0,
            "upper_bound": 48
        },
        {
            "from": "23",
            "to": "101",
            "cost": 7843,
            "lower_bound": 0,
            "upper_bound": 72
        },
        {
            "from": "23",
            "to": "68",
            "cost": 5860,
            "lower_bound": 0,
            "upper_bound": 319
        },
        {
            "from": "23",
            "to": "46",
            "cost": 498,
            "lower_bound": 0,
            "upper_bound": 524
        },
        {
            "from": "44",
            "to": "98",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1094
        },
        {
            "from": "44",
            "to": "255",
            "cost": 2483,
            "lower_bound": 0,
            "upper_bound": 446
        },
        {
            "from": "44",
            "to": "228",
            "cost": 9600,
            "lower_bound": 0,
            "upper_bound": 797
        },
        {
            "from": "57",
            "to": "202",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1094
        },
        {
            "from": "57",
            "to": "80",
            "cost": 8307,
            "lower_bound": 0,
            "upper_bound": 822
        },
        {
            "from": "57",
            "to": "82",
            "cost": 5213,
            "lower_bound": 0,
            "upper_bound": 718
        },
        {
            "from": "57",
            "to": "79",
            "cost": 482,
            "lower_bound": 0,
            "upper_bound": 127
        },
        {
            "from": "57",
            "to": "184",
            "cost": 5573,
            "lower_bound": 0,
            "upper_bound": 309
        },
        {
            "from": "57",
            "to": "234",
            "cost": 7824,
            "lower_bound": 0,
            "upper_bound": 619
        },
        {
            "from": "70",
            "to": "133",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1094
        },
        {
            "from": "70",
            "to": "75",
            "cost": 7396,
            "lower_bound": 0,
            "upper_bound": 644
        },
        {
            "from": "98",
            "to": "213",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1094
        },
        {
            "from": "98",
            "to": "236",
            "cost": 1245,
            "lower_bound": 0,
            "upper_bound": 164
        },
        {
            "from": "98",
            "to": "63",
            "cost": 5039,
            "lower_bound": 0,
            "upper_bound": 338
        },
        {
            "from": "98",
            "to": "170",
            "cost": 5085,
            "lower_bound": 0,
            "upper_bound": 899
        },
        {
            "from": "98",
            "to": "78",
            "cost": 9236,
            "lower_bound": 0,
            "upper_bound": 246
        },
        {
            "from": "98",
            "to": "42",
            "cost": 5867,
            "lower_bound": 0,
            "upper_bound": 981
        },
        {
            "from": "98",
            "to": "229",
            "cost": 2879,
            "lower_bound": 0,
            "upper_bound": 405
        },
        {
            "from": "98",
            "to": "39",
            "cost": 5414,
            "lower_bound": 0,
            "upper_bound": 851
        },
        {
            "from": "98",
            "to": "220",
            "cost": 2046,
            "lower_bound": 0,
            "upper_bound": 516
        },
        {
            "from": "98",
            "to": "124",
            "cost": 4844,
            "lower_bound": 0,
            "upper_bound": 208
        },
        {
            "from": "98",
            "to": "151",
            "cost": 4460,
            "lower_bound": 0,
            "upper_bound": 453
        },
        {
            "from": "106",
            "to": "23",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1094
        },
        {
            "from": "106",
            "to": "194",
            "cost": 7239,
            "lower_bound": 0,
            "upper_bound": 546
        },
        {
            "from": "106",
            "to": "24",
            "cost": 3978,
            "lower_bound": 0,
            "upper_bound": 223
        },
        {
            "from": "106",
            "to": "54",
            "cost": 3328,
            "lower_bound": 0,
            "upper_bound": 864
        },
        {
            "from": "106",
            "to": "78",
            "cost": 6007,
            "lower_bound": 0,
            "upper_bound": 657
        },
        {
            "from": "106",
            "to": "192",
            "cost": 7484,
            "lower_bound": 0,
            "upper_bound": 291
        },
        {
            "from": "106",
            "to": "191",
            "cost": 4108,
            "lower_bound": 0,
            "upper_bound": 265
        },
        {
            "from": "106",
            "to": "223",
            "cost": 2075,
            "lower_bound": 0,
            "upper_bound": 90
        },
        {
            "from": "106",
            "to": "159",
            "cost": 8651,
            "lower_bound": 0,
            "upper_bound": 988
        },
        {
            "from": "106",
            "to": "108",
            "cost": 9496,
            "lower_bound": 0,
            "upper_bound": 148
        },
        {
            "from": "111",
            "to": "209",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1094
        },
        {
            "from": "111",
            "to": "177",
            "cost": 1914,
            "lower_bound": 0,
            "upper_bound": 907
        },
        {
            "from": "111",
            "to": "39",
            "cost": 8107,
            "lower_bound": 0,
            "upper_bound": 363
        },
        {
            "from": "111",
            "to": "208",
            "cost": 2324,
            "lower_bound": 0,
            "upper_bound": 58
        },
        {
            "from": "111",
            "to": "67",
            "cost": 3050,
            "lower_bound": 0,
            "upper_bound": 24
        },
        {
            "from": "111",
            "to": "19",
            "cost": 4740,
            "lower_bound": 0,
            "upper_bound": 952
        },
        {
            "from": "122",
            "to": "57",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1094
        },
        {
            "from": "122",
            "to": "192",
            "cost": 6709,
            "lower_bound": 0,
            "upper_bound": 635
        },
        {
            "from": "122",
            "to": "202",
            "cost": 2315,
            "lower_bound": 0,
            "upper_bound": 283
        },
        {
            "from": "122",
            "to": "103",
            "cost": 1960,
            "lower_bound": 0,
            "upper_bound": 919
        },
        {
            "from": "122",
            "to": "19",
            "cost": 5147,
            "lower_bound": 0,
            "upper_bound": 157
        },
        {
            "from": "122",
            "to": "115",
            "cost": 9056,
            "lower_bound": 0,
            "upper_bound": 321
        },
        {
            "from": "122",
            "to": "166",
            "cost": 7702,
            "lower_bound": 0,
            "upper_bound": 830
        },
        {
            "from": "122",
            "to": "60",
            "cost": 2678,
            "lower_bound": 0,
            "upper_bound": 633
        },
        {
            "from": "122",
            "to": "93",
            "cost": 7814,
            "lower_bound": 0,
            "upper_bound": 58
        },
        {
            "from": "122",
            "to": "221",
            "cost": 6362,
            "lower_bound": 0,
            "upper_bound": 204
        },
        {
            "from": "122",
            "to": "225",
            "cost": 3486,
            "lower_bound": 0,
            "upper_bound": 459
        },
        {
            "from": "122",
            "to": "255",
            "cost": 9981,
            "lower_bound": 0,
            "upper_bound": 942
        },
        {
            "from": "122",
            "to": "114",
            "cost": 4340,
            "lower_bound": 0,
            "upper_bound": 458
        },
        {
            "from": "122",
            "to": "70",
            "cost": 7264,
            "lower_bound": 0,
            "upper_bound": 298
        },
        {
            "from": "133",
            "to": "122",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1094
        },
        {
            "from": "133",
            "to": "58",
            "cost": 2681,
            "lower_bound": 0,
            "upper_bound": 105
        },
        {
            "from": "133",
            "to": "182",
            "cost": 7367,
            "lower_bound": 0,
            "upper_bound": 45
        },
        {
            "from": "133",
            "to": "191",
            "cost": 4700,
            "lower_bound": 0,
            "upper_bound": 1000
        },
        {
            "from": "133",
            "to": "156",
            "cost": 7864,
            "lower_bound": 0,
            "upper_bound": 214
        },
        {
            "from": "176",
            "to": "244",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1094
        },
        {
            "from": "176",
            "to": "199",
            "cost": 9075,
            "lower_bound": 0,
            "upper_bound": 289
        },
        {
            "from": "176",
            "to": "91",
            "cost": 8732,
            "lower_bound": 0,
            "upper_bound": 705
        },
        {
            "from": "176",
            "to": "138",
            "cost": 1698,
            "lower_bound": 0,
            "upper_bound": 600
        },
        {
            "from": "176",
            "to": "132",
            "cost": 2312,
            "lower_bound": 0,
            "upper_bound": 373
        },
        {
            "from": "202",
            "to": "18",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1094
        },
        {
            "from": "202",
            "to": "233",
            "cost": 6812,
            "lower_bound": 0,
            "upper_bound": 686
        },
        {
            "from": "202",
            "to": "46",
            "cost": 3207,
            "lower_bound": 0,
            "upper_bound": 516
        },
        {
            "from": "202",
            "to": "185",
            "cost": 170,
            "lower_bound": 0,
            "upper_bound": 760
        },
        {
            "from": "202",
            "to": "157",
            "cost": 5742,
            "lower_bound": 0,
            "upper_bound": 129
        },
        {
            "from": "202",
            "to": "186",
            "cost": 1875,
            "lower_bound": 0,
            "upper_bound": 387
        },
        {
            "from": "202",
            "to": "64",
            "cost": 5707,
            "lower_bound": 0,
            "upper_bound": 360
        },
        {
            "from": "202",
            "to": "165",
            "cost": 2146,
            "lower_bound": 0,
            "upper_bound": 547
        },
        {
            "from": "202",
            "to": "210",
            "cost": 8629,
            "lower_bound": 0,
            "upper_bound": 101
        },
        {
            "from": "202",
            "to": "96",
            "cost": 6697,
            "lower_bound": 0,
            "upper_bound": 113
        },
        {
            "from": "202",
            "to": "27",
            "cost": 2966,
            "lower_bound": 0,
            "upper_bound": 439
        },
        {
            "from": "202",
            "to": "196",
            "cost": 764,
            "lower_bound": 0,
            "upper_bound": 373
        },
        {
            "from": "202",
            "to": "133",
            "cost": 7830,
            "lower_bound": 0,
            "upper_bound": 714
        },
        {
            "from": "209",
            "to": "176",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1094
        },
        {
            "from": "209",
            "to": "129",
            "cost": 4973,
            "lower_bound": 0,
            "upper_bound": 979
        },
        {
            "from": "209",
            "to": "218",
            "cost": 3301,
            "lower_bound": 0,
            "upper_bound": 195
        },
        {
            "from": "209",
            "to": "250",
            "cost": 9896,
            "lower_bound": 0,
            "upper_bound": 470
        },
        {
            "from": "209",
            "to": "101",
            "cost": 6873,
            "lower_bound": 0,
            "upper_bound": 376
        },
        {
            "from": "209",
            "to": "48",
            "cost": 6189,
            "lower_bound": 0,
            "upper_bound": 150
        },
        {
            "from": "213",
            "to": "111",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1094
        },
        {
            "from": "213",
            "to": "73",
            "cost": 5005,
            "lower_bound": 0,
            "upper_bound": 269
        },
        {
            "from": "213",
            "to": "36",
            "cost": 2119,
            "lower_bound": 0,
            "upper_bound": 704
        },
        {
            "from": "213",
            "to": "79",
            "cost": 7903,
            "lower_bound": 0,
            "upper_bound": 467
        },
        {
            "from": "213",
            "to": "226",
            "cost": 4529,
            "lower_bound": 0,
            "upper_bound": 479
        },
        {
            "from": "213",
            "to": "187",
            "cost": 8313,
            "lower_bound": 0,
            "upper_bound": 93
        },
        {
            "from": "213",
            "to": "201",
            "cost": 8612,
            "lower_bound": 0,
            "upper_bound": 597
        },
        {
            "from": "213",
            "to": "109",
            "cost": 9365,
            "lower_bound": 0,
            "upper_bound": 61
        },
        {
            "from": "213",
            "to": "82",
            "cost": 9432,
            "lower_bound": 0,
            "upper_bound": 245
        },
        {
            "from": "6",
            "to": "221",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 414
        },
        {
            "from": "6",
            "to": "109",
            "cost": 150,
            "lower_bound": 0,
            "upper_bound": 233
        },
        {
            "from": "6",
            "to": "202",
            "cost": 1846,
            "lower_bound": 0,
            "upper_bound": 615
        },
        {
            "from": "6",
            "to": "219",
            "cost": 1133,
            "lower_bound": 0,
            "upper_bound": 784
        },
        {
            "from": "6",
            "to": "74",
            "cost": 941,
            "lower_bound": 0,
            "upper_bound": 136
        },
        {
            "from": "6",
            "to": "41",
            "cost": 8733,
            "lower_bound": 0,
            "upper_bound": 878
        },
        {
            "from": "6",
            "to": "150",
            "cost": 4958,
            "lower_bound": 0,
            "upper_bound": 267
        },
        {
            "from": "6",
            "to": "29",
            "cost": 2877,
            "lower_bound": 0,
            "upper_bound": 705
        },
        {
            "from": "6",
            "to": "252",
            "cost": 3186,
            "lower_bound": 0,
            "upper_bound": 896
        },
        {
            "from": "30",
            "to": "236",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 414
        },
        {
            "from": "30",
            "to": "174",
            "cost": 3298,
            "lower_bound": 0,
            "upper_bound": 824
        },
        {
            "from": "30",
            "to": "81",
            "cost": 4038,
            "lower_bound": 0,
            "upper_bound": 125
        },
        {
            "from": "30",
            "to": "215",
            "cost": 8154,
            "lower_bound": 0,
            "upper_bound": 982
        },
        {
            "from": "30",
            "to": "35",
            "cost": 5207,
            "lower_bound": 0,
            "upper_bound": 809
        },
        {
            "from": "38",
            "to": "253",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 414
        },
        {
            "from": "38",
            "to": "135",
            "cost": 3149,
            "lower_bound": 0,
            "upper_bound": 444
        },
        {
            "from": "38",
            "to": "227",
            "cost": 2524,
            "lower_bound": 0,
            "upper_bound": 962
        },
        {
            "from": "38",
            "to": "193",
            "cost": 3715,
            "lower_bound": 0,
            "upper_bound": 198
        },
        {
            "from": "38",
            "to": "249",
            "cost": 1111,
            "lower_bound": 0,
            "upper_bound": 958
        },
        {
            "from": "38",
            "to": "223",
            "cost": 3420,
            "lower_bound": 0,
            "upper_bound": 93
        },
        {
            "from": "38",
            "to": "166",
            "cost": 7430,
            "lower_bound": 0,
            "upper_bound": 695
        },
        {
            "from": "38",
            "to": "246",
            "cost": 5999,
            "lower_bound": 0,
            "upper_bound": 681
        },
        {
            "from": "38",
            "to": "70",
            "cost": 9255,
            "lower_bound": 0,
            "upper_bound": 784
        },
        {
            "from": "38",
            "to": "205",
            "cost": 6396,
            "lower_bound": 0,
            "upper_bound": 575
        },
        {
            "from": "38",
            "to": "175",
            "cost": 9711,
            "lower_bound": 0,
            "upper_bound": 471
        },
        {
            "from": "38",
            "to": "221",
            "cost": 9849,
            "lower_bound": 0,
            "upper_bound": 633
        },
        {
            "from": "40",
            "to": "252",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 414
        },
        {
            "from": "40",
            "to": "49",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 414
        },
        {
            "from": "40",
            "to": "140",
            "cost": 7922,
            "lower_bound": 0,
            "upper_bound": 678
        },
        {
            "from": "40",
            "to": "82",
            "cost": 6892,
            "lower_bound": 0,
            "upper_bound": 297
        },
        {
            "from": "40",
            "to": "174",
            "cost": 9327,
            "lower_bound": 0,
            "upper_bound": 745
        },
        {
            "from": "40",
            "to": "47",
            "cost": 7334,
            "lower_bound": 0,
            "upper_bound": 754
        },
        {
            "from": "40",
            "to": "152",
            "cost": 4638,
            "lower_bound": 0,
            "upper_bound": 448
        },
        {
            "from": "40",
            "to": "42",
            "cost": 3722,
            "lower_bound": 0,
            "upper_bound": 77
        },
        {
            "from": "40",
            "to": "141",
            "cost": 5983,
            "lower_bound": 0,
            "upper_bound": 522
        },
        {
            "from": "40",
            "to": "207",
            "cost": 2272,
            "lower_bound": 0,
            "upper_bound": 622
        },
        {
            "from": "40",
            "to": "179",
            "cost": 9659,
            "lower_bound": 0,
            "upper_bound": 289
        },
        {
            "from": "40",
            "to": "139",
            "cost": 7947,
            "lower_bound": 0,
            "upper_bound": 294
        },
        {
            "from": "40",
            "to": "25",
            "cost": 7555,
            "lower_bound": 0,
            "upper_bound": 278
        },
        {
            "from": "40",
            "to": "147",
            "cost": 2628,
            "lower_bound": 0,
            "upper_bound": 610
        },
        {
            "from": "40",
            "to": "202",
            "cost": 7665,
            "lower_bound": 0,
            "upper_bound": 118
        },
        {
            "from": "49",
            "to": "38",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 414
        },
        {
            "from": "49",
            "to": "233",
            "cost": 3067,
            "lower_bound": 0,
            "upper_bound": 836
        },
        {
            "from": "49",
            "to": "94",
            "cost": 1004,
            "lower_bound": 0,
            "upper_bound": 410
        },
        {
            "from": "49",
            "to": "102",
            "cost": 1371,
            "lower_bound": 0,
            "upper_bound": 776
        },
        {
            "from": "49",
            "to": "99",
            "cost": 9840,
            "lower_bound": 0,
            "upper_bound": 156
        },
        {
            "from": "49",
            "to": "197",
            "cost": 372,
            "lower_bound": 0,
            "upper_bound": 16
        },
        {
            "from": "49",
            "to": "202",
            "cost": 5719,
            "lower_bound": 0,
            "upper_bound": 82
        },
        {
            "from": "49",
            "to": "196",
            "cost": 9851,
            "lower_bound": 0,
            "upper_bound": 9
        },
        {
            "from": "49",
            "to": "204",
            "cost": 6880,
            "lower_bound": 0,
            "upper_bound": 837
        },
        {
            "from": "49",
            "to": "174",
            "cost": 2601,
            "lower_bound": 0,
            "upper_bound": 673
        },
        {
            "from": "49",
            "to": "83",
            "cost": 9168,
            "lower_bound": 0,
            "upper_bound": 620
        },
        {
            "from": "53",
            "to": "171",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 414
        },
        {
            "from": "53",
            "to": "93",
            "cost": 1331,
            "lower_bound": 0,
            "upper_bound": 357
        },
        {
            "from": "53",
            "to": "98",
            "cost": 4180,
            "lower_bound": 0,
            "upper_bound": 627
        },
        {
            "from": "53",
            "to": "39",
            "cost": 3556,
            "lower_bound": 0,
            "upper_bound": 192
        },
        {
            "from": "53",
            "to": "99",
            "cost": 5776,
            "lower_bound": 0,
            "upper_bound": 760
        },
        {
            "from": "53",
            "to": "55",
            "cost": 3494,
            "lower_bound": 0,
            "upper_bound": 429
        },
        {
            "from": "53",
            "to": "168",
            "cost": 5587,
            "lower_bound": 0,
            "upper_bound": 715
        },
        {
            "from": "53",
            "to": "76",
            "cost": 5611,
            "lower_bound": 0,
            "upper_bound": 749
        },
        {
            "from": "53",
            "to": "117",
            "cost": 4097,
            "lower_bound": 0,
            "upper_bound": 554
        },
        {
            "from": "124",
            "to": "134",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 414
        },
        {
            "from": "124",
            "to": "203",
            "cost": 7260,
            "lower_bound": 0,
            "upper_bound": 883
        },
        {
            "from": "124",
            "to": "232",
            "cost": 3365,
            "lower_bound": 0,
            "upper_bound": 185
        },
        {
            "from": "124",
            "to": "227",
            "cost": 8956,
            "lower_bound": 0,
            "upper_bound": 989
        },
        {
            "from": "134",
            "to": "235",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 414
        },
        {
            "from": "134",
            "to": "74",
            "cost": 6624,
            "lower_bound": 0,
            "upper_bound": 306
        },
        {
            "from": "134",
            "to": "237",
            "cost": 3244,
            "lower_bound": 0,
            "upper_bound": 148
        },
        {
            "from": "134",
            "to": "78",
            "cost": 7237,
            "lower_bound": 0,
            "upper_bound": 646
        },
        {
            "from": "134",
            "to": "230",
            "cost": 5175,
            "lower_bound": 0,
            "upper_bound": 460
        },
        {
            "from": "134",
            "to": "79",
            "cost": 4041,
            "lower_bound": 0,
            "upper_bound": 513
        },
        {
            "from": "134",
            "to": "33",
            "cost": 3172,
            "lower_bound": 0,
            "upper_bound": 63
        },
        {
            "from": "134",
            "to": "256",
            "cost": 1438,
            "lower_bound": 0,
            "upper_bound": 877
        },
        {
            "from": "134",
            "to": "252",
            "cost": 4958,
            "lower_bound": 0,
            "upper_bound": 963
        },
        {
            "from": "134",
            "to": "204",
            "cost": 1471,
            "lower_bound": 0,
            "upper_bound": 203
        },
        {
            "from": "165",
            "to": "212",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 414
        },
        {
            "from": "165",
            "to": "121",
            "cost": 1274,
            "lower_bound": 0,
            "upper_bound": 901
        },
        {
            "from": "165",
            "to": "231",
            "cost": 1354,
            "lower_bound": 0,
            "upper_bound": 906
        },
        {
            "from": "165",
            "to": "160",
            "cost": 8367,
            "lower_bound": 0,
            "upper_bound": 314
        },
        {
            "from": "165",
            "to": "147",
            "cost": 6793,
            "lower_bound": 0,
            "upper_bound": 803
        },
        {
            "from": "171",
            "to": "30",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 414
        },
        {
            "from": "171",
            "to": "237",
            "cost": 8868,
            "lower_bound": 0,
            "upper_bound": 432
        },
        {
            "from": "171",
            "to": "103",
            "cost": 2136,
            "lower_bound": 0,
            "upper_bound": 160
        },
        {
            "from": "212",
            "to": "53",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 414
        },
        {
            "from": "212",
            "to": "86",
            "cost": 390,
            "lower_bound": 0,
            "upper_bound": 620
        },
        {
            "from": "212",
            "to": "244",
            "cost": 2171,
            "lower_bound": 0,
            "upper_bound": 721
        },
        {
            "from": "212",
            "to": "197",
            "cost": 6505,
            "lower_bound": 0,
            "upper_bound": 432
        },
        {
            "from": "212",
            "to": "243",
            "cost": 4452,
            "lower_bound": 0,
            "upper_bound": 852
        },
        {
            "from": "221",
            "to": "165",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 414
        },
        {
            "from": "221",
            "to": "160",
            "cost": 4600,
            "lower_bound": 0,
            "upper_bound": 667
        },
        {
            "from": "235",
            "to": "40",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 414
        },
        {
            "from": "235",
            "to": "174",
            "cost": 6902,
            "lower_bound": 0,
            "upper_bound": 125
        },
        {
            "from": "235",
            "to": "242",
            "cost": 3413,
            "lower_bound": 0,
            "upper_bound": 783
        },
        {
            "from": "235",
            "to": "222",
            "cost": 1971,
            "lower_bound": 0,
            "upper_bound": 751
        },
        {
            "from": "236",
            "to": "124",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 414
        },
        {
            "from": "236",
            "to": "167",
            "cost": 8773,
            "lower_bound": 0,
            "upper_bound": 962
        },
        {
            "from": "236",
            "to": "181",
            "cost": 3456,
            "lower_bound": 0,
            "upper_bound": 935
        },
        {
            "from": "236",
            "to": "87",
            "cost": 9996,
            "lower_bound": 0,
            "upper_bound": 958
        },
        {
            "from": "236",
            "to": "97",
            "cost": 9266,
            "lower_bound": 0,
            "upper_bound": 357
        },
        {
            "from": "236",
            "to": "191",
            "cost": 9509,
            "lower_bound": 0,
            "upper_bound": 992
        },
        {
            "from": "236",
            "to": "110",
            "cost": 5986,
            "lower_bound": 0,
            "upper_bound": 882
        },
        {
            "from": "236",
            "to": "186",
            "cost": 3492,
            "lower_bound": 0,
            "upper_bound": 716
        },
        {
            "from": "236",
            "to": "162",
            "cost": 3002,
            "lower_bound": 0,
            "upper_bound": 169
        },
        {
            "from": "236",
            "to": "90",
            "cost": 8287,
            "lower_bound": 0,
            "upper_bound": 715
        },
        {
            "from": "236",
            "to": "213",
            "cost": 5367,
            "lower_bound": 0,
            "upper_bound": 911
        },
        {
            "from": "236",
            "to": "206",
            "cost": 2965,
            "lower_bound": 0,
            "upper_bound": 992
        },
        {
            "from": "7",
            "to": "75",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 686
        },
        {
            "from": "7",
            "to": "96",
            "cost": 1881,
            "lower_bound": 0,
            "upper_bound": 962
        },
        {
            "from": "7",
            "to": "38",
            "cost": 9847,
            "lower_bound": 0,
            "upper_bound": 45
        },
        {
            "from": "7",
            "to": "171",
            "cost": 6117,
            "lower_bound": 0,
            "upper_bound": 549
        },
        {
            "from": "7",
            "to": "242",
            "cost": 412,
            "lower_bound": 0,
            "upper_bound": 212
        },
        {
            "from": "7",
            "to": "161",
            "cost": 4950,
            "lower_bound": 0,
            "upper_bound": 768
        },
        {
            "from": "7",
            "to": "34",
            "cost": 1220,
            "lower_bound": 0,
            "upper_bound": 901
        },
        {
            "from": "7",
            "to": "66",
            "cost": 4494,
            "lower_bound": 0,
            "upper_bound": 651
        },
        {
            "from": "7",
            "to": "59",
            "cost": 7285,
            "lower_bound": 0,
            "upper_bound": 219
        },
        {
            "from": "7",
            "to": "62",
            "cost": 4464,
            "lower_bound": 0,
            "upper_bound": 733
        },
        {
            "from": "7",
            "to": "55",
            "cost": 7419,
            "lower_bound": 0,
            "upper_bound": 791
        },
        {
            "from": "7",
            "to": "88",
            "cost": 8369,
            "lower_bound": 0,
            "upper_bound": 357
        },
        {
            "from": "7",
            "to": "124",
            "cost": 751,
            "lower_bound": 0,
            "upper_bound": 165
        },
        {
            "from": "7",
            "to": "69",
            "cost": 3317,
            "lower_bound": 0,
            "upper_bound": 702
        },
        {
            "from": "7",
            "to": "136",
            "cost": 3049,
            "lower_bound": 0,
            "upper_bound": 35
        },
        {
            "from": "22",
            "to": "205",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 686
        },
        {
            "from": "22",
            "to": "117",
            "cost": 5005,
            "lower_bound": 0,
            "upper_bound": 867
        },
        {
            "from": "22",
            "to": "225",
            "cost": 2218,
            "lower_bound": 0,
            "upper_bound": 976
        },
        {
            "from": "22",
            "to": "20",
            "cost": 3500,
            "lower_bound": 0,
            "upper_bound": 191
        },
        {
            "from": "22",
            "to": "245",
            "cost": 2829,
            "lower_bound": 0,
            "upper_bound": 333
        },
        {
            "from": "22",
            "to": "70",
            "cost": 1649,
            "lower_bound": 0,
            "upper_bound": 255
        },
        {
            "from": "22",
            "to": "158",
            "cost": 4643,
            "lower_bound": 0,
            "upper_bound": 759
        },
        {
            "from": "22",
            "to": "171",
            "cost": 3090,
            "lower_bound": 0,
            "upper_bound": 919
        },
        {
            "from": "22",
            "to": "64",
            "cost": 8893,
            "lower_bound": 0,
            "upper_bound": 413
        },
        {
            "from": "22",
            "to": "188",
            "cost": 1757,
            "lower_bound": 0,
            "upper_bound": 623
        },
        {
            "from": "22",
            "to": "170",
            "cost": 6310,
            "lower_bound": 0,
            "upper_bound": 426
        },
        {
            "from": "22",
            "to": "227",
            "cost": 6580,
            "lower_bound": 0,
            "upper_bound": 567
        },
        {
            "from": "22",
            "to": "136",
            "cost": 7934,
            "lower_bound": 0,
            "upper_bound": 231
        },
        {
            "from": "22",
            "to": "74",
            "cost": 6372,
            "lower_bound": 0,
            "upper_bound": 770
        },
        {
            "from": "34",
            "to": "246",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 686
        },
        {
            "from": "34",
            "to": "223",
            "cost": 1215,
            "lower_bound": 0,
            "upper_bound": 519
        },
        {
            "from": "34",
            "to": "168",
            "cost": 5395,
            "lower_bound": 0,
            "upper_bound": 973
        },
        {
            "from": "34",
            "to": "99",
            "cost": 8063,
            "lower_bound": 0,
            "upper_bound": 167
        },
        {
            "from": "34",
            "to": "235",
            "cost": 9000,
            "lower_bound": 0,
            "upper_bound": 308
        },
        {
            "from": "34",
            "to": "147",
            "cost": 3120,
            "lower_bound": 0,
            "upper_bound": 190
        },
        {
            "from": "34",
            "to": "97",
            "cost": 1153,
            "lower_bound": 0,
            "upper_bound": 563
        },
        {
            "from": "34",
            "to": "182",
            "cost": 3206,
            "lower_bound": 0,
            "upper_bound": 496
        },
        {
            "from": "34",
            "to": "249",
            "cost": 2297,
            "lower_bound": 0,
            "upper_bound": 246
        },
        {
            "from": "34",
            "to": "84",
            "cost": 1136,
            "lower_bound": 0,
            "upper_bound": 630
        },
        {
            "from": "35",
            "to": "150",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 686
        },
        {
            "from": "35",
            "to": "81",
            "cost": 4392,
            "lower_bound": 0,
            "upper_bound": 857
        },
        {
            "from": "35",
            "to": "69",
            "cost": 3462,
            "lower_bound": 0,
            "upper_bound": 387
        },
        {
            "from": "35",
            "to": "63",
            "cost": 1262,
            "lower_bound": 0,
            "upper_bound": 14
        },
        {
            "from": "35",
            "to": "50",
            "cost": 2363,
            "lower_bound": 0,
            "upper_bound": 874
        },
        {
            "from": "35",
            "to": "239",
            "cost": 4112,
            "lower_bound": 0,
            "upper_bound": 661
        },
        {
            "from": "35",
            "to": "109",
            "cost": 1601,
            "lower_bound": 0,
            "upper_bound": 726
        },
        {
            "from": "35",
            "to": "253",
            "cost": 4500,
            "lower_bound": 0,
            "upper_bound": 451
        },
        {
            "from": "35",
            "to": "256",
            "cost": 5940,
            "lower_bound": 0,
            "upper_bound": 333
        },
        {
            "from": "35",
            "to": "78",
            "cost": 1559,
            "lower_bound": 0,
            "upper_bound": 834
        },
        {
            "from": "35",
            "to": "101",
            "cost": 3103,
            "lower_bound": 0,
            "upper_bound": 965
        },
        {
            "from": "35",
            "to": "129",
            "cost": 9036,
            "lower_bound": 0,
            "upper_bound": 43
        },
        {
            "from": "51",
            "to": "253",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 686
        },
        {
            "from": "51",
            "to": "92",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 686
        },
        {
            "from": "51",
            "to": "115",
            "cost": 7737,
            "lower_bound": 0,
            "upper_bound": 41
        },
        {
            "from": "51",
            "to": "44",
            "cost": 3221,
            "lower_bound": 0,
            "upper_bound": 41
        },
        {
            "from": "51",
            "to": "78",
            "cost": 6299,
            "lower_bound": 0,
            "upper_bound": 348
        },
        {
            "from": "51",
            "to": "21",
            "cost": 8749,
            "lower_bound": 0,
            "upper_bound": 666
        },
        {
            "from": "51",
            "to": "148",
            "cost": 7047,
            "lower_bound": 0,
            "upper_bound": 645
        },
        {
            "from": "51",
            "to": "130",
            "cost": 1550,
            "lower_bound": 0,
            "upper_bound": 931
        },
        {
            "from": "51",
            "to": "236",
            "cost": 1602,
            "lower_bound": 0,
            "upper_bound": 255
        },
        {
            "from": "51",
            "to": "93",
            "cost": 2935,
            "lower_bound": 0,
            "upper_bound": 533
        },
        {
            "from": "75",
            "to": "178",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 686
        },
        {
            "from": "75",
            "to": "130",
            "cost": 6997,
            "lower_bound": 0,
            "upper_bound": 358
        },
        {
            "from": "75",
            "to": "222",
            "cost": 293,
            "lower_bound": 0,
            "upper_bound": 271
        },
        {
            "from": "75",
            "to": "155",
            "cost": 9569,
            "lower_bound": 0,
            "upper_bound": 600
        },
        {
            "from": "75",
            "to": "250",
            "cost": 3323,
            "lower_bound": 0,
            "upper_bound": 590
        },
        {
            "from": "75",
            "to": "190",
            "cost": 4981,
            "lower_bound": 0,
            "upper_bound": 748
        },
        {
            "from": "75",
            "to": "226",
            "cost": 4873,
            "lower_bound": 0,
            "upper_bound": 71
        },
        {
            "from": "75",
            "to": "216",
            "cost": 3007,
            "lower_bound": 0,
            "upper_bound": 782
        },
        {
            "from": "75",
            "to": "142",
            "cost": 5251,
            "lower_bound": 0,
            "upper_bound": 130
        },
        {
            "from": "75",
            "to": "166",
            "cost": 6114,
            "lower_bound": 0,
            "upper_bound": 434
        },
        {
            "from": "75",
            "to": "167",
            "cost": 4199,
            "lower_bound": 0,
            "upper_bound": 864
        },
        {
            "from": "75",
            "to": "39",
            "cost": 6530,
            "lower_bound": 0,
            "upper_bound": 298
        },
        {
            "from": "75",
            "to": "35",
            "cost": 164,
            "lower_bound": 0,
            "upper_bound": 367
        },
        {
            "from": "75",
            "to": "198",
            "cost": 3894,
            "lower_bound": 0,
            "upper_bound": 269
        },
        {
            "from": "75",
            "to": "40",
            "cost": 5871,
            "lower_bound": 0,
            "upper_bound": 548
        },
        {
            "from": "92",
            "to": "22",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 686
        },
        {
            "from": "92",
            "to": "42",
            "cost": 725,
            "lower_bound": 0,
            "upper_bound": 820
        },
        {
            "from": "92",
            "to": "115",
            "cost": 239,
            "lower_bound": 0,
            "upper_bound": 388
        },
        {
            "from": "92",
            "to": "179",
            "cost": 2994,
            "lower_bound": 0,
            "upper_bound": 863
        },
        {
            "from": "92",
            "to": "225",
            "cost": 4257,
            "lower_bound": 0,
            "upper_bound": 195
        },
        {
            "from": "92",
            "to": "187",
            "cost": 3870,
            "lower_bound": 0,
            "upper_bound": 383
        },
        {
            "from": "92",
            "to": "164",
            "cost": 7670,
            "lower_bound": 0,
            "upper_bound": 70
        },
        {
            "from": "92",
            "to": "58",
            "cost": 5979,
            "lower_bound": 0,
            "upper_bound": 988
        },
        {
            "from": "150",
            "to": "172",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 686
        },
        {
            "from": "150",
            "to": "26",
            "cost": 9426,
            "lower_bound": 0,
            "upper_bound": 872
        },
        {
            "from": "172",
            "to": "34",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 686
        },
        {
            "from": "172",
            "to": "131",
            "cost": 5506,
            "lower_bound": 0,
            "upper_bound": 490
        },
        {
            "from": "172",
            "to": "67",
            "cost": 9181,
            "lower_bound": 0,
            "upper_bound": 764
        },
        {
            "from": "172",
            "to": "164",
            "cost": 1660,
            "lower_bound": 0,
            "upper_bound": 894
        },
        {
            "from": "172",
            "to": "53",
            "cost": 6208,
            "lower_bound": 0,
            "upper_bound": 985
        },
        {
            "from": "172",
            "to": "144",
            "cost": 2889,
            "lower_bound": 0,
            "upper_bound": 275
        },
        {
            "from": "178",
            "to": "51",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 686
        },
        {
            "from": "178",
            "to": "226",
            "cost": 1344,
            "lower_bound": 0,
            "upper_bound": 383
        },
        {
            "from": "178",
            "to": "256",
            "cost": 1954,
            "lower_bound": 0,
            "upper_bound": 359
        },
        {
            "from": "178",
            "to": "56",
            "cost": 5208,
            "lower_bound": 0,
            "upper_bound": 968
        },
        {
            "from": "178",
            "to": "153",
            "cost": 9782,
            "lower_bound": 0,
            "upper_bound": 169
        },
        {
            "from": "178",
            "to": "234",
            "cost": 1617,
            "lower_bound": 0,
            "upper_bound": 124
        },
        {
            "from": "178",
            "to": "95",
            "cost": 90,
            "lower_bound": 0,
            "upper_bound": 549
        },
        {
            "from": "178",
            "to": "177",
            "cost": 2126,
            "lower_bound": 0,
            "upper_bound": 54
        },
        {
            "from": "178",
            "to": "22",
            "cost": 4256,
            "lower_bound": 0,
            "upper_bound": 300
        },
        {
            "from": "178",
            "to": "85",
            "cost": 9456,
            "lower_bound": 0,
            "upper_bound": 517
        },
        {
            "from": "178",
            "to": "76",
            "cost": 1146,
            "lower_bound": 0,
            "upper_bound": 554
        },
        {
            "from": "205",
            "to": "225",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 686
        },
        {
            "from": "205",
            "to": "176",
            "cost": 1357,
            "lower_bound": 0,
            "upper_bound": 435
        },
        {
            "from": "205",
            "to": "84",
            "cost": 9134,
            "lower_bound": 0,
            "upper_bound": 299
        },
        {
            "from": "205",
            "to": "136",
            "cost": 1129,
            "lower_bound": 0,
            "upper_bound": 805
        },
        {
            "from": "205",
            "to": "178",
            "cost": 7388,
            "lower_bound": 0,
            "upper_bound": 926
        },
        {
            "from": "205",
            "to": "110",
            "cost": 9208,
            "lower_bound": 0,
            "upper_bound": 34
        },
        {
            "from": "205",
            "to": "45",
            "cost": 3582,
            "lower_bound": 0,
            "upper_bound": 558
        },
        {
            "from": "205",
            "to": "185",
            "cost": 6211,
            "lower_bound": 0,
            "upper_bound": 813
        },
        {
            "from": "205",
            "to": "62",
            "cost": 5570,
            "lower_bound": 0,
            "upper_bound": 994
        },
        {
            "from": "225",
            "to": "35",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 686
        },
        {
            "from": "225",
            "to": "145",
            "cost": 3857,
            "lower_bound": 0,
            "upper_bound": 43
        },
        {
            "from": "225",
            "to": "240",
            "cost": 8866,
            "lower_bound": 0,
            "upper_bound": 829
        },
        {
            "from": "225",
            "to": "169",
            "cost": 2663,
            "lower_bound": 0,
            "upper_bound": 980
        },
        {
            "from": "225",
            "to": "211",
            "cost": 1881,
            "lower_bound": 0,
            "upper_bound": 363
        },
        {
            "from": "225",
            "to": "142",
            "cost": 2194,
            "lower_bound": 0,
            "upper_bound": 339
        },
        {
            "from": "225",
            "to": "141",
            "cost": 4773,
            "lower_bound": 0,
            "upper_bound": 592
        },
        {
            "from": "225",
            "to": "130",
            "cost": 3318,
            "lower_bound": 0,
            "upper_bound": 278
        },
        {
            "from": "8",
            "to": "108",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1055
        },
        {
            "from": "8",
            "to": "176",
            "cost": 1146,
            "lower_bound": 0,
            "upper_bound": 110
        },
        {
            "from": "8",
            "to": "93",
            "cost": 2044,
            "lower_bound": 0,
            "upper_bound": 79
        },
        {
            "from": "8",
            "to": "65",
            "cost": 4865,
            "lower_bound": 0,
            "upper_bound": 725
        },
        {
            "from": "8",
            "to": "129",
            "cost": 3681,
            "lower_bound": 0,
            "upper_bound": 226
        },
        {
            "from": "8",
            "to": "95",
            "cost": 7897,
            "lower_bound": 0,
            "upper_bound": 889
        },
        {
            "from": "8",
            "to": "202",
            "cost": 2877,
            "lower_bound": 0,
            "upper_bound": 828
        },
        {
            "from": "42",
            "to": "67",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1055
        },
        {
            "from": "42",
            "to": "135",
            "cost": 2871,
            "lower_bound": 0,
            "upper_bound": 256
        },
        {
            "from": "42",
            "to": "195",
            "cost": 6964,
            "lower_bound": 0,
            "upper_bound": 106
        },
        {
            "from": "42",
            "to": "100",
            "cost": 9856,
            "lower_bound": 0,
            "upper_bound": 599
        },
        {
            "from": "42",
            "to": "130",
            "cost": 2646,
            "lower_bound": 0,
            "upper_bound": 474
        },
        {
            "from": "42",
            "to": "46",
            "cost": 4520,
            "lower_bound": 0,
            "upper_bound": 715
        },
        {
            "from": "42",
            "to": "155",
            "cost": 1305,
            "lower_bound": 0,
            "upper_bound": 816
        },
        {
            "from": "42",
            "to": "121",
            "cost": 7248,
            "lower_bound": 0,
            "upper_bound": 500
        },
        {
            "from": "42",
            "to": "123",
            "cost": 5414,
            "lower_bound": 0,
            "upper_bound": 587
        },
        {
            "from": "42",
            "to": "35",
            "cost": 2875,
            "lower_bound": 0,
            "upper_bound": 756
        },
        {
            "from": "50",
            "to": "115",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1055
        },
        {
            "from": "50",
            "to": "150",
            "cost": 9675,
            "lower_bound": 0,
            "upper_bound": 381
        },
        {
            "from": "50",
            "to": "218",
            "cost": 884,
            "lower_bound": 0,
            "upper_bound": 335
        },
        {
            "from": "50",
            "to": "137",
            "cost": 3566,
            "lower_bound": 0,
            "upper_bound": 304
        },
        {
            "from": "50",
            "to": "200",
            "cost": 5250,
            "lower_bound": 0,
            "upper_bound": 291
        },
        {
            "from": "50",
            "to": "104",
            "cost": 1775,
            "lower_bound": 0,
            "upper_bound": 304
        },
        {
            "from": "50",
            "to": "160",
            "cost": 7627,
            "lower_bound": 0,
            "upper_bound": 203
        },
        {
            "from": "50",
            "to": "235",
            "cost": 2697,
            "lower_bound": 0,
            "upper_bound": 213
        },
        {
            "from": "50",
            "to": "197",
            "cost": 8693,
            "lower_bound": 0,
            "upper_bound": 650
        },
        {
            "from": "50",
            "to": "26",
            "cost": 584,
            "lower_bound": 0,
            "upper_bound": 148
        },
        {
            "from": "50",
            "to": "136",
            "cost": 8975,
            "lower_bound": 0,
            "upper_bound": 850
        },
        {
            "from": "50",
            "to": "36",
            "cost": 519,
            "lower_bound": 0,
            "upper_bound": 622
        },
        {
            "from": "67",
            "to": "160",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1055
        },
        {
            "from": "67",
            "to": "110",
            "cost": 3713,
            "lower_bound": 0,
            "upper_bound": 755
        },
        {
            "from": "67",
            "to": "159",
            "cost": 9695,
            "lower_bound": 0,
            "upper_bound": 835
        },
        {
            "from": "81",
            "to": "136",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1055
        },
        {
            "from": "81",
            "to": "253",
            "cost": 5841,
            "lower_bound": 0,
            "upper_bound": 63
        },
        {
            "from": "81",
            "to": "128",
            "cost": 300,
            "lower_bound": 0,
            "upper_bound": 242
        },
        {
            "from": "81",
            "to": "193",
            "cost": 7778,
            "lower_bound": 0,
            "upper_bound": 125
        },
        {
            "from": "81",
            "to": "223",
            "cost": 9167,
            "lower_bound": 0,
            "upper_bound": 408
        },
        {
            "from": "81",
            "to": "182",
            "cost": 1261,
            "lower_bound": 0,
            "upper_bound": 448
        },
        {
            "from": "81",
            "to": "137",
            "cost": 3677,
            "lower_bound": 0,
            "upper_bound": 801
        },
        {
            "from": "81",
            "to": "36",
            "cost": 7716,
            "lower_bound": 0,
            "upper_bound": 687
        },
        {
            "from": "81",
            "to": "52",
            "cost": 5892,
            "lower_bound": 0,
            "upper_bound": 925
        },
        {
            "from": "81",
            "to": "248",
            "cost": 1656,
            "lower_bound": 0,
            "upper_bound": 989
        },
        {
            "from": "81",
            "to": "141",
            "cost": 9904,
            "lower_bound": 0,
            "upper_bound": 980
        },
        {
            "from": "81",
            "to": "66",
            "cost": 4355,
            "lower_bound": 0,
            "upper_bound": 280
        },
        {
            "from": "108",
            "to": "149",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1055
        },
        {
            "from": "108",
            "to": "36",
            "cost": 4254,
            "lower_bound": 0,
            "upper_bound": 187
        },
        {
            "from": "108",
            "to": "18",
            "cost": 5716,
            "lower_bound": 0,
            "upper_bound": 219
        },
        {
            "from": "108",
            "to": "137",
            "cost": 8290,
            "lower_bound": 0,
            "upper_bound": 845
        },
        {
            "from": "108",
            "to": "73",
            "cost": 6901,
            "lower_bound": 0,
            "upper_bound": 420
        },
        {
            "from": "108",
            "to": "122",
            "cost": 7139,
            "lower_bound": 0,
            "upper_bound": 66
        },
        {
            "from": "108",
            "to": "88",
            "cost": 4240,
            "lower_bound": 0,
            "upper_bound": 438
        },
        {
            "from": "115",
            "to": "232",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1055
        },
        {
            "from": "115",
            "to": "89",
            "cost": 3799,
            "lower_bound": 0,
            "upper_bound": 728
        },
        {
            "from": "115",
            "to": "116",
            "cost": 3742,
            "lower_bound": 0,
            "upper_bound": 46
        },
        {
            "from": "115",
            "to": "174",
            "cost": 1947,
            "lower_bound": 0,
            "upper_bound": 955
        },
        {
            "from": "115",
            "to": "177",
            "cost": 1280,
            "lower_bound": 0,
            "upper_bound": 561
        },
        {
            "from": "115",
            "to": "27",
            "cost": 8107,
            "lower_bound": 0,
            "upper_bound": 548
        },
        {
            "from": "115",
            "to": "183",
            "cost": 8452,
            "lower_bound": 0,
            "upper_bound": 556
        },
        {
            "from": "115",
            "to": "229",
            "cost": 9547,
            "lower_bound": 0,
            "upper_bound": 165
        },
        {
            "from": "115",
            "to": "39",
            "cost": 408,
            "lower_bound": 0,
            "upper_bound": 171
        },
        {
            "from": "115",
            "to": "201",
            "cost": 2420,
            "lower_bound": 0,
            "upper_bound": 713
        },
        {
            "from": "115",
            "to": "107",
            "cost": 6452,
            "lower_bound": 0,
            "upper_bound": 196
        },
        {
            "from": "115",
            "to": "17",
            "cost": 8914,
            "lower_bound": 0,
            "upper_bound": 875
        },
        {
            "from": "115",
            "to": "215",
            "cost": 7861,
            "lower_bound": 0,
            "upper_bound": 46
        },
        {
            "from": "115",
            "to": "210",
            "cost": 4045,
            "lower_bound": 0,
            "upper_bound": 81
        },
        {
            "from": "115",
            "to": "113",
            "cost": 4722,
            "lower_bound": 0,
            "upper_bound": 519
        },
        {
            "from": "130",
            "to": "244",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1055
        },
        {
            "from": "130",
            "to": "81",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1055
        },
        {
            "from": "130",
            "to": "33",
            "cost": 1842,
            "lower_bound": 0,
            "upper_bound": 250
        },
        {
            "from": "130",
            "to": "189",
            "cost": 1076,
            "lower_bound": 0,
            "upper_bound": 265
        },
        {
            "from": "130",
            "to": "57",
            "cost": 2348,
            "lower_bound": 0,
            "upper_bound": 175
        },
        {
            "from": "130",
            "to": "201",
            "cost": 7172,
            "lower_bound": 0,
            "upper_bound": 485
        },
        {
            "from": "130",
            "to": "106",
            "cost": 1627,
            "lower_bound": 0,
            "upper_bound": 324
        },
        {
            "from": "130",
            "to": "77",
            "cost": 8364,
            "lower_bound": 0,
            "upper_bound": 540
        },
        {
            "from": "130",
            "to": "218",
            "cost": 5929,
            "lower_bound": 0,
            "upper_bound": 339
        },
        {
            "from": "130",
            "to": "242",
            "cost": 3682,
            "lower_bound": 0,
            "upper_bound": 380
        },
        {
            "from": "130",
            "to": "168",
            "cost": 7624,
            "lower_bound": 0,
            "upper_bound": 345
        },
        {
            "from": "130",
            "to": "211",
            "cost": 6806,
            "lower_bound": 0,
            "upper_bound": 409
        },
        {
            "from": "130",
            "to": "127",
            "cost": 5976,
            "lower_bound": 0,
            "upper_bound": 884
        },
        {
            "from": "130",
            "to": "118",
            "cost": 536,
            "lower_bound": 0,
            "upper_bound": 325
        },
        {
            "from": "136",
            "to": "231",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1055
        },
        {
            "from": "136",
            "to": "79",
            "cost": 7036,
            "lower_bound": 0,
            "upper_bound": 423
        },
        {
            "from": "136",
            "to": "162",
            "cost": 4686,
            "lower_bound": 0,
            "upper_bound": 220
        },
        {
            "from": "136",
            "to": "62",
            "cost": 8256,
            "lower_bound": 0,
            "upper_bound": 26
        },
        {
            "from": "136",
            "to": "22",
            "cost": 4174,
            "lower_bound": 0,
            "upper_bound": 579
        },
        {
            "from": "136",
            "to": "39",
            "cost": 7909,
            "lower_bound": 0,
            "upper_bound": 131
        },
        {
            "from": "136",
            "to": "35",
            "cost": 744,
            "lower_bound": 0,
            "upper_bound": 559
        },
        {
            "from": "149",
            "to": "151",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1055
        },
        {
            "from": "149",
            "to": "140",
            "cost": 1063,
            "lower_bound": 0,
            "upper_bound": 907
        },
        {
            "from": "149",
            "to": "175",
            "cost": 9329,
            "lower_bound": 0,
            "upper_bound": 526
        },
        {
            "from": "149",
            "to": "229",
            "cost": 5858,
            "lower_bound": 0,
            "upper_bound": 428
        },
        {
            "from": "151",
            "to": "130",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1055
        },
        {
            "from": "151",
            "to": "116",
            "cost": 5198,
            "lower_bound": 0,
            "upper_bound": 736
        },
        {
            "from": "151",
            "to": "245",
            "cost": 6396,
            "lower_bound": 0,
            "upper_bound": 184
        },
        {
            "from": "151",
            "to": "88",
            "cost": 5602,
            "lower_bound": 0,
            "upper_bound": 964
        },
        {
            "from": "151",
            "to": "80",
            "cost": 1545,
            "lower_bound": 0,
            "upper_bound": 825
        },
        {
            "from": "151",
            "to": "49",
            "cost": 692,
            "lower_bound": 0,
            "upper_bound": 551
        },
        {
            "from": "151",
            "to": "30",
            "cost": 798,
            "lower_bound": 0,
            "upper_bound": 483
        },
        {
            "from": "151",
            "to": "239",
            "cost": 495,
            "lower_bound": 0,
            "upper_bound": 70
        },
        {
            "from": "151",
            "to": "73",
            "cost": 7751,
            "lower_bound": 0,
            "upper_bound": 740
        },
        {
            "from": "160",
            "to": "188",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1055
        },
        {
            "from": "160",
            "to": "65",
            "cost": 1339,
            "lower_bound": 0,
            "upper_bound": 426
        },
        {
            "from": "160",
            "to": "61",
            "cost": 7077,
            "lower_bound": 0,
            "upper_bound": 276
        },
        {
            "from": "160",
            "to": "217",
            "cost": 4604,
            "lower_bound": 0,
            "upper_bound": 100
        },
        {
            "from": "160",
            "to": "131",
            "cost": 5604,
            "lower_bound": 0,
            "upper_bound": 595
        },
        {
            "from": "160",
            "to": "241",
            "cost": 4173,
            "lower_bound": 0,
            "upper_bound": 714
        },
        {
            "from": "160",
            "to": "45",
            "cost": 1076,
            "lower_bound": 0,
            "upper_bound": 58
        },
        {
            "from": "160",
            "to": "228",
            "cost": 9419,
            "lower_bound": 0,
            "upper_bound": 998
        },
        {
            "from": "182",
            "to": "50",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1055
        },
        {
            "from": "182",
            "to": "197",
            "cost": 1355,
            "lower_bound": 0,
            "upper_bound": 671
        },
        {
            "from": "182",
            "to": "117",
            "cost": 6649,
            "lower_bound": 0,
            "upper_bound": 771
        },
        {
            "from": "182",
            "to": "95",
            "cost": 2238,
            "lower_bound": 0,
            "upper_bound": 391
        },
        {
            "from": "182",
            "to": "54",
            "cost": 4197,
            "lower_bound": 0,
            "upper_bound": 804
        },
        {
            "from": "182",
            "to": "161",
            "cost": 1513,
            "lower_bound": 0,
            "upper_bound": 778
        },
        {
            "from": "182",
            "to": "41",
            "cost": 1265,
            "lower_bound": 0,
            "upper_bound": 671
        },
        {
            "from": "182",
            "to": "78",
            "cost": 6697,
            "lower_bound": 0,
            "upper_bound": 750
        },
        {
            "from": "182",
            "to": "79",
            "cost": 2066,
            "lower_bound": 0,
            "upper_bound": 617
        },
        {
            "from": "182",
            "to": "108",
            "cost": 7101,
            "lower_bound": 0,
            "upper_bound": 892
        },
        {
            "from": "182",
            "to": "123",
            "cost": 5984,
            "lower_bound": 0,
            "upper_bound": 596
        },
        {
            "from": "188",
            "to": "245",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1055
        },
        {
            "from": "188",
            "to": "18",
            "cost": 6213,
            "lower_bound": 0,
            "upper_bound": 1000
        },
        {
            "from": "188",
            "to": "66",
            "cost": 403,
            "lower_bound": 0,
            "upper_bound": 75
        },
        {
            "from": "188",
            "to": "191",
            "cost": 510,
            "lower_bound": 0,
            "upper_bound": 689
        },
        {
            "from": "188",
            "to": "48",
            "cost": 8506,
            "lower_bound": 0,
            "upper_bound": 3
        },
        {
            "from": "231",
            "to": "182",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1055
        },
        {
            "from": "231",
            "to": "121",
            "cost": 8180,
            "lower_bound": 0,
            "upper_bound": 800
        },
        {
            "from": "231",
            "to": "237",
            "cost": 2358,
            "lower_bound": 0,
            "upper_bound": 763
        },
        {
            "from": "231",
            "to": "123",
            "cost": 1953,
            "lower_bound": 0,
            "upper_bound": 296
        },
        {
            "from": "231",
            "to": "74",
            "cost": 7490,
            "lower_bound": 0,
            "upper_bound": 805
        },
        {
            "from": "231",
            "to": "139",
            "cost": 6787,
            "lower_bound": 0,
            "upper_bound": 354
        },
        {
            "from": "231",
            "to": "136",
            "cost": 1679,
            "lower_bound": 0,
            "upper_bound": 409
        },
        {
            "from": "232",
            "to": "42",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1055
        },
        {
            "from": "232",
            "to": "236",
            "cost": 180,
            "lower_bound": 0,
            "upper_bound": 647
        },
        {
            "from": "232",
            "to": "29",
            "cost": 8697,
            "lower_bound": 0,
            "upper_bound": 416
        },
        {
            "from": "232",
            "to": "20",
            "cost": 9866,
            "lower_bound": 0,
            "upper_bound": 921
        },
        {
            "from": "232",
            "to": "187",
            "cost": 8780,
            "lower_bound": 0,
            "upper_bound": 462
        },
        {
            "from": "232",
            "to": "121",
            "cost": 1467,
            "lower_bound": 0,
            "upper_bound": 458
        },
        {
            "from": "232",
            "to": "130",
            "cost": 8249,
            "lower_bound": 0,
            "upper_bound": 642
        },
        {
            "from": "232",
            "to": "215",
            "cost": 6401,
            "lower_bound": 0,
            "upper_bound": 404
        },
        {
            "from": "232",
            "to": "254",
            "cost": 6648,
            "lower_bound": 0,
            "upper_bound": 515
        },
        {
            "from": "232",
            "to": "73",
            "cost": 735,
            "lower_bound": 0,
            "upper_bound": 376
        },
        {
            "from": "9",
            "to": "157",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 372
        },
        {
            "from": "9",
            "to": "199",
            "cost": 9637,
            "lower_bound": 0,
            "upper_bound": 515
        },
        {
            "from": "9",
            "to": "208",
            "cost": 7911,
            "lower_bound": 0,
            "upper_bound": 459
        },
        {
            "from": "9",
            "to": "133",
            "cost": 7534,
            "lower_bound": 0,
            "upper_bound": 149
        },
        {
            "from": "9",
            "to": "67",
            "cost": 9211,
            "lower_bound": 0,
            "upper_bound": 399
        },
        {
            "from": "9",
            "to": "85",
            "cost": 9941,
            "lower_bound": 0,
            "upper_bound": 296
        },
        {
            "from": "39",
            "to": "77",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 372
        },
        {
            "from": "39",
            "to": "95",
            "cost": 4703,
            "lower_bound": 0,
            "upper_bound": 356
        },
        {
            "from": "39",
            "to": "44",
            "cost": 3988,
            "lower_bound": 0,
            "upper_bound": 542
        },
        {
            "from": "39",
            "to": "48",
            "cost": 3104,
            "lower_bound": 0,
            "upper_bound": 856
        },
        {
            "from": "39",
            "to": "172",
            "cost": 193,
            "lower_bound": 0,
            "upper_bound": 539
        },
        {
            "from": "39",
            "to": "205",
            "cost": 9585,
            "lower_bound": 0,
            "upper_bound": 388
        },
        {
            "from": "39",
            "to": "41",
            "cost": 9820,
            "lower_bound": 0,
            "upper_bound": 165
        },
        {
            "from": "66",
            "to": "152",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 372
        },
        {
            "from": "66",
            "to": "102",
            "cost": 1136,
            "lower_bound": 0,
            "upper_bound": 395
        },
        {
            "from": "66",
            "to": "63",
            "cost": 4892,
            "lower_bound": 0,
            "upper_bound": 505
        },
        {
            "from": "66",
            "to": "41",
            "cost": 7360,
            "lower_bound": 0,
            "upper_bound": 513
        },
        {
            "from": "68",
            "to": "69",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 372
        },
        {
            "from": "68",
            "to": "198",
            "cost": 2283,
            "lower_bound": 0,
            "upper_bound": 379
        },
        {
            "from": "68",
            "to": "101",
            "cost": 3333,
            "lower_bound": 0,
            "upper_bound": 368
        },
        {
            "from": "68",
            "to": "141",
            "cost": 9775,
            "lower_bound": 0,
            "upper_bound": 703
        },
        {
            "from": "68",
            "to": "31",
            "cost": 7532,
            "lower_bound": 0,
            "upper_bound": 499
        },
        {
            "from": "68",
            "to": "82",
            "cost": 7463,
            "lower_bound": 0,
            "upper_bound": 449
        },
        {
            "from": "69",
            "to": "143",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 372
        },
        {
            "from": "69",
            "to": "156",
            "cost": 1079,
            "lower_bound": 0,
            "upper_bound": 468
        },
        {
            "from": "69",
            "to": "116",
            "cost": 6179,
            "lower_bound": 0,
            "upper_bound": 464
        },
        {
            "from": "69",
            "to": "240",
            "cost": 979,
            "lower_bound": 0,
            "upper_bound": 143
        },
        {
            "from": "69",
            "to": "168",
            "cost": 9421,
            "lower_bound": 0,
            "upper_bound": 264
        },
        {
            "from": "69",
            "to": "115",
            "cost": 7120,
            "lower_bound": 0,
            "upper_bound": 423
        },
        {
            "from": "69",
            "to": "183",
            "cost": 7589,
            "lower_bound": 0,
            "upper_bound": 947
        },
        {
            "from": "69",
            "to": "130",
            "cost": 5137,
            "lower_bound": 0,
            "upper_bound": 981
        },
        {
            "from": "69",
            "to": "71",
            "cost": 3178,
            "lower_bound": 0,
            "upper_bound": 358
        },
        {
            "from": "69",
            "to": "249",
            "cost": 8506,
            "lower_bound": 0,
            "upper_bound": 439
        },
        {
            "from": "69",
            "to": "191",
            "cost": 7508,
            "lower_bound": 0,
            "upper_bound": 793
        },
        {
            "from": "77",
            "to": "66",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 372
        },
        {
            "from": "77",
            "to": "46",
            "cost": 6929,
            "lower_bound": 0,
            "upper_bound": 695
        },
        {
            "from": "77",
            "to": "233",
            "cost": 7205,
            "lower_bound": 0,
            "upper_bound": 533
        },
        {
            "from": "77",
            "to": "256",
            "cost": 3552,
            "lower_bound": 0,
            "upper_bound": 574
        },
        {
            "from": "88",
            "to": "120",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 372
        },
        {
            "from": "88",
            "to": "193",
            "cost": 3336,
            "lower_bound": 0,
            "upper_bound": 526
        },
        {
            "from": "88",
            "to": "94",
            "cost": 773,
            "lower_bound": 0,
            "upper_bound": 980
        },
        {
            "from": "88",
            "to": "54",
            "cost": 2554,
            "lower_bound": 0,
            "upper_bound": 214
        },
        {
            "from": "88",
            "to": "231",
            "cost": 1189,
            "lower_bound": 0,
            "upper_bound": 506
        },
        {
            "from": "88",
            "to": "47",
            "cost": 1278,
            "lower_bound": 0,
            "upper_bound": 224
        },
        {
            "from": "120",
            "to": "68",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 372
        },
        {
            "from": "120",
            "to": "248",
            "cost": 1300,
            "lower_bound": 0,
            "upper_bound": 81
        },
        {
            "from": "120",
            "to": "190",
            "cost": 9956,
            "lower_bound": 0,
            "upper_bound": 59
        },
        {
            "from": "120",
            "to": "143",
            "cost": 1995,
            "lower_bound": 0,
            "upper_bound": 189
        },
        {
            "from": "120",
            "to": "44",
            "cost": 8381,
            "lower_bound": 0,
            "upper_bound": 222
        },
        {
            "from": "120",
            "to": "177",
            "cost": 2477,
            "lower_bound": 0,
            "upper_bound": 280
        },
        {
            "from": "120",
            "to": "201",
            "cost": 3747,
            "lower_bound": 0,
            "upper_bound": 891
        },
        {
            "from": "120",
            "to": "37",
            "cost": 9910,
            "lower_bound": 0,
            "upper_bound": 915
        },
        {
            "from": "120",
            "to": "181",
            "cost": 6224,
            "lower_bound": 0,
            "upper_bound": 163
        },
        {
            "from": "120",
            "to": "20",
            "cost": 3443,
            "lower_bound": 0,
            "upper_bound": 210
        },
        {
            "from": "120",
            "to": "22",
            "cost": 2269,
            "lower_bound": 0,
            "upper_bound": 671
        },
        {
            "from": "120",
            "to": "18",
            "cost": 3475,
            "lower_bound": 0,
            "upper_bound": 637
        },
        {
            "from": "120",
            "to": "157",
            "cost": 2420,
            "lower_bound": 0,
            "upper_bound": 438
        },
        {
            "from": "139",
            "to": "245",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 372
        },
        {
            "from": "139",
            "to": "180",
            "cost": 2411,
            "lower_bound": 0,
            "upper_bound": 645
        },
        {
            "from": "139",
            "to": "87",
            "cost": 1161,
            "lower_bound": 0,
            "upper_bound": 471
        },
        {
            "from": "139",
            "to": "130",
            "cost": 6213,
            "lower_bound": 0,
            "upper_bound": 460
        },
        {
            "from": "139",
            "to": "26",
            "cost": 4745,
            "lower_bound": 0,
            "upper_bound": 538
        },
        {
            "from": "139",
            "to": "191",
            "cost": 1522,
            "lower_bound": 0,
            "upper_bound": 516
        },
        {
            "from": "139",
            "to": "18",
            "cost": 8313,
            "lower_bound": 0,
            "upper_bound": 110
        },
        {
            "from": "139",
            "to": "85",
            "cost": 8365,
            "lower_bound": 0,
            "upper_bound": 221
        },
        {
            "from": "139",
            "to": "195",
            "cost": 6682,
            "lower_bound": 0,
            "upper_bound": 157
        },
        {
            "from": "139",
            "to": "83",
            "cost": 9394,
            "lower_bound": 0,
            "upper_bound": 587
        },
        {
            "from": "139",
            "to": "141",
            "cost": 5293,
            "lower_bound": 0,
            "upper_bound": 452
        },
        {
            "from": "139",
            "to": "34",
            "cost": 7528,
            "lower_bound": 0,
            "upper_bound": 292
        },
        {
            "from": "139",
            "to": "252",
            "cost": 8598,
            "lower_bound": 0,
            "upper_bound": 555
        },
        {
            "from": "143",
            "to": "167",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 372
        },
        {
            "from": "143",
            "to": "255",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 372
        },
        {
            "from": "143",
            "to": "119",
            "cost": 6313,
            "lower_bound": 0,
            "upper_bound": 910
        },
        {
            "from": "143",
            "to": "186",
            "cost": 8844,
            "lower_bound": 0,
            "upper_bound": 173
        },
        {
            "from": "143",
            "to": "202",
            "cost": 320,
            "lower_bound": 0,
            "upper_bound": 629
        },
        {
            "from": "143",
            "to": "34",
            "cost": 6642,
            "lower_bound": 0,
            "upper_bound": 578
        },
        {
            "from": "143",
            "to": "171",
            "cost": 775,
            "lower_bound": 0,
            "upper_bound": 577
        },
        {
            "from": "143",
            "to": "189",
            "cost": 9275,
            "lower_bound": 0,
            "upper_bound": 304
        },
        {
            "from": "143",
            "to": "140",
            "cost": 1398,
            "lower_bound": 0,
            "upper_bound": 212
        },
        {
            "from": "143",
            "to": "131",
            "cost": 7372,
            "lower_bound": 0,
            "upper_bound": 584
        },
        {
            "from": "143",
            "to": "243",
            "cost": 1783,
            "lower_bound": 0,
            "upper_bound": 835
        },
        {
            "from": "143",
            "to": "181",
            "cost": 8770,
            "lower_bound": 0,
            "upper_bound": 928
        },
        {
            "from": "143",
            "to": "177",
            "cost": 2855,
            "lower_bound": 0,
            "upper_bound": 306
        },
        {
            "from": "146",
            "to": "189",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 372
        },
        {
            "from": "146",
            "to": "35",
            "cost": 8860,
            "lower_bound": 0,
            "upper_bound": 742
        },
        {
            "from": "146",
            "to": "129",
            "cost": 8539,
            "lower_bound": 0,
            "upper_bound": 606
        },
        {
            "from": "146",
            "to": "136",
            "cost": 2805,
            "lower_bound": 0,
            "upper_bound": 879
        },
        {
            "from": "146",
            "to": "37",
            "cost": 5928,
            "lower_bound": 0,
            "upper_bound": 164
        },
        {
            "from": "146",
            "to": "199",
            "cost": 9078,
            "lower_bound": 0,
            "upper_bound": 314
        },
        {
            "from": "146",
            "to": "177",
            "cost": 5357,
            "lower_bound": 0,
            "upper_bound": 946
        },
        {
            "from": "152",
            "to": "139",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 372
        },
        {
            "from": "152",
            "to": "217",
            "cost": 3623,
            "lower_bound": 0,
            "upper_bound": 825
        },
        {
            "from": "157",
            "to": "88",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 372
        },
        {
            "from": "157",
            "to": "121",
            "cost": 4893,
            "lower_bound": 0,
            "upper_bound": 602
        },
        {
            "from": "157",
            "to": "238",
            "cost": 7653,
            "lower_bound": 0,
            "upper_bound": 708
        },
        {
            "from": "157",
            "to": "61",
            "cost": 5054,
            "lower_bound": 0,
            "upper_bound": 129
        },
        {
            "from": "157",
            "to": "139",
            "cost": 497,
            "lower_bound": 0,
            "upper_bound": 101
        },
        {
            "from": "157",
            "to": "175",
            "cost": 7705,
            "lower_bound": 0,
            "upper_bound": 497
        },
        {
            "from": "157",
            "to": "163",
            "cost": 1005,
            "lower_bound": 0,
            "upper_bound": 725
        },
        {
            "from": "157",
            "to": "234",
            "cost": 7333,
            "lower_bound": 0,
            "upper_bound": 50
        },
        {
            "from": "157",
            "to": "49",
            "cost": 3419,
            "lower_bound": 0,
            "upper_bound": 403
        },
        {
            "from": "157",
            "to": "239",
            "cost": 6477,
            "lower_bound": 0,
            "upper_bound": 139
        },
        {
            "from": "157",
            "to": "248",
            "cost": 4022,
            "lower_bound": 0,
            "upper_bound": 325
        },
        {
            "from": "167",
            "to": "146",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 372
        },
        {
            "from": "167",
            "to": "54",
            "cost": 8348,
            "lower_bound": 0,
            "upper_bound": 263
        },
        {
            "from": "167",
            "to": "152",
            "cost": 9470,
            "lower_bound": 0,
            "upper_bound": 419
        },
        {
            "from": "167",
            "to": "233",
            "cost": 2332,
            "lower_bound": 0,
            "upper_bound": 509
        },
        {
            "from": "167",
            "to": "165",
            "cost": 7292,
            "lower_bound": 0,
            "upper_bound": 971
        },
        {
            "from": "167",
            "to": "92",
            "cost": 1956,
            "lower_bound": 0,
            "upper_bound": 253
        },
        {
            "from": "167",
            "to": "182",
            "cost": 6954,
            "lower_bound": 0,
            "upper_bound": 397
        },
        {
            "from": "167",
            "to": "218",
            "cost": 5393,
            "lower_bound": 0,
            "upper_bound": 870
        },
        {
            "from": "167",
            "to": "126",
            "cost": 6488,
            "lower_bound": 0,
            "upper_bound": 751
        },
        {
            "from": "167",
            "to": "24",
            "cost": 7985,
            "lower_bound": 0,
            "upper_bound": 327
        },
        {
            "from": "189",
            "to": "199",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 372
        },
        {
            "from": "189",
            "to": "234",
            "cost": 996,
            "lower_bound": 0,
            "upper_bound": 584
        },
        {
            "from": "189",
            "to": "75",
            "cost": 4049,
            "lower_bound": 0,
            "upper_bound": 751
        },
        {
            "from": "189",
            "to": "152",
            "cost": 5017,
            "lower_bound": 0,
            "upper_bound": 312
        },
        {
            "from": "189",
            "to": "235",
            "cost": 9773,
            "lower_bound": 0,
            "upper_bound": 906
        },
        {
            "from": "189",
            "to": "210",
            "cost": 4295,
            "lower_bound": 0,
            "upper_bound": 554
        },
        {
            "from": "189",
            "to": "250",
            "cost": 749,
            "lower_bound": 0,
            "upper_bound": 899
        },
        {
            "from": "189",
            "to": "218",
            "cost": 7878,
            "lower_bound": 0,
            "upper_bound": 973
        },
        {
            "from": "189",
            "to": "219",
            "cost": 3661,
            "lower_bound": 0,
            "upper_bound": 368
        },
        {
            "from": "189",
            "to": "45",
            "cost": 3154,
            "lower_bound": 0,
            "upper_bound": 606
        },
        {
            "from": "189",
            "to": "146",
            "cost": 8404,
            "lower_bound": 0,
            "upper_bound": 997
        },
        {
            "from": "189",
            "to": "221",
            "cost": 8762,
            "lower_bound": 0,
            "upper_bound": 829
        },
        {
            "from": "199",
            "to": "39",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 372
        },
        {
            "from": "199",
            "to": "212",
            "cost": 5508,
            "lower_bound": 0,
            "upper_bound": 464
        },
        {
            "from": "199",
            "to": "143",
            "cost": 4044,
            "lower_bound": 0,
            "upper_bound": 772
        },
        {
            "from": "199",
            "to": "30",
            "cost": 1419,
            "lower_bound": 0,
            "upper_bound": 77
        },
        {
            "from": "199",
            "to": "204",
            "cost": 9704,
            "lower_bound": 0,
            "upper_bound": 318
        },
        {
            "from": "199",
            "to": "146",
            "cost": 4278,
            "lower_bound": 0,
            "upper_bound": 280
        },
        {
            "from": "199",
            "to": "230",
            "cost": 8697,
            "lower_bound": 0,
            "upper_bound": 52
        },
        {
            "from": "199",
            "to": "67",
            "cost": 9019,
            "lower_bound": 0,
            "upper_bound": 16
        },
        {
            "from": "199",
            "to": "216",
            "cost": 2582,
            "lower_bound": 0,
            "upper_bound": 700
        },
        {
            "from": "199",
            "to": "149",
            "cost": 4865,
            "lower_bound": 0,
            "upper_bound": 267
        },
        {
            "from": "10",
            "to": "36",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2273
        },
        {
            "from": "10",
            "to": "58",
            "cost": 2210,
            "lower_bound": 0,
            "upper_bound": 716
        },
        {
            "from": "10",
            "to": "133",
            "cost": 1136,
            "lower_bound": 0,
            "upper_bound": 469
        },
        {
            "from": "10",
            "to": "40",
            "cost": 9766,
            "lower_bound": 0,
            "upper_bound": 621
        },
        {
            "from": "10",
            "to": "183",
            "cost": 8222,
            "lower_bound": 0,
            "upper_bound": 501
        },
        {
            "from": "10",
            "to": "143",
            "cost": 3104,
            "lower_bound": 0,
            "upper_bound": 522
        },
        {
            "from": "10",
            "to": "196",
            "cost": 3741,
            "lower_bound": 0,
            "upper_bound": 69
        },
        {
            "from": "10",
            "to": "48",
            "cost": 662,
            "lower_bound": 0,
            "upper_bound": 703
        },
        {
            "from": "10",
            "to": "57",
            "cost": 3251,
            "lower_bound": 0,
            "upper_bound": 986
        },
        {
            "from": "33",
            "to": "135",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2273
        },
        {
            "from": "33",
            "to": "219",
            "cost": 6931,
            "lower_bound": 0,
            "upper_bound": 264
        },
        {
            "from": "33",
            "to": "214",
            "cost": 5780,
            "lower_bound": 0,
            "upper_bound": 171
        },
        {
            "from": "33",
            "to": "153",
            "cost": 3899,
            "lower_bound": 0,
            "upper_bound": 430
        },
        {
            "from": "33",
            "to": "250",
            "cost": 7981,
            "lower_bound": 0,
            "upper_bound": 348
        },
        {
            "from": "33",
            "to": "34",
            "cost": 8302,
            "lower_bound": 0,
            "upper_bound": 269
        },
        {
            "from": "33",
            "to": "217",
            "cost": 296,
            "lower_bound": 0,
            "upper_bound": 972
        },
        {
            "from": "33",
            "to": "75",
            "cost": 2450,
            "lower_bound": 0,
            "upper_bound": 503
        },
        {
            "from": "33",
            "to": "72",
            "cost": 152,
            "lower_bound": 0,
            "upper_bound": 237
        },
        {
            "from": "33",
            "to": "149",
            "cost": 3641,
            "lower_bound": 0,
            "upper_bound": 382
        },
        {
            "from": "33",
            "to": "208",
            "cost": 9863,
            "lower_bound": 0,
            "upper_bound": 77
        },
        {
            "from": "33",
            "to": "160",
            "cost": 6320,
            "lower_bound": 0,
            "upper_bound": 55
        },
        {
            "from": "33",
            "to": "55",
            "cost": 1668,
            "lower_bound": 0,
            "upper_bound": 145
        },
        {
            "from": "36",
            "to": "64",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2273
        },
        {
            "from": "36",
            "to": "30",
            "cost": 9509,
            "lower_bound": 0,
            "upper_bound": 864
        },
        {
            "from": "36",
            "to": "56",
            "cost": 9251,
            "lower_bound": 0,
            "upper_bound": 570
        },
        {
            "from": "36",
            "to": "167",
            "cost": 9232,
            "lower_bound": 0,
            "upper_bound": 485
        },
        {
            "from": "36",
            "to": "91",
            "cost": 3504,
            "lower_bound": 0,
            "upper_bound": 589
        },
        {
            "from": "36",
            "to": "130",
            "cost": 5507,
            "lower_bound": 0,
            "upper_bound": 972
        },
        {
            "from": "36",
            "to": "49",
            "cost": 863,
            "lower_bound": 0,
            "upper_bound": 888
        },
        {
            "from": "36",
            "to": "202",
            "cost": 7855,
            "lower_bound": 0,
            "upper_bound": 568
        },
        {
            "from": "36",
            "to": "139",
            "cost": 6505,
            "lower_bound": 0,
            "upper_bound": 469
        },
        {
            "from": "64",
            "to": "233",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2273
        },
        {
            "from": "64",
            "to": "83",
            "cost": 5802,
            "lower_bound": 0,
            "upper_bound": 762
        },
        {
            "from": "64",
            "to": "107",
            "cost": 2909,
            "lower_bound": 0,
            "upper_bound": 962
        },
        {
            "from": "64",
            "to": "74",
            "cost": 662,
            "lower_bound": 0,
            "upper_bound": 343
        },
        {
            "from": "64",
            "to": "152",
            "cost": 3614,
            "lower_bound": 0,
            "upper_bound": 450
        },
        {
            "from": "64",
            "to": "141",
            "cost": 256,
            "lower_bound": 0,
            "upper_bound": 543
        },
        {
            "from": "64",
            "to": "170",
            "cost": 9670,
            "lower_bound": 0,
            "upper_bound": 412
        },
        {
            "from": "64",
            "to": "158",
            "cost": 6909,
            "lower_bound": 0,
            "upper_bound": 681
        },
        {
            "from": "64",
            "to": "175",
            "cost": 1954,
            "lower_bound": 0,
            "upper_bound": 987
        },
        {
            "from": "64",
            "to": "67",
            "cost": 4704,
            "lower_bound": 0,
            "upper_bound": 186
        },
        {
            "from": "64",
            "to": "70",
            "cost": 568,
            "lower_bound": 0,
            "upper_bound": 134
        },
        {
            "from": "64",
            "to": "191",
            "cost": 8446,
            "lower_bound": 0,
            "upper_bound": 672
        },
        {
            "from": "64",
            "to": "89",
            "cost": 2046,
            "lower_bound": 0,
            "upper_bound": 816
        },
        {
            "from": "64",
            "to": "63",
            "cost": 1160,
            "lower_bound": 0,
            "upper_bound": 53
        },
        {
            "from": "94",
            "to": "119",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2273
        },
        {
            "from": "94",
            "to": "82",
            "cost": 8863,
            "lower_bound": 0,
            "upper_bound": 980
        },
        {
            "from": "94",
            "to": "56",
            "cost": 5749,
            "lower_bound": 0,
            "upper_bound": 649
        },
        {
            "from": "94",
            "to": "177",
            "cost": 5244,
            "lower_bound": 0,
            "upper_bound": 529
        },
        {
            "from": "94",
            "to": "99",
            "cost": 6469,
            "lower_bound": 0,
            "upper_bound": 597
        },
        {
            "from": "94",
            "to": "40",
            "cost": 9423,
            "lower_bound": 0,
            "upper_bound": 539
        },
        {
            "from": "94",
            "to": "212",
            "cost": 8971,
            "lower_bound": 0,
            "upper_bound": 434
        },
        {
            "from": "94",
            "to": "244",
            "cost": 4973,
            "lower_bound": 0,
            "upper_bound": 831
        },
        {
            "from": "94",
            "to": "234",
            "cost": 3609,
            "lower_bound": 0,
            "upper_bound": 732
        },
        {
            "from": "94",
            "to": "194",
            "cost": 3972,
            "lower_bound": 0,
            "upper_bound": 797
        },
        {
            "from": "94",
            "to": "248",
            "cost": 2640,
            "lower_bound": 0,
            "upper_bound": 864
        },
        {
            "from": "103",
            "to": "250",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2273
        },
        {
            "from": "103",
            "to": "132",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2273
        },
        {
            "from": "103",
            "to": "62",
            "cost": 8970,
            "lower_bound": 0,
            "upper_bound": 499
        },
        {
            "from": "103",
            "to": "136",
            "cost": 298,
            "lower_bound": 0,
            "upper_bound": 966
        },
        {
            "from": "103",
            "to": "101",
            "cost": 6595,
            "lower_bound": 0,
            "upper_bound": 712
        },
        {
            "from": "103",
            "to": "198",
            "cost": 4564,
            "lower_bound": 0,
            "upper_bound": 707
        },
        {
            "from": "103",
            "to": "169",
            "cost": 8681,
            "lower_bound": 0,
            "upper_bound": 286
        },
        {
            "from": "103",
            "to": "207",
            "cost": 515,
            "lower_bound": 0,
            "upper_bound": 652
        },
        {
            "from": "103",
            "to": "243",
            "cost": 6011,
            "lower_bound": 0,
            "upper_bound": 479
        },
        {
            "from": "119",
            "to": "33",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2273
        },
        {
            "from": "119",
            "to": "223",
            "cost": 5181,
            "lower_bound": 0,
            "upper_bound": 871
        },
        {
            "from": "119",
            "to": "123",
            "cost": 1903,
            "lower_bound": 0,
            "upper_bound": 175
        },
        {
            "from": "119",
            "to": "84",
            "cost": 1944,
            "lower_bound": 0,
            "upper_bound": 716
        },
        {
            "from": "119",
            "to": "154",
            "cost": 7217,
            "lower_bound": 0,
            "upper_bound": 549
        },
        {
            "from": "119",
            "to": "20",
            "cost": 542,
            "lower_bound": 0,
            "upper_bound": 268
        },
        {
            "from": "119",
            "to": "222",
            "cost": 5282,
            "lower_bound": 0,
            "upper_bound": 872
        },
        {
            "from": "119",
            "to": "57",
            "cost": 2331,
            "lower_bound": 0,
            "upper_bound": 760
        },
        {
            "from": "132",
            "to": "206",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2273
        },
        {
            "from": "132",
            "to": "101",
            "cost": 239,
            "lower_bound": 0,
            "upper_bound": 501
        },
        {
            "from": "132",
            "to": "26",
            "cost": 3026,
            "lower_bound": 0,
            "upper_bound": 27
        },
        {
            "from": "132",
            "to": "226",
            "cost": 4003,
            "lower_bound": 0,
            "upper_bound": 192
        },
        {
            "from": "132",
            "to": "234",
            "cost": 9653,
            "lower_bound": 0,
            "upper_bound": 16
        },
        {
            "from": "132",
            "to": "168",
            "cost": 1440,
            "lower_bound": 0,
            "upper_bound": 1000
        },
        {
            "from": "132",
            "to": "106",
            "cost": 7726,
            "lower_bound": 0,
            "upper_bound": 161
        },
        {
            "from": "132",
            "to": "204",
            "cost": 8553,
            "lower_bound": 0,
            "upper_bound": 804
        },
        {
            "from": "132",
            "to": "161",
            "cost": 1361,
            "lower_bound": 0,
            "upper_bound": 579
        },
        {
            "from": "132",
            "to": "237",
            "cost": 6569,
            "lower_bound": 0,
            "upper_bound": 709
        },
        {
            "from": "132",
            "to": "97",
            "cost": 5063,
            "lower_bound": 0,
            "upper_bound": 428
        },
        {
            "from": "132",
            "to": "49",
            "cost": 3581,
            "lower_bound": 0,
            "upper_bound": 402
        },
        {
            "from": "135",
            "to": "203",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2273
        },
        {
            "from": "135",
            "to": "146",
            "cost": 1419,
            "lower_bound": 0,
            "upper_bound": 485
        },
        {
            "from": "203",
            "to": "103",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2273
        },
        {
            "from": "203",
            "to": "212",
            "cost": 6846,
            "lower_bound": 0,
            "upper_bound": 772
        },
        {
            "from": "203",
            "to": "201",
            "cost": 1010,
            "lower_bound": 0,
            "upper_bound": 290
        },
        {
            "from": "203",
            "to": "119",
            "cost": 5588,
            "lower_bound": 0,
            "upper_bound": 902
        },
        {
            "from": "203",
            "to": "120",
            "cost": 8617,
            "lower_bound": 0,
            "upper_bound": 251
        },
        {
            "from": "203",
            "to": "228",
            "cost": 4792,
            "lower_bound": 0,
            "upper_bound": 517
        },
        {
            "from": "203",
            "to": "163",
            "cost": 7725,
            "lower_bound": 0,
            "upper_bound": 548
        },
        {
            "from": "203",
            "to": "24",
            "cost": 5086,
            "lower_bound": 0,
            "upper_bound": 52
        },
        {
            "from": "206",
            "to": "244",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2273
        },
        {
            "from": "206",
            "to": "226",
            "cost": 1681,
            "lower_bound": 0,
            "upper_bound": 835
        },
        {
            "from": "206",
            "to": "98",
            "cost": 5190,
            "lower_bound": 0,
            "upper_bound": 936
        },
        {
            "from": "206",
            "to": "251",
            "cost": 7776,
            "lower_bound": 0,
            "upper_bound": 707
        },
        {
            "from": "206",
            "to": "143",
            "cost": 8411,
            "lower_bound": 0,
            "upper_bound": 880
        },
        {
            "from": "206",
            "to": "58",
            "cost": 9285,
            "lower_bound": 0,
            "upper_bound": 485
        },
        {
            "from": "206",
            "to": "248",
            "cost": 8605,
            "lower_bound": 0,
            "upper_bound": 193
        },
        {
            "from": "206",
            "to": "103",
            "cost": 2970,
            "lower_bound": 0,
            "upper_bound": 51
        },
        {
            "from": "206",
            "to": "51",
            "cost": 7736,
            "lower_bound": 0,
            "upper_bound": 656
        },
        {
            "from": "233",
            "to": "94",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2273
        },
        {
            "from": "233",
            "to": "143",
            "cost": 8504,
            "lower_bound": 0,
            "upper_bound": 232
        },
        {
            "from": "233",
            "to": "61",
            "cost": 3432,
            "lower_bound": 0,
            "upper_bound": 416
        },
        {
            "from": "233",
            "to": "186",
            "cost": 5871,
            "lower_bound": 0,
            "upper_bound": 595
        },
        {
            "from": "11",
            "to": "99",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 92
        },
        {
            "from": "11",
            "to": "232",
            "cost": 7362,
            "lower_bound": 0,
            "upper_bound": 18
        },
        {
            "from": "11",
            "to": "243",
            "cost": 9471,
            "lower_bound": 0,
            "upper_bound": 983
        },
        {
            "from": "11",
            "to": "255",
            "cost": 3427,
            "lower_bound": 0,
            "upper_bound": 320
        },
        {
            "from": "11",
            "to": "44",
            "cost": 8376,
            "lower_bound": 0,
            "upper_bound": 514
        },
        {
            "from": "17",
            "to": "162",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 92
        },
        {
            "from": "17",
            "to": "33",
            "cost": 1445,
            "lower_bound": 0,
            "upper_bound": 912
        },
        {
            "from": "17",
            "to": "133",
            "cost": 8423,
            "lower_bound": 0,
            "upper_bound": 976
        },
        {
            "from": "17",
            "to": "99",
            "cost": 4432,
            "lower_bound": 0,
            "upper_bound": 101
        },
        {
            "from": "17",
            "to": "38",
            "cost": 6925,
            "lower_bound": 0,
            "upper_bound": 815
        },
        {
            "from": "17",
            "to": "155",
            "cost": 7092,
            "lower_bound": 0,
            "upper_bound": 498
        },
        {
            "from": "17",
            "to": "53",
            "cost": 9974,
            "lower_bound": 0,
            "upper_bound": 378
        },
        {
            "from": "17",
            "to": "187",
            "cost": 1766,
            "lower_bound": 0,
            "upper_bound": 363
        },
        {
            "from": "17",
            "to": "208",
            "cost": 1482,
            "lower_bound": 0,
            "upper_bound": 660
        },
        {
            "from": "17",
            "to": "138",
            "cost": 5066,
            "lower_bound": 0,
            "upper_bound": 380
        },
        {
            "from": "17",
            "to": "175",
            "cost": 7943,
            "lower_bound": 0,
            "upper_bound": 462
        },
        {
            "from": "17",
            "to": "64",
            "cost": 3583,
            "lower_bound": 0,
            "upper_bound": 372
        },
        {
            "from": "17",
            "to": "69",
            "cost": 5606,
            "lower_bound": 0,
            "upper_bound": 201
        },
        {
            "from": "17",
            "to": "202",
            "cost": 4284,
            "lower_bound": 0,
            "upper_bound": 133
        },
        {
            "from": "17",
            "to": "25",
            "cost": 4326,
            "lower_bound": 0,
            "upper_bound": 646
        },
        {
            "from": "59",
            "to": "251",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 92
        },
        {
            "from": "59",
            "to": "61",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 92
        },
        {
            "from": "59",
            "to": "238",
            "cost": 9181,
            "lower_bound": 0,
            "upper_bound": 712
        },
        {
            "from": "59",
            "to": "46",
            "cost": 9876,
            "lower_bound": 0,
            "upper_bound": 845
        },
        {
            "from": "59",
            "to": "250",
            "cost": 5706,
            "lower_bound": 0,
            "upper_bound": 327
        },
        {
            "from": "59",
            "to": "173",
            "cost": 789,
            "lower_bound": 0,
            "upper_bound": 449
        },
        {
            "from": "59",
            "to": "144",
            "cost": 7910,
            "lower_bound": 0,
            "upper_bound": 844
        },
        {
            "from": "59",
            "to": "199",
            "cost": 3483,
            "lower_bound": 0,
            "upper_bound": 451
        },
        {
            "from": "59",
            "to": "105",
            "cost": 5586,
            "lower_bound": 0,
            "upper_bound": 294
        },
        {
            "from": "59",
            "to": "27",
            "cost": 981,
            "lower_bound": 0,
            "upper_bound": 328
        },
        {
            "from": "59",
            "to": "73",
            "cost": 4783,
            "lower_bound": 0,
            "upper_bound": 588
        },
        {
            "from": "59",
            "to": "44",
            "cost": 4984,
            "lower_bound": 0,
            "upper_bound": 246
        },
        {
            "from": "59",
            "to": "200",
            "cost": 7444,
            "lower_bound": 0,
            "upper_bound": 594
        },
        {
            "from": "59",
            "to": "192",
            "cost": 6441,
            "lower_bound": 0,
            "upper_bound": 637
        },
        {
            "from": "59",
            "to": "70",
            "cost": 6690,
            "lower_bound": 0,
            "upper_bound": 201
        },
        {
            "from": "61",
            "to": "144",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 92
        },
        {
            "from": "61",
            "to": "27",
            "cost": 5206,
            "lower_bound": 0,
            "upper_bound": 161
        },
        {
            "from": "61",
            "to": "255",
            "cost": 2517,
            "lower_bound": 0,
            "upper_bound": 689
        },
        {
            "from": "61",
            "to": "164",
            "cost": 4165,
            "lower_bound": 0,
            "upper_bound": 536
        },
        {
            "from": "99",
            "to": "187",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 92
        },
        {
            "from": "99",
            "to": "165",
            "cost": 2363,
            "lower_bound": 0,
            "upper_bound": 752
        },
        {
            "from": "99",
            "to": "107",
            "cost": 7605,
            "lower_bound": 0,
            "upper_bound": 970
        },
        {
            "from": "99",
            "to": "171",
            "cost": 8298,
            "lower_bound": 0,
            "upper_bound": 828
        },
        {
            "from": "99",
            "to": "32",
            "cost": 9705,
            "lower_bound": 0,
            "upper_bound": 632
        },
        {
            "from": "99",
            "to": "184",
            "cost": 9559,
            "lower_bound": 0,
            "upper_bound": 774
        },
        {
            "from": "99",
            "to": "251",
            "cost": 8020,
            "lower_bound": 0,
            "upper_bound": 664
        },
        {
            "from": "99",
            "to": "98",
            "cost": 9790,
            "lower_bound": 0,
            "upper_bound": 725
        },
        {
            "from": "99",
            "to": "248",
            "cost": 768,
            "lower_bound": 0,
            "upper_bound": 692
        },
        {
            "from": "99",
            "to": "207",
            "cost": 7407,
            "lower_bound": 0,
            "upper_bound": 529
        },
        {
            "from": "99",
            "to": "198",
            "cost": 628,
            "lower_bound": 0,
            "upper_bound": 527
        },
        {
            "from": "99",
            "to": "229",
            "cost": 8430,
            "lower_bound": 0,
            "upper_bound": 308
        },
        {
            "from": "99",
            "to": "218",
            "cost": 8478,
            "lower_bound": 0,
            "upper_bound": 511
        },
        {
            "from": "99",
            "to": "80",
            "cost": 8006,
            "lower_bound": 0,
            "upper_bound": 964
        },
        {
            "from": "128",
            "to": "17",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 92
        },
        {
            "from": "128",
            "to": "154",
            "cost": 6688,
            "lower_bound": 0,
            "upper_bound": 989
        },
        {
            "from": "128",
            "to": "227",
            "cost": 5755,
            "lower_bound": 0,
            "upper_bound": 238
        },
        {
            "from": "128",
            "to": "124",
            "cost": 2226,
            "lower_bound": 0,
            "upper_bound": 980
        },
        {
            "from": "128",
            "to": "114",
            "cost": 3028,
            "lower_bound": 0,
            "upper_bound": 252
        },
        {
            "from": "128",
            "to": "245",
            "cost": 251,
            "lower_bound": 0,
            "upper_bound": 586
        },
        {
            "from": "128",
            "to": "204",
            "cost": 7322,
            "lower_bound": 0,
            "upper_bound": 775
        },
        {
            "from": "128",
            "to": "53",
            "cost": 6650,
            "lower_bound": 0,
            "upper_bound": 77
        },
        {
            "from": "144",
            "to": "207",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 92
        },
        {
            "from": "144",
            "to": "226",
            "cost": 4941,
            "lower_bound": 0,
            "upper_bound": 608
        },
        {
            "from": "159",
            "to": "240",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 92
        },
        {
            "from": "159",
            "to": "67",
            "cost": 3616,
            "lower_bound": 0,
            "upper_bound": 585
        },
        {
            "from": "159",
            "to": "53",
            "cost": 2572,
            "lower_bound": 0,
            "upper_bound": 598
        },
        {
            "from": "159",
            "to": "223",
            "cost": 7576,
            "lower_bound": 0,
            "upper_bound": 348
        },
        {
            "from": "159",
            "to": "108",
            "cost": 2794,
            "lower_bound": 0,
            "upper_bound": 508
        },
        {
            "from": "159",
            "to": "253",
            "cost": 8101,
            "lower_bound": 0,
            "upper_bound": 541
        },
        {
            "from": "159",
            "to": "251",
            "cost": 8739,
            "lower_bound": 0,
            "upper_bound": 114
        },
        {
            "from": "162",
            "to": "159",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 92
        },
        {
            "from": "162",
            "to": "78",
            "cost": 5306,
            "lower_bound": 0,
            "upper_bound": 309
        },
        {
            "from": "162",
            "to": "197",
            "cost": 242,
            "lower_bound": 0,
            "upper_bound": 590
        },
        {
            "from": "162",
            "to": "129",
            "cost": 6745,
            "lower_bound": 0,
            "upper_bound": 79
        },
        {
            "from": "162",
            "to": "170",
            "cost": 7670,
            "lower_bound": 0,
            "upper_bound": 409
        },
        {
            "from": "162",
            "to": "17",
            "cost": 1360,
            "lower_bound": 0,
            "upper_bound": 351
        },
        {
            "from": "162",
            "to": "211",
            "cost": 8944,
            "lower_bound": 0,
            "upper_bound": 391
        },
        {
            "from": "162",
            "to": "80",
            "cost": 891,
            "lower_bound": 0,
            "upper_bound": 567
        },
        {
            "from": "162",
            "to": "131",
            "cost": 7251,
            "lower_bound": 0,
            "upper_bound": 348
        },
        {
            "from": "169",
            "to": "59",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 92
        },
        {
            "from": "169",
            "to": "93",
            "cost": 8940,
            "lower_bound": 0,
            "upper_bound": 254
        },
        {
            "from": "187",
            "to": "128",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 92
        },
        {
            "from": "187",
            "to": "192",
            "cost": 558,
            "lower_bound": 0,
            "upper_bound": 34
        },
        {
            "from": "207",
            "to": "214",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 92
        },
        {
            "from": "207",
            "to": "190",
            "cost": 4048,
            "lower_bound": 0,
            "upper_bound": 376
        },
        {
            "from": "207",
            "to": "131",
            "cost": 6399,
            "lower_bound": 0,
            "upper_bound": 43
        },
        {
            "from": "207",
            "to": "79",
            "cost": 7171,
            "lower_bound": 0,
            "upper_bound": 694
        },
        {
            "from": "207",
            "to": "150",
            "cost": 9014,
            "lower_bound": 0,
            "upper_bound": 27
        },
        {
            "from": "207",
            "to": "204",
            "cost": 608,
            "lower_bound": 0,
            "upper_bound": 112
        },
        {
            "from": "207",
            "to": "247",
            "cost": 7084,
            "lower_bound": 0,
            "upper_bound": 38
        },
        {
            "from": "207",
            "to": "180",
            "cost": 542,
            "lower_bound": 0,
            "upper_bound": 341
        },
        {
            "from": "207",
            "to": "42",
            "cost": 8173,
            "lower_bound": 0,
            "upper_bound": 260
        },
        {
            "from": "207",
            "to": "89",
            "cost": 335,
            "lower_bound": 0,
            "upper_bound": 921
        },
        {
            "from": "207",
            "to": "205",
            "cost": 9163,
            "lower_bound": 0,
            "upper_bound": 843
        },
        {
            "from": "207",
            "to": "82",
            "cost": 5381,
            "lower_bound": 0,
            "upper_bound": 696
        },
        {
            "from": "207",
            "to": "215",
            "cost": 4520,
            "lower_bound": 0,
            "upper_bound": 769
        },
        {
            "from": "207",
            "to": "65",
            "cost": 8813,
            "lower_bound": 0,
            "upper_bound": 888
        },
        {
            "from": "207",
            "to": "35",
            "cost": 8960,
            "lower_bound": 0,
            "upper_bound": 424
        },
        {
            "from": "214",
            "to": "242",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 92
        },
        {
            "from": "214",
            "to": "74",
            "cost": 3974,
            "lower_bound": 0,
            "upper_bound": 699
        },
        {
            "from": "214",
            "to": "141",
            "cost": 3389,
            "lower_bound": 0,
            "upper_bound": 183
        },
        {
            "from": "214",
            "to": "64",
            "cost": 2871,
            "lower_bound": 0,
            "upper_bound": 522
        },
        {
            "from": "214",
            "to": "169",
            "cost": 5608,
            "lower_bound": 0,
            "upper_bound": 63
        },
        {
            "from": "214",
            "to": "134",
            "cost": 2133,
            "lower_bound": 0,
            "upper_bound": 931
        },
        {
            "from": "214",
            "to": "50",
            "cost": 5936,
            "lower_bound": 0,
            "upper_bound": 506
        },
        {
            "from": "214",
            "to": "79",
            "cost": 1376,
            "lower_bound": 0,
            "upper_bound": 450
        },
        {
            "from": "240",
            "to": "169",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 92
        },
        {
            "from": "240",
            "to": "120",
            "cost": 7935,
            "lower_bound": 0,
            "upper_bound": 888
        },
        {
            "from": "240",
            "to": "200",
            "cost": 9531,
            "lower_bound": 0,
            "upper_bound": 897
        },
        {
            "from": "240",
            "to": "29",
            "cost": 4111,
            "lower_bound": 0,
            "upper_bound": 427
        },
        {
            "from": "240",
            "to": "137",
            "cost": 8194,
            "lower_bound": 0,
            "upper_bound": 169
        },
        {
            "from": "240",
            "to": "149",
            "cost": 7432,
            "lower_bound": 0,
            "upper_bound": 252
        },
        {
            "from": "240",
            "to": "177",
            "cost": 1895,
            "lower_bound": 0,
            "upper_bound": 506
        },
        {
            "from": "12",
            "to": "140",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 590
        },
        {
            "from": "12",
            "to": "234",
            "cost": 6458,
            "lower_bound": 0,
            "upper_bound": 714
        },
        {
            "from": "12",
            "to": "31",
            "cost": 7346,
            "lower_bound": 0,
            "upper_bound": 583
        },
        {
            "from": "60",
            "to": "184",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 590
        },
        {
            "from": "60",
            "to": "209",
            "cost": 689,
            "lower_bound": 0,
            "upper_bound": 198
        },
        {
            "from": "60",
            "to": "159",
            "cost": 8429,
            "lower_bound": 0,
            "upper_bound": 398
        },
        {
            "from": "60",
            "to": "224",
            "cost": 27,
            "lower_bound": 0,
            "upper_bound": 848
        },
        {
            "from": "60",
            "to": "198",
            "cost": 3401,
            "lower_bound": 0,
            "upper_bound": 141
        },
        {
            "from": "60",
            "to": "74",
            "cost": 1703,
            "lower_bound": 0,
            "upper_bound": 113
        },
        {
            "from": "60",
            "to": "222",
            "cost": 5064,
            "lower_bound": 0,
            "upper_bound": 15
        },
        {
            "from": "60",
            "to": "241",
            "cost": 7775,
            "lower_bound": 0,
            "upper_bound": 535
        },
        {
            "from": "60",
            "to": "105",
            "cost": 3157,
            "lower_bound": 0,
            "upper_bound": 750
        },
        {
            "from": "60",
            "to": "51",
            "cost": 273,
            "lower_bound": 0,
            "upper_bound": 643
        },
        {
            "from": "60",
            "to": "240",
            "cost": 7666,
            "lower_bound": 0,
            "upper_bound": 748
        },
        {
            "from": "60",
            "to": "191",
            "cost": 703,
            "lower_bound": 0,
            "upper_bound": 494
        },
        {
            "from": "60",
            "to": "221",
            "cost": 8702,
            "lower_bound": 0,
            "upper_bound": 721
        },
        {
            "from": "60",
            "to": "107",
            "cost": 9740,
            "lower_bound": 0,
            "upper_bound": 486
        },
        {
            "from": "105",
            "to": "126",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 590
        },
        {
            "from": "105",
            "to": "219",
            "cost": 6745,
            "lower_bound": 0,
            "upper_bound": 969
        },
        {
            "from": "105",
            "to": "43",
            "cost": 87,
            "lower_bound": 0,
            "upper_bound": 954
        },
        {
            "from": "105",
            "to": "151",
            "cost": 9696,
            "lower_bound": 0,
            "upper_bound": 925
        },
        {
            "from": "105",
            "to": "25",
            "cost": 5699,
            "lower_bound": 0,
            "upper_bound": 260
        },
        {
            "from": "105",
            "to": "252",
            "cost": 6062,
            "lower_bound": 0,
            "upper_bound": 717
        },
        {
            "from": "105",
            "to": "147",
            "cost": 4354,
            "lower_bound": 0,
            "upper_bound": 591
        },
        {
            "from": "105",
            "to": "205",
            "cost": 1904,
            "lower_bound": 0,
            "upper_bound": 280
        },
        {
            "from": "105",
            "to": "121",
            "cost": 3117,
            "lower_bound": 0,
            "upper_bound": 29
        },
        {
            "from": "105",
            "to": "251",
            "cost": 2060,
            "lower_bound": 0,
            "upper_bound": 68
        },
        {
            "from": "126",
            "to": "127",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 590
        },
        {
            "from": "126",
            "to": "82",
            "cost": 1781,
            "lower_bound": 0,
            "upper_bound": 672
        },
        {
            "from": "126",
            "to": "140",
            "cost": 8177,
            "lower_bound": 0,
            "upper_bound": 248
        },
        {
            "from": "126",
            "to": "155",
            "cost": 2277,
            "lower_bound": 0,
            "upper_bound": 375
        },
        {
            "from": "126",
            "to": "57",
            "cost": 2381,
            "lower_bound": 0,
            "upper_bound": 560
        },
        {
            "from": "126",
            "to": "41",
            "cost": 7575,
            "lower_bound": 0,
            "upper_bound": 422
        },
        {
            "from": "126",
            "to": "132",
            "cost": 5816,
            "lower_bound": 0,
            "upper_bound": 338
        },
        {
            "from": "126",
            "to": "109",
            "cost": 4699,
            "lower_bound": 0,
            "upper_bound": 717
        },
        {
            "from": "126",
            "to": "81",
            "cost": 7644,
            "lower_bound": 0,
            "upper_bound": 993
        },
        {
            "from": "126",
            "to": "160",
            "cost": 9137,
            "lower_bound": 0,
            "upper_bound": 966
        },
        {
            "from": "126",
            "to": "94",
            "cost": 6268,
            "lower_bound": 0,
            "upper_bound": 452
        },
        {
            "from": "126",
            "to": "148",
            "cost": 4557,
            "lower_bound": 0,
            "upper_bound": 436
        },
        {
            "from": "126",
            "to": "252",
            "cost": 6626,
            "lower_bound": 0,
            "upper_bound": 762
        },
        {
            "from": "126",
            "to": "120",
            "cost": 1692,
            "lower_bound": 0,
            "upper_bound": 571
        },
        {
            "from": "126",
            "to": "73",
            "cost": 7037,
            "lower_bound": 0,
            "upper_bound": 931
        },
        {
            "from": "127",
            "to": "227",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 590
        },
        {
            "from": "127",
            "to": "241",
            "cost": 4657,
            "lower_bound": 0,
            "upper_bound": 995
        },
        {
            "from": "127",
            "to": "107",
            "cost": 736,
            "lower_bound": 0,
            "upper_bound": 834
        },
        {
            "from": "140",
            "to": "241",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 590
        },
        {
            "from": "140",
            "to": "200",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 590
        },
        {
            "from": "140",
            "to": "131",
            "cost": 3253,
            "lower_bound": 0,
            "upper_bound": 795
        },
        {
            "from": "140",
            "to": "35",
            "cost": 5902,
            "lower_bound": 0,
            "upper_bound": 48
        },
        {
            "from": "140",
            "to": "85",
            "cost": 1988,
            "lower_bound": 0,
            "upper_bound": 158
        },
        {
            "from": "140",
            "to": "18",
            "cost": 9972,
            "lower_bound": 0,
            "upper_bound": 620
        },
        {
            "from": "140",
            "to": "133",
            "cost": 6935,
            "lower_bound": 0,
            "upper_bound": 643
        },
        {
            "from": "140",
            "to": "123",
            "cost": 4924,
            "lower_bound": 0,
            "upper_bound": 526
        },
        {
            "from": "184",
            "to": "211",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 590
        },
        {
            "from": "184",
            "to": "253",
            "cost": 4329,
            "lower_bound": 0,
            "upper_bound": 23
        },
        {
            "from": "184",
            "to": "106",
            "cost": 1123,
            "lower_bound": 0,
            "upper_bound": 112
        },
        {
            "from": "184",
            "to": "179",
            "cost": 8607,
            "lower_bound": 0,
            "upper_bound": 723
        },
        {
            "from": "184",
            "to": "152",
            "cost": 8930,
            "lower_bound": 0,
            "upper_bound": 662
        },
        {
            "from": "200",
            "to": "105",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 590
        },
        {
            "from": "200",
            "to": "138",
            "cost": 1444,
            "lower_bound": 0,
            "upper_bound": 688
        },
        {
            "from": "200",
            "to": "17",
            "cost": 817,
            "lower_bound": 0,
            "upper_bound": 592
        },
        {
            "from": "200",
            "to": "238",
            "cost": 4239,
            "lower_bound": 0,
            "upper_bound": 41
        },
        {
            "from": "200",
            "to": "48",
            "cost": 7823,
            "lower_bound": 0,
            "upper_bound": 113
        },
        {
            "from": "200",
            "to": "61",
            "cost": 2616,
            "lower_bound": 0,
            "upper_bound": 94
        },
        {
            "from": "200",
            "to": "94",
            "cost": 348,
            "lower_bound": 0,
            "upper_bound": 913
        },
        {
            "from": "200",
            "to": "204",
            "cost": 6830,
            "lower_bound": 0,
            "upper_bound": 219
        },
        {
            "from": "200",
            "to": "212",
            "cost": 9997,
            "lower_bound": 0,
            "upper_bound": 614
        },
        {
            "from": "200",
            "to": "125",
            "cost": 6327,
            "lower_bound": 0,
            "upper_bound": 638
        },
        {
            "from": "200",
            "to": "175",
            "cost": 3443,
            "lower_bound": 0,
            "upper_bound": 25
        },
        {
            "from": "200",
            "to": "211",
            "cost": 9819,
            "lower_bound": 0,
            "upper_bound": 259
        },
        {
            "from": "200",
            "to": "184",
            "cost": 3652,
            "lower_bound": 0,
            "upper_bound": 937
        },
        {
            "from": "200",
            "to": "118",
            "cost": 6333,
            "lower_bound": 0,
            "upper_bound": 35
        },
        {
            "from": "211",
            "to": "250",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 590
        },
        {
            "from": "211",
            "to": "177",
            "cost": 2140,
            "lower_bound": 0,
            "upper_bound": 757
        },
        {
            "from": "211",
            "to": "78",
            "cost": 5779,
            "lower_bound": 0,
            "upper_bound": 393
        },
        {
            "from": "211",
            "to": "251",
            "cost": 1682,
            "lower_bound": 0,
            "upper_bound": 6
        },
        {
            "from": "211",
            "to": "88",
            "cost": 2830,
            "lower_bound": 0,
            "upper_bound": 900
        },
        {
            "from": "211",
            "to": "238",
            "cost": 8472,
            "lower_bound": 0,
            "upper_bound": 38
        },
        {
            "from": "211",
            "to": "249",
            "cost": 8108,
            "lower_bound": 0,
            "upper_bound": 368
        },
        {
            "from": "227",
            "to": "60",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 590
        },
        {
            "from": "227",
            "to": "155",
            "cost": 8512,
            "lower_bound": 0,
            "upper_bound": 958
        },
        {
            "from": "227",
            "to": "33",
            "cost": 5329,
            "lower_bound": 0,
            "upper_bound": 745
        },
        {
            "from": "227",
            "to": "45",
            "cost": 7463,
            "lower_bound": 0,
            "upper_bound": 7
        },
        {
            "from": "227",
            "to": "54",
            "cost": 316,
            "lower_bound": 0,
            "upper_bound": 15
        },
        {
            "from": "227",
            "to": "77",
            "cost": 3329,
            "lower_bound": 0,
            "upper_bound": 127
        },
        {
            "from": "227",
            "to": "104",
            "cost": 9449,
            "lower_bound": 0,
            "upper_bound": 392
        },
        {
            "from": "227",
            "to": "206",
            "cost": 4414,
            "lower_bound": 0,
            "upper_bound": 275
        },
        {
            "from": "227",
            "to": "71",
            "cost": 5409,
            "lower_bound": 0,
            "upper_bound": 113
        },
        {
            "from": "13",
            "to": "218",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 503
        },
        {
            "from": "13",
            "to": "52",
            "cost": 6208,
            "lower_bound": 0,
            "upper_bound": 873
        },
        {
            "from": "13",
            "to": "110",
            "cost": 8429,
            "lower_bound": 0,
            "upper_bound": 900
        },
        {
            "from": "20",
            "to": "82",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 503
        },
        {
            "from": "20",
            "to": "237",
            "cost": 1856,
            "lower_bound": 0,
            "upper_bound": 723
        },
        {
            "from": "20",
            "to": "224",
            "cost": 3540,
            "lower_bound": 0,
            "upper_bound": 966
        },
        {
            "from": "25",
            "to": "83",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 503
        },
        {
            "from": "25",
            "to": "151",
            "cost": 5010,
            "lower_bound": 0,
            "upper_bound": 856
        },
        {
            "from": "25",
            "to": "166",
            "cost": 370,
            "lower_bound": 0,
            "upper_bound": 509
        },
        {
            "from": "25",
            "to": "96",
            "cost": 9699,
            "lower_bound": 0,
            "upper_bound": 641
        },
        {
            "from": "25",
            "to": "123",
            "cost": 8932,
            "lower_bound": 0,
            "upper_bound": 751
        },
        {
            "from": "25",
            "to": "168",
            "cost": 1831,
            "lower_bound": 0,
            "upper_bound": 202
        },
        {
            "from": "25",
            "to": "59",
            "cost": 8855,
            "lower_bound": 0,
            "upper_bound": 574
        },
        {
            "from": "37",
            "to": "173",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 503
        },
        {
            "from": "37",
            "to": "134",
            "cost": 7622,
            "lower_bound": 0,
            "upper_bound": 465
        },
        {
            "from": "37",
            "to": "250",
            "cost": 9184,
            "lower_bound": 0,
            "upper_bound": 646
        },
        {
            "from": "37",
            "to": "102",
            "cost": 5577,
            "lower_bound": 0,
            "upper_bound": 115
        },
        {
            "from": "37",
            "to": "230",
            "cost": 7400,
            "lower_bound": 0,
            "upper_bound": 294
        },
        {
            "from": "37",
            "to": "100",
            "cost": 6906,
            "lower_bound": 0,
            "upper_bound": 681
        },
        {
            "from": "37",
            "to": "35",
            "cost": 4023,
            "lower_bound": 0,
            "upper_bound": 88
        },
        {
            "from": "37",
            "to": "75",
            "cost": 3970,
            "lower_bound": 0,
            "upper_bound": 776
        },
        {
            "from": "37",
            "to": "144",
            "cost": 2903,
            "lower_bound": 0,
            "upper_bound": 296
        },
        {
            "from": "37",
            "to": "64",
            "cost": 3792,
            "lower_bound": 0,
            "upper_bound": 523
        },
        {
            "from": "37",
            "to": "18",
            "cost": 6380,
            "lower_bound": 0,
            "upper_bound": 168
        },
        {
            "from": "37",
            "to": "190",
            "cost": 6980,
            "lower_bound": 0,
            "upper_bound": 77
        },
        {
            "from": "37",
            "to": "151",
            "cost": 5634,
            "lower_bound": 0,
            "upper_bound": 118
        },
        {
            "from": "62",
            "to": "107",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 503
        },
        {
            "from": "62",
            "to": "244",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 503
        },
        {
            "from": "62",
            "to": "32",
            "cost": 6133,
            "lower_bound": 0,
            "upper_bound": 846
        },
        {
            "from": "62",
            "to": "73",
            "cost": 4340,
            "lower_bound": 0,
            "upper_bound": 423
        },
        {
            "from": "62",
            "to": "202",
            "cost": 4578,
            "lower_bound": 0,
            "upper_bound": 813
        },
        {
            "from": "62",
            "to": "58",
            "cost": 5748,
            "lower_bound": 0,
            "upper_bound": 690
        },
        {
            "from": "62",
            "to": "225",
            "cost": 9394,
            "lower_bound": 0,
            "upper_bound": 437
        },
        {
            "from": "62",
            "to": "33",
            "cost": 3631,
            "lower_bound": 0,
            "upper_bound": 176
        },
        {
            "from": "62",
            "to": "74",
            "cost": 8997,
            "lower_bound": 0,
            "upper_bound": 438
        },
        {
            "from": "62",
            "to": "47",
            "cost": 44,
            "lower_bound": 0,
            "upper_bound": 812
        },
        {
            "from": "62",
            "to": "138",
            "cost": 6292,
            "lower_bound": 0,
            "upper_bound": 518
        },
        {
            "from": "71",
            "to": "62",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 503
        },
        {
            "from": "71",
            "to": "111",
            "cost": 2839,
            "lower_bound": 0,
            "upper_bound": 903
        },
        {
            "from": "71",
            "to": "158",
            "cost": 405,
            "lower_bound": 0,
            "upper_bound": 555
        },
        {
            "from": "71",
            "to": "136",
            "cost": 2772,
            "lower_bound": 0,
            "upper_bound": 484
        },
        {
            "from": "71",
            "to": "36",
            "cost": 9094,
            "lower_bound": 0,
            "upper_bound": 324
        },
        {
            "from": "71",
            "to": "143",
            "cost": 7634,
            "lower_bound": 0,
            "upper_bound": 719
        },
        {
            "from": "71",
            "to": "34",
            "cost": 9795,
            "lower_bound": 0,
            "upper_bound": 228
        },
        {
            "from": "71",
            "to": "179",
            "cost": 178,
            "lower_bound": 0,
            "upper_bound": 592
        },
        {
            "from": "71",
            "to": "237",
            "cost": 5091,
            "lower_bound": 0,
            "upper_bound": 463
        },
        {
            "from": "82",
            "to": "37",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 503
        },
        {
            "from": "82",
            "to": "47",
            "cost": 9542,
            "lower_bound": 0,
            "upper_bound": 625
        },
        {
            "from": "82",
            "to": "188",
            "cost": 840,
            "lower_bound": 0,
            "upper_bound": 185
        },
        {
            "from": "82",
            "to": "228",
            "cost": 4447,
            "lower_bound": 0,
            "upper_bound": 469
        },
        {
            "from": "82",
            "to": "242",
            "cost": 2582,
            "lower_bound": 0,
            "upper_bound": 557
        },
        {
            "from": "82",
            "to": "254",
            "cost": 4032,
            "lower_bound": 0,
            "upper_bound": 59
        },
        {
            "from": "82",
            "to": "98",
            "cost": 7697,
            "lower_bound": 0,
            "upper_bound": 479
        },
        {
            "from": "82",
            "to": "66",
            "cost": 7946,
            "lower_bound": 0,
            "upper_bound": 886
        },
        {
            "from": "82",
            "to": "202",
            "cost": 8151,
            "lower_bound": 0,
            "upper_bound": 993
        },
        {
            "from": "83",
            "to": "166",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 503
        },
        {
            "from": "83",
            "to": "158",
            "cost": 6573,
            "lower_bound": 0,
            "upper_bound": 518
        },
        {
            "from": "83",
            "to": "147",
            "cost": 5974,
            "lower_bound": 0,
            "upper_bound": 197
        },
        {
            "from": "83",
            "to": "187",
            "cost": 2878,
            "lower_bound": 0,
            "upper_bound": 726
        },
        {
            "from": "83",
            "to": "31",
            "cost": 5453,
            "lower_bound": 0,
            "upper_bound": 619
        },
        {
            "from": "83",
            "to": "85",
            "cost": 4011,
            "lower_bound": 0,
            "upper_bound": 476
        },
        {
            "from": "101",
            "to": "204",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 503
        },
        {
            "from": "101",
            "to": "192",
            "cost": 5920,
            "lower_bound": 0,
            "upper_bound": 265
        },
        {
            "from": "101",
            "to": "57",
            "cost": 9492,
            "lower_bound": 0,
            "upper_bound": 765
        },
        {
            "from": "101",
            "to": "207",
            "cost": 6271,
            "lower_bound": 0,
            "upper_bound": 977
        },
        {
            "from": "101",
            "to": "130",
            "cost": 4570,
            "lower_bound": 0,
            "upper_bound": 70
        },
        {
            "from": "101",
            "to": "211",
            "cost": 343,
            "lower_bound": 0,
            "upper_bound": 160
        },
        {
            "from": "101",
            "to": "242",
            "cost": 6022,
            "lower_bound": 0,
            "upper_bound": 42
        },
        {
            "from": "101",
            "to": "246",
            "cost": 8422,
            "lower_bound": 0,
            "upper_bound": 872
        },
        {
            "from": "107",
            "to": "252",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 503
        },
        {
            "from": "107",
            "to": "39",
            "cost": 4000,
            "lower_bound": 0,
            "upper_bound": 899
        },
        {
            "from": "107",
            "to": "30",
            "cost": 6826,
            "lower_bound": 0,
            "upper_bound": 788
        },
        {
            "from": "107",
            "to": "26",
            "cost": 878,
            "lower_bound": 0,
            "upper_bound": 887
        },
        {
            "from": "107",
            "to": "170",
            "cost": 9336,
            "lower_bound": 0,
            "upper_bound": 511
        },
        {
            "from": "107",
            "to": "256",
            "cost": 2531,
            "lower_bound": 0,
            "upper_bound": 864
        },
        {
            "from": "107",
            "to": "242",
            "cost": 2807,
            "lower_bound": 0,
            "upper_bound": 175
        },
        {
            "from": "107",
            "to": "124",
            "cost": 9476,
            "lower_bound": 0,
            "upper_bound": 536
        },
        {
            "from": "107",
            "to": "208",
            "cost": 777,
            "lower_bound": 0,
            "upper_bound": 717
        },
        {
            "from": "107",
            "to": "46",
            "cost": 6763,
            "lower_bound": 0,
            "upper_bound": 259
        },
        {
            "from": "107",
            "to": "100",
            "cost": 1832,
            "lower_bound": 0,
            "upper_bound": 71
        },
        {
            "from": "107",
            "to": "42",
            "cost": 3872,
            "lower_bound": 0,
            "upper_bound": 477
        },
        {
            "from": "107",
            "to": "28",
            "cost": 9119,
            "lower_bound": 0,
            "upper_bound": 373
        },
        {
            "from": "166",
            "to": "20",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 503
        },
        {
            "from": "166",
            "to": "216",
            "cost": 2611,
            "lower_bound": 0,
            "upper_bound": 960
        },
        {
            "from": "166",
            "to": "121",
            "cost": 4456,
            "lower_bound": 0,
            "upper_bound": 239
        },
        {
            "from": "166",
            "to": "103",
            "cost": 6621,
            "lower_bound": 0,
            "upper_bound": 741
        },
        {
            "from": "166",
            "to": "119",
            "cost": 3463,
            "lower_bound": 0,
            "upper_bound": 375
        },
        {
            "from": "166",
            "to": "25",
            "cost": 3993,
            "lower_bound": 0,
            "upper_bound": 815
        },
        {
            "from": "166",
            "to": "148",
            "cost": 296,
            "lower_bound": 0,
            "upper_bound": 212
        },
        {
            "from": "166",
            "to": "72",
            "cost": 1724,
            "lower_bound": 0,
            "upper_bound": 644
        },
        {
            "from": "166",
            "to": "170",
            "cost": 5899,
            "lower_bound": 0,
            "upper_bound": 312
        },
        {
            "from": "166",
            "to": "235",
            "cost": 3227,
            "lower_bound": 0,
            "upper_bound": 946
        },
        {
            "from": "166",
            "to": "38",
            "cost": 1177,
            "lower_bound": 0,
            "upper_bound": 813
        },
        {
            "from": "166",
            "to": "157",
            "cost": 1726,
            "lower_bound": 0,
            "upper_bound": 382
        },
        {
            "from": "166",
            "to": "79",
            "cost": 6553,
            "lower_bound": 0,
            "upper_bound": 153
        },
        {
            "from": "166",
            "to": "188",
            "cost": 5198,
            "lower_bound": 0,
            "upper_bound": 300
        },
        {
            "from": "166",
            "to": "236",
            "cost": 69,
            "lower_bound": 0,
            "upper_bound": 723
        },
        {
            "from": "170",
            "to": "71",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 503
        },
        {
            "from": "170",
            "to": "141",
            "cost": 2118,
            "lower_bound": 0,
            "upper_bound": 638
        },
        {
            "from": "170",
            "to": "99",
            "cost": 4510,
            "lower_bound": 0,
            "upper_bound": 588
        },
        {
            "from": "170",
            "to": "75",
            "cost": 4667,
            "lower_bound": 0,
            "upper_bound": 142
        },
        {
            "from": "170",
            "to": "114",
            "cost": 9671,
            "lower_bound": 0,
            "upper_bound": 916
        },
        {
            "from": "170",
            "to": "167",
            "cost": 3525,
            "lower_bound": 0,
            "upper_bound": 868
        },
        {
            "from": "170",
            "to": "160",
            "cost": 4264,
            "lower_bound": 0,
            "upper_bound": 898
        },
        {
            "from": "170",
            "to": "144",
            "cost": 6498,
            "lower_bound": 0,
            "upper_bound": 652
        },
        {
            "from": "170",
            "to": "164",
            "cost": 6242,
            "lower_bound": 0,
            "upper_bound": 860
        },
        {
            "from": "170",
            "to": "124",
            "cost": 2691,
            "lower_bound": 0,
            "upper_bound": 716
        },
        {
            "from": "170",
            "to": "104",
            "cost": 116,
            "lower_bound": 0,
            "upper_bound": 370
        },
        {
            "from": "170",
            "to": "218",
            "cost": 1131,
            "lower_bound": 0,
            "upper_bound": 36
        },
        {
            "from": "170",
            "to": "185",
            "cost": 3167,
            "lower_bound": 0,
            "upper_bound": 733
        },
        {
            "from": "170",
            "to": "194",
            "cost": 6688,
            "lower_bound": 0,
            "upper_bound": 792
        },
        {
            "from": "173",
            "to": "170",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 503
        },
        {
            "from": "173",
            "to": "144",
            "cost": 2685,
            "lower_bound": 0,
            "upper_bound": 739
        },
        {
            "from": "173",
            "to": "35",
            "cost": 485,
            "lower_bound": 0,
            "upper_bound": 947
        },
        {
            "from": "173",
            "to": "197",
            "cost": 3079,
            "lower_bound": 0,
            "upper_bound": 949
        },
        {
            "from": "173",
            "to": "43",
            "cost": 4070,
            "lower_bound": 0,
            "upper_bound": 937
        },
        {
            "from": "173",
            "to": "159",
            "cost": 4006,
            "lower_bound": 0,
            "upper_bound": 374
        },
        {
            "from": "173",
            "to": "168",
            "cost": 6718,
            "lower_bound": 0,
            "upper_bound": 308
        },
        {
            "from": "173",
            "to": "194",
            "cost": 2252,
            "lower_bound": 0,
            "upper_bound": 436
        },
        {
            "from": "173",
            "to": "195",
            "cost": 5554,
            "lower_bound": 0,
            "upper_bound": 455
        },
        {
            "from": "173",
            "to": "205",
            "cost": 5680,
            "lower_bound": 0,
            "upper_bound": 826
        },
        {
            "from": "173",
            "to": "92",
            "cost": 8561,
            "lower_bound": 0,
            "upper_bound": 190
        },
        {
            "from": "204",
            "to": "25",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 503
        },
        {
            "from": "204",
            "to": "27",
            "cost": 6557,
            "lower_bound": 0,
            "upper_bound": 269
        },
        {
            "from": "204",
            "to": "20",
            "cost": 1404,
            "lower_bound": 0,
            "upper_bound": 853
        },
        {
            "from": "204",
            "to": "89",
            "cost": 8051,
            "lower_bound": 0,
            "upper_bound": 81
        },
        {
            "from": "204",
            "to": "96",
            "cost": 4061,
            "lower_bound": 0,
            "upper_bound": 318
        },
        {
            "from": "204",
            "to": "74",
            "cost": 4735,
            "lower_bound": 0,
            "upper_bound": 725
        },
        {
            "from": "204",
            "to": "134",
            "cost": 2725,
            "lower_bound": 0,
            "upper_bound": 833
        },
        {
            "from": "204",
            "to": "128",
            "cost": 4190,
            "lower_bound": 0,
            "upper_bound": 827
        },
        {
            "from": "204",
            "to": "49",
            "cost": 5055,
            "lower_bound": 0,
            "upper_bound": 764
        },
        {
            "from": "204",
            "to": "125",
            "cost": 8857,
            "lower_bound": 0,
            "upper_bound": 194
        },
        {
            "from": "204",
            "to": "152",
            "cost": 3023,
            "lower_bound": 0,
            "upper_bound": 268
        },
        {
            "from": "204",
            "to": "197",
            "cost": 4115,
            "lower_bound": 0,
            "upper_bound": 290
        },
        {
            "from": "204",
            "to": "129",
            "cost": 5918,
            "lower_bound": 0,
            "upper_bound": 595
        },
        {
            "from": "204",
            "to": "93",
            "cost": 5368,
            "lower_bound": 0,
            "upper_bound": 770
        },
        {
            "from": "218",
            "to": "101",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 503
        },
        {
            "from": "218",
            "to": "121",
            "cost": 3804,
            "lower_bound": 0,
            "upper_bound": 173
        },
        {
            "from": "218",
            "to": "39",
            "cost": 7394,
            "lower_bound": 0,
            "upper_bound": 968
        },
        {
            "from": "218",
            "to": "110",
            "cost": 7896,
            "lower_bound": 0,
            "upper_bound": 996
        },
        {
            "from": "218",
            "to": "94",
            "cost": 6648,
            "lower_bound": 0,
            "upper_bound": 209
        },
        {
            "from": "218",
            "to": "199",
            "cost": 8640,
            "lower_bound": 0,
            "upper_bound": 535
        },
        {
            "from": "218",
            "to": "216",
            "cost": 4107,
            "lower_bound": 0,
            "upper_bound": 334
        },
        {
            "from": "14",
            "to": "26",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1905
        },
        {
            "from": "14",
            "to": "60",
            "cost": 7861,
            "lower_bound": 0,
            "upper_bound": 196
        },
        {
            "from": "14",
            "to": "52",
            "cost": 4392,
            "lower_bound": 0,
            "upper_bound": 554
        },
        {
            "from": "14",
            "to": "189",
            "cost": 5259,
            "lower_bound": 0,
            "upper_bound": 988
        },
        {
            "from": "14",
            "to": "57",
            "cost": 6049,
            "lower_bound": 0,
            "upper_bound": 373
        },
        {
            "from": "14",
            "to": "136",
            "cost": 1703,
            "lower_bound": 0,
            "upper_bound": 605
        },
        {
            "from": "14",
            "to": "130",
            "cost": 6420,
            "lower_bound": 0,
            "upper_bound": 466
        },
        {
            "from": "14",
            "to": "18",
            "cost": 4897,
            "lower_bound": 0,
            "upper_bound": 465
        },
        {
            "from": "14",
            "to": "219",
            "cost": 2981,
            "lower_bound": 0,
            "upper_bound": 948
        },
        {
            "from": "14",
            "to": "44",
            "cost": 5293,
            "lower_bound": 0,
            "upper_bound": 779
        },
        {
            "from": "14",
            "to": "255",
            "cost": 8885,
            "lower_bound": 0,
            "upper_bound": 50
        },
        {
            "from": "14",
            "to": "176",
            "cost": 7675,
            "lower_bound": 0,
            "upper_bound": 271
        },
        {
            "from": "21",
            "to": "95",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1905
        },
        {
            "from": "21",
            "to": "139",
            "cost": 6030,
            "lower_bound": 0,
            "upper_bound": 411
        },
        {
            "from": "21",
            "to": "230",
            "cost": 8324,
            "lower_bound": 0,
            "upper_bound": 25
        },
        {
            "from": "21",
            "to": "183",
            "cost": 3094,
            "lower_bound": 0,
            "upper_bound": 373
        },
        {
            "from": "21",
            "to": "127",
            "cost": 952,
            "lower_bound": 0,
            "upper_bound": 446
        },
        {
            "from": "21",
            "to": "216",
            "cost": 6416,
            "lower_bound": 0,
            "upper_bound": 830
        },
        {
            "from": "21",
            "to": "176",
            "cost": 5433,
            "lower_bound": 0,
            "upper_bound": 359
        },
        {
            "from": "21",
            "to": "218",
            "cost": 4986,
            "lower_bound": 0,
            "upper_bound": 121
        },
        {
            "from": "21",
            "to": "179",
            "cost": 8150,
            "lower_bound": 0,
            "upper_bound": 842
        },
        {
            "from": "21",
            "to": "102",
            "cost": 1046,
            "lower_bound": 0,
            "upper_bound": 633
        },
        {
            "from": "21",
            "to": "170",
            "cost": 7971,
            "lower_bound": 0,
            "upper_bound": 21
        },
        {
            "from": "26",
            "to": "179",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1905
        },
        {
            "from": "26",
            "to": "52",
            "cost": 1554,
            "lower_bound": 0,
            "upper_bound": 495
        },
        {
            "from": "26",
            "to": "23",
            "cost": 1840,
            "lower_bound": 0,
            "upper_bound": 497
        },
        {
            "from": "26",
            "to": "154",
            "cost": 5702,
            "lower_bound": 0,
            "upper_bound": 994
        },
        {
            "from": "26",
            "to": "62",
            "cost": 2755,
            "lower_bound": 0,
            "upper_bound": 822
        },
        {
            "from": "26",
            "to": "151",
            "cost": 2479,
            "lower_bound": 0,
            "upper_bound": 764
        },
        {
            "from": "26",
            "to": "123",
            "cost": 2876,
            "lower_bound": 0,
            "upper_bound": 944
        },
        {
            "from": "26",
            "to": "29",
            "cost": 6842,
            "lower_bound": 0,
            "upper_bound": 126
        },
        {
            "from": "32",
            "to": "245",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1905
        },
        {
            "from": "32",
            "to": "152",
            "cost": 2097,
            "lower_bound": 0,
            "upper_bound": 512
        },
        {
            "from": "32",
            "to": "154",
            "cost": 2498,
            "lower_bound": 0,
            "upper_bound": 839
        },
        {
            "from": "32",
            "to": "113",
            "cost": 9544,
            "lower_bound": 0,
            "upper_bound": 781
        },
        {
            "from": "32",
            "to": "123",
            "cost": 1726,
            "lower_bound": 0,
            "upper_bound": 608
        },
        {
            "from": "32",
            "to": "136",
            "cost": 1806,
            "lower_bound": 0,
            "upper_bound": 228
        },
        {
            "from": "32",
            "to": "206",
            "cost": 1214,
            "lower_bound": 0,
            "upper_bound": 906
        },
        {
            "from": "63",
            "to": "183",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1905
        },
        {
            "from": "63",
            "to": "193",
            "cost": 5062,
            "lower_bound": 0,
            "upper_bound": 569
        },
        {
            "from": "63",
            "to": "27",
            "cost": 8191,
            "lower_bound": 0,
            "upper_bound": 666
        },
        {
            "from": "63",
            "to": "152",
            "cost": 967,
            "lower_bound": 0,
            "upper_bound": 520
        },
        {
            "from": "63",
            "to": "100",
            "cost": 3975,
            "lower_bound": 0,
            "upper_bound": 860
        },
        {
            "from": "63",
            "to": "19",
            "cost": 2624,
            "lower_bound": 0,
            "upper_bound": 501
        },
        {
            "from": "63",
            "to": "172",
            "cost": 3607,
            "lower_bound": 0,
            "upper_bound": 669
        },
        {
            "from": "63",
            "to": "121",
            "cost": 4530,
            "lower_bound": 0,
            "upper_bound": 302
        },
        {
            "from": "63",
            "to": "254",
            "cost": 7905,
            "lower_bound": 0,
            "upper_bound": 329
        },
        {
            "from": "63",
            "to": "117",
            "cost": 9976,
            "lower_bound": 0,
            "upper_bound": 712
        },
        {
            "from": "63",
            "to": "81",
            "cost": 6242,
            "lower_bound": 0,
            "upper_bound": 273
        },
        {
            "from": "63",
            "to": "248",
            "cost": 1602,
            "lower_bound": 0,
            "upper_bound": 123
        },
        {
            "from": "63",
            "to": "56",
            "cost": 7429,
            "lower_bound": 0,
            "upper_bound": 235
        },
        {
            "from": "63",
            "to": "101",
            "cost": 391,
            "lower_bound": 0,
            "upper_bound": 721
        },
        {
            "from": "63",
            "to": "102",
            "cost": 1940,
            "lower_bound": 0,
            "upper_bound": 953
        },
        {
            "from": "91",
            "to": "97",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1905
        },
        {
            "from": "91",
            "to": "128",
            "cost": 2120,
            "lower_bound": 0,
            "upper_bound": 630
        },
        {
            "from": "91",
            "to": "178",
            "cost": 6130,
            "lower_bound": 0,
            "upper_bound": 305
        },
        {
            "from": "91",
            "to": "74",
            "cost": 5808,
            "lower_bound": 0,
            "upper_bound": 831
        },
        {
            "from": "91",
            "to": "116",
            "cost": 391,
            "lower_bound": 0,
            "upper_bound": 303
        },
        {
            "from": "91",
            "to": "42",
            "cost": 1016,
            "lower_bound": 0,
            "upper_bound": 822
        },
        {
            "from": "91",
            "to": "171",
            "cost": 3795,
            "lower_bound": 0,
            "upper_bound": 738
        },
        {
            "from": "91",
            "to": "194",
            "cost": 5517,
            "lower_bound": 0,
            "upper_bound": 633
        },
        {
            "from": "91",
            "to": "44",
            "cost": 7380,
            "lower_bound": 0,
            "upper_bound": 397
        },
        {
            "from": "91",
            "to": "64",
            "cost": 8786,
            "lower_bound": 0,
            "upper_bound": 807
        },
        {
            "from": "91",
            "to": "205",
            "cost": 860,
            "lower_bound": 0,
            "upper_bound": 471
        },
        {
            "from": "91",
            "to": "103",
            "cost": 9051,
            "lower_bound": 0,
            "upper_bound": 318
        },
        {
            "from": "95",
            "to": "222",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1905
        },
        {
            "from": "95",
            "to": "194",
            "cost": 9586,
            "lower_bound": 0,
            "upper_bound": 689
        },
        {
            "from": "95",
            "to": "170",
            "cost": 4252,
            "lower_bound": 0,
            "upper_bound": 257
        },
        {
            "from": "95",
            "to": "53",
            "cost": 1896,
            "lower_bound": 0,
            "upper_bound": 134
        },
        {
            "from": "95",
            "to": "96",
            "cost": 9675,
            "lower_bound": 0,
            "upper_bound": 158
        },
        {
            "from": "95",
            "to": "241",
            "cost": 52,
            "lower_bound": 0,
            "upper_bound": 625
        },
        {
            "from": "95",
            "to": "213",
            "cost": 264,
            "lower_bound": 0,
            "upper_bound": 915
        },
        {
            "from": "95",
            "to": "186",
            "cost": 2775,
            "lower_bound": 0,
            "upper_bound": 995
        },
        {
            "from": "95",
            "to": "155",
            "cost": 2549,
            "lower_bound": 0,
            "upper_bound": 568
        },
        {
            "from": "95",
            "to": "69",
            "cost": 7218,
            "lower_bound": 0,
            "upper_bound": 615
        },
        {
            "from": "97",
            "to": "32",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1905
        },
        {
            "from": "97",
            "to": "107",
            "cost": 8140,
            "lower_bound": 0,
            "upper_bound": 956
        },
        {
            "from": "97",
            "to": "226",
            "cost": 609,
            "lower_bound": 0,
            "upper_bound": 23
        },
        {
            "from": "97",
            "to": "147",
            "cost": 1794,
            "lower_bound": 0,
            "upper_bound": 709
        },
        {
            "from": "97",
            "to": "235",
            "cost": 1902,
            "lower_bound": 0,
            "upper_bound": 217
        },
        {
            "from": "97",
            "to": "156",
            "cost": 8603,
            "lower_bound": 0,
            "upper_bound": 385
        },
        {
            "from": "179",
            "to": "21",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1905
        },
        {
            "from": "179",
            "to": "210",
            "cost": 9659,
            "lower_bound": 0,
            "upper_bound": 270
        },
        {
            "from": "179",
            "to": "45",
            "cost": 665,
            "lower_bound": 0,
            "upper_bound": 556
        },
        {
            "from": "179",
            "to": "196",
            "cost": 4004,
            "lower_bound": 0,
            "upper_bound": 866
        },
        {
            "from": "183",
            "to": "91",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1905
        },
        {
            "from": "183",
            "to": "252",
            "cost": 8667,
            "lower_bound": 0,
            "upper_bound": 533
        },
        {
            "from": "196",
            "to": "63",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1905
        },
        {
            "from": "196",
            "to": "110",
            "cost": 8168,
            "lower_bound": 0,
            "upper_bound": 182
        },
        {
            "from": "196",
            "to": "66",
            "cost": 2020,
            "lower_bound": 0,
            "upper_bound": 917
        },
        {
            "from": "196",
            "to": "45",
            "cost": 1588,
            "lower_bound": 0,
            "upper_bound": 691
        },
        {
            "from": "196",
            "to": "97",
            "cost": 8330,
            "lower_bound": 0,
            "upper_bound": 352
        },
        {
            "from": "196",
            "to": "120",
            "cost": 834,
            "lower_bound": 0,
            "upper_bound": 303
        },
        {
            "from": "196",
            "to": "74",
            "cost": 8848,
            "lower_bound": 0,
            "upper_bound": 735
        },
        {
            "from": "196",
            "to": "151",
            "cost": 2962,
            "lower_bound": 0,
            "upper_bound": 926
        },
        {
            "from": "196",
            "to": "93",
            "cost": 6056,
            "lower_bound": 0,
            "upper_bound": 184
        },
        {
            "from": "196",
            "to": "35",
            "cost": 6228,
            "lower_bound": 0,
            "upper_bound": 868
        },
        {
            "from": "216",
            "to": "196",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1905
        },
        {
            "from": "216",
            "to": "254",
            "cost": 4435,
            "lower_bound": 0,
            "upper_bound": 157
        },
        {
            "from": "216",
            "to": "58",
            "cost": 1769,
            "lower_bound": 0,
            "upper_bound": 55
        },
        {
            "from": "216",
            "to": "197",
            "cost": 414,
            "lower_bound": 0,
            "upper_bound": 298
        },
        {
            "from": "216",
            "to": "184",
            "cost": 2362,
            "lower_bound": 0,
            "upper_bound": 570
        },
        {
            "from": "216",
            "to": "71",
            "cost": 949,
            "lower_bound": 0,
            "upper_bound": 948
        },
        {
            "from": "216",
            "to": "116",
            "cost": 5061,
            "lower_bound": 0,
            "upper_bound": 449
        },
        {
            "from": "216",
            "to": "75",
            "cost": 2423,
            "lower_bound": 0,
            "upper_bound": 987
        },
        {
            "from": "216",
            "to": "162",
            "cost": 117,
            "lower_bound": 0,
            "upper_bound": 568
        },
        {
            "from": "216",
            "to": "251",
            "cost": 1808,
            "lower_bound": 0,
            "upper_bound": 804
        },
        {
            "from": "216",
            "to": "50",
            "cost": 1865,
            "lower_bound": 0,
            "upper_bound": 487
        },
        {
            "from": "216",
            "to": "181",
            "cost": 4298,
            "lower_bound": 0,
            "upper_bound": 490
        },
        {
            "from": "216",
            "to": "72",
            "cost": 9015,
            "lower_bound": 0,
            "upper_bound": 687
        },
        {
            "from": "216",
            "to": "253",
            "cost": 3386,
            "lower_bound": 0,
            "upper_bound": 914
        },
        {
            "from": "216",
            "to": "202",
            "cost": 1844,
            "lower_bound": 0,
            "upper_bound": 568
        },
        {
            "from": "222",
            "to": "216",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1905
        },
        {
            "from": "222",
            "to": "248",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 1905
        },
        {
            "from": "222",
            "to": "251",
            "cost": 9465,
            "lower_bound": 0,
            "upper_bound": 637
        },
        {
            "from": "222",
            "to": "135",
            "cost": 2703,
            "lower_bound": 0,
            "upper_bound": 126
        },
        {
            "from": "222",
            "to": "182",
            "cost": 1230,
            "lower_bound": 0,
            "upper_bound": 262
        },
        {
            "from": "222",
            "to": "106",
            "cost": 9042,
            "lower_bound": 0,
            "upper_bound": 413
        },
        {
            "from": "222",
            "to": "30",
            "cost": 6362,
            "lower_bound": 0,
            "upper_bound": 561
        },
        {
            "from": "222",
            "to": "84",
            "cost": 9266,
            "lower_bound": 0,
            "upper_bound": 578
        },
        {
            "from": "15",
            "to": "45",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 800
        },
        {
            "from": "15",
            "to": "238",
            "cost": 9874,
            "lower_bound": 0,
            "upper_bound": 154
        },
        {
            "from": "15",
            "to": "97",
            "cost": 7951,
            "lower_bound": 0,
            "upper_bound": 877
        },
        {
            "from": "15",
            "to": "223",
            "cost": 8239,
            "lower_bound": 0,
            "upper_bound": 387
        },
        {
            "from": "15",
            "to": "164",
            "cost": 8030,
            "lower_bound": 0,
            "upper_bound": 552
        },
        {
            "from": "15",
            "to": "135",
            "cost": 2102,
            "lower_bound": 0,
            "upper_bound": 97
        },
        {
            "from": "41",
            "to": "220",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 800
        },
        {
            "from": "41",
            "to": "218",
            "cost": 5739,
            "lower_bound": 0,
            "upper_bound": 131
        },
        {
            "from": "41",
            "to": "95",
            "cost": 7789,
            "lower_bound": 0,
            "upper_bound": 113
        },
        {
            "from": "41",
            "to": "61",
            "cost": 632,
            "lower_bound": 0,
            "upper_bound": 246
        },
        {
            "from": "41",
            "to": "129",
            "cost": 3464,
            "lower_bound": 0,
            "upper_bound": 935
        },
        {
            "from": "41",
            "to": "92",
            "cost": 7555,
            "lower_bound": 0,
            "upper_bound": 599
        },
        {
            "from": "41",
            "to": "119",
            "cost": 6917,
            "lower_bound": 0,
            "upper_bound": 972
        },
        {
            "from": "41",
            "to": "81",
            "cost": 4453,
            "lower_bound": 0,
            "upper_bound": 595
        },
        {
            "from": "41",
            "to": "63",
            "cost": 3142,
            "lower_bound": 0,
            "upper_bound": 293
        },
        {
            "from": "41",
            "to": "30",
            "cost": 5764,
            "lower_bound": 0,
            "upper_bound": 270
        },
        {
            "from": "43",
            "to": "193",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 800
        },
        {
            "from": "43",
            "to": "53",
            "cost": 1835,
            "lower_bound": 0,
            "upper_bound": 947
        },
        {
            "from": "43",
            "to": "125",
            "cost": 2697,
            "lower_bound": 0,
            "upper_bound": 215
        },
        {
            "from": "43",
            "to": "44",
            "cost": 3070,
            "lower_bound": 0,
            "upper_bound": 711
        },
        {
            "from": "43",
            "to": "139",
            "cost": 8560,
            "lower_bound": 0,
            "upper_bound": 786
        },
        {
            "from": "43",
            "to": "240",
            "cost": 8679,
            "lower_bound": 0,
            "upper_bound": 420
        },
        {
            "from": "45",
            "to": "41",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 800
        },
        {
            "from": "45",
            "to": "182",
            "cost": 8380,
            "lower_bound": 0,
            "upper_bound": 996
        },
        {
            "from": "45",
            "to": "192",
            "cost": 7281,
            "lower_bound": 0,
            "upper_bound": 707
        },
        {
            "from": "45",
            "to": "49",
            "cost": 4102,
            "lower_bound": 0,
            "upper_bound": 202
        },
        {
            "from": "48",
            "to": "191",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 800
        },
        {
            "from": "48",
            "to": "219",
            "cost": 4469,
            "lower_bound": 0,
            "upper_bound": 489
        },
        {
            "from": "48",
            "to": "30",
            "cost": 6533,
            "lower_bound": 0,
            "upper_bound": 10
        },
        {
            "from": "48",
            "to": "239",
            "cost": 7718,
            "lower_bound": 0,
            "upper_bound": 193
        },
        {
            "from": "48",
            "to": "69",
            "cost": 7978,
            "lower_bound": 0,
            "upper_bound": 432
        },
        {
            "from": "48",
            "to": "19",
            "cost": 1712,
            "lower_bound": 0,
            "upper_bound": 428
        },
        {
            "from": "48",
            "to": "65",
            "cost": 1771,
            "lower_bound": 0,
            "upper_bound": 582
        },
        {
            "from": "48",
            "to": "123",
            "cost": 576,
            "lower_bound": 0,
            "upper_bound": 922
        },
        {
            "from": "48",
            "to": "223",
            "cost": 8072,
            "lower_bound": 0,
            "upper_bound": 545
        },
        {
            "from": "48",
            "to": "215",
            "cost": 9570,
            "lower_bound": 0,
            "upper_bound": 363
        },
        {
            "from": "48",
            "to": "106",
            "cost": 9699,
            "lower_bound": 0,
            "upper_bound": 493
        },
        {
            "from": "72",
            "to": "113",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 800
        },
        {
            "from": "72",
            "to": "243",
            "cost": 5529,
            "lower_bound": 0,
            "upper_bound": 442
        },
        {
            "from": "72",
            "to": "219",
            "cost": 7062,
            "lower_bound": 0,
            "upper_bound": 10
        },
        {
            "from": "72",
            "to": "250",
            "cost": 4600,
            "lower_bound": 0,
            "upper_bound": 668
        },
        {
            "from": "72",
            "to": "115",
            "cost": 7745,
            "lower_bound": 0,
            "upper_bound": 634
        },
        {
            "from": "84",
            "to": "194",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 800
        },
        {
            "from": "84",
            "to": "100",
            "cost": 60,
            "lower_bound": 0,
            "upper_bound": 653
        },
        {
            "from": "84",
            "to": "27",
            "cost": 1600,
            "lower_bound": 0,
            "upper_bound": 446
        },
        {
            "from": "84",
            "to": "29",
            "cost": 9393,
            "lower_bound": 0,
            "upper_bound": 144
        },
        {
            "from": "84",
            "to": "148",
            "cost": 4419,
            "lower_bound": 0,
            "upper_bound": 824
        },
        {
            "from": "84",
            "to": "128",
            "cost": 5170,
            "lower_bound": 0,
            "upper_bound": 714
        },
        {
            "from": "84",
            "to": "109",
            "cost": 2772,
            "lower_bound": 0,
            "upper_bound": 284
        },
        {
            "from": "84",
            "to": "85",
            "cost": 5078,
            "lower_bound": 0,
            "upper_bound": 328
        },
        {
            "from": "84",
            "to": "105",
            "cost": 6520,
            "lower_bound": 0,
            "upper_bound": 302
        },
        {
            "from": "85",
            "to": "72",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 800
        },
        {
            "from": "85",
            "to": "120",
            "cost": 9465,
            "lower_bound": 0,
            "upper_bound": 366
        },
        {
            "from": "85",
            "to": "138",
            "cost": 5793,
            "lower_bound": 0,
            "upper_bound": 179
        },
        {
            "from": "85",
            "to": "118",
            "cost": 6933,
            "lower_bound": 0,
            "upper_bound": 417
        },
        {
            "from": "85",
            "to": "200",
            "cost": 4809,
            "lower_bound": 0,
            "upper_bound": 700
        },
        {
            "from": "85",
            "to": "140",
            "cost": 768,
            "lower_bound": 0,
            "upper_bound": 238
        },
        {
            "from": "85",
            "to": "28",
            "cost": 8185,
            "lower_bound": 0,
            "upper_bound": 769
        },
        {
            "from": "85",
            "to": "245",
            "cost": 6892,
            "lower_bound": 0,
            "upper_bound": 353
        },
        {
            "from": "85",
            "to": "136",
            "cost": 3704,
            "lower_bound": 0,
            "upper_bound": 188
        },
        {
            "from": "85",
            "to": "156",
            "cost": 439,
            "lower_bound": 0,
            "upper_bound": 913
        },
        {
            "from": "85",
            "to": "88",
            "cost": 9927,
            "lower_bound": 0,
            "upper_bound": 135
        },
        {
            "from": "85",
            "to": "159",
            "cost": 2023,
            "lower_bound": 0,
            "upper_bound": 9
        },
        {
            "from": "85",
            "to": "94",
            "cost": 6015,
            "lower_bound": 0,
            "upper_bound": 350
        },
        {
            "from": "112",
            "to": "84",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 800
        },
        {
            "from": "112",
            "to": "227",
            "cost": 7951,
            "lower_bound": 0,
            "upper_bound": 559
        },
        {
            "from": "112",
            "to": "213",
            "cost": 7085,
            "lower_bound": 0,
            "upper_bound": 233
        },
        {
            "from": "112",
            "to": "121",
            "cost": 1857,
            "lower_bound": 0,
            "upper_bound": 391
        },
        {
            "from": "113",
            "to": "48",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 800
        },
        {
            "from": "113",
            "to": "219",
            "cost": 6913,
            "lower_bound": 0,
            "upper_bound": 332
        },
        {
            "from": "113",
            "to": "56",
            "cost": 7431,
            "lower_bound": 0,
            "upper_bound": 779
        },
        {
            "from": "131",
            "to": "174",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 800
        },
        {
            "from": "131",
            "to": "165",
            "cost": 2725,
            "lower_bound": 0,
            "upper_bound": 437
        },
        {
            "from": "131",
            "to": "185",
            "cost": 3829,
            "lower_bound": 0,
            "upper_bound": 781
        },
        {
            "from": "154",
            "to": "241",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 800
        },
        {
            "from": "154",
            "to": "43",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 800
        },
        {
            "from": "154",
            "to": "217",
            "cost": 247,
            "lower_bound": 0,
            "upper_bound": 53
        },
        {
            "from": "154",
            "to": "145",
            "cost": 9678,
            "lower_bound": 0,
            "upper_bound": 532
        },
        {
            "from": "154",
            "to": "238",
            "cost": 7305,
            "lower_bound": 0,
            "upper_bound": 796
        },
        {
            "from": "154",
            "to": "143",
            "cost": 5184,
            "lower_bound": 0,
            "upper_bound": 983
        },
        {
            "from": "154",
            "to": "161",
            "cost": 3635,
            "lower_bound": 0,
            "upper_bound": 426
        },
        {
            "from": "154",
            "to": "168",
            "cost": 5081,
            "lower_bound": 0,
            "upper_bound": 691
        },
        {
            "from": "174",
            "to": "186",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 800
        },
        {
            "from": "174",
            "to": "225",
            "cost": 7648,
            "lower_bound": 0,
            "upper_bound": 892
        },
        {
            "from": "174",
            "to": "96",
            "cost": 8449,
            "lower_bound": 0,
            "upper_bound": 993
        },
        {
            "from": "174",
            "to": "248",
            "cost": 8089,
            "lower_bound": 0,
            "upper_bound": 852
        },
        {
            "from": "174",
            "to": "233",
            "cost": 6124,
            "lower_bound": 0,
            "upper_bound": 521
        },
        {
            "from": "174",
            "to": "169",
            "cost": 5509,
            "lower_bound": 0,
            "upper_bound": 49
        },
        {
            "from": "174",
            "to": "110",
            "cost": 9363,
            "lower_bound": 0,
            "upper_bound": 926
        },
        {
            "from": "186",
            "to": "85",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 800
        },
        {
            "from": "186",
            "to": "40",
            "cost": 2981,
            "lower_bound": 0,
            "upper_bound": 959
        },
        {
            "from": "186",
            "to": "247",
            "cost": 6142,
            "lower_bound": 0,
            "upper_bound": 501
        },
        {
            "from": "186",
            "to": "157",
            "cost": 132,
            "lower_bound": 0,
            "upper_bound": 830
        },
        {
            "from": "186",
            "to": "24",
            "cost": 1849,
            "lower_bound": 0,
            "upper_bound": 718
        },
        {
            "from": "186",
            "to": "39",
            "cost": 5192,
            "lower_bound": 0,
            "upper_bound": 303
        },
        {
            "from": "186",
            "to": "169",
            "cost": 7379,
            "lower_bound": 0,
            "upper_bound": 975
        },
        {
            "from": "186",
            "to": "89",
            "cost": 7821,
            "lower_bound": 0,
            "upper_bound": 607
        },
        {
            "from": "186",
            "to": "59",
            "cost": 2862,
            "lower_bound": 0,
            "upper_bound": 808
        },
        {
            "from": "186",
            "to": "202",
            "cost": 6568,
            "lower_bound": 0,
            "upper_bound": 503
        },
        {
            "from": "191",
            "to": "249",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 800
        },
        {
            "from": "191",
            "to": "100",
            "cost": 5046,
            "lower_bound": 0,
            "upper_bound": 237
        },
        {
            "from": "191",
            "to": "24",
            "cost": 8512,
            "lower_bound": 0,
            "upper_bound": 796
        },
        {
            "from": "191",
            "to": "28",
            "cost": 3487,
            "lower_bound": 0,
            "upper_bound": 89
        },
        {
            "from": "191",
            "to": "18",
            "cost": 6949,
            "lower_bound": 0,
            "upper_bound": 772
        },
        {
            "from": "191",
            "to": "112",
            "cost": 1342,
            "lower_bound": 0,
            "upper_bound": 469
        },
        {
            "from": "191",
            "to": "195",
            "cost": 1660,
            "lower_bound": 0,
            "upper_bound": 696
        },
        {
            "from": "191",
            "to": "176",
            "cost": 9689,
            "lower_bound": 0,
            "upper_bound": 920
        },
        {
            "from": "191",
            "to": "245",
            "cost": 4852,
            "lower_bound": 0,
            "upper_bound": 164
        },
        {
            "from": "191",
            "to": "87",
            "cost": 5387,
            "lower_bound": 0,
            "upper_bound": 881
        },
        {
            "from": "193",
            "to": "223",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 800
        },
        {
            "from": "193",
            "to": "48",
            "cost": 1613,
            "lower_bound": 0,
            "upper_bound": 535
        },
        {
            "from": "193",
            "to": "107",
            "cost": 2440,
            "lower_bound": 0,
            "upper_bound": 218
        },
        {
            "from": "193",
            "to": "89",
            "cost": 8644,
            "lower_bound": 0,
            "upper_bound": 181
        },
        {
            "from": "193",
            "to": "206",
            "cost": 7531,
            "lower_bound": 0,
            "upper_bound": 400
        },
        {
            "from": "193",
            "to": "120",
            "cost": 5195,
            "lower_bound": 0,
            "upper_bound": 111
        },
        {
            "from": "193",
            "to": "18",
            "cost": 3322,
            "lower_bound": 0,
            "upper_bound": 234
        },
        {
            "from": "193",
            "to": "128",
            "cost": 7464,
            "lower_bound": 0,
            "upper_bound": 112
        },
        {
            "from": "194",
            "to": "154",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 800
        },
        {
            "from": "194",
            "to": "239",
            "cost": 1493,
            "lower_bound": 0,
            "upper_bound": 237
        },
        {
            "from": "194",
            "to": "159",
            "cost": 3244,
            "lower_bound": 0,
            "upper_bound": 124
        },
        {
            "from": "194",
            "to": "222",
            "cost": 2177,
            "lower_bound": 0,
            "upper_bound": 766
        },
        {
            "from": "194",
            "to": "150",
            "cost": 5855,
            "lower_bound": 0,
            "upper_bound": 596
        },
        {
            "from": "194",
            "to": "241",
            "cost": 7858,
            "lower_bound": 0,
            "upper_bound": 272
        },
        {
            "from": "194",
            "to": "145",
            "cost": 1372,
            "lower_bound": 0,
            "upper_bound": 940
        },
        {
            "from": "194",
            "to": "45",
            "cost": 1692,
            "lower_bound": 0,
            "upper_bound": 492
        },
        {
            "from": "194",
            "to": "50",
            "cost": 5281,
            "lower_bound": 0,
            "upper_bound": 899
        },
        {
            "from": "194",
            "to": "29",
            "cost": 5619,
            "lower_bound": 0,
            "upper_bound": 754
        },
        {
            "from": "194",
            "to": "231",
            "cost": 3646,
            "lower_bound": 0,
            "upper_bound": 676
        },
        {
            "from": "194",
            "to": "37",
            "cost": 8186,
            "lower_bound": 0,
            "upper_bound": 29
        },
        {
            "from": "194",
            "to": "91",
            "cost": 2266,
            "lower_bound": 0,
            "upper_bound": 723
        },
        {
            "from": "220",
            "to": "112",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 800
        },
        {
            "from": "220",
            "to": "95",
            "cost": 4306,
            "lower_bound": 0,
            "upper_bound": 867
        },
        {
            "from": "220",
            "to": "176",
            "cost": 4729,
            "lower_bound": 0,
            "upper_bound": 395
        },
        {
            "from": "220",
            "to": "149",
            "cost": 3626,
            "lower_bound": 0,
            "upper_bound": 846
        },
        {
            "from": "220",
            "to": "83",
            "cost": 4808,
            "lower_bound": 0,
            "upper_bound": 82
        },
        {
            "from": "220",
            "to": "203",
            "cost": 326,
            "lower_bound": 0,
            "upper_bound": 312
        },
        {
            "from": "220",
            "to": "246",
            "cost": 699,
            "lower_bound": 0,
            "upper_bound": 758
        },
        {
            "from": "220",
            "to": "85",
            "cost": 5029,
            "lower_bound": 0,
            "upper_bound": 732
        },
        {
            "from": "220",
            "to": "151",
            "cost": 6855,
            "lower_bound": 0,
            "upper_bound": 830
        },
        {
            "from": "220",
            "to": "37",
            "cost": 2336,
            "lower_bound": 0,
            "upper_bound": 666
        },
        {
            "from": "220",
            "to": "238",
            "cost": 3112,
            "lower_bound": 0,
            "upper_bound": 669
        },
        {
            "from": "220",
            "to": "74",
            "cost": 1568,
            "lower_bound": 0,
            "upper_bound": 586
        },
        {
            "from": "220",
            "to": "71",
            "cost": 9209,
            "lower_bound": 0,
            "upper_bound": 300
        },
        {
            "from": "220",
            "to": "116",
            "cost": 228,
            "lower_bound": 0,
            "upper_bound": 796
        },
        {
            "from": "223",
            "to": "131",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 800
        },
        {
            "from": "223",
            "to": "154",
            "cost": 9578,
            "lower_bound": 0,
            "upper_bound": 68
        },
        {
            "from": "223",
            "to": "226",
            "cost": 1677,
            "lower_bound": 0,
            "upper_bound": 52
        },
        {
            "from": "223",
            "to": "185",
            "cost": 7366,
            "lower_bound": 0,
            "upper_bound": 998
        },
        {
            "from": "223",
            "to": "125",
            "cost": 3037,
            "lower_bound": 0,
            "upper_bound": 58
        },
        {
            "from": "16",
            "to": "54",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2350
        },
        {
            "from": "16",
            "to": "244",
            "cost": 2022,
            "lower_bound": 0,
            "upper_bound": 557
        },
        {
            "from": "16",
            "to": "209",
            "cost": 1881,
            "lower_bound": 0,
            "upper_bound": 493
        },
        {
            "from": "16",
            "to": "226",
            "cost": 7709,
            "lower_bound": 0,
            "upper_bound": 226
        },
        {
            "from": "16",
            "to": "121",
            "cost": 7570,
            "lower_bound": 0,
            "upper_bound": 271
        },
        {
            "from": "16",
            "to": "78",
            "cost": 2666,
            "lower_bound": 0,
            "upper_bound": 863
        },
        {
            "from": "16",
            "to": "81",
            "cost": 876,
            "lower_bound": 0,
            "upper_bound": 146
        },
        {
            "from": "16",
            "to": "19",
            "cost": 8572,
            "lower_bound": 0,
            "upper_bound": 281
        },
        {
            "from": "16",
            "to": "134",
            "cost": 4245,
            "lower_bound": 0,
            "upper_bound": 935
        },
        {
            "from": "24",
            "to": "102",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2350
        },
        {
            "from": "24",
            "to": "254",
            "cost": 2160,
            "lower_bound": 0,
            "upper_bound": 397
        },
        {
            "from": "24",
            "to": "42",
            "cost": 4139,
            "lower_bound": 0,
            "upper_bound": 878
        },
        {
            "from": "24",
            "to": "72",
            "cost": 2273,
            "lower_bound": 0,
            "upper_bound": 606
        },
        {
            "from": "24",
            "to": "35",
            "cost": 7333,
            "lower_bound": 0,
            "upper_bound": 606
        },
        {
            "from": "24",
            "to": "128",
            "cost": 2601,
            "lower_bound": 0,
            "upper_bound": 569
        },
        {
            "from": "54",
            "to": "137",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2350
        },
        {
            "from": "54",
            "to": "248",
            "cost": 1900,
            "lower_bound": 0,
            "upper_bound": 526
        },
        {
            "from": "54",
            "to": "174",
            "cost": 1541,
            "lower_bound": 0,
            "upper_bound": 557
        },
        {
            "from": "54",
            "to": "138",
            "cost": 5397,
            "lower_bound": 0,
            "upper_bound": 135
        },
        {
            "from": "54",
            "to": "232",
            "cost": 8613,
            "lower_bound": 0,
            "upper_bound": 616
        },
        {
            "from": "54",
            "to": "235",
            "cost": 9759,
            "lower_bound": 0,
            "upper_bound": 815
        },
        {
            "from": "54",
            "to": "199",
            "cost": 3737,
            "lower_bound": 0,
            "upper_bound": 233
        },
        {
            "from": "54",
            "to": "59",
            "cost": 1660,
            "lower_bound": 0,
            "upper_bound": 166
        },
        {
            "from": "54",
            "to": "186",
            "cost": 8066,
            "lower_bound": 0,
            "upper_bound": 747
        },
        {
            "from": "54",
            "to": "126",
            "cost": 9069,
            "lower_bound": 0,
            "upper_bound": 57
        },
        {
            "from": "54",
            "to": "151",
            "cost": 7530,
            "lower_bound": 0,
            "upper_bound": 373
        },
        {
            "from": "54",
            "to": "97",
            "cost": 1526,
            "lower_bound": 0,
            "upper_bound": 773
        },
        {
            "from": "54",
            "to": "201",
            "cost": 4602,
            "lower_bound": 0,
            "upper_bound": 457
        },
        {
            "from": "54",
            "to": "40",
            "cost": 7115,
            "lower_bound": 0,
            "upper_bound": 827
        },
        {
            "from": "54",
            "to": "107",
            "cost": 2262,
            "lower_bound": 0,
            "upper_bound": 884
        },
        {
            "from": "79",
            "to": "138",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2350
        },
        {
            "from": "79",
            "to": "240",
            "cost": 9898,
            "lower_bound": 0,
            "upper_bound": 184
        },
        {
            "from": "100",
            "to": "129",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2350
        },
        {
            "from": "100",
            "to": "23",
            "cost": 1251,
            "lower_bound": 0,
            "upper_bound": 863
        },
        {
            "from": "100",
            "to": "241",
            "cost": 3316,
            "lower_bound": 0,
            "upper_bound": 282
        },
        {
            "from": "100",
            "to": "194",
            "cost": 9648,
            "lower_bound": 0,
            "upper_bound": 621
        },
        {
            "from": "100",
            "to": "88",
            "cost": 7013,
            "lower_bound": 0,
            "upper_bound": 12
        },
        {
            "from": "100",
            "to": "97",
            "cost": 2366,
            "lower_bound": 0,
            "upper_bound": 30
        },
        {
            "from": "100",
            "to": "221",
            "cost": 5043,
            "lower_bound": 0,
            "upper_bound": 133
        },
        {
            "from": "100",
            "to": "166",
            "cost": 127,
            "lower_bound": 0,
            "upper_bound": 290
        },
        {
            "from": "100",
            "to": "227",
            "cost": 7219,
            "lower_bound": 0,
            "upper_bound": 572
        },
        {
            "from": "100",
            "to": "255",
            "cost": 1006,
            "lower_bound": 0,
            "upper_bound": 384
        },
        {
            "from": "102",
            "to": "239",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2350
        },
        {
            "from": "102",
            "to": "66",
            "cost": 8234,
            "lower_bound": 0,
            "upper_bound": 294
        },
        {
            "from": "102",
            "to": "152",
            "cost": 3771,
            "lower_bound": 0,
            "upper_bound": 157
        },
        {
            "from": "102",
            "to": "127",
            "cost": 8777,
            "lower_bound": 0,
            "upper_bound": 694
        },
        {
            "from": "102",
            "to": "159",
            "cost": 4472,
            "lower_bound": 0,
            "upper_bound": 212
        },
        {
            "from": "102",
            "to": "41",
            "cost": 6151,
            "lower_bound": 0,
            "upper_bound": 627
        },
        {
            "from": "102",
            "to": "150",
            "cost": 8554,
            "lower_bound": 0,
            "upper_bound": 170
        },
        {
            "from": "102",
            "to": "145",
            "cost": 4853,
            "lower_bound": 0,
            "upper_bound": 76
        },
        {
            "from": "102",
            "to": "69",
            "cost": 3274,
            "lower_bound": 0,
            "upper_bound": 605
        },
        {
            "from": "102",
            "to": "129",
            "cost": 4357,
            "lower_bound": 0,
            "upper_bound": 332
        },
        {
            "from": "102",
            "to": "47",
            "cost": 4421,
            "lower_bound": 0,
            "upper_bound": 135
        },
        {
            "from": "118",
            "to": "217",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2350
        },
        {
            "from": "118",
            "to": "243",
            "cost": 1282,
            "lower_bound": 0,
            "upper_bound": 480
        },
        {
            "from": "118",
            "to": "103",
            "cost": 2326,
            "lower_bound": 0,
            "upper_bound": 506
        },
        {
            "from": "118",
            "to": "101",
            "cost": 5131,
            "lower_bound": 0,
            "upper_bound": 836
        },
        {
            "from": "118",
            "to": "216",
            "cost": 7142,
            "lower_bound": 0,
            "upper_bound": 48
        },
        {
            "from": "118",
            "to": "91",
            "cost": 460,
            "lower_bound": 0,
            "upper_bound": 668
        },
        {
            "from": "118",
            "to": "77",
            "cost": 6481,
            "lower_bound": 0,
            "upper_bound": 505
        },
        {
            "from": "118",
            "to": "60",
            "cost": 1525,
            "lower_bound": 0,
            "upper_bound": 372
        },
        {
            "from": "118",
            "to": "129",
            "cost": 7894,
            "lower_bound": 0,
            "upper_bound": 479
        },
        {
            "from": "118",
            "to": "228",
            "cost": 9828,
            "lower_bound": 0,
            "upper_bound": 327
        },
        {
            "from": "118",
            "to": "47",
            "cost": 194,
            "lower_bound": 0,
            "upper_bound": 147
        },
        {
            "from": "118",
            "to": "38",
            "cost": 9254,
            "lower_bound": 0,
            "upper_bound": 349
        },
        {
            "from": "129",
            "to": "148",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2350
        },
        {
            "from": "129",
            "to": "78",
            "cost": 2637,
            "lower_bound": 0,
            "upper_bound": 367
        },
        {
            "from": "129",
            "to": "150",
            "cost": 3287,
            "lower_bound": 0,
            "upper_bound": 855
        },
        {
            "from": "137",
            "to": "142",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2350
        },
        {
            "from": "137",
            "to": "132",
            "cost": 8253,
            "lower_bound": 0,
            "upper_bound": 482
        },
        {
            "from": "137",
            "to": "114",
            "cost": 6776,
            "lower_bound": 0,
            "upper_bound": 960
        },
        {
            "from": "138",
            "to": "118",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2350
        },
        {
            "from": "138",
            "to": "174",
            "cost": 4802,
            "lower_bound": 0,
            "upper_bound": 1
        },
        {
            "from": "138",
            "to": "69",
            "cost": 1358,
            "lower_bound": 0,
            "upper_bound": 410
        },
        {
            "from": "138",
            "to": "90",
            "cost": 7261,
            "lower_bound": 0,
            "upper_bound": 145
        },
        {
            "from": "138",
            "to": "194",
            "cost": 1892,
            "lower_bound": 0,
            "upper_bound": 631
        },
        {
            "from": "138",
            "to": "227",
            "cost": 1456,
            "lower_bound": 0,
            "upper_bound": 728
        },
        {
            "from": "138",
            "to": "157",
            "cost": 5931,
            "lower_bound": 0,
            "upper_bound": 620
        },
        {
            "from": "142",
            "to": "100",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2350
        },
        {
            "from": "142",
            "to": "205",
            "cost": 6985,
            "lower_bound": 0,
            "upper_bound": 321
        },
        {
            "from": "142",
            "to": "214",
            "cost": 3943,
            "lower_bound": 0,
            "upper_bound": 96
        },
        {
            "from": "142",
            "to": "168",
            "cost": 8502,
            "lower_bound": 0,
            "upper_bound": 199
        },
        {
            "from": "142",
            "to": "73",
            "cost": 387,
            "lower_bound": 0,
            "upper_bound": 731
        },
        {
            "from": "142",
            "to": "17",
            "cost": 1151,
            "lower_bound": 0,
            "upper_bound": 69
        },
        {
            "from": "142",
            "to": "231",
            "cost": 8826,
            "lower_bound": 0,
            "upper_bound": 290
        },
        {
            "from": "142",
            "to": "146",
            "cost": 1736,
            "lower_bound": 0,
            "upper_bound": 839
        },
        {
            "from": "142",
            "to": "107",
            "cost": 2123,
            "lower_bound": 0,
            "upper_bound": 443
        },
        {
            "from": "148",
            "to": "79",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2350
        },
        {
            "from": "148",
            "to": "114",
            "cost": 4502,
            "lower_bound": 0,
            "upper_bound": 727
        },
        {
            "from": "148",
            "to": "32",
            "cost": 4062,
            "lower_bound": 0,
            "upper_bound": 158
        },
        {
            "from": "148",
            "to": "107",
            "cost": 3500,
            "lower_bound": 0,
            "upper_bound": 576
        },
        {
            "from": "148",
            "to": "99",
            "cost": 7969,
            "lower_bound": 0,
            "upper_bound": 229
        },
        {
            "from": "148",
            "to": "76",
            "cost": 3273,
            "lower_bound": 0,
            "upper_bound": 398
        },
        {
            "from": "148",
            "to": "78",
            "cost": 9708,
            "lower_bound": 0,
            "upper_bound": 409
        },
        {
            "from": "217",
            "to": "24",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2350
        },
        {
            "from": "217",
            "to": "43",
            "cost": 4727,
            "lower_bound": 0,
            "upper_bound": 765
        },
        {
            "from": "217",
            "to": "173",
            "cost": 3616,
            "lower_bound": 0,
            "upper_bound": 368
        },
        {
            "from": "217",
            "to": "203",
            "cost": 5080,
            "lower_bound": 0,
            "upper_bound": 207
        },
        {
            "from": "217",
            "to": "67",
            "cost": 3569,
            "lower_bound": 0,
            "upper_bound": 191
        },
        {
            "from": "217",
            "to": "178",
            "cost": 6112,
            "lower_bound": 0,
            "upper_bound": 320
        },
        {
            "from": "217",
            "to": "213",
            "cost": 7362,
            "lower_bound": 0,
            "upper_bound": 576
        },
        {
            "from": "217",
            "to": "148",
            "cost": 7307,
            "lower_bound": 0,
            "upper_bound": 587
        },
        {
            "from": "217",
            "to": "162",
            "cost": 5794,
            "lower_bound": 0,
            "upper_bound": 255
        },
        {
            "from": "234",
            "to": "243",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2350
        },
        {
            "from": "234",
            "to": "208",
            "cost": 9833,
            "lower_bound": 0,
            "upper_bound": 148
        },
        {
            "from": "234",
            "to": "181",
            "cost": 4451,
            "lower_bound": 0,
            "upper_bound": 935
        },
        {
            "from": "234",
            "to": "40",
            "cost": 9956,
            "lower_bound": 0,
            "upper_bound": 682
        },
        {
            "from": "234",
            "to": "37",
            "cost": 9471,
            "lower_bound": 0,
            "upper_bound": 207
        },
        {
            "from": "234",
            "to": "21",
            "cost": 8544,
            "lower_bound": 0,
            "upper_bound": 942
        },
        {
            "from": "234",
            "to": "126",
            "cost": 2081,
            "lower_bound": 0,
            "upper_bound": 706
        },
        {
            "from": "234",
            "to": "145",
            "cost": 1822,
            "lower_bound": 0,
            "upper_bound": 272
        },
        {
            "from": "234",
            "to": "115",
            "cost": 1692,
            "lower_bound": 0,
            "upper_bound": 490
        },
        {
            "from": "239",
            "to": "234",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2350
        },
        {
            "from": "239",
            "to": "255",
            "cost": 10000,
            "lower_bound": 0,
            "upper_bound": 2350
        },
        {
            "from": "239",
            "to": "31",
            "cost": 4512,
            "lower_bound": 0,
            "upper_bound": 602
        },
        {
            "from": "239",
            "to": "167",
            "cost": 1079,
            "lower_bound": 0,
            "upper_bound": 99
        },
        {
            "from": "239",
            "to": "160",
            "cost": 6445,
            "lower_bound": 0,
            "upper_bound": 108
        },
        {
            "from": "239",
            "to": "90",
            "cost": 2921,
            "lower_bound": 0,
            "upper_bound": 764
        },
        {
            "from": "239",
            "to": "178",
            "cost": 3958,
            "lower_bound": 0,
            "upper_bound": 757
        },
        {
            "from": "239",
            "to": "78",
            "cost": 5795,
            "lower_bound": 0,
            "upper_bound": 17
        },
        {
            "from": "239",
            "to": "213",
            "cost": 8704,
            "lower_bound": 0,
            "upper_bound": 844
        }
]

solution, total_cost = solve_min_cost_flow(nodes, arcs)
if solution:
    print("Flussmengen auf den Kanten (Fluss > 0):")
    for arc, flow in solution.items():
        if flow > 0:
            print(f"Kante {arc}: Fluss {flow}")
    print(f"Anzahl der Kanten mit Fluss > 0: {len([flow for flow in solution.values() if flow > 0])}")
    print(f"Minimale Gesamtkosten des Netzwerks: {total_cost}")

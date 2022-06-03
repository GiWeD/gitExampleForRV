
#/usr/bin/python3
from tracemalloc import stop
from web3 import Web3
import numpy as np
from ABIFolder.ABI import ABI
InterfaceABI = ABI()

import matplotlib.pyplot as plt
import pandas as pd
import json


############################################################################################################################################################################
############################################################################################################################################################################
############################################################################################################################################################################
############################################################################################################################################################################
############################################################################################################################################################################
############################################################################################################################################################################

#init web3
print("Starting w3 contract interface")
FantomRPC              = "https://rpc.ftm.tools/"
w3                      = Web3(Web3.HTTPProvider(FantomRPC))
lastBlock = w3.eth.get_block_number()


gaugeAddress  = "0x420b17f69618610DE18caCd1499460EFb29e1d8f"
gaugeAbi = InterfaceABI.get_gauge_Abi()
gaugeContract = w3.eth.contract(address=gaugeAddress, abi=gaugeAbi)
LPTokens = gaugeContract.functions.tokens().call()
strategyProxy = "0xbBf62f98D2F15F4D92a71a676a9baAC84eaB37d8"

erc20Abi = InterfaceABI.get_ERC20_Abi()
LPABI = json.loads(' [{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}] ')


gaugeAddresses = list()
gaugeTotalBalance = list()
length = len(LPTokens)

print("Reading Info from Gauges")
for i in range(length):
    #print("Gauge: %d/%d" % (i,length), end='\r')
    gaugeAddresses.append(gaugeContract.functions.gauges(LPTokens[i]).call())
    tokenContract = w3.eth.contract(address=LPTokens[i], abi=erc20Abi)
    balance = tokenContract.functions.balanceOf(gaugeAddresses[i]).call()
    gaugeTotalBalance.append(balance)

inSpiritContract = w3.eth.contract(address="0x2FBFf41a9efAEAE77538bd63f1ea489494acdc08", abi=erc20Abi)
inSpiritTotalSupply = inSpiritContract.functions.totalSupply().call()

liquidInSpirit = inSpiritContract.functions.balanceOf(strategyProxy).call()

data = pd.read_csv("./csvData/contractAddresses.csv")
strategyLP = data["LP Address"]
strategy = data["strategy"]



# Condition to get max Boost
# TotalDepositedInThePool * LiquidInSpirit / TotalInSpirit >= UserBalance
 
AdjBalance = list()
strategyBalance = list()
boost = list()
share = list()
name = list()
inSpiritToGetMaxBoost = list()
strategyBalanceForMaxBoost = list()
deltaBalanceBoost = list()



flag = False

print("Reading strategy params and finding maxboost")
for i in range(length):

    lpToken = LPTokens[i]
    
    AdjBalance.append(  ( (gaugeTotalBalance[i] * liquidInSpirit) / inSpiritTotalSupply) * 0.6  )

    print("LP: %d/%d" % (i,length))
    
    for x in range(len(strategyLP)):
        
        
        if( strategyLP[x] == lpToken  and  strategy[x] != "0x0000000000000000000000000000000000000000"):
            print("LP: %s\t StratLP: %s" % (lpToken, strategyLP[x]), end='\r')
            gaugeContract = w3.eth.contract(address = gaugeAddresses[i], abi=erc20Abi)
            strategyBalance.append ( gaugeContract.functions.balanceOf(strategyProxy).call() )
            share.append ( strategyBalance[i] / gaugeTotalBalance[i] )


            flag = True
            break
    
    
    if ( flag == False):
        strategyBalance.append( 0 )
        share.append ( 0 )

    

    if(strategyBalance[i] != 0):

        if( (strategyBalance[i]*0.4 + AdjBalance[i])/strategyBalance[i] >= 1 ):
            boost.append(2.5)
            inSpiritToGetMaxBoost.append(0)
        else: 
            find = min(strategyBalance[i]*0.4 + AdjBalance[i], strategyBalance[i]) / strategyBalance[i]
            boost.append(find/0.4)

            inSpiritToGetMaxBoost.append( ( inSpiritTotalSupply * strategyBalance[i] / gaugeTotalBalance[i] ) - liquidInSpirit )

            
    else:
        boost.append(0)
        inSpiritToGetMaxBoost.append(False)


    strategyBalanceForMaxBoost.append( (gaugeTotalBalance[i] * liquidInSpirit) / inSpiritTotalSupply )
    deltaBalanceBoost.append( strategyBalanceForMaxBoost[i] - strategyBalance[i] )


    # Name
    tokenContract = w3.eth.contract(address=lpToken, abi=LPABI)
    # read token0,1 address
    tempTokenZeroAddress = tokenContract.functions.token0().call()
    tempTokenOneAddress = tokenContract.functions.token1().call()
    # load ERC-20 token 0
    tempAddress = w3.toChecksumAddress(str(tempTokenZeroAddress))
    tokenContract = w3.eth.contract(address = tempAddress, abi = erc20Abi)
    tempTokenZeroSymbol = tokenContract.functions.symbol().call()
    # load ERC-20 token 1
    tempAddress = w3.toChecksumAddress(str(tempTokenOneAddress))
    tokenContract = w3.eth.contract(address = tempAddress, abi = erc20Abi)
    tempTokenOneSymbol = tokenContract.functions.symbol().call()
    # create string
    tempString = tempTokenZeroSymbol + "-" + tempTokenOneSymbol
    name.append( tempString )

            
    
    flag = False

print(boost)

# fix eth decimals
for i in range(length):
    strategyBalance[i] = strategyBalance[i] / 1e18
    inSpiritToGetMaxBoost[i] = inSpiritToGetMaxBoost[i] / 1e18
    gaugeTotalBalance[i] = gaugeTotalBalance[i] / 1e18
    strategyBalanceForMaxBoost[i] = strategyBalanceForMaxBoost[i] / 1e18
    deltaBalanceBoost[i] = deltaBalanceBoost[i] / 1e18


data2 = list ( zip ( name,LPTokens,gaugeAddresses,gaugeTotalBalance,strategyBalance,share,boost, inSpiritToGetMaxBoost, strategyBalanceForMaxBoost , deltaBalanceBoost   ) )
data = pd.DataFrame(data2, columns=['LPName','LPTokens','GaugeAddress','PoolBalance','StrategyBalance', 'share','BoostFactor', 'inSpiritToGetMaxBoost', 'strategyBalanceForMaxBoost','deltaBalanceBoost'])
data.index.name = 'pid'
data.to_csv("./csvData/maxBoost.csv", encoding='utf-8')




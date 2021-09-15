import json
import config
from web3 import Web3

def computeRooms(_propertyId, _progress):
    data = __fetchDataAtProgress(_propertyId, _progress)
    height = __computeHeightAtProgress(data['x'], data['z'], data['height'], _progress)
    return (data['width'] * data['length']) * (round(height) - 1)

def computeHeight(_propertyId, _progress):
    data = __fetchDataAtProgress(_propertyId, _progress)
    return __computeHeightAtProgress(data['x'], data['z'], data['height'], _progress)

# this is a private function from the contract that i've recreated to be able to use
def __computeHeightAtProgress(_x, _z, _height, progress):
    x = 50 - _x if _x < 50 else _x - 50
    z = 50 - _z if _z < 50 else _z - 50
    distance = x if x > z else z

    if(distance > progress):
        return 1
    
    scale = 100 - (distance * 100) / progress
    height = 2 * progress * _height * scale / 10000
    return height if height > 0 else 1

def __fetchDataAtProgress(_propertyId, _progress):
    infura_url = 'https://mainnet.infura.io/v3/' + config.infura_token
    web3 = Web3(Web3.HTTPProvider(infura_url))

    # we need to make available the functionality we would like to draw from the contract. 
    # the abi could contain all functionality, but its not necessary
    abi = json.loads('[{\"constant\":true,\"inputs\":[{\"name\":\"_id\",\"type\":\"uint256\"}],\"name\":\"getProperty\",\"outputs\":[{\"name\":\"parent\",\"type\":\"uint32\"},{\"name\":\"class\",\"type\":\"uint8\"},{\"name\":\"x\",\"type\":\"uint8\"},{\"name\":\"y\",\"type\":\"uint8\"},{\"name\":\"z\",\"type\":\"uint8\"},{\"name\":\"dx\",\"type\":\"uint8\"},{\"name\":\"dz\",\"type\":\"uint8\"},{\"name\":\"height\",\"type\":\"uint8\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"}]')
    address = '0x31d4C5be1082A88F2ABAFeA549B6C189C2cf057F'

    contract = web3.eth.contract(address=address, abi=abi)

    # example response call from 103 - [3, 1, 51, 1, 36, 3, 2, 46]
    # these values are parent (district?), class, x, y, z, dx, dz, height respectively
    properties = ['parent', 'class', 'x', 'y', 'z', 'width', 'length', 'height']
    propertyNumber = int(_propertyId)
    progress = int(_progress)

    data = contract.functions.getProperty(propertyNumber).call()
    return dict(zip(properties, data))

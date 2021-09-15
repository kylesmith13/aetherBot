import config
import json
import config
from web3 import Web3

def computeInfo(_propertyId, _progress):
    data = __fetchDataAtProgress(_propertyId, _progress)
    height = __computeHeightAtProgress(data['x'], data['z'], data['height'], _progress)
    return {'rooms': __rooms(data, height), 'floors': height}

def __rooms(_data, _height):
    return (_data['width'] * _data['length']) * (round(_height) - 1)

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
    abi = json.loads(config.contract_abi)
    address = config.contract_address

    contract = web3.eth.contract(address=address, abi=abi)

    # example response call from 103 - [3, 1, 51, 1, 36, 3, 2, 46]
    # these values are parent (district?), class, x, y, z, dx, dz, height respectively
    properties = ['parent', 'class', 'x', 'y', 'z', 'width', 'length', 'height']
    propertyNumber = int(_propertyId)

    data = contract.functions.getProperty(propertyNumber).call()
    return dict(zip(properties, data))

import os

token = os.environ['token']
infura_token = os.environ['infura_token']
contract_address = '0x31d4C5be1082A88F2ABAFeA549B6C189C2cf057F'
contract_abi = '[{\"constant\":true,\"inputs\":[{\"name\":\"_id\",\"type\":\"uint256\"}],\"name\":\"getProperty\",\"outputs\":[{\"name\":\"parent\",\"type\":\"uint32\"},{\"name\":\"class\",\"type\":\"uint8\"},{\"name\":\"x\",\"type\":\"uint8\"},{\"name\":\"y\",\"type\":\"uint8\"},{\"name\":\"z\",\"type\":\"uint8\"},{\"name\":\"dx\",\"type\":\"uint8\"},{\"name\":\"dz\",\"type\":\"uint8\"},{\"name\":\"height\",\"type\":\"uint8\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"}]'

version = 0.1
footer = "made with \u2764\uFE0F  by katalyst.eth"

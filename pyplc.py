#! /usr/bin/env python

from pymodbus.client.sync import ModbusTcpClient
import struct 

class PyPlc:
	def __init__(self, ip, port = 502):
		self.client = ModbusTcpClient(ip, port=502)
		connected = self.client.connect()

	def AnalogRead(address):
		rr = self.client.read_holding_registers(address, count=2, unit=1)

		a = int(rr.registers[0])
		b = int(rr.registers[1])

		return struct.unpack("<f", struct.pack("<HH", a, b))[0]	#read from modbus	

	def AnalogWrite(address, value):
		assert(type(value) is float)
	
		[a, b] = struct.unpack("<HH", struct.pack("<f", value))	

		rr = self.client.write_register(address, a)
		rr = self.client.write_register(address + 1, b)

	def DigitalWrite(address, value):
		assert(value == True or value == False)
		rq = self.client.write_coil(address, value)

	def DigitalRead(address):
		rq = self.client.read_coil(address, count=1, unit=1)

    def __del__(self):
        self.client.disconnect() 

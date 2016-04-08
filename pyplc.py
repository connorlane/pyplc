#! /usr/bin/env python

from pymodbus.client.sync import ModbusTcpClient
import struct 

class PyPlc:
	def __init__(self, ip, port = 502):
		
		client = ModbusTcpClient('192.168.0.221', port=502)
		connected = client.connect()

	def AnalogRead(address):
		rr = client.read_holding_registers(address, count=2, unit=1)

		a = int(rr.registers[0])
		b = int(rr.registers[1])

		return struct.unpack("<f", struct.pack("<HH", a, b))[0]	#read from modbus	

	def AnalogWrite(address, value):
		assert(type(value) is float)
	
		[a, b] = struct.unpack("<HH", struct.pack("<f", value))	

		rr = client.write_register(address, a)
		rr = client.write_register(address + 1, b)

	def DigitalWrite(address, value):
		assert(value == True or value == False)
		rq = client.write_coil(address, value)

	def DigitalRead(address):
		rq = client.read_coil(address, count=1, unit=1)


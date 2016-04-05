#! /usr/bin/env python

from pymodbus.client.sync import ModbusTcpClient
import struct 

NUM_INPUTS = 4
NUM_OUTPUTS = 2

client = ModbusTcpClient('192.168.0.221', port=502)
connected = client.connect()

def ReadInput(client, input_num):
	assert(input_num >= 0 and input_num < NUM_INPUTS)

	rr = client.read_holding_registers(28672, count=2, unit=1)

	a = int(rr.registers[0])
	b = int(rr.registers[1])

	return struct.unpack("<f", struct.pack("<HH", a, b))[0]

def WriteOutput(client, output_num, value):
	assert(output_num >=0 and output_num < NUM_OUTPUTS)

	[a, b] = struct.unpack("<HH", struct.pack("<f", value))	

	print a
	print b

	rr = client.write_register(output_num + 28692, a)
	rr = client.write_register(output_num + 28693, b)

print ReadInput(client, 1)

WriteOutput(client, 0, 3.14159)


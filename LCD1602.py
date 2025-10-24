#!/usr/bin/env python3

import time
import smbus2 as smbus

_bus = None
_addr = None
_backlight = 1

def _write_word(data):
    temp = data
    if _backlight == 1:
        temp |= 0x08
    else:
        temp &= 0xF7
    _bus.write_byte(_addr, temp)

def _send_command(cmd):
    high = cmd & 0xF0
    high |= 0x04
    _write_word(high)
    time.sleep(0.002)
    high &= 0xFB
    _write_word(high)

    low = (cmd & 0x0F) << 4
    low |= 0x04
    _write_word(low)
    time.sleep(0.002)
    low &= 0xFB
    _write_word(low)

def _send_data(data):
    high = data & 0xF0
    high |= 0x05
    _write_word(high)
    time.sleep(0.002)
    high &= 0xFB
    _write_word(high)

    low = (data & 0x0F) << 4
    low |= 0x05
    _write_word(low)
    time.sleep(0.002)
    low &= 0xFB
    _write_word(low)

def init(address=0x27, backlight=True, bus_id=1):
    global _bus
    global _addr
    global _backlight

    _addr = address
    _backlight = 1 if backlight else 0
    _bus = smbus.SMBus(bus_id)

    time.sleep(0.05)
    _send_command(0x33)
    time.sleep(0.005)
    _send_command(0x32)
    time.sleep(0.005)
    _send_command(0x28)
    time.sleep(0.005)
    _send_command(0x0C)
    time.sleep(0.005)
    clear()
    time.sleep(0.005)

    _bus.write_byte(_addr, 0x08)

def clear():
    _send_command(0x01)
    time.sleep(0.005)

def goto_xy(x, y):
    if x < 0:
        x = 0
    if x > 15:
        x = 15
    if y < 0:
        y = 0
    if y > 1:
        y = 1
    addr = 0x80 + 0x40 * y + x
    _send_command(addr)

def write(x, y, text):
    goto_xy(x, y)
    for ch in text:
        _send_data(ord(ch))

def set_backlight(on):
    global _backlight
    _backlight = 1 if on else 0
    _bus.write_byte(_addr, 0x00 | (0x08 if _backlight else 0x00))

def close_bus():
    _bus.close()

if __name__ == "__main__":
    init(0x27, True, 1)
    write_text(0, 0, "HELLO")
    write_text(0, 1, "KAAN")
    time.sleep(2)
    close_bus()

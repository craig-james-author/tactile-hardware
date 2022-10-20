#!/bin/sh
diskutil unmount `mount | grep CIRCUITPY | cut -f1 -d' '`

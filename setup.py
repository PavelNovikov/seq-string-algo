#!/usr/bin/env python

import os
import sys

from setuptools import setup

setup(
	name = "seq-string-algo",
	version = "0.01",
	cffi_modules = [
		"seq_string_algo/build_suffix_array.py:ffi",
		"seq_string_algo/build_edit_distance.py:ffi"
	]
)

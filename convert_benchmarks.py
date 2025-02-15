#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 or CC0-1.0
import sys
from mupq import mupq
    
def usage():  
    print("Usage: python3 convert_benchmarks.py csv|md|tex")
    sys.exit(1) 
 
if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
    if sys.argv[1] == "csv": 
        converter = mupq.CsvConverter()
    elif sys.argv[1] == "md":
        converter = mupq.MarkdownConverter()
    elif sys.argv[1] == "tex":
        converter = mupq.TexConverter()
    else:
        usage()
    converter.convert()

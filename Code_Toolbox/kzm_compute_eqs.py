#!/usr/bin/env python

"""
For my reference: 
EQ = collections.namedtuple("EQ", ["mag", "depth", "lon", "lat", "date", "eventID"])
"""

import read_catalog

def compute_max_depth(EQCat):
    """
    Compute maximum depth within earthquake catalog
    Inputs: EQCat -- list of EQ objects
    Outputs: max depth -- float 
    """
    
    depth_list = [x.depth for x in EQCat]  # list of 450 floats
    print(max(depth_list), " km depth");
    return max(depth_list)


if __name__ == "__main__":
    catfilename = "../Example_Data/USGS_catalog_example.txt" # config stage 
    MyEQCat = read_catalog.read_file(catfilename)  # input stage
    max_depth = compute_max_depth(MyEQCat)       # compute stage

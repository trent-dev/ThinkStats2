"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def CleanFemResp(df):
    pass

def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz',
                nrows=None):
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    CleanFemResp(df)
    return df

def ValidatePregnum(resp, preg):
    respToPregMap = nsfg.MakePregMap(preg)
    for index, pregnum in resp.pregnum.iteritems():
        caseid = resp.caseid[index]
        pregCount = len(respToPregMap[caseid])
        if pregCount != pregnum:
            print(caseid, pregCount, pregnum)
            return False

    return True

def PrintPregNums(df):
    print(df.pregnum.value_counts().sort_index())

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    # read and validate the respondent file
    resp = ReadFemResp()

    assert(len(resp) == 7643)

    # read and validate the pregnancy file
    preg = nsfg.ReadFemPreg()
    print(preg.shape)

    assert len(preg) == 13593

    # validate that the pregnum column in `resp` matches the number
    # of entries in `preg`
    assert(ValidatePregnum(resp, preg))

    PrintPregNums(preg)

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)

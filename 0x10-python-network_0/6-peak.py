#!/usr/bin/python3

""" Finds the prak in the list """


def find_peak(list_of_integers):
    """ Finds the peak of the list o f integers """

    if list_of_integers == []:
        return None

    """ Integer list il """
    il = list_of_integers
    end = len(list_of_integers)
    cen = int(end / 2)

    if cen - 1 < 0 and cen + 1 >= end:
        return il[cen]
    elif cen - 1 < 0:
        return il[cen] if il[cen] > il[cen + 1] else il[cen + 1]
    elif cen + 1 >= end:
        return il[cen] if il[cen] > il[cen - 1] else il[cen - 1]

    if il[cen - 1] < il[cen] > il[cen + 1]:
        return il[cen]

    if il[cen + 1] > il[cen - 1]:
        return find_peak(il[cen:])
    return find_peak(il[:cen])

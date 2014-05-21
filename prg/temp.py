#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      alexander.svensson
#
# Created:     30-07-2013
# Copyright:   (c) alexander.svensson 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    with open(r'C:\ProgramData\Radius Control Systems\Uni-View\EBEM\Data\Settings\standard.mnu', 'r') as outfile:
        data=outfile.readlines()
        print(data)


if __name__ == '__main__':
    main()
